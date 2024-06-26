from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from keyboards import return_to_menu_kb

from db.user_service import UserService
from form import Form

from handlers.router import router


@router.callback_query(F.data.startswith('stop_tracking'))
async def stop_tracking_item(callback: CallbackQuery, user_service: UserService):
    number = int(callback.data.split('stop_tracking_')[1])
    await user_service.delete_user_product(callback.from_user.id, number)
    await callback.message.edit_text('Вы больше не отслеживаете этот товар', reply_markup=InlineKeyboardMarkup(
    inline_keyboard=[[]]))
    # await callback.message.edit()
    await callback.answer()
    # await callback.message.delete_reply_markup()
