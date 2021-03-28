# -*- coding: utf-8 -*-
"""
@author: pablo

"""

from telegram.ext import ConversationHandler


# different constants to easily store user data in context.user_data (persistent dict across conversations)
(
    CHAT_ID,
    MSG_ID,     #bot's message id, useful for deleting it via delete_message
    MAIL,
    LIBRARY,
    HALL,
    MONTH,
    DAY,
    NAME,
    ID,         #student's "codice matricola"
    PHONE,
    START_OVER,
    NEW_USER,
) = map(chr, range(12))

# Meta state
STOPPING = map(chr, range(12, 13))
# Shortcut for ConversationHandler.END
END = ConversationHandler.END

# State definitions for top level conversation
SELECTING_OPTION,COLLECT_HALL_INFO,COLLECT_USER_DATA,COLLECT_DATE,DELETE_USER = map(chr, range(13, 18))

# State definitions for second and third level conversations
MODIFY_DATA, RESTART, BOOKING_CONFIRMATION, ADD_USER_TO_DATABASE, DATA_CONFIRMATION, COLLECT_PHONE, COLLECT_ID, COLLECT_EMAIL, COLLECT_NAME = map(chr, range(18, 27))

# different constants for buttons callbacks
SHOW_INFO, BACK, CONFIRM_HALL,BOOK, DELETE_SUB, MODIFY, NEW_SUB, SELF_SUB, SUB, CHANGE_HALL, SEATS_LEFT , COMPLETE_SUB, SUB_MENU,  = map(chr, range(27, 40))
