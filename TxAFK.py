#========================================================================#
#                _             __  __           _       _                #
#      /\       | |           |  \/  |         | |     | |               #
#     /  \   ___| |_ _ __ ___ | \  / | ___   __| |_   _| | ___  ___      #
#    / /\ \ / __| __| '__/ _ \| |\/| |/ _ \ / _` | | | | |/ _ \/ __|     #
#   / ____ \\__ \ |_| | | (_) | |  | | (_) | (_| | |_| | |  __/\__ \     #
#  /_/    \_\___/\__|_|  \___/|_|  |_|\___/ \__,_|\__,_|_|\___||___/     #
#                                                                        #
#                         © Copyright 2022                               #
#                                                                        #
#                https://t.me/Den4ikSuperOstryyPer4ik                    #
#                              and                                       #
#                      https://t.me/ToXicUse                             #
#                                                                        # 
#                 🔒 Licensed under the GNU AGPLv3                       #
#             https://www.gnu.org/licenses/agpl-3.0.html                 #
#                                                                        # 
# meta channel: @AstroModules                                            #
#                                                                        #
#                                                                        #
#========================== Imports =====================================#
# meta developer: @ToXicUse

from .. import loader, utils

import logging
import datetime
import time

from telethon import types
from telethon import functions

from telethon.errors.rpcerrorlist import UsernameOccupiedError
from telethon.tl.functions.account import UpdateProfileRequest, UpdateUsernameRequest
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import Message

#=========================== Logger ===========================================#

logger = logging.getLogger(__name__)

#=========================== Loader ========================================#

@loader.tds
class TxAFKMod(loader.Module):
	"""Афк модуль от Токса с изменением био и имени

	🚀 version: 1.0
	💻 type: private"""

	strings = {
		"name": "TxAFK",
		"gone": "<b>Я ушел в афк!</b>",
		"back": "<b>Режим AFK отключен</b>",
		"what": "<b>А где текст?</b>",
		"afk": """<b>Я сейчас нахожусь в АФК.</b>
		(не появлялся в сети <code>{}</code> ) """,
		"fb_bot": "Юзер вашего фидбэк бота (если имеется)",
		"biography": "Ссылка на ваш сайт (канал) с биографией",
		"custom_text__afk_text": "Кастомный текст афк",
		"txt": "<b>{}</b> <code>{}</code>",
		"standart_bio_text": "Стандартное био в профиле",
		"afk_bio": "На данный момент в АФК. Связь только через ",
		"afk_bio_nofb": "В афк.",
		"lname": "| afk.",
		"lname0": "ㅤ",
	}
#============================ Client =========================================#

	async def client_ready(self, client, db):
		self._db = db
		self._me = await client.get_me()
		if self._tg_id == 5243326600:
			raise loader.LoadError

#============================ Config ===========================================#

	def __init__(self):
		self.config = loader.ModuleConfig(
			loader.ConfigValue(
				"feedback_bot",
				"None",
				doc=lambda: self.strings("fb_bot"),
			),
			loader.ConfigValue(
				"custom_text__afk",
				"None",
				doc=lambda: self.strings("custom_text__afk_text"),
			),
			loader.ConfigValue(
				"standart_bio",
				"{ toxbio.ml } - bio; { @FeedbackTx_bot } - feedback; { @nohelloru } - please.",
				doc=lambda: self.strings("standart_bio_text"),
			),
		)

#========================== GoAfk ===========================================#

	async def goafkcmd(self, message):
		"""Войти в AFK режим"""
		try:
			user_id = (
				(
					(
						await self._client.get_entity(
							args if not args.isdigit() else int(args)
						)
					).id
				)
				if args
				else reply.sender_id
			)
		except Exception:
			user_id = self._tg_id

		user = await self._client(GetFullUserRequest(user_id))
		user_ent = user.users[0]
		
		self._db.set(__name__, "afk", True)
		self._db.set(__name__, "gone", time.time())
		self._db.set(__name__, "ratelimit", [])
		a_afk_bio_nofb = self.strings("afk_bio_nofb")
		lastname = self.strings("lname")
		if self.config['feedback_bot'] == None:
			await message.client(UpdateProfileRequest(about=a_afk_bio_nofb, last_name=lastname))
		else:
			a_afk_bio = self.strings("afk_bio")
			feedback = self.config['feedback_bot']
			aaa = a_afk_bio + feedback
			await message.client(UpdateProfileRequest(about=aaa))
		await self.allmodules.log("goafk")
		await utils.answer(message, self.strings("gone", message))

#========================== UnAfk ===============================================#
	async def ungoafkcmd(self, message):
		"""Выйти из режима AFK"""
		sbio = self.config['standart_bio']
		lastname0 = self.strings('lname0')
		self._db.set(__name__, "afk", False)
		self._db.set(__name__, "gone", None)
		self._db.set(__name__, "ratelimit", [])
		await self.allmodules.log("unafk")
		await message.client(UpdateProfileRequest(about=sbio, last_name=lastname0))
		await utils.answer(message, self.strings("back", message))

#========================== Config ========================================#

	async def txcfgcmd(self, message):
		"""Конфиг модуля"""
		await self.allmodules.commands["config"](
					await utils.answer(message, f"{self.get_prefix()}config TxAFK")
				)

#========================== Watcher ==================================#

	async def watcher(self, message):
		if not isinstance(message, types.Message):
			return
		if message.mentioned or getattr(message.to_id, "user_id", None) == self._me.id:
			afk_state = self.get_afk()
			if not afk_state:
				return
			logger.debug("tagged!")
			ratelimit = self._db.get(__name__, "ratelimit", [])
			if utils.get_chat_id(message) in ratelimit:
				return
			else:
				self._db.setdefault(__name__, {}).setdefault("ratelimit", []).append(
					utils.get_chat_id(message)
				)
				self._db.save()
			user = await utils.get_user(message)
			if user.is_self or user.bot or user.verified:
				logger.debug("User is self, bot or verified.")
				return
			if self.get_afk() is False:
				return
			now = datetime.datetime.now().replace(microsecond=0)
			gone = datetime.datetime.fromtimestamp(
				self._db.get(__name__, "gone")
			).replace(microsecond=0)
			diff = now - gone
			ctext = self.config['custom_text__afk']
			aoaoa = self.strings("txt", message).format(ctext, diff)
			await utils.answer(message, aoaoa, reply_to=message)

#============================================================================#

	def get_afk(self):
		return self._db.get(__name__, "afk", False)

#============================================================================#