# Copyright (C) 2015-2020 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional

from .photo_size import PhotoSize


@dataclass(frozen=True)
class Video:
    """\
    Represents Video object:
    https://core.telegram.org/bots/api#video
    """

    file_id: str
    file_unique_id: str
    width: int
    height: int
    duration: int
    thumb: Optional[PhotoSize]
    mime_type: Optional[str]
    file_size: Optional[int]

    @classmethod
    def parse(cls, data: dict) -> Optional['Video']:
        if data is None:
            return None

        return cls(data['file_id'], data['file_unique_id'], data['width'], data['height'], data['duration'],
                   PhotoSize.parse(data.get('thumb')), data.get('mime_type'), data.get('file_size'))
