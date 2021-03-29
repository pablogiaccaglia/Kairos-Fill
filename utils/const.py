# -*- coding: utf-8 -*-
"""
@author: pablo

"""

from telegram.ext import ConversationHandler


# different constants to easily store user data in context.user_data (persistent dict across conversations)
(
    CHAT_ID,
    MSG_ID,     #bot's message id, useful for deleting it via delete_message
    LIBRARY,
    HALL,
    MONTH,
    DAY,
    ID,         #student's "codice matricola"
    PW,
    START_OVER,
    NEW_USER,
) = map(chr, range(10))

# Meta state
STOPPING = map(chr, range(10, 11))
# Shortcut for ConversationHandler.END
END = ConversationHandler.END

# State definitions for top level conversation
SELECTING_OPTION, COLLECT_HALL_INFO, COLLECT_USER_DATA, COLLECT_DATE, DELETE_USER = map(chr, range(11, 16))

# State definitions for second and third level conversations
MODIFY_DATA, RESTART, BOOKING_CONFIRMATION, ADD_USER_TO_DATABASE, DATA_CONFIRMATION, COLLECT_PASSWORD, COLLECT_ID, COLLECT_NAME = map(chr, range(16, 24))

# different constants for buttons callbacks
SHOW_INFO, BACK, CONFIRM_HALL, BOOK, DELETE_SUB, MODIFY, NEW_SUB, SELF_SUB, SUB, CHANGE_HALL, SEATS_LEFT, COMPLETE_SUB, SUB_MENU,  = map(chr, range(24, 37))
