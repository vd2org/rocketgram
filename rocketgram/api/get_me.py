# Copyright (C) 2015-2020 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass

from .request import Request
from .. import api


@dataclass(frozen=True)
class GetMe(Request):
    """\
    Represents GetMe request object:
    https://core.telegram.org/bots/api#getme
    """

    def parse_result(self, data) -> 'api.User':
        assert isinstance(data, dict), "Should be dict."
        return api.User.parse(data)

    async def send2(self) -> 'api.User':
        res = await self._send()
        return res.result
