# Copyright (C) 2015-2020 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Union, Optional

from .request import Request
from .utils import BoolResultMixin


@dataclass(frozen=True)
class PromoteChatMember(BoolResultMixin, Request):
    """\
    Represents PromoteChatMember request object:
    https://core.telegram.org/bots/api#promotechatmember
    """

    chat_id: Union[int, str]
    user_id: int
    can_change_info: Optional[bool] = None
    can_post_messages: Optional[bool] = None
    can_edit_messages: Optional[bool] = None
    can_delete_messages: Optional[bool] = None
    can_invite_users: Optional[bool] = None
    can_restrict_members: Optional[bool] = None
    can_pin_messages: Optional[bool] = None
    can_promote_members: Optional[bool] = None
