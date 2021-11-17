# -*- coding: utf-8 -*-
"""
@author: pablo

"""

### MODULES

import time

# From env
from telegram import ParseMode, Update
from telegram.bot import Bot
from telegram.ext import Updater, CallbackContext
from telegram_bot_calendar import DetailedTelegramCalendar

# From Package
from database.users_database import UsersDatabase
from fillscripts import single_booking
from utils import const as c
from utils import date_parser
from utils import keyboards


class SbaBot:

    def __init__(self, token):
        # Create the Updater and pass it your bot's token.
        self.updater = Updater(token)

        # Get the dispatcher to register handlers
        self.dispatcher = self.updater.dispatcher
        # Initialize calendar with italian words
        self.__LSTEP = {'y': 'anno📅', 'm': 'mese🗓', 'd': 'giorno📆'}

    # Top level conversation callbacks

    def start(self, update: Update, context: CallbackContext) -> None:

        """SbaBot greetings message and general commands"""
        self.__contextDataInit(context)  # initializing/clearing user input data
        self.__deleteLastMessages(context, update)  # delete bot and user last sent messages

        # If we're starting over we don't need do send a greetings message
        if context.user_data.get(c.START_OVER):
            text = "Dimmi cosa fare👇"
            self.__sendMessage(context, text, keyboards.initial_keyboard)

        else:
            username = update.message.from_user.first_name
            startmsg = self.__greetings(username)
            sent_message = update.message.reply_text(text=startmsg, parse_mode=ParseMode.MARKDOWN,
                                                     disable_web_page_preview=True,
                                                     reply_markup=keyboards.initial_keyboard)
            context.user_data[c.MSG_ID] = sent_message.message_id

        return c.SELECTING_OPTION

    def autofiller_options(self, update: Update, context: CallbackContext) -> None:

        print("ciao")

        context.user_data[c.NEW_USER] = 1
        update.callback_query.answer()
        text = "Dimmi cosa fare👇"
        keyboard = keyboards.subKeyboard
        self.__editMessage(update, text, keyboard)

        return c.COLLECT_HALL_INFO

    def ask_for_date(self, update: Update, context: CallbackContext) -> None:

        context.user_data[c.NEW_USER] = 0
        calendar, step, = DetailedTelegramCalendar().build()
        text = f'Seleziona {self.__LSTEP[step]}'
        self.__editMessage(update, text, calendar)
        return c.COLLECT_DATE

    def date_handler(self, update: Update, context: CallbackContext) -> None:

        query = update.callback_query
        querydata = query.data
        result, key, step = DetailedTelegramCalendar().process(querydata)

        # scelta anno, mese, giorno
        if not result and key:
            text = f'Seleziona {self.__LSTEP[step]}'
            keyboard = key
            self.__editMessage(update, text, keyboard)
            return c.COLLECT_DATE

        # strada intrapresa dopo la scelta del giorno
        else:

            res = str(result)  # data scelta dall'utente = str(result)
            parsedRes = date_parser.dateParser(res)

            context.user_data[c.MONTH] = parsedRes[0]
            context.user_data[c.DAY] = parsedRes[1]

            text = f"Hai selezionato {result} \n Dimmi cosa fare👇"
            keyboard = keyboards.dateConfirmationKeyboard

        self.__editMessage(update, text, keyboard)

        return c.COLLECT_HALL_INFO

    def ask_for_hall(self, update: Update, context: CallbackContext) -> None:

        query = update.callback_query
        querydata = query.data
        level = str(querydata)

        if level == c.MODIFY:
            context.user_data[c.NEW_USER] = 2

        text = "Comincia scegliendo l'aula📄"
        keyboard = keyboards.hallsKeyboard
        self.__editMessage(update, text, keyboard)

        return c.COLLECT_USER_DATA

    def hall_confirmation(self, update: Update, context: CallbackContext) -> None:

        query = update.callback_query
        querydata = int(query.data)

        print(keyboards.halls[querydata])
        hall = keyboards.halls[querydata]
        context.user_data[c.HALL] = hall

        if context.user_data[c.NEW_USER] == 1:
            keyboard = keyboards.subHallConfirmationKeyboard

        else:
            keyboard = keyboards.bookHallConfirmationKeyboard

        text = f"Aula scelta : {hall}\nOra ti chiederò alcune informazioni personali🛂, fammi sapere se hai cambiato idea!"
        self.__editMessage(update, text, keyboard)

        return c.COLLECT_ID

    def ask_for_id(self, update: Update, context: CallbackContext) -> None:

        text = "Inserisci la tua matricola 📇:"
        self.__editMessage(update, text)

        # next state in conversation
        return c.COLLECT_PASSWORD

    def ask_for_password(self, update: Update, context: CallbackContext) -> None:
        self.__deleteLastMessages(context, update)

        if self.__check_id(update.message.text):
            context.user_data[c.ID] = int(update.message.text)
            text = "Scrivimi la tua password 🔐"
            self.__sendMessage(context, text)
            return c.DATA_CONFIRMATION

        else:
            text = "Codice Matricola non valido! 🥴\nScrivimi il tuo codice matricola🔢"
            self.__sendMessage(context, text)
            return c.COLLECT_PASSWORD

    def __check_id(self, id):
        try:
            if 5000000 <= int(id) < 8000000:
                return True
            else:
                raise Exception

        except Exception:
            return False

    def confirm_data(self, update: Update, context: CallbackContext) -> None:

        self.__deleteLastMessages(context, update)
        context.user_data[c.PW] = update.message.text

        msg = """Ecco i tuoi dati, sono giusti?

✍Biblioteca: {}
✍Aula: {}
✍Mese: {}
✍Giorno: {}
✍Matricola: {}
✍Password: {}

"Dimmi cosa fare👇""".format(context.user_data[c.LIBRARY], context.user_data[c.HALL], context.user_data[c.MONTH],
                             context.user_data[c.DAY], context.user_data[c.ID],
                             context.user_data[c.PW])

        if context.user_data[c.NEW_USER] > 0:
            keyboard = keyboards.subConfirmationKeyboard
            self.__sendMessage(context, msg, keyboard)
            return c.ADD_USER_TO_DATABASE
        else:
            keyboard = keyboards.bookConfirmationKeyboard
            self.__sendMessage(context, msg, keyboard)
            return c.BOOKING_CONFIRMATION

    def update_database(self, update: Update, context: CallbackContext) -> None:

        users = UsersDatabase.get_users()
        user_id = [i['user_id'] for i in users]
        students_ids = [j['CodMatricola'] for j in users]
        user_flag = context.user_data[c.NEW_USER]

        chat_id = str(context.user_data[c.CHAT_ID])
        student_id = str(context.user_data[c.ID])
        password = context.user_data[c.PW]
        library = context.user_data[c.LIBRARY]
        hall = context.user_data[c.HALL]

        # user requests to sub but it's already in sss
        if chat_id in user_id and user_flag == 1 and student_id in students_ids:
            text = "Sei già registrato!😅, cosa vuoi fare?"
            keyboard = keyboards.modifySubKeyboard
            self.__editMessage(update, text, keyboard)
            context.user_data[c.NEW_USER] = 0

            return c.MODIFY_DATA

        else:

            # modify user data in sss
            if chat_id in user_id and user_flag == 2 and student_id in students_ids:
                UsersDatabase.delete_user(student_id)
                UsersDatabase.add_user(student_id, password, library, hall, chat_id)

                text = "Registrazione completata ✔️i dati sono stati modificati correttamente, alle 00:00 avverà la prima prenotazione!"

            # user requests to modify data but it's unregistered
            if (chat_id not in user_id or student_id not in students_ids) and user_flag == 2:
                UsersDatabase.add_user(student_id, password, library, hall, chat_id)

                text = "Non eri iscritto! Non ti preoccupare, registrazione completata ✔️alle 00:00 avverà la prima prenotazione!"

            # new user in sss
            if student_id not in students_ids and user_flag == 1:
                UsersDatabase.add_user(student_id, password, library, hall, chat_id)

                text = "Registrazione completata ✔️alle 00:00 avverà la prima prenotazione!"

            keyboard = keyboards.completedActionKeyboard
            self.__editMessage(update, text, keyboard)
            return c.END

    def modify_user_data(self, update: Update, context: CallbackContext) -> None:

        users = UsersDatabase.get_users()
        students_ids = [i['CodMatricola'] for i in users]

        chat_id = str(context.user_data[c.CHAT_ID])
        student_id = str(context.user_data[c.ID])
        password = context.user_data[c.PW]
        library = context.user_data[c.LIBRARY]
        hall = context.user_data[c.HALL]

        if student_id in students_ids:
            UsersDatabase.delete_user(student_id)

        UsersDatabase.add_user(student_id, password, library, hall, chat_id)

        text = "Registrazione completata 🤙 \n Ho modificato i tuoi dati ✔️alle 00:00 avverà la prima prenotazione!"
        keyboard = keyboards.completedActionKeyboard
        self.__editMessage(update, text, keyboard)

        return c.END

    def id_to_delete(self, update: Update, context: CallbackContext) -> None:

        text = "Inserisci il tuo codice matricola👇:"
        # update.callback_query.answer()
        self.__editMessage(update, text)

        return c.DELETE_USER

    def delete_user(self, update: Update, context: CallbackContext) -> None:

        self.__deleteLastMessages(context, update)

        users = UsersDatabase.get_users()
        matricola = update.message.text
        matricole = [i['CodMatricola'] for i in users]

        if matricola in matricole:

            UsersDatabase.delete_user(matricola)
            text = "Utente disiscritto😕"
            keyboard = keyboards.completedActionKeyboard

        else:

            text = "Matricola non trovata😵\n\n✋Ti sei iscritto/a? Hai sbagliato numero?✋\n"
            keyboard = keyboards.idNotFoundKeyboard

        self.__sendMessage(context, text, keyboard)

        return c.DELETE_USER

    def reserve_seat(self, update: Update, context: CallbackContext) -> None:

        text = "🎛Sto prenotando..🎛"
        self.__editMessage(update, text)

        student_id = context.user_data[c.ID]
        password = context.user_data[c.PW]
        library = context.user_data[c.LIBRARY]
        hall = context.user_data[c.HALL]
        day = context.user_data[c.DAY]
        month = context.user_data[c.MONTH]

        val = single_booking.fillerUserData(library, hall, day, month, student_id, password)

        keyboard = keyboards.completedActionKeyboard

        if val:
            msg = "Posti esauriti o non disponibili!🙁"

        else:
            msg = "Prenotazione confermata🤩🔁"

        self.__editMessage(update, msg, keyboard)

        time.sleep(3)
        # sent_message = update.message.reply_text("🤔Cosa vuoi fare?🤔", reply_markup = keyboard)
        # telegram.bot.Bot.delete_message(context.bot,chat_id=context.user_data[CHAT_ID], message_id=context.user_data[MSG_ID])

        # context.user_data[c.MSG_ID] = sent_message.message_id

        return c.END

    def get_user_info(self, update: Update, context: CallbackContext) -> None:

        student_id = context.user_data[c.CHAT_ID]
        user_info = UsersDatabase.get_user(student_id)

        text = "Ecco i tuoi dati: \n\n"

        for sub in user_info:
            msg = """⚈Matricola: {}
⚈Password: {}
⚈Biblioteca: {}
⚈Aula: {}
---------------------------------------
""".format(sub["CodMatricola"], sub["Password"], sub["Biblioteca"], sub["Aula"])
            text = text + msg

        keyboard = keyboards.completedActionKeyboard
        self.__editMessage(update, text, keyboard)

    def back_to_main_menu(self, update: Update, context: CallbackContext) -> None:
        """Return to main menu"""
        context.user_data[c.START_OVER] = True
        self.start(update, context)

        return c.SELECTING_OPTION

    def stop_nested(self, update: Update, context: CallbackContext) -> None:

        self.__deleteLastMessages(context, update)

        context.user_data[c.START_OVER] = False

        text = 'Okay, bye.'
        self.__sendMessage(context, text)

        return c.STOPPING

    def stop_bot(self, update: Update, context: CallbackContext) -> None:
        """Completely end conversation"""

        self.__deleteLastMessages(context, update)

        context.user_data[c.START_OVER] = False

        text = 'Okay, bye.'
        self.__sendMessage(context, text)

        return c.END

    def end(self, update: Update, context: CallbackContext) -> None:
        """End conversation from InlineKeyboardButton."""
        context.user_data[c.START_OVER] = False

        text = 'See you around!'
        self.__editMessage(update, text)

        return c.END

    def __contextDataInit(self, context: CallbackContext) -> None:

        context.user_data[c.LIBRARY] = "Lettere"
        context.user_data[c.DAY] = "❌"
        context.user_data[c.MONTH] = "❌"
        context.user_data[c.ID] = 0000000
        context.user_data[c.NEW_USER] = 0

    def __deleteLastMessages(self, context: CallbackContext, update: Update) -> None:

        if c.CHAT_ID not in context.user_data:
            context.user_data[c.CHAT_ID] = update.message.chat_id
            # delete user's last message
            Bot.delete_message(context.bot, chat_id=update.message.chat_id, message_id=update.message.message_id)
        else:
            # delete bot's last message
            Bot.delete_message(context.bot, chat_id=context.user_data[c.CHAT_ID],
                               message_id=context.user_data[c.MSG_ID])
            try:
                # delete user's last message, if present
                Bot.delete_message(context.bot, chat_id=update.message.chat_id, message_id=update.message.message_id)
            except:
                pass

    def __greetings(self, username):

        str1 = "*Ciao {} 👋*\n".format(username)
        str2 = """
Con questo bot è possibile prenotare un posto della Biblioteca Umanistica📚 in modo automatico 

I comandi sono estremamente semplici ed intuitivi 😎

*Comandi del bot*
➛/start - Messaggio di Benvenuto 👋
➛*Prenota* - Cliccami per prenotare 🚀
➛*Iscriviti*- Cliccami per attivare le prenotazioni automatiche
➛*Elimina iscrizione* - Cliccami per disattivare le prenotazioni automatiche
➛*Info iscrizione* - Cliccami per visualizzare la/le tue prenotazioni attive
➛/stop - Cliccami per arrestare il bot


📴*Spegnimento/riavvio bot*📴
In ogni momento di utilizzo,in caso di malfunzionamento o errore di battitura, digita /stop per arrestare il bot
➡➡➡/stop⬅⬅⬅


🎛*Prenotazioni automatiche*🎛

Una volta cliccato *Prenota* potrai utilizzare i seguenti bottoni :

📅 *Cambia data* - Riscegli la data

🔬 *Scelta aula* - Cliccami per selezionare l'aula

📴 *Arresta Bot* - Cliccami per arrestare il bot, /start per riavviarlo

💡*About me*💡
Questo bot è basato sui dati dell' [SBA](https://www.sbafirenze.it/tools/)
Se hai bisogno, [contattarmi](https://t.me/pepsikoi)
            """

        return str1 + str2

    def __sendMessage(self, context: CallbackContext, text, keyboard=None) -> None:
        sent_message = context.bot.send_message(chat_id=context.user_data[c.CHAT_ID], text=text, reply_markup=keyboard)
        context.user_data[c.MSG_ID] = sent_message.message_id

    def __editMessage(self, update: Update, text, keyboard=None) -> None:
        update.callback_query.answer()
        update.callback_query.edit_message_text(text=text, reply_markup=keyboard)
