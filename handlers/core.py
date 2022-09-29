from aiogram import types

from loader import dp
from keyboards.default import goal_for_using


@dp.message_handler(text_contains="Tavsiya")
async def bot_echo(message: types.Message):
    await message.answer(
        "Yaxshi, notebook sizga nima maqsadda kerak\n"
        "Quyidagilardan birini tanlang",
        reply_markup=goal_for_using
    )
