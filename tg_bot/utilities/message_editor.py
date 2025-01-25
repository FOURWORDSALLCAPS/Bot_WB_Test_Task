from typing import Optional, Union
from pydantic import ValidationError

from aiogram.enums import ContentType
from aiogram.exceptions import TelegramBadRequest
from aiogram.types import (
    CallbackQuery,
    InlineKeyboardMarkup,
    InputFile,
    Message,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
)

from tg_bot.base import bot


async def one_message_editor(
    event: CallbackQuery | Message,
    text: Optional[str] = None,
    reply_markup: Optional[Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove]] = None,
    photo: Union[InputFile, str] = None,
    document: Union[InputFile, str] = None,
    video: Union[InputFile, str] = None,
    parse_mode: Optional[str] = 'HTML',
    disable_web_page_preview: bool = False,
    message_effect_id: Optional[str] = None,
) -> None:
    content_type = {ContentType.PHOTO}

    async def delete_message(msg: Message) -> None:
        try:
            await msg.delete()
        except TelegramBadRequest:
            pass

    if isinstance(event, CallbackQuery):
        message = event.message
        if not photo and not video and not document and message.content_type not in content_type:
            try:
                await message.edit_text(
                    text=text,
                    parse_mode=parse_mode,
                    reply_markup=reply_markup,
                    disable_web_page_preview=disable_web_page_preview,
                    message_effect_id=message_effect_id,
                )
                return
            except (TelegramBadRequest, ValidationError):
                await delete_message(message)

    else:
        message = event

    await delete_message(message)

    if photo:
        await message.answer_photo(
            photo=photo,
            caption=text,
            reply_markup=reply_markup,
            parse_mode=parse_mode,
            disable_web_page_preview=disable_web_page_preview,
            message_effect_id=message_effect_id,
        )
    else:
        message_id = await message.answer(
            text=text,
            reply_markup=reply_markup,
            parse_mode=parse_mode,
            disable_web_page_preview=disable_web_page_preview,
            message_effect_id=message_effect_id,
        )
        delete_message_ids = [message_id.message_id - i for i in range(1, 4)]
        for delete_message_id in delete_message_ids:
            try:
                await bot.delete_message(chat_id=message.chat.id, message_id=delete_message_id)
            except TelegramBadRequest:
                pass
