#               _             __  __           _       _
#     /\       | |           |  \/  |         | |     | |
#    /  \   ___| |_ _ __ ___ | \  / | ___   __| |_   _| | ___  ___
#   / /\ \ / __| __| '__/ _ \| |\/| |/ _ \ / _` | | | | |/ _ \/ __|
#  / ____ \\__ \ |_| | | (_) | |  | | (_) | (_| | |_| | |  __/\__ \
# /_/    \_\___/\__|_|  \___/|_|  |_|\___/ \__,_|\__,_|_|\___||___/
#
#               © Copyright 2022
#
#      https://t.me/Den4ikSuperOstryyPer4ik
#                      and
#             https://t.me/ToXicUse
#
#       🔒 Licensed under the GNU AGPLv3
#    https://www.gnu.org/licenses/agpl-3.0.html
# meta developer: @AstroModules

from .. import loader, utils
import time
from time import sleep

@loader.tds
class TwinkManagerMod(loader.Module):
    """Менеджер для управления твинками 

    Version: 0.0.1 ~beta"""

    strings = {
    	"name": "Twink-Manager",
    	"first_prefix": "Префикс первого твинка",
    	"second_prefix": "Префикс второго твинка",
        "command_for_you": "Вы хотите чтобы все команды выполнялись также и на вашем основном аккаунте?"
    }

    def __init__(self):
        self.config = loader.ModuleConfig(
            loader.ConfigValue(
                "1-prefix",
                "!",
                doc=lambda: self.strings("first_prefix"),
            ),
            loader.ConfigValue(
                "2-prefix",
                "None",
                doc=lambda: self.strings("second_prefix"),
            ),
            loader.ConfigValue(
                "all_accounts",
                False,
                doc=lambda: self.strings("command_for_you"),
                validator=loader.validators.Boolean(),
            ),
        )

    @loader.command()
    async def trestartcmd(self, message):
        """- Перезагрузить аккаунты"""
        restart = "restart --force"
        prf1 = self.config['1-prefix']
        prf2 = self.config['2-prefix']
        MyAcc = self.config['you_account']
        if MyAcc == "False":
            if prf1 == "None":
                await message.edit("В конфиге не найден первый префикс.\nПожалуйста, заполните конфиг")
            if prf2 == "None":
                await message.edit(f"{prf1}{restart}")
                sleep(0.5)
                await message.edit('🕘 <em>Выполняется перезагрузка ваших твинков...</em>')
            else:
                await message.edit(f"{prf1}{restart}")
                await message.edit(f"{prf2}{restart}")
                sleep(0.5)
                await message.edit('🕘 <em>Выполняется перезагрузка ваших твинков...</em>')

        else:
            if prf1 == "None":
                await message.edit("❗️ В конфиге не найден первый префикс.\nПожалуйста, заполните конфиг")
            if prf2 == "None":
                await message.edit(f"{prf1}{restart}")
                sleep(0.5)
                await self.allmodules.commands["restart"](
                    await utils.answer(message, f"{self.get_prefix()}{restart}")
                )
            else:
                await message.edit(f"{prf1}{restart}")
                await message.edit(f"{prf2}{restart}")
                sleep(0.5)
                await self.allmodules.commands["restart"](
                    await utils.answer(message, f"{self.get_prefix()}{restart}")
                )

    @loader.command()
    async def tpingcmd(self, message):
        """- Проверить пинг на аккаунтах"""
        ping = "ping"
        prf1 = self.config['1-prefix']
        prf2 = self.config['2-prefix']
        MyAcc = self.config['you_account']
        if MyAcc == False:
            if prf1 == None:
                await message.edit("❗️ В конфиге не найден первый префикс.\nПожалуйста, заполните конфиг")
            if prf2 == None:
                await message.edit(f"{prf1}{ping}")
                sleep(0.5)
                await message.edit('✅ <em>Проверка пинга завершена</em>')
            else:
                await message.edit(f"{prf1}{ping}")
                await message.edit(f"{prf2}{ping}")
                sleep(0.5)
                await message.edit('✅ <em>Проверка пинга завершена</em>')

        else:
            if prf1 == None:
                await message.edit("❗️ В конфиге не найден первый префикс.\nПожалуйста, заполните конфиг")
            if prf2 == None:
                await message.edit(f"{prf1}{ping}")
                sleep(0.5)
                await self.allmodules.commands["ping"](
                    await utils.answer(message, f"{self.get_prefix()}{ping}")
                )
            else:
                await message.edit(f"{prf1}{ping}")
                await message.edit(f"{prf2}{ping}")
                sleep(0.5)
                await self.allmodules.commands["ping"](
                    await utils.answer(message, f"{self.get_prefix()}{ping}")
                )



    @loader.command()
    async def tupdatecmd(self, message):
        """- Загрузить обновление на аккаунтах"""
        update = "update --force"
        prf1 = self.config['1-prefix']
        prf2 = self.config['2-prefix']
        MyAcc = self.config['you_account']
        if MyAcc == False:
            if prf1 == None:
                await message.edit("❗️ В конфиге не найден первый префикс.\nПожалуйста, заполните конфиг")
            if prf2 == None:
                await message.edit(f"{prf1}{update}")
                sleep(0.5)
                await message.edit('🕘 <em>Выполняется обновление Hikka на ваших аккаунтах...</em>')
            else:
                await message.edit(f"{prf1}{update}")
                await message.edit(f"{prf2}{update}")
                sleep(0.5)
                await message.edit('🕘 <em>Выполняется обновление Hikka на ваших аккаунтах...</em>')

        else:
            if prf1 == None:
                await message.edit("❗️ В конфиге не найден первый префикс.\nПожалуйста, заполните конфиг")
            if prf2 == None:
                await message.edit(f"{prf1}{update}")
                sleep(0.5)
                await self.allmodules.commands["update"](
                    await utils.answer(message, f"{self.get_prefix()}{update}")
                )
            else:
                await message.edit(f"{prf1}{update}")
                await message.edit(f"{prf2}{update}")
                sleep(0.5)
                await self.allmodules.commands["update"](
                    await utils.answer(message, f"{self.get_prefix()}{update}")
                )



    @loader.command()
    async def thelpcmd(self, message):
        """- Вывести списки модулей на аккаунтах"""
        helpp = "help"
        prf1 = self.config['1-prefix']
        prf2 = self.config['2-prefix']
        MyAcc = self.config['you_account']
        if MyAcc == False:
            if prf1 == None:
                await message.edit("❗️ В конфиге не найден первый префикс.\nПожалуйста, заполните конфиг")
            if prf2 == None:
                await message.edit(f"{prf1}{helpp}")
                sleep(0.5)
                await message.edit('✅ <em>Список модулей успешно вызван</em>')
            else:
                await message.edit(f"{prf1}{helpp}")
                await message.edit(f"{prf2}{helpp}")
                sleep(0.5)
                await message.edit('✅ <em>Список модулей успешно вызван</em>')

        else:
            if prf1 == None:
                await message.edit("❗️ В конфиге не найден первый префикс.\nПожалуйста, заполните конфиг")
            if prf2 == None:
                await message.edit(f"{prf1}{helpp}")
                sleep(0.5)
                await self.allmodules.commands["help"](
                    await utils.answer(message, f"{self.get_prefix()}{helpp}")
                )
            else:
                await message.edit(f"{prf1}{helpp}")
                await message.edit(f"{prf2}{helpp}")
                sleep(0.5)
                await self.allmodules.commands["help"](
                    await utils.answer(message, f"{self.get_prefix()}{helpp}")
                )


    @loader.command()
    async def tterminalcmd(self, message):
        """- Выполнить команду в терминале"""
        terminal = "terminal"
        args = utils.get_args_raw(message) 
        prf1 = self.config['1-prefix']
        prf2 = self.config['2-prefix']
        MyAcc = self.config['you_account']
        if MyAcc == False:
            if prf1 == None:
                await message.edit("❗️ В конфиге не найден первый префикс.\nПожалуйста, заполните конфиг")
            if prf2 == None:
                await message.edit(f"{prf1}{terminal} {args}")
                sleep(0.5)
                await message.edit('✅ <em>Команда успешно выполнена</em>')
            else:
                await message.edit(f"{prf1}{terminal} {args}")
                await message.edit(f"{prf2}{terminal} {args}")
                sleep(0.5)
                await message.edit('✅ <em>Команда успешно выполнена</em>')
        else:
            if prf1 == None:
                await message.edit("❗️ В конфиге не найден первый префикс.\nПожалуйста, заполните конфиг")
            if prf2 == None:
                await message.edit(f"{prf1}{terminal}")
                sleep(0.5)
                await self.allmodules.commands["terminal"](
                    await utils.answer(message, f"{self.get_prefix()}{terminal} {args}")
                )
            else:
                await message.edit(f"{prf1}{terminal} {args}")
                await message.edit(f"{prf2}{terminal} {args}")
                sleep(0.5)
                await self.allmodules.commands["terminal"](
                    await utils.answer(message, f"{self.get_prefix()}{terminal} {args}")
                )


    @loader.command()
    async def tdlmodcmd(self, message):
        """- Загрузить модуль на аккаунты"""
        dlmod = "dlmod"
        prf1 = self.config['1-prefix']
        prf2 = self.config['2-prefix']
        args = utils.get_args_raw(message)
        MyAcc = self.config['you_account']
        if MyAcc == False:
            if prf1 == None:
                await message.edit("❗️ В конфиге не найден первый префикс.\nПожалуйста, заполните конфиг")
            if prf2 == None:
                await message.edit(f"{prf1}{dlmod} {args}")
                sleep(0.5)
                await message.edit('✅ <em>Модуль успешно загружен на аккаунтах</em>')
            else:
                await message.edit(f"{prf1}{dlmod} {args}")
                await message.edit(f"{prf2}{dlmod} {args}")
                sleep(0.5)
                await message.edit('✅ <em>Модуль успешно загружен на аккаунтах</em>')
        else:
            if prf1 == None:
                await message.edit("❗️ В конфиге не найден первый префикс.\nПожалуйста, заполните конфиг")
            if prf2 == None:
                await message.edit(f"{prf1}{dlmod}")
                sleep(0.5)
                await self.allmodules.commands["dlmod"](
                    await utils.answer(message, f"{self.get_prefix()}{dlmod} {args}")
                )
            else:
                await message.edit(f"{prf1}{dlmod} {args}")
                await message.edit(f"{prf2}{dlmod} {args}")
                sleep(0.5)
                await self.allmodules.commands["dlmod"](
                    await utils.answer(message, f"{self.get_prefix()}{dlmod} {args}")
                )
