import io
import time

from PIL import Image
from telethon.errors import (
    ChatAdminRequiredError,
    PhotoCropSizeSmallError,
    UserAdminInvalidError,
)
from telethon.tl.functions.channels import (
    EditAdminRequest,
    EditBannedRequest,
    EditPhotoRequest,
)
from telethon.tl.functions.messages import EditChatAdminRequest
from telethon.tl.types import ChatAdminRights, ChatBannedRights

from .. import loader, utils

# ================== CONSTANS ========================

UNMUTE_RIGHTS = ChatAdminRights(
    post_messages=None,
    add_admins=None,
    invite_users=None,
    change_info=None,
    ban_users=None,
    delete_messages=None,
    pin_messages=None,
    edit_messages=None,
)

DEMOTE_RIGHTS = ChatBannedRights(
    until_date=None,
    view_messages=None,
    send_messages=None,
    send_media=False,
    send_stickers=False,
    send_gifs=False,
    send_games=False,
    send_inline=False,
    embed_links=False,
)

BANNED_RIGHTS = ChatBannedRights(
    until_date=None,
    view_messages=True,
    send_messages=True,
    send_media=True,
    send_stickers=True,
    send_gifs=True,
    send_games=True,
    send_inline=True,
    embed_links=True,
)

UNBAN_RIGHTS = ChatBannedRights(
    until_date=None,
    view_messages=None,
    send_messages=None,
    send_media=None,
    send_stickers=None,
    send_gifs=None,
    send_games=None,
    send_inline=None,
    embed_links=None,
)


# =====================================================



@loader.tds
class AdminToolsMod(loader.Module):
    """Admin Tools"""

    strings = {
        "name": "Admin Tools",
        "not_pic": "<b>This isn`t an pic/sticker.</b>",
        "wait": "<b>Waiting...</b>",
        "pic_so_small": "<b>The image is too small, try another one.</b>",
        "pic_changed": "<b>Chat pic changed.</b>",
        "promote_none": "<b>No one to promote.</b>",
        "who": "<b>Who is it?</b>",
        "not_admin": "<b>I`m not an admin here.</b>",
        "promoted": "<b>{} promoted to admin rights.\nRank: {}</b>",
        "wtf_is_it": "<b>What is it?</b>",
        "this_isn`t_a_chat": "<b>This isn`t a chat!</b>",
        "demote_none": "<b>No one to demote.</b>",
        "demoted": "<b>{} demoted to admin rights.</b>",
        "pinning": "<b>Pin...</b>",
        "pin_none": "<b>Reply to the message to pin it.</b>",
        "unpinning": "<b>Unpin...</b>",
        "unpin_none": "<b>Nothing to unpin.</b>",
        "no_rights": "<b>I don`t have rights.</b>",
        "pinned": "<b>Pinned successfully!</b>",
        "unpinned": "<b>Unpinned successfully!</b>",
        "can`t_kick": "<b>Can`t kick.</b>",
        "kicking": "<b>Kick...</b>",
        "kick_none": "<b>No one to kick.</b>",
        "kicked": "<b>{} kicked from chat.</b>",
        "kicked_for_reason": "<b>{} kicked from chat.\nReason: {}.</b>",
        "banning": "<b>Ban...</b>",
        "banned": "<b>{} banned in chat.</b>",
        "banned_for_reason": "<b>{} banned in chat.\nReason: {}</b>",
        "ban_none": "<b>No one to ban.</b>",
        "unban_none": "<b>No one to unban.</b>",
        "unbanned": "<b>{} unbanned in chat.</b>",
        "mute_none": "<b>No one to mute.</b>",
        "muted": "<b>{} now muted for </b>",
        "no_args": "<b>Invalid arguments specified.</b>",
        "unmute_none": "<b>No one to unmute.</b>",
        "unmuted": "<b>{} now unmuted.</b>",
        "no_reply": "<b>No reply.</b>",
        "del_u_search": "<b>Search for deleted accounts...</b>",
        "del_u_kicking": "<b>Kick deleted accounts...\nOh~, I can do it?!</b>",
    }
    
    
    
     async def unmediacmd(self, message):
        """Command .demote for demote user to admin rights.\nUse: .demote <@ or reply>."""
        if message.is_private:
            return await utils.answer(
                message, self.strings("this_isn`t_a_chat", message)
            )
        try:
            reply = await message.get_reply_message()

            chat = await message.get_chat()
            if not chat.admin_rights and not chat.creator:
                return await utils.answer(message, self.strings("not_admin", message))

            if reply:
                user = await message.client.get_entity(reply.sender_id)
            else:
                args = utils.get_args_raw(message)
                if not args:
                    return await utils.answer(
                        message, self.strings("demote_none", message)
                    )
                user = await message.client.get_entity(
                    args if not args.isnumeric() else int(args)
                )

            try:
                if message.is_channel:
                    await message.client(
                        EditAdminRequest(message.chat_id, user.id, DEMOTE_RIGHTS, "")
                    )
                else:
                    await message.client(
                        EditChatAdminRequest(message.chat_id, user.id, False)
                    )
            except ChatAdminRequiredError:
                return await utils.answer(message, self.strings("no_rights", message))
            else:
                return await utils.answer(
                    message, self.strings("demoted", message).format(user.first_name)
                )
        except ValueError:
            return await utils.answer(message, self.strings("no_args"))
