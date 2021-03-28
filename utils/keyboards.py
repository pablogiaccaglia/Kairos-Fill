# -*- coding: utf-8 -*-
"""
@author: pablo

"""
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from collections import namedtuple
import const as c

indiciAulee = namedtuple("indiciAulee", "field1 field2")

i0 = indiciAulee(field1='Posti studio atrio primo piano', field2=0)
i1 = indiciAulee(field1='Posti studio atrio secondo piano', field2=1)
i2 = indiciAulee(field1='Posti studio corridoi antichistica secondo piano', field2=2)
i3 = indiciAulee(field1='Posti studio corridoio lingue primo piano', field2=3)
i4 = indiciAulee(field1='Posti studio corridoio linguistica secondo piano', field2=4)
i5 = indiciAulee(field1='Posti studio corridoio neolatine piano terra', field2=5)
i6 = indiciAulee(field1='Posti studio corridoio paleografia primo piano', field2=6)
i7 = indiciAulee(field1='Posti studio Sala A secondo piano', field2=7)
i8 = indiciAulee(field1='Posti studio Sala C secondo piano', field2=8)
i9 = indiciAulee(field1='Posti studio Sala D secondo piano', field2=9)
i10 = indiciAulee(field1='Posti studio SALA M primo piano', field2=10)
i11 = indiciAulee(field1='Sala archeologia', field2=11)
i12 = indiciAulee(field1='Sala CEDAF', field2=12)
i13 = indiciAulee(field1='Sala dialettologia', field2=13)
i14 = indiciAulee(field1='Sala E secondo piano', field2=14)
i15 = indiciAulee(field1='Sala filologia classica-storia antica', field2=15)
i16 = indiciAulee(field1='Sala filosofia 1', field2=16)
i17 = indiciAulee(field1='Sala filosofia 2', field2=17)
i18 = indiciAulee(field1='Sala francese', field2=18)
i19 = indiciAulee(field1='Sala germanistica', field2=19)
i20 = indiciAulee(field1='Sala italianistica e spettacolo', field2=20)
i21 = indiciAulee(field1='Sala lingue straniere', field2=21)
i22 = indiciAulee(field1='Sala linguistica', field2=22)
i23 = indiciAulee(field1='Sala medioevo e rinascimento', field2=23)
i24 = indiciAulee(field1='Sala orientalistica', field2=24)
i25 = indiciAulee(field1='Sala riviste linguistica', field2=25)
i26 = indiciAulee(field1='Sala russo', field2=26)
i27 = indiciAulee(field1='Sala scandinavistica', field2=27)
i28 = indiciAulee(field1='Sala slavistica', field2=28)
i29 = indiciAulee(field1='Sala spagnolo 1', field2=29)
i30 = indiciAulee(field1='Sala spagnolo 2', field2=30)
i31 = indiciAulee(field1='Sala storia', field2=31)

indici = [i0, i1, i2, i3, i4, i5, i6, i7, i8, i9, i10, i11, i12, i13, i14, i15, i16, i17, i18, i19, i20, i21, i22, i23,
          i24, i25, i26, i27, i28, i29, i30, i31]

halls = ['Posti studio atrio primo piano', 'Posti studio atrio secondo piano',
        'Posti studio corridoi antichistica secondo piano', 'Posti studio corridoio lingue primo piano',
        'Posti studio corridoio linguistica secondo piano',
        'Posti studio corridoio neolatine piano terra', 'Posti studio corridoio paleografia primo piano',
        'Posti studio Sala A secondo piano', 'Posti studio Sala C secondo piano', 'Posti studio Sala D secondo piano',
        'Posti studio SALA M primo piano', 'Sala archeologia', 'Sala CEDAF', 'Sala dialettologia',
        'Sala E secondo piano', 'Sala filologia classica-storia antica', 'Sala filosofia 1', 'Sala filosofia 2',
        'Sala francese', 'Sala germanistica',
        'Sala italianistica e spettacolo', 'Sala lingue straniere', 'Sala linguistica', 'Sala medioevo e rinascimento',
        'Sala orientalistica', 'Sala riviste linguistica', 'Sala russo', 'Sala scandinavistica', 'Sala slavistica',
        'Sala spagnolo 1', 'Sala spagnolo 2', 'Sala storia']

halls_buttons = [
         [InlineKeyboardButton(halls[0], callback_data='0')],
         [InlineKeyboardButton(halls[1], callback_data='1')],
         [InlineKeyboardButton(halls[2], callback_data='2')],
         [InlineKeyboardButton(halls[3], callback_data='3')],
         [InlineKeyboardButton(halls[4], callback_data='4')],
         [InlineKeyboardButton(halls[5], callback_data='5')],
         [InlineKeyboardButton(halls[6], callback_data='6')],
         [InlineKeyboardButton(halls[7], callback_data='7')],
         [InlineKeyboardButton(halls[8], callback_data='8')],
         [InlineKeyboardButton(halls[9], callback_data='9')],
         [InlineKeyboardButton(halls[10], callback_data='10')],
         [InlineKeyboardButton(halls[11], callback_data='11')],
         [InlineKeyboardButton(halls[12], callback_data='12')],
         [InlineKeyboardButton(halls[13], callback_data='13')],
         [InlineKeyboardButton(halls[14], callback_data='14')],
         [InlineKeyboardButton(halls[15], callback_data='15')],
         [InlineKeyboardButton(halls[16], callback_data='16')],
         [InlineKeyboardButton(halls[17], callback_data='17')],
         [InlineKeyboardButton(halls[18], callback_data='18')],
         [InlineKeyboardButton(halls[19], callback_data='19')],
         [InlineKeyboardButton(halls[20], callback_data='20')],
         [InlineKeyboardButton(halls[21], callback_data='21')],
         [InlineKeyboardButton(halls[22], callback_data='22')],
         [InlineKeyboardButton(halls[23], callback_data='23')],
         [InlineKeyboardButton(halls[24], callback_data='24')],
         [InlineKeyboardButton(halls[25], callback_data='25')],
         [InlineKeyboardButton(halls[26], callback_data='26')],
         [InlineKeyboardButton(halls[27], callback_data='27')],
         [InlineKeyboardButton(halls[28], callback_data='28')],
         [InlineKeyboardButton(halls[29], callback_data='29')],
         [InlineKeyboardButton(halls[30], callback_data='30')],
         [InlineKeyboardButton(halls[31], callback_data='31')]
]

MENU = 0

buttons = [
        InlineKeyboardButton("Scelta Aula", callback_data=str(c.COLLECT_HALL_INFO)),    #0
        InlineKeyboardButton("Cambio data", callback_data=str(c.BOOK)),                 #1
        InlineKeyboardButton("Disponibilità aulee", callback_data=str(c.SEATS_LEFT)),   #2
        InlineKeyboardButton("Arresta Bot", callback_data=str(c.END)),                  #3
        InlineKeyboardButton("Torna al Main Menu", callback_data=str(c.BACK)),          #4
        InlineKeyboardButton("Iscriviti", callback_data=str(c.SELF_SUB)),               #5
        InlineKeyboardButton("Iscrivi qualcuno", callback_data=str(c.NEW_SUB)),         #6
        InlineKeyboardButton("Modifica iscrizione", callback_data=str(c.MODIFY)),       #7
        InlineKeyboardButton("Prenota", callback_data=str(c.BOOK)),                     #8
        InlineKeyboardButton("Iscrizione", callback_data=str(c.SUB)),                   #9
        InlineKeyboardButton("Elimina iscrizione", callback_data=str(c.DELETE_SUB)),    #10
        InlineKeyboardButton("Info iscrizione", callback_data=str(c.SHOW_INFO)),        #11
        InlineKeyboardButton("Torna indietro", callback_data=str(c.BACK)),              #12
        InlineKeyboardButton("Conferma aula", callback_data=str(c.CONFIRM_HALL)),       #13
        InlineKeyboardButton("Cambia aula", callback_data=str(c.CHANGE_HALL)),          #14
        InlineKeyboardButton("Registrati", callback_data=str(c.COMPLETE_SUB)),          #15
        InlineKeyboardButton("Modifica dati", callback_data=str(c.CHANGE_HALL)),        #16
        InlineKeyboardButton("Ritorna al menu", callback_data=str(c.SUB_MENU)),         #17
        InlineKeyboardButton("Ritorna al Main Menu", callback_data=str(c.BACK)),        #18
        InlineKeyboardButton("Ritorna al Main Menu", callback_data=str(c.RESTART)),     #19
        InlineKeyboardButton("Riprova", callback_data=str(c.DELETE_SUB)),               #20
        InlineKeyboardButton("Torna indietro", callback_data=str(c.SUB_MENU)),          #21
]

custom_keyboard1 = [buttons[0], buttons[1], buttons[2], buttons[3], buttons[4]]
custom_keyboard2 = [buttons[8], buttons[9], buttons[10], buttons[11], buttons[3]]       #main menu keyboard
custom_keyboard3 = [buttons[5], buttons[6], buttons[7], buttons[3], buttons[4]]         #sub keyboard
custom_keyboard4 = [buttons[13], buttons[14], buttons[21]]                              #hall confirmation keyboard
custom_keyboard5 = [buttons[15], buttons[16], buttons[17]]
custom_keyboard6 = [buttons[8], buttons[16], buttons[4]]
custom_keyboard7 = [buttons[20], buttons[4], buttons[3]]
custom_keyboard8 = [buttons[18], buttons[3]]
custom_keyboard9 = [buttons[13], buttons[14], buttons[12]]
custom_keyboard10 = [buttons[7], buttons[3], buttons[4]]



def build_menu(buttonss, n_cols, header_buttons=None, footer_buttons=None):
    menu = [buttonss[i:i + n_cols] for i in range(0, len(buttonss), n_cols)]
    if header_buttons:
        menu.insert(0, [header_buttons])
    if footer_buttons:
        menu.append([footer_buttons])
    return menu


initial_keyboard = InlineKeyboardMarkup(build_menu(custom_keyboard2, n_cols=2), resize_keyboard=True)

subHallConfirmationKeyboard = InlineKeyboardMarkup(build_menu(custom_keyboard4, n_cols=2), resize_keyboard=True)
bookHallConfirmationKeyboard = InlineKeyboardMarkup(build_menu(custom_keyboard9, n_cols=2), resize_keyboard=True)
subConfirmationKeyboard = InlineKeyboardMarkup(build_menu(custom_keyboard5, n_cols=2), resize_keyboard=True)
bookConfirmationKeyboard = InlineKeyboardMarkup(build_menu(custom_keyboard6, n_cols=2), resize_keyboard=True)
idNotFoundKeyboard = InlineKeyboardMarkup(build_menu(custom_keyboard7, n_cols=2), resize_keyboard=True)
completedActionKeyboard = InlineKeyboardMarkup(build_menu(custom_keyboard8, n_cols=1), resize_keyboard=True)
dateConfirmationKeyboard = InlineKeyboardMarkup(build_menu(custom_keyboard1, n_cols=2), resize_keyboard=True)
hallsKeyboard = InlineKeyboardMarkup(halls_buttons)
subKeyboard = InlineKeyboardMarkup(build_menu(custom_keyboard3, n_cols=2), resize_keyboard=True)
modifySubKeyboard = InlineKeyboardMarkup(build_menu(custom_keyboard10, n_cols=2), resize_keyboard=True)
