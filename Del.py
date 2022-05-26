# meta developer: @ToXicUse, @Den4ikSuperOstryyPer4ik

from .. import loader, utils

import logging
import datetime
import time
import asyncio
import telethon

logger = logging.getLogger(__name__)


def register(cb):
    cb(WAITMod())


@loader.tds
class DelMod(loader.Module):
    """Менеджер удаления сообщений"""
    strings = {"name": "Del",
               "from_where": "<b>Which messages should be purged?</b>",
               "not_supergroup_bot": "<b>Purges can only take place in supergroups</b>",
               "delete_what": "<b>What message should be deleted?</b>",}

    def __init__(self):
        self.name = self.strings["name"]

    def config_complete(self):
        pass


    async def waitcmd(self, message):
        """Эта команда удаляет сообхение через n секунд, \nписать нужно так: .wait <n>, если хотите секунды\nи так .wait <n>m, если хотите ждать в минутах\n(например .wait 5m)"""
        args = utils.get_args(message)
        if not args or len(args) > 1:
            await utils.answer(message, "Вы не указали число секунд или указали несколько параметров")
        else:
            try:
                g = -1
                h = ""
                try:
                    g = int(args[0][:len(args[0])])
                except:
                    try:
                        g = int(args[0][:len(args[0]) - 1])
                        h = args[0][len(args[0]) - 1]
                    except:
                        await utils.answer(message, "Вы указали не число!")
                if g > 0:
                    if h == 's' or h == '':
                        x = g
                        lst = "Через " + str(x) + " секунд это сообщение удалится"
                        await utils.answer(message, lst)

                        dd = time.time()

                        while time.time() - dd < x:
                            now = "Через " + str(x - round(time.time() - dd)) + " секунд это сообщение удалится"
                            if now != lst:
                                await utils.answer(message, now)
                            lst = now
                        await message.delete()
                    elif h == 'm':
                        x = g
                        lst = "Через " + str(x) + " минут это сообщение удалится"
                        await utils.answer(message, lst)

                        dd = time.time()

                        ff = x * 60

                        llst = x
                        while time.time() - dd < ff:
                            oo = round((ff - round(time.time() - dd)) / 60)
                            nw = oo
                            if nw == llst:
                                await asyncio.sleep(0.1)
                                continue
                            now = "Через " + str(nw) + " минут это сообщение удалится"
                            await utils.answer(message, now)
                            llst = nw
                        await message.delete()
                    else:
                        await utils.answer(message, "Вы указали не число!")
            except:
                await utils.answer(message, "Упс, ошибочка вышла!")
                
                
                
    @loader.group_admin_delete_messages
    @loader.ratelimit
    async def purgecmd(self, message):
        """Purge from the replied message"""
        if not message.is_reply:
            await utils.answer(message, self.strings("from_where", message))
            return

        from_users = set()
        args = utils.get_args(message)
        for arg in args:
            try:
                entity = await message.client.get_entity(arg)
                if isinstance(entity, telethon.tl.types.User):
                    from_users.add(entity.id)
            except ValueError:
                pass

        msgs = []
        from_ids = set()
        if await message.client.is_bot():
            if not message.is_channel:
                await utils.answer(message, self.strings("not_supergroup_bot", message))
                return
            for msg in range(message.reply_to_msg_id, message.id + 1):
                msgs.append(msg)
                if len(msgs) >= 99:
                    logger.debug(msgs)
                    await message.client.delete_messages(message.to_id, msgs)
                    msgs.clear()
        else:
            async for msg in message.client.iter_messages(
                entity=message.to_id, min_id=message.reply_to_msg_id - 1, reverse=True
            ):
                if from_users and msg.sender_id not in from_users:
                    continue
                msgs.append(msg.id)
                from_ids.add(msg.sender_id)
                if len(msgs) >= 99:
                    logger.debug(msgs)
                    await message.client.delete_messages(message.to_id, msgs)
                    msgs.clear()
        if msgs:
            logger.debug(msgs)
            await message.client.delete_messages(message.to_id, msgs)
        await self.allmodules.log("purge", group=message.to_id, affected_uids=from_ids)

    @loader.group_admin_delete_messages
    @loader.ratelimit
    async def delcmd(self, message):
        """Delete the replied message"""
        msgs = [message.id]
        if not message.is_reply:
            if await message.client.is_bot():
                await utils.answer(message, self.strings("delete_what", message))
                return
            msg = await message.client.iter_messages(
                message.to_id, 1, max_id=message.id
            ).__anext__()
        else:
            msg = await message.get_reply_message()
        msgs.append(msg.id)
        logger.debug(msgs)
        await message.client.delete_messages(message.to_id, msgs)
        await self.allmodules.log(
            "delete", group=message.to_id, affected_uids=[msg.sender_id]
        )    
