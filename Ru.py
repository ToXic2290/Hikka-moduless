# meta developer: @ToXicUse

import logging

from .. import loader, utils

logger = logging.getLogger(__name__)


@loader.tds
class MorzeMod(loader.Module):
    """Конвертация текста на норм язык"""

    strings = {"name": "NormYazik"}


    @loader.unrestricted
    async def rucmd(self, message):
        """.ru [реплай или текст]"""

        en = {
            "f": "А",
            ",": "Б",
            "d": "В",
            "u": "Г",
            "l": "Д",
            "t": "Е",
            ";": "Ж",
            "p": "З",
            "b": "И",
            "q": "Й",
            "r": "К",
            "k": "Л",
            "v": "М",
            "y": "Н",
            "j": "О",
            "g": "П",
            "h": "Р",
            "c": "С",
            "n": "Т",
            "e": "У",
            "a": "Ф",
            "[": "Х",
            "w": "Ц",
            "x": "Ч",
            "i": "Ш",
            "o": "Щ",
            "]": "Ъ",
            "s": "Ы",
            "m": "Ь",
            "'": "Э",
            ".": "Ю",
            "z": "Я",
        }

        reply = await message.get_reply_message()
        text = utils.get_args_raw(message)

        if reply and not text:
            text = reply.raw_text
        if not text:
            return await utils.answer(
                message, "<code>Вы не ввели текст или не сделали реплай.</code>"
            )
        x = ""
        for word in text.split("  "):

            for letter in word.split():
                x += en[letter].lower()
            x += " "
        await message.edit(x)
