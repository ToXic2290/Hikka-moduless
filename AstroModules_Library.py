from .. import loader
import time

class txAM_Lib(loader.Library):
  developer = "@ToXicUse"
  version = (0, 0, 2)


  # Pc-Manager
  async def message_q(
    self,
    text: str,
    user_id: int,
    mark_read: bool = False,
    delete: bool = False,
  ):
    """Отправляет сообщение и возращает ответ"""
    async with self.client.conversation(user_id) as conv:
        msg = await conv.send_message(text)
        response = await conv.get_response()
        if mark_read:
            await conv.mark_read()

        if delete:
            await msg.delete()
            await response.delete()

        return response


  async def message_g(
    self,
    text: str,
    user_id: int,
    mark_read: bool = False,
    delete: bool = False,
  ):
    """Отправляет сообщение и возращает ответ"""
    async with self.client.conversation(user_id) as conv:
        msg = await conv.send_message(text)
        response1 = await conv.get_response()
        response2 = await conv.get_response()
        if mark_read:
            await conv.mark_read()

        if delete:
            await msg.delete()
            await response1.delete()
            await response2.delete()

        return response2
  
  async def message_s(
    self,
    text: str,
    user_id: int,
    mark_read: bool = False,
    delete: bool = False,
  ):
    """Отправляет сообщение и возращает ответ"""
    async with self.client.conversation(user_id) as conv:
        msg = await conv.send_message(text)
        response1 = await conv.get_response()
        response2 = await conv.get_response()
        time.sleep(5)
        response3 = await conv.get_response()
        if mark_read:
            await conv.mark_read()

        if delete:
            await msg.delete()
            await response1.delete()
            await response2.delete()
            await response3.delete()

        return response3