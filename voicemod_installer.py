#               _             __  __           _       _
#     /\       | |           |  \/  |         | |     | |
#    /  \   ___| |_ _ __ ___ | \  / | ___   __| |_   _| | ___  ___
#   / /\ \ / __| __| '__/ _ \| |\/| |/ _ \ / _` | | | | |/ _ \/ __|
#  / ____ \\__ \ |_| | | (_) | |  | | (_) | (_| | |_| | |  __/\__ \
# /_/    \_\___/\__|_|  \___/|_|  |_|\___/ \__,_|\__,_|_|\___||___/
#
#               © Copyright 2023
#
#      https://t.me/Den4ikSuperOstryyPer4ik
#                      and
#             https://t.me/ToXicUse
#
#       🔒 Licensed under the GNU AGPLv3
#    https://www.gnu.org/licenses/agpl-3.0.html
#
# meta developer: @AstroModules

from .. import loader, utils

import os
import asyncio
import subprocess

@loader.tds
class VoiceModInstall(loader.Module):
    '''Module for install VoiceMod by AstroModules'''

    strings = {
        'name': 'VoiceModInstall',
        'installing_ffmpeg': '<emoji document_id=5307675706283533118>🫥</emoji> <b>Installing FFMPEG...</b>',
        'installing_nodejs': '<emoji document_id=5328239124933515868>⚙️</emoji> <b>Installing NodeJs...</b>',
        'installing_shazam': '<emoji document_id=5334694808671756040>🧊</emoji> <b>Installing ShazamAPI...</b>',
        'installing_youtubedl': '<emoji document_id=5328311576736833844>🔴</emoji> <b>Installing youtube-dl...</b>',
        'installing_pytgcalls': '<emoji document_id=5325872701032635449>⏳</emoji> <b>Installing pytgcalls...</b>',
        'attempting_for_install': (
            '<emoji document_id=5305794398938735107>💭</emoji> <b>'
            'Requirements installed. Trying to install module...</b>'
        ),
        'installed_all': '<emoji document_id=6325696222313055607>😶</emoji> <b>Module secessfully installed!</b>',
        'егор': '<emoji document_id=5258291768587197831>✖️</emoji> <b>Error! Please, try again</b>'
    }

    strings_ru = {
        'installing_ffmpeg': '<emoji document_id=5307675706283533118>🫥</emoji> <b>Установка FFMPEG...</b>',
        'installing_nodejs': '<emoji document_id=5328239124933515868>⚙️</emoji> <b>Установка NodeJs...</b>',
        'installing_shazam': '<emoji document_id=5334694808671756040>🧊</emoji> <b>Установка ShazamAPI...</b>',
        'installing_youtubedl': '<emoji document_id=5328311576736833844>🔴</emoji> <b>Установка youtube-dl...</b>',
        'installing_pytgcalls': '<emoji document_id=5325872701032635449>⏳</emoji> <b>Установка pytgcalls...</b>',
        'attempting_for_install': (
            '<emoji document_id=5305794398938735107>💭</emoji> <b>'
            'Зависимости установлены. Пробую загрузить модуль...</b>'
        ),
        'installed_all': '<emoji document_id=6325696222313055607>😶</emoji> <b>VoiceMod успешно установлен!</b>',
        'егор': '<emoji document_id=5258291768587197831>✖️</emoji> <b>Произошла ошибка! Прпробуйте снова</b>'
    }

    async def check_module(self):
        return any([True if 'VoiceMod' else False in mod for mod in self.allmodules.modules])

    @loader.command(ru_doc='- установить VoiceMod на Хикку')
    async def install(self, message):
        '''
        - install VoiceMod to Hikka.
        '''

        check_sudo = subprocess.check_output(['whoami']).decode().strip()
        if check_sudo == 'root':
            sudo = False
        else:
            sudo = True
        try:
            subprocess.check_output(['node','-v']).decode().strip()
        except:
            await utils.answer(message, self.strings('installing_nodejs'))
            command_0 = 'curl -sL https://deb.nodesource.com/setup_18.x -o nodesource_setup.sh'
            command_1 = 'bash nodesource_setup.sh'
            command_2 = 'apt-get install -y nodejs'
            if sudo:
                command_0 = f'sudo -S {command_0}' 
                command_1 = f'sudo -S {command_1}' 
                command_2 = f'sudo -S {command_2}' 
            os.system(command_0)
            await asyncio.sleep(0.5)
            os.system(command_1)
            await asyncio.sleep(0.5)
            os.system(command_2)

        b = await utils.answer(message, self.strings('installing_pytgcalls'))
        command = 'pip install tgcalls --no-deps'
        os.system(command)

        command = 'pip install pytgcalls --no-deps'
        os.system(command)
        os.system('pip install numpy')
        os.system('pip install pydub')

        c = await utils.answer(b, self.strings('installing_ffmpeg'))
        command = 'pip install ffmpeg-python'
        os.system(command)

        d = await utils.answer(c, self.strings('installing_youtubedl'))
        command = 'pip install youtube-dl --no-deps'
        os.system(command)

        e = await utils.answer(d, self.strings('installing_shazam'))
        command = 'pip install ShazamAPI --no-deps'
        os.system(command)
        await asyncio.sleep(1)

        attempt = await utils.answer(e, self.strings('attempting_for_install'))
        msg = await self.client.send_message(message.chat_id, '<i>Installing...</i>')
        await self.allmodules.commands["dlmod"](await utils.answer(msg, f"{self.get_prefix()}dlmod voicemod"))

        installed = await self.check_module()

        if installed:
            await utils.answer(attempt, self.strings('installed_all'))
        else:
            await utils.answer(attempt, self.strings('егор'))
