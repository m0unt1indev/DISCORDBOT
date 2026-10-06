import disnake                      # ! импорт Discord-API (disnake)
from disnake.ext import commands  # ! обращается к disnake для использования метода commands 

intents = disnake.Intents.default()   # ! создает переменную и стандартные значения для получения событий Discord 
intents.members=True
intents.message_content=True           # ! Разрешает боту получать информацию об участниках и содержимое сообщений.

bot = commands.Bot(               # ! инициализация объекта бота. (создает экземпляр бота)
    command_prefix="!",         # ! Cимвол, с которого должны начинаться команды для этого бота (например, !help).
    intents=intents               # ! передача прав доступа и разрешений (намерений) для отслеживания событий (например, сообщений или участников)
)



# ! декоратор bot.event, который обращается к функции on_ready, и выдает сообщение о запуске бота 
@bot.event
async def on_ready():
    print(f'Бот запущен {bot.user}')       # * выводит текст в терминал о том, что запуск бота успешно произведен 




# ! комманда /ping
@bot.slash_command(name='ping', description='узнать вашу задержку')  # ! декоратор bot.slash_command, превращает код в slash команду дискорда 
async def ping(inter):         # ! async def — это специальный вид функции Python, который используется для асинхронного выполнения, она нужна для того что бы функция не зависала на месте, а ping это название функции.
    latency = round(bot.latency * 1000)  # * bot.latency * 1000 это метод disnake, который позволяет получить задержку пользователя.
    if latency < 100:  # *  обращаемся к переменной latency к которой присвоен метод определения задержки ползователя, и проверяет условие  
      status = "🟢Отличное соединение!"
    elif latency < 200:       # *  проверяет второе условие, оно срабатывает при задержке пользователя 100-199 
       status = "🟡Нормальное соединение!"
    else:                         # * работает при задержке <200
       status = "🔴Высокая задержка!" 
    await inter.response.send_message(f'Ваша задержка: {latency}ms\n{status}')  # ! await говорит: «Подожди завершения этой асинхронной операции».
# ! inter — это объект взаимодействия с Discord.
# ! Discord передаёт нашей функции информацию об этом взаимодействии.
# ! Например, через inter мы можем получить информацию о пользователе, сервере и самой команде.
# * send_message = Говорим Discord:
# * «Отправь сообщение».



# ! command /say 
@bot.slash_command(  # ! декоратор превращает код в / комманду 
name='say',          # * название и описание комманды 
description='Сообщение от имени бота'

)                     # ! асинхронная функция выполняющая фунцию say 
async def say(
    inter,
    текст: str 
):
 await inter.response.send_message(текст)



# ! вопрос-ответ
answers = {                                                       # * список вопрос-ответ
"привет": "👋 Привет! Рад тебя видеть!",
"кто ты?": "🤖 Я Discord-бот, написанный на Python!",
"как дела?": "😎 Отлично! Спасибо, что спросил!",
"что ты умеешь?": "🛠️ Пока учусь, но скоро буду уметь гораздо больше!",
"спасибо": "😊 Пожалуйста!"
}

@bot.event                                 # ! дикоратор позволяет работать дискорду с сообщениями 
async def on_message(message):
   if message.author == bot.user:     
       return
   
   text = message.content.lower()           # ! получили текст сообщения и сохранили его в text c поддержкой нижнего регистра.
   
   if text in answers:                                    # ! in проверяет:
    await message.channel.send(answers[text])             # ! Есть ли такой ключ в словаре answers?
    
    await bot.process_commands(message)







bot.run('MTU1NjY0NTY2MTg5MjU0MjQ4NA.GeaTCo.Cv0cs-P4Q71DRtR8KIRmDUthEure47RudaEIXA')   # ! отвечает за запуск бота 