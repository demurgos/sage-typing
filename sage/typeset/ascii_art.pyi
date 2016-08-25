from typing import Any

import sage.typeset.character_art


class AsciiArt(sage.typeset.character_art.CharacterArt):
    pass


def ascii_art(*obj: Any, **kwds: Any) -> AsciiArt : ...
