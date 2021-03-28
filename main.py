# -*- coding: utf-8 -*-
"""
@author: pablo

"""

# From env

from telegram.ext import CommandHandler, CallbackQueryHandler, ConversationHandler, MessageHandler, Filters
from telegram_bot_calendar import DetailedTelegramCalendar
import logging

from utils import const as c
from BotClass import SbaBot

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

logger = logging.getLogger(__name__)


def main():
    # Create the Updater and pass it your bot's token.
    TOKEN = "your token here"

    bot = SbaBot(TOKEN)

    # Set up third level ConversationHandler (collecting sub/booking features)
    add_user_to_database = ConversationHandler(
        entry_points=[CallbackQueryHandler(bot.update_database, pattern='^' + str(c.COMPLETE_SUB) + '$')],

        states={
            c.MODIFY_DATA: [CallbackQueryHandler(bot.modify_user_data, pattern='^' + str(c.MODIFY) + '$')],
            c.END: [bot.end]
        },

        fallbacks=[CallbackQueryHandler(bot.back_to_main_menu, pattern='^' + str(c.BACK) + '$'),
                   CommandHandler('stop', bot.stop_nested),
                   ],

        map_to_parent={
            c.BACK: c.BACK,
            c.STOPPING: c.STOPPING,
        },

    )

    delete_user_from_db = ConversationHandler(
        entry_points=[MessageHandler(Filters.text & ~Filters.command, bot.delete_user)],

        states={
            c.DELETE_USER: [CallbackQueryHandler(bot.id_to_delete, pattern='^' + str(c.DELETE_SUB) + '$')],
        },

        fallbacks=[
            # CallbackQueryHandler(bot.back_to_main_menu, pattern='^' + str(c.BACK) + '$'),
            # CommandHandler('stop', bot.stop_nested),
        ],

        map_to_parent={
            c.DELETE_USER: c.DELETE_USER,
            c.END: c.END,
            c.STOPPING: c.END,

        },

    )

    # Set up second level ConversationHandler (sub to Sba Autofiller)
    collect_user_data = ConversationHandler(
        entry_points=[CallbackQueryHandler(bot.hall_confirmation, pattern='[0-9]+$')],

        states={
            c.COLLECT_NAME: [CallbackQueryHandler(bot.ask_for_name, pattern='^' + str(c.CONFIRM_HALL) + '$')],
            c.COLLECT_EMAIL: [MessageHandler(Filters.text & ~Filters.command, bot.ask_for_email)],
            c.COLLECT_ID: [MessageHandler(Filters.text & ~Filters.command, bot.ask_for_id)],
            c.COLLECT_PHONE: [MessageHandler(Filters.text & ~Filters.command, bot.ask_for_phone)],
            c.DATA_CONFIRMATION: [MessageHandler(Filters.text & ~Filters.command, bot.confirm_data)],
            c.ADD_USER_TO_DATABASE: [add_user_to_database],
            c.BOOKING_CONFIRMATION: [CallbackQueryHandler(bot.reserve_seat, pattern='^' + str(c.BOOK) + '$')],
        },
        fallbacks=[
            CallbackQueryHandler(bot.back_to_main_menu, pattern='^' + str(c.BACK) + '$'),
            CallbackQueryHandler(bot.autofiller_options, pattern='^' + str(c.SUB_MENU) + '$'),
            # CallbackQueryHandler(bot.autofiller_options, pattern='^' + str(c.RESTART) + '$'),
            CallbackQueryHandler(bot.ask_for_hall, pattern='^' + str(c.CHANGE_HALL) + '$'),
            CallbackQueryHandler(bot.ask_for_name, pattern='^' + str(c.CONFIRM_HALL) + '$'),
            CommandHandler('stop', bot.stop_nested),
        ],
        map_to_parent={
            # Return to top level menu
            c.END: c.COLLECT_HALL_INFO,

            # End conversation alltogether
            c.SELECTING_OPTION: c.SELECTING_OPTION,
            c.STOPPING: c.END,
            c.COLLECT_HALL_INFO: c.COLLECT_HALL_INFO,
            c.COLLECT_USER_DATA: c.COLLECT_USER_DATA,
        },
    )

    # Set up top level ConversationHandler (selecting main command)
    # Because the states of the third level conversation map to the ones of the second level
    # conversation, we need to make sure the top level conversation can also handle them
    user_info_handlers = [
        collect_user_data,
    ]

    delete_user_handlers = [
        delete_user_from_db,
    ]

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', bot.start)],
        states={
            c.SELECTING_OPTION: [
                CallbackQueryHandler(bot.autofiller_options, pattern='^' + str(c.SUB) + '$'),
                CallbackQueryHandler(bot.ask_for_date, pattern='^' + str(c.BOOK) + '$'),
                CallbackQueryHandler(bot.id_to_delete, pattern='^' + str(c.DELETE_SUB) + '$'),
                CallbackQueryHandler(bot.end, pattern='^' + str(c.END) + '$'),
                CallbackQueryHandler(bot.get_user_info, pattern='^' + str(c.SHOW_INFO) + '$')

            ],
            c.COLLECT_HALL_INFO: [CallbackQueryHandler(bot.ask_for_hall,
                                                       pattern='^' + str(c.MODIFY) + '$|^' + str(
                                                           c.NEW_SUB) + '$|^' + str(c.SELF_SUB) + '$|^' + str(
                                                           c.COLLECT_HALL_INFO) + '$')],
            c.COLLECT_USER_DATA: user_info_handlers,
            c.COLLECT_DATE: [CallbackQueryHandler(bot.date_handler, DetailedTelegramCalendar().func())],
            c.DELETE_USER: delete_user_handlers,
            c.STOPPING: [CommandHandler('start', bot.start)],

        },

        fallbacks=[CommandHandler('stop', bot.stop_bot),
                   CallbackQueryHandler(bot.autofiller_options, pattern='^' + str(c.SUB) + '$'),
                   CallbackQueryHandler(bot.ask_for_hall, pattern='^' + str(c.MODIFY) + '$'),
                   CallbackQueryHandler(bot.end, pattern='^' + str(c.END) + '$'),
                   CallbackQueryHandler(bot.back_to_main_menu, pattern='^' + str(c.BACK) + '$'),
                   CallbackQueryHandler(bot.ask_for_date, pattern='^' + str(c.BOOK) + '$'),
                   ]

    )

    bot.dispatcher.add_handler(conv_handler)

    bot.updater.start_polling()

    bot.updater.idle()


if __name__ == '__main__':
    main()
