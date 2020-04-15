# Copyright (C) 2015-2020 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).

import logging
from contextvars import ContextVar
from typing import List, Optional

from . import bot, api, executors

current_executor = ContextVar('current_executor')
current_bot = ContextVar('current_bot')
current_webhook_requests = ContextVar('current_webhook_requests')

current_update = ContextVar('current_update')
current_message = ContextVar('current_message')
current_chat = ContextVar('current_chat')
current_user = ContextVar('current_user')

logger = logging.getLogger('rocketgram.context')


class Context:
    __slots__ = tuple()

    @property
    def executor(self) -> Optional['executors.Executor']:
        """Returns Executor object for current request."""

        return current_executor.get(None)

    @executor.setter
    def executor(self, executor: 'executors.Executor'):
        current_executor.set(executor)

    @property
    def bot(self) -> Optional['bot.Bot']:
        """Returns current Bot object."""

        return current_bot.get(None)

    @bot.setter
    def bot(self, bot: 'bot.Bot'):
        current_bot.set(bot)

    @property
    def update(self) -> Optional['api.Update']:
        """Returns Update object for current request."""

        return current_update.get(None)

    @update.setter
    def update(self, update: 'api.Update'):
        current_update.set(update)

    @property
    def message(self) -> Optional['api.Message']:
        """Returns Message object for current request."""

        return current_message.get(None)

    @message.setter
    def message(self, update: 'api.Message'):
        current_message.set(update)

    @property
    def chat(self) -> Optional['api.Chat']:
        """Returns Chat object for current request."""

        return current_chat.get(None)

    @chat.setter
    def chat(self, chat: 'api.Chat'):
        current_chat.set(chat)

    @property
    def user(self) -> Optional['api.User']:
        """Returns User object for current request."""

        return current_user.get(None)

    @user.setter
    def user(self, user: 'api.User'):
        current_user.set(user)

    @staticmethod
    def webhook(request: 'api.Request'):
        """Sets Request object to be sent through webhook-request mechanism."""

        current_webhook_requests.get().append(request)

    @property
    def webhook_requests(self) -> List['api.Request']:
        """Returns list of current requests awaits sent through webhook-request mechanism."""

        return current_webhook_requests.get()

    @webhook_requests.setter
    def webhook_requests(self, webhook_requests):
        """Returns list of current requests awaits sent through webhook-request mechanism."""

        current_webhook_requests.set(webhook_requests)


context = Context()
del Context
