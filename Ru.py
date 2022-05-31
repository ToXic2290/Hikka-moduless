# meta developer: @ToXicUse

import logging

from .. import loader, utils

logger = logging.getLogger(__name__)


@loader.tds
class MorzeMod(loader.Module):
    """Конвертация текста на норм язык"""

    strings = {"name": "Tss..."}

    @loader.unrestricted
    async def xxcmd(self, message):
        """.xx [реплай или текст]"""
        de = {
            "А": "f",
            "Б": ",",
            "В": "d",
            "Г": "u",
            "Д": "l",
            "Е": "t",
            "Ж": ";",
            "З": "p",
            "И": "b",
            "Й": "q",
            "К": "r",
            "Л": "k",
            "М": "v",
            "Н": "y",
            "О": "j",
            "П": "g",
            "Р": "h",
            "С": "c",
            "Т": "n",
            "У": "e",
            "Ф": "a",
            "Х": "[",
            "Ц": "w",
            "Ч": "x",
            "Ш": "i",
            "Щ": "o",
            "Ъ": "]",
            "Ы": "s",
            "Ь": "m",
            "Э": "'",
            "Ю": ".",
            "Я": "z",
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
        for word in text.split():

            for letter in word.upper():
                x += de[letter]
            x += ""
        await message.edit(x)

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
            x += ""
        await message.edit(x)
