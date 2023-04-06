# ---------------------------------------------------------------------------------
#  /\_/\  🌐 This module was loaded through https://t.me/hikkamods_bot
# ( o.o )  🔐 Licensed under the GNU AGPLv3.
#  > ^ <   ⚠️ Owner of heta.hikariatama.ru doesn't take any responsibilities or intellectual property rights regarding this script
# ---------------------------------------------------------------------------------
# Name: voicechat
# Description: Toolkit for VoiceChats handling
# Author: hikariatama
# Commands:
# .vcq    | .qrm   | .qadd    | .qaddv | .qnext
# .qpause | .qstop | .qresume
# ---------------------------------------------------------------------------------


__version__ = (2, 1, 0)

#             █ █ ▀ █▄▀ ▄▀█ █▀█ ▀
#             █▀█ █ █ █ █▀█ █▀▄ █
#              © Copyright 2022
#           https://t.me/hikariatama
#
# 🔒      Licensed under the GNU AGPLv3
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html

# meta pic: https://static.hikari.gay/voicechat_icon.png
# meta banner: https://mods.hikariatama.ru/badges/voicechat.jpg
# meta developer: @darkmodules
# requires: py-tgcalls youtube_dl
# scope: hikka_only
# scope: hikka_min 1.2.10

import asyncio
import atexit
import contextlib
import logging
import os
import re
import shutil
import tempfile
import json

from pytgcalls import PyTgCalls, StreamType, types
from pytgcalls.binding import Binding
from pytgcalls.environment import Environment
from pytgcalls.exceptions import AlreadyJoinedError, NoActiveGroupCall, NotInGroupCallError
from pytgcalls.handlers import HandlersHolder
from pytgcalls.methods import Methods
from pytgcalls.mtproto import MtProtoClient
from pytgcalls.scaffold import Scaffold
from pytgcalls.types import Cache
from pytgcalls.types.call_holder import CallHolder
from pytgcalls.types.update_solver import UpdateSolver
from telethon.tl.functions.phone import CreateGroupCallRequest
from telethon.tl.types import DocumentAttributeFilename, Message
from youtube_dl import YoutubeDL

from .. import loader, utils
from ..inline.types import InlineCall
from ..tl_cache import CustomTelegramClient

logging.getLogger("pytgcalls").setLevel(logging.ERROR)


@loader.tds
class VoiceShitMod(loader.Module):
    """Toolkit for VoiceChats handling, Originally made by @hikarimods"""

    strings = {
        "name": "VoiceShit",
        "already_joined": "🚫 <b>You are already in VoiceChat</b>",
        "joined": "🎙 <b>Joined VoiceChat</b>",
        "no_reply": "🚫 <b>Reply to a message</b>",
        "no_queue": "🚫 <b>No queue</b>",
        "queue": "🎙 <b>Queue</b>:\n\n{}",
        "queueadd": "🎧 <b>{} added to queue</b>",
        "queueaddv": "🎬 <b>{} added to queue</b>",
        "downloading": "📥 <b>Downloading...</b>",
        "playing": "🎶 <b>Playing {}</b>",
        "playing_with_next": "🎶 <b>Playing {}</b>\n➡️ <b>Next: {}</b>",
        "pause": "🎵 Pause",
        "play": "🎵 Play",
        "mute": "🔇 Mute",
        "unmute": "🔈 Unmute",
        "next": "➡️ Next",
        "stopped": "🚨 <b>Stopped</b>",
        "stop": "🚨 Stop",
        "choose_delete": "♻️ <b>Choose a queue item to delete</b>",
    }

    strings_ru = {
        "already_joined": "🚫 <b>Уже в голосовом чате</b>",
        "joined": "🎙 <b>Присоединился к голосовому чату</b>",
        "no_reply": "🚫 <b>Ответьте на сообщение</b>",
        "no_queue": "🚫 <b>Очередь пуста</b>",
        "queue": "🎙 <b>Очередь</b>:\n\n{}",
        "queueadd": "🎧 <b>{} добавлен в очередь</b>",
        "queueaddv": "📼 <b>{} добавлен в очередь</b>",
        "downloading": "📥 <b>Загрузка...</b>",
        "playing": "🎶 <b>Играет {}</b>",
        "playing_with_next": "🎶 <b>Играет {}</b>\n➡️ <b>Далее: {}</b>",
        "pause": "🎵 Пауза",
        "play": "🎵 Играть",
        "mute": "🔇 Заглушить",
        "unmute": "🔈 Включить",
        "next": "➡️ Далее",
        "stopped": "🚨 <b>Остановлено</b>",
        "stop": "🚨 Остановить",
        "choose_delete": "♻️ <b>Выберите элемент очереди для удаления</b>",
    }

    _calls = {}
    _muted = {}
    _forms = {}
    _queue = {}

    def __init__(self):
        self.config = loader.ModuleConfig(
            loader.ConfigValue(
                "silent_queue",
                False,
                "Do not notify about track changes in chat",
                validator=loader.validators.Boolean(),
            ),
            loader.ConfigValue(
                "repeat",
                True,
                "Repeat the queue",
                validator=loader.validators.Boolean(),
            )
        )

    async def client_ready(self, client, db):
        if not self.get("saved_queue"):
            self.set("saved_queue", {})

        # Monkeypatch pytgcalls MtProtoClient to support hikka's custom one

        class HikkaTLClient(MtProtoClient):
            def __init__(
                self,
                cache_duration: int,
                client: CustomTelegramClient,
            ):
                self._bind_client = None
                from pytgcalls.mtproto.telethon_client import TelethonClient

                self._bind_client = TelethonClient(
                    cache_duration,
                    client,
                )

        class CustomPyTgCalls(PyTgCalls):
            def __init__(
                self,
                app: CustomTelegramClient,
                cache_duration: int = 120,
                overload_quiet_mode: bool = False,
                # BETA SUPPORT, BY DEFAULT IS DISABLED
                multi_thread: bool = False,
            ):
                Methods.__init__(self)
                Scaffold.__init__(self)
                self._app = HikkaTLClient(
                    cache_duration,
                    app,
                )
                self._is_running = False
                self._env_checker = Environment(
                    self._REQUIRED_NODEJS_VERSION,
                    self._REQUIRED_PYROGRAM_VERSION,
                    self._REQUIRED_TELETHON_VERSION,
                    self._app.client,
                )
                self._call_holder = CallHolder()
                self._cache_user_peer = Cache()
                self._wait_result = UpdateSolver()
                self._on_event_update = HandlersHolder()
                self._binding = Binding(
                    overload_quiet_mode,
                    multi_thread,
                )

                def cleanup():
                    if self._async_core is not None:
                        self._async_core.cancel()

                atexit.register(cleanup)

        # //

        self._app = CustomPyTgCalls(client)
        self._dir = tempfile.mkdtemp()
        await self._app.start()
        self._app._on_event_update.add_handler("STREAM_END_HANDLER", self.stream_ended)
        self.musicdl = await self.import_lib(
            "https://libs.hikariatama.ru/musicdl.py",
            suspend_on_error=True,
        )

    async def stream_ended(self, client: PyTgCalls, update: types.Update):
        chat_id = update.chat_id
        with contextlib.suppress(IndexError):
            if self.config["repeat"]:
                track = self._queue[chat_id][0]
                track["playing"] = False
                self._queue[chat_id].append(track)
            self._queue[chat_id].pop(0)

        if not self._queue.get(chat_id):
            with contextlib.suppress(Exception):
                await client.leave_group_call(chat_id)
            return

        self._queue[chat_id][0]["playing"] = True

        if self._queue[chat_id][0]["audio"]:
            await self.play(chat_id, self._queue[chat_id][0]["data"])
        else:
            if self._queue[chat_id][0]["youtube"]:
                await self.play_video_yt(chat_id, self._queue[chat_id][0]["data"])
            else:
                await self.play_video(chat_id, self._queue[chat_id][0]["data"])

    async def _play(
        self,
        chat_id: int,
        stream,
        stream_type,
        reattempt: bool = False,
    ):
        self._muted.setdefault(chat_id, False)
        try:
            await self._app.join_group_call(
                chat_id,
                stream,
                stream_type=stream_type,
            )
        except AlreadyJoinedError:
            await self._app.change_stream(chat_id, stream)
        except NoActiveGroupCall:
            if reattempt:
                raise

            await self._client(CreateGroupCallRequest(chat_id))
            await self._play(chat_id, stream, stream_type, True)

    def _get_fn(self, message: Message) -> str:
        filename = None
        with contextlib.suppress(Exception):
            attr = next(
                attr for attr in getattr(message, "document", message).attributes
            )
            filename = (
                getattr(attr, "performer", "") + " - " + getattr(attr, "title", "")
            )

        if not filename:
            with contextlib.suppress(Exception):
                filename = next(
                    attr
                    for attr in getattr(message, "document", message).attributes
                    if isinstance(attr, DocumentAttributeFilename)
                ).file_name

        return filename

    @loader.command("Сохранить очередь")
    async def qsave(self, message):
        """Save the queue"""
        data = self._queue[utils.get_chat_id(message)]

        for track in data:
            track["data"] = track["data"].decode("latin1")

        self.set("saved_queue", json.dumps(data))
        await utils.answer(message, "Done!")

    @loader.command("Загрузить очередь")
    async def qload(self, message):
        """Load the queue"""
        data = json.loads(self.get("saved_queue"))

        for track in data:
            track["data"] = track["data"].encode("latin1")

        self._queue[utils.get_chat_id(message)] = data
        await utils.answer(message, "Done!")

    @loader.command("Переключить режим 'повторять эту очередь вечно'")
    async def qloop(self, message):
        """Switch the 'repeat this queue forever'"""
        self.config["repeat"] = not self.config["repeat"]
        await utils.answer(message, f"loop is now: {self.config['repeat']}")

    @loader.command(ru_doc="<ответ на песню или ее имя> - Добавить песню в очередь прослушивания чата")
    async def qadd(self, message: Message):
        """<reply to song or its name> - Add song to chat's voicechat queue"""
        reply = await message.get_reply_message()
        song = utils.get_args_raw(message)
        if (not reply or not reply.media) and not song:
            await utils.answer(message, self.strings("no_reply"))
            return

        message = await utils.answer(message, self.strings("downloading"))
        filename = None

        if not reply or not reply.media and song:
            song, filename = await self._download_audio(song, message)
            if not song:
                await utils.answer(message, self.strings("no_reply"))
                return

        if song:
            raw_data = song
        else:
            raw_data = await self._client.download_file(reply.document, bytes)

            filename = self._get_fn(reply)

        if not filename:
            filename = "Some cool song"

        filename = re.sub(r"\(.*?\)", "", filename)

        chat_id = utils.get_chat_id(message)

        self._queue.setdefault(chat_id, []).append(
            {"data": raw_data, "filename": filename, "playing": False, "audio": True}
        )

        if not any(i["playing"] for i in self._queue[chat_id]):
            self._queue[chat_id][-1]["playing"] = True
            await self.play(chat_id, raw_data)

        await utils.answer(message, self.strings("queueadd").format(filename))

    @loader.command()
    async def qrestart(self, message):
        """Rejoin the call in case you accidentally joined it"""
        chat_id = utils.get_chat_id(message)
        track = next((x for x in self._queue[chat_id] if x["playing"]), None)

        if not track:
            return

        file = os.path.join(self._dir, f"{utils.rand(8)}.ogg")
        with open(file, "wb") as f:
            f.write(track["data"])

        #await self.play(chat_id, track["data"])

        with contextlib.suppress(AlreadyJoinedError, NotInGroupCallError):
            await self._app.leave_group_call(chat_id)

        await self._app.join_group_call(
            chat_id,
            types.AudioPiped(file, types.HighQualityAudio()),
            stream_type=StreamType().pulse_stream,
        )

        await utils.answer(message, "Done!")

    @loader.command(ru_doc="<ответ на видео или ссылка на YouTube> - Добавить видео в очередь чата",)
    async def qaddv(self, message: Message):
        """<reply to video or yt link> - Add video to chat's voicechat queue"""
        reply = await message.get_reply_message()
        link = utils.get_args_raw(message)
        if (not reply or not reply.media) and not link:
            await utils.answer(message, self.strings("no_reply"))
            return

        filename = None
        message = await utils.answer(message, self.strings("downloading"))
        if reply and reply.media:
            raw_data = await self._client.download_file(reply.document, bytes)

            filename = self._get_fn(reply)

        else:
            raw_data = link
            with contextlib.suppress(Exception):
                with YoutubeDL() as ydl:
                    filename = ydl.extract_info(link, download=False).get(
                        "title",
                        None,
                    )

        if not filename:
            filename = "Some cool video"

        filename = re.sub(r"\(.*?\)", "", filename)

        chat_id = utils.get_chat_id(message)

        self._queue.setdefault(chat_id, []).append(
            {
                "data": raw_data,
                "filename": filename,
                "playing": False,
                "audio": False,
                "youtube": not (reply and reply.media),
            }
        )

        if not any(i["playing"] for i in self._queue[chat_id]):
            self._queue[chat_id][-1]["playing"] = True
            if self._queue[chat_id][-1]["youtube"]:
                await self.play_video_yt(chat_id, raw_data)
            else:
                await self.play_video(chat_id, raw_data)

        await utils.answer(message, self.strings("queueadd").format(filename))

    @loader.command(ru_doc="Переключить трек")
    async def qnext(self, message: Message):
        """Skips current audio in queue"""
        chat_id = utils.get_chat_id(message)

        if len(self._queue.get(chat_id, [])) <= 1:
            await utils.answer(message, self.strings("no_queue"))
            return

        if self.config["repeat"]:
            track = self._queue[chat_id][0]
            track["playing"] = False
            self._queue[chat_id].append(track)
        self._queue[chat_id].pop(0)
        self._queue[chat_id][0]["playing"] = True
        if self._queue[chat_id][0]["audio"]:
            await self.play(chat_id, self._queue[chat_id][0]["data"])
        else:
            if self._queue[chat_id][0]["youtube"]:
                await self.play_video_yt(chat_id, self._queue[chat_id][0]["data"])
            else:
                await self.play_video(chat_id, self._queue[chat_id][0]["data"])

        await message.delete()

    async def _download_audio(self, name: str, message: Message) -> bytes:
        result = await self.musicdl.dl(name, only_document=True)
        try:
            return await self._client.download_file(result, bytes), self._get_fn(result)
        except Exception:
            return None, None

    async def vcqcmd(self, message: Message):
        """Get current chat's queue"""
        chat_id = utils.get_chat_id(message)
        if not self._queue.get(chat_id):
            await utils.answer(message, self.strings("no_queue"))
            return

        await utils.answer(
            message,
            self.strings("queue").format(
                "\n".join(
                    [
                        ("🎧" if i["playing"] else "🕓")
                        + ("" if i["audio"] else "🎬")
                        + f" {i['filename']}"
                        for i in self._queue[chat_id]
                    ]
                )
            ),
        )

    async def qrmcmd(self, message: Message):
        """Remove song from queue"""
        chat_id = utils.get_chat_id(message)
        if not self._queue.get(chat_id) or all(
            i["playing"] for i in self._queue[chat_id]
        ):
            await utils.answer(message, self.strings("no_queue"))
            return

        await self.inline.form(
            message=message,
            text=self.strings("choose_delete"),
            reply_markup=utils.chunks(
                [
                    {
                        "text": ("🎧" if i["audio"] else "🎬") + i["filename"],
                        "callback": self._inline__delete,
                        "args": (chat_id, index),
                    }
                    for index, i in enumerate(self._queue[chat_id])
                    if not i["playing"]
                ],
                2,
            ),
        )

    async def _inline__delete(self, call: InlineCall, chat_id: int, index: int):
        del self._queue[chat_id][index]
        await call.answer("OK")
        await call.delete()

    async def _inline__pause(self, call: InlineCall, chat_id: int):
        await self._app.pause_stream(chat_id)
        msg, markup = self._get_inline_info(chat_id)
        await call.edit(msg, reply_markup=markup)

    async def _inline__play(self, call: InlineCall, chat_id: int):
        await self._app.resume_stream(chat_id)
        msg, markup = self._get_inline_info(chat_id)
        await call.edit(msg, reply_markup=markup)

    async def _inline__mute(self, call: InlineCall, chat_id: int):
        await self._app.mute_stream(chat_id)
        self._muted[chat_id] = True
        msg, markup = self._get_inline_info(chat_id)
        await call.edit(msg, reply_markup=markup)

    async def _inline__unmute(self, call: InlineCall, chat_id: int):
        await self._app.unmute_stream(chat_id)
        self._muted[chat_id] = False
        msg, markup = self._get_inline_info(chat_id)
        await call.edit(msg, reply_markup=markup)

    async def _inline__stop(self, call: InlineCall, chat_id: int):
        with contextlib.suppress(KeyError):
            del self._queue[chat_id]

        with contextlib.suppress(KeyError):
            del self._forms[chat_id]

        with contextlib.suppress(KeyError):
            del self._muted[chat_id]

        await self._app.leave_group_call(chat_id)
        await utils.answer(call, self.strings("stopped"))

    async def _inline__next(self, call: InlineCall, chat_id: int):
        self._queue[chat_id].pop(0)
        self._queue[chat_id][0]["playing"] = True
        if self._queue[chat_id][0]["audio"]:
            await self.play(chat_id, self._queue[chat_id][0]["data"])
        else:
            if self._queue[chat_id][0]["youtube"]:
                await self.play_video_yt(chat_id, self._queue[chat_id][0]["data"])
            else:
                await self.play_video(chat_id, self._queue[chat_id][0]["data"])

        msg, markup = self._get_inline_info(chat_id)
        await call.edit(msg, reply_markup=markup)

    def _get_inline_info(self, chat_id: int) -> tuple:
        if not self._queue.get(chat_id):
            return None, None

        if len(self._queue[chat_id]) == 1:
            msg = self.strings("playing").format(
                utils.escape_html(self._queue[chat_id][0]["filename"]),
            )
        else:
            msg = self.strings("playing_with_next").format(
                utils.escape_html(self._queue[chat_id][0]["filename"]),
                utils.escape_html(self._queue[chat_id][1]["filename"]),
            )

        try:
            is_playing = self._app.get_call(chat_id).status == "playing"
        except Exception:
            is_playing = True

        markup = [
            [
                {
                    "text": self.strings("stop"),
                    "callback": self._inline__stop,
                    "args": (chat_id,),
                },
            ],
            [
                *(
                    [
                        {
                            "text": self.strings("pause"),
                            "callback": self._inline__pause,
                            "args": (chat_id,),
                        }
                    ]
                    if is_playing
                    else [
                        {
                            "text": self.strings("play"),
                            "callback": self._inline__play,
                            "args": (chat_id,),
                        }
                    ]
                ),
                *(
                    [
                        {
                            "text": self.strings("mute"),
                            "callback": self._inline__mute,
                            "args": (chat_id,),
                        }
                    ]
                    if not self._muted.get(chat_id, False)
                    else [
                        {
                            "text": self.strings("unmute"),
                            "callback": self._inline__unmute,
                            "args": (chat_id,),
                        }
                    ]
                ),
            ],
            *(
                [
                    [
                        {
                            "text": self.strings("next"),
                            "callback": self._inline__next,
                            "args": (chat_id,),
                        }
                    ]
                ]
                if len(self._queue[chat_id]) > 1
                else []
            ),
        ]

        return msg, markup

    @loader.command(ru_doc="Приостановить воспроизведение")
    async def qpause(self, message: Message):
        """Pause current chat's queue"""
        chat_id = utils.get_chat_id(message)
        with contextlib.suppress(Exception):
            await self._app.pause_stream(chat_id)

        msg, markup = self._get_inline_info(chat_id)
        with contextlib.suppress(Exception):
            await self._forms[chat_id].delete()
        self._forms[chat_id] = await utils.answer(message, msg, reply_markup=markup)

    @loader.command(ru_doc="Остановить воспроизведение")
    async def qstop(self, message: Message):
        """Stop current chat's queue"""
        await self._inline__stop(message, utils.get_chat_id(message))

    @loader.command(ru_doc="Продолжить воспроизведение")
    async def qresume(self, message: Message):
        """Resume current chat's queue"""
        chat_id = utils.get_chat_id(message)
        with contextlib.suppress(Exception):
            await self._app.resume_stream(chat_id)

        msg, markup = self._get_inline_info(chat_id)
        with contextlib.suppress(Exception):
            await self._forms[chat_id].delete()
        self._forms[chat_id] = await utils.answer(message, msg, reply_markup=markup)

    async def play(self, chat_id: int, array: bytes):
        file = os.path.join(self._dir, f"{utils.rand(8)}.ogg")
        with open(file, "wb") as f:
            f.write(array)

        await self._play(
            chat_id,
            types.AudioPiped(file, types.HighQualityAudio()),
            StreamType().pulse_stream,
        )
        await asyncio.sleep(1)
        if not self.config["silent_queue"]:
            msg, markup = self._get_inline_info(chat_id)
            with contextlib.suppress(Exception):
                await self._forms[chat_id].delete()
            self._forms[chat_id] = await self.inline.form(
                message=chat_id, text=msg, reply_markup=markup
            )

    async def play_video(self, chat_id: int, array: bytes):
        file = os.path.join(self._dir, f"{utils.rand(8)}.mp4")
        with open(file, "wb") as f:
            f.write(array)

        await self._play(
            chat_id,
            types.AudioVideoPiped(
                file,
                types.HighQualityAudio(),
                types.HighQualityVideo(),
            ),
            StreamType().pulse_stream,
        )
        await asyncio.sleep(1)
        if not self.config["silent_queue"]:
            msg, markup = self._get_inline_info(chat_id)
            with contextlib.suppress(Exception):
                await self._forms[chat_id].delete()
            self._forms[chat_id] = await self.inline.form(
                message=chat_id, text=msg, reply_markup=markup
            )

    async def play_video_yt(self, chat_id: int, link: str):
        proc = await asyncio.create_subprocess_exec(
            "youtube-dl",
            "-g",
            "-f",
            "worst",
            link,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        stdout, _ = await proc.communicate()
        await self._play(
            chat_id,
            types.AudioVideoPiped(
                stdout.decode().split("\n")[0],
                types.HighQualityAudio(),
                types.HighQualityVideo(),
            ),
            StreamType().pulse_stream,
        )
        await asyncio.sleep(1)
        if not self.config["silent_queue"]:
            msg, markup = self._get_inline_info(chat_id)
            with contextlib.suppress(Exception):
                await self._forms[chat_id].delete()
            self._forms[chat_id] = await self.inline.form(
                message=chat_id,
                text=msg,
                reply_markup=markup,
            )

    async def on_unload(self):
        shutil.rmtree(self._dir)
        for chat_id in self._muted:
            await self._app.leave_group_call(chat_id)