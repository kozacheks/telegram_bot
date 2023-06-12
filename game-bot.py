from telegram.ext import CommandHandler, Application

async def start(update, context):
    chat = update.effective_chat
    await context.bot.send_message(chat_id=chat.id, text="Привіт, це гейм бот. Бот буде виводити жанр та короткий сюжет гри, щоб дізнатися які ігри ви можете вивести, напишіть /help.")

async def help(update, context):
    chat = update.effective_chat
    await context.bot.send_message(chat_id=chat.id, text="Список команд: /the_witcher_3, /stalker_shadow_of_chernobyl, /stalker_clear_sky, /stalker_call_of_pripyat")

async def the_witcher_3(update, context):
    chat = update.effective_chat
    await context.bot.send_message(chat_id=chat.id, text="Жанр: рольова-екшн гра. Короткий сюжет: Гра розпочинається роликом, який демонструє пошуки Йеннефер Ґеральтом та Весемиром. Пошуки їх заводять в село Білий Сад, де два відьмаки й зупиняються. Там вони дізнаються про недавню битву між темерійцями та нільфгаардцями. Весемір зупиняється в таверні, а Ґеральт відправляється в табір нільфгаардців. Там командир гарнізону розповідає відьмаку про те, що Йеннефер у Визимі — столиці окупованої Темерії. Але перед цим Ґеральт мав вбити грифона, щоб отримати інформацію. Відьмак повертається до Весеміра. Разом вбивши грифона, вони йдуть до таверни, де потім відбувається сутичка між відьмаками та п'яними темерійськими патріотами. Останніх, відьмаки вбивають. На виході із таверни вони натикаються на нільфгаардців та Йеннефер, що несподівано з'явилась. Вона говорить, що імператор Емгир хоче аудієнції з Ґеральтом. Весемир вирушає до Каер Морену у справах, а Ґеральт з Йеннефер вирушає до Емгира. Під час подорожі, на «Білого вовка» та його супутницю нападає Дикий Гон, але попри на це, вони приїжджають на імператорський прийом. Імператор Емгир хоче, щоб Ґеральт знайшов його дочку Цірі, що нещодавно повернулася. І Ґеральт вирушає на пошуки… https://th.bing.com/th/id/OIP.H83H9Bq_0H7m_ZyY04O82AHaEK?w=299&h=180&c=7&r=0&o=5&dpr=1.2&pid=1.7")

async def stalker_shadow_of_chernobyl(update, context):
    chat = update.effective_chat
    await context.bot.send_message(chat_id=chat.id, text="Жанр: шутер від першої особи, виживання/хоррор з елементами рольової гри і природницького бойовика. Короткий сюжет: Перша гра серії. Гравець бере на себе роль сталкера Міченого, що страждає на амнезію, якому доручено вбити іншого сталкера — Стрільця. Перемагаючи ворогів та допомагаючи іншим сталкерам, протагоніст знаходить підказки розгадки таємниць свого минулого та справжньої особистості. В «S.T.A.L.K.E.R.: Тінь Чорнобиля» є 7 кінцівок. Вони залежать від різних факторів: зароблених грошей, підтримки певних фракцій, відновлення пам'яті героя. https://th.bing.com/th/id/OIP.uR6mI8j6emYOa0Eh-mds3QHaEK?w=333&h=187&c=7&r=0&o=5&dpr=1.2&pid=1.7")

async def stalker_clear_sky(update, context):
    chat = update.effective_chat
    await context.bot.send_message(chat_id=chat.id, text="Жанр: шутер від першої особи, виживання/хоррор з елементами рольової гри і природницького бойовика. Короткий сюжет: Друга гра серії, пріквел оригінальної гри «S.T.A.L.K.E.R.: Тінь Чорнобиля». Гравець приймає роль Шраму — найманця-ветерана. Під час супроводу вчених у Зоні, його накриває викид. Та найманця рятує угруповання Чисте Небо, що досліджує природу Зони та намагається її зрозуміти. В процесі гри, гравцеві доведеться приймати різні сторони протистояння в Зоні, щоб допомогти Чистому Небу досягти їх мети. https://th.bing.com/th/id/OIP.ZgoGwrjLQJdF8O09AS3QtAHaEo?w=290&h=181&c=7&r=0&o=5&dpr=1.2&pid=1.7")

async def stalker_call_of_pripyat(update, context):
    chat = update.effective_chat
    await context.bot.send_message(chat_id=chat.id, text="Жанр: шутер від першої особи, виживання/хоррор з елементами рольової гри і природницького бойовика. Короткий сюжет: Третя гра серії, події якої відбуваються незабаром після подій «S.T.A.L.K.E.R.: Тінь Чорнобиля». Дізнавшись, що шлях до центру Зони відкрито, уряд вирішує взяти його під свій контроль за допомогою операції «Фарватер», під час якої вони планують дослідити території перед відправкою основних збройних сил. Та не дивлячись на ретельні приготування, операція провалюється, а гвинтокрили зазнають аварії. Для виявлення причин аварії Служба безпеки України відправляє в Зону колишнього сталкера, майора Олександра Дегтярьова. https://th.bing.com/th/id/OIP.4K5HpHSQ2laZm_RQDmxy3QAAAA?w=115&h=180&c=7&r=0&o=5&dpr=1.2&pid=1.7")

application = Application.builder().token("6182553923:AAGGQREItSspwbmX-xP_fFhqLq62osFNaTc").build()
application.add_handler(CommandHandler("start", start))
application.add_handler(CommandHandler("help", help))
application.add_handler(CommandHandler("the_witcher_3", the_witcher_3))
application.add_handler(CommandHandler("stalker_shadow_of_chernobyl", stalker_shadow_of_chernobyl))
application.add_handler(CommandHandler("stalker_clear_sky", stalker_clear_sky))
application.add_handler(CommandHandler("stalker_call_of_pripyat", stalker_call_of_pripyat))
application.run_polling()