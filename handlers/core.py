from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp
from data.computers import computer_types
from keyboards.default import menu, goal_for_using, computer_or_back


@dp.message_handler(text_contains='Tavsiya')
async def comp_suggest(message: types.Message, state: FSMContext):
    await message.answer(
        'Yaxshi, kompyuter sizga nima maqsadda kerak\n'
        'Quyidagilardan birini tanlang',
        reply_markup=goal_for_using
    )
    await state.reset_data()


@dp.message_handler(text_contains='Dasturlash')
async def comp_suggest(message: types.Message, state: FSMContext):
    await message.answer(
        computer_types['programming']['about'],
        reply_markup=computer_or_back
    )
    await state.update_data(type='programming')


@dp.message_handler(text_contains='Grafik dizayn')
async def comp_suggest(message: types.Message, state: FSMContext):
    await message.answer(
        computer_types['graphics']['about'],
        reply_markup=computer_or_back
    )
    await state.update_data(type='graphics')


@dp.message_handler(text_contains='O\'yin uchun')
async def comp_suggest(message: types.Message, state: FSMContext):
    await message.answer(
        computer_types['gaming']['about'],
        reply_markup=computer_or_back
    )
    await state.update_data(type='gaming')


@dp.message_handler(text_contains='Ofis uchun')
async def comp_suggest(message: types.Message, state: FSMContext):
    await message.answer(
        computer_types['office']['about'],
        reply_markup=computer_or_back
    )
    await state.update_data(type='office')


@dp.message_handler(text_contains='Kompyuter ko\'rish')
async def comp_suggest(message: types.Message, state: FSMContext):
    state_data = await state.get_data()
    comp_type = state_data.get('type')
    if not comp_type:
        await message.answer(
            f"Salom, {message.from_user.full_name}!\n"
            "Bu yerda siz, o'zingizga mos keladigan\n"
            "notebook uchun tavsiyalar olishingiz mumkin",
            reply_markup=menu
        )
        return
    await message.answer(
        computer_types[comp_type]['title'],
        reply_markup=computer_or_back
    )
    for comp in computer_types[comp_type]['computers']:
        await message.answer(comp)


@dp.message_handler(text_contains='Orqaga')
async def comp_suggest(message: types.Message, state: FSMContext):
    await message.answer(
        'Yaxshi, kompyuter sizga nima maqsadda kerak\n'
        'Quyidagilardan birini tanlang',
        reply_markup=goal_for_using
    )
    await state.reset_data()
