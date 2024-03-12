from schemas import User, Request
from constants import TG_IDS
from utils import get_gemini_token
from aiogram import types
from aiogram.dispatcher.middlewares import BaseMiddleware

class DbCheckMiddleware(BaseMiddleware):
    async def on_process_message(self, message: types.Message, data: dict):

        token = await get_gemini_token()
        user = await User.get_or_none(telegram_id=message.from_user.id)

        if not user:
            user = await User.create(telegram_id=message.from_user.id,
                                     username=message.from_user.username,
                                     first_name=message.from_user.first_name,
                                     last_name=message.from_user.last_name)

        if user.balance <= 0 or message.from_user.id not in TG_IDS:
            raise PermissionError("Извините, Вы не можете отправлять запросы")

        else:

            data['params'] = {"user": user, "token": token}

            await Request.create(
                user=user,
                query=message.text,
                token=token,
            )


