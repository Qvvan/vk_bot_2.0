import vk_api, json
import copy
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from datetime import datetime, date
import calendar
from monday import schedule
from vk_api.keyboard import VkKeyboard, VkKeyboardColor


token = "08e1dd015f60d5c33c2f4cda4905981f0889eee1d34cf007eed697a1323dc64e12ca8f3c8365b0a1641f3"

vk_session = vk_api.VkApi(token = token)
vk = vk_session.get_api()
longpoll = VkBotLongPoll(vk_session, 199359389)

current_datetime = datetime.now()
time1 = str(current_datetime.hour) + ':' + str(current_datetime.minute)
print(time1)

my_date = date.today()
day1 = calendar.day_name[my_date.weekday()]

nums = int(datetime.utcnow().isocalendar()[1])
x = datetime.now()

k = 1
lll = 0

def otmena_par(para, msg):
    para[int(msg)] = 0

def add_par(para, msg):
    para[int(msg)] = 1

def sender(id, text):
    vk_session.method('messages.send', {'chat_id': id, "message": text, "random_id": 0})

def send_message(id, text, keyboard=None):
    vk_session.method("messages.send", {"chat_id": id, "message": text,
                                "random_id": 0,
                                "keyboard": keyboard})


id = 3
name = "@q.onee(.)@id120956346(.)@id82574142(.)@jojokir(.)@blake1000(.)@fijiplayer(.)@evsenadinjo(.)@pfrolov20(.)@absolutelycarnage(.)@id167848868(.)@dureman23 (.)@id404333201(.)@goddamndatisvadem(.)@id193373728(.)@tvojsutener(.)@bahus99(.)@r.sanya12(.)@i.golovin2001(.)@danila_chr(.)@id118566325(.)@stuffed_shirt(.)@nepomasti(.)@ibetadam99(.)@zlydenheh(.)@id458896500(.)@hevabat(.)@idaftt(.)@4dam22(.)@jleandoer96(.)@billy_milligan11(.)......................................................"

monday_para0 = ['0', 'Нап. тел. среды и методы защиты', 'Технологии сети интернет', 'Мультисервисные сети и системы', 'Линии радиосвязи и методы их защиты', 'Окно']
tuesday_para0 = ['0', 'Микропроцессорная техника', 'Окно', 'Микропроцессорная техника', 'Инф-онные технологии и программирование', 'Цифр-ые сети передачи и методы их защиты']
wednesday_para0 = ['0', 'Окно', 'Окно', 'ВвИТ', 'ВвИТ', 'Цифр-ые сети передачи и методы их защиты']
thursday_para0 = ['0', 'Мультисервисные сети и системы', 'Микропроцессорная техника', 'Инф-онные технологии и программирование', 'Цифр-ые сети передачи и методы их защиты', 'Окно']
friday_para0 = ['0', 'Окно', 'Физра', 'Инф-онные технологии и программирование', 'Цифр-ые сети передачи и методы их защиты', 'Окно']
saturday_para0 = ['0', 'Мультисервисные сети и системы', 'Инф-онные технологии и программирование', 'Линии радиосвязи и методы их защиты', 'Окно', 'Окно']

monday_para1 = ['0', 'Нап. тел. среды и методы защиты', 'Технологии сети интернет', 'Мультисервисные сети и системы', 'Линии радиосвязи и методы их защиты', 'Окно']
tuesday_para1 = ['0', 'Цифр-ые сети передачи и методы их защиты', 'Микропроцессорная техника', 'Инф-онные технологии и программирование', 'Окно', 'Микропроцессорная техника']
wednesday_para1 = ['0', 'ВвИТ', 'Окно', 'Окно', 'Окно', 'Окно']
thursday_para1 = ['0', 'Мультисервисные сети и системы', 'Микропроцессорная техника', 'Инф-онные технологии и программирование', 'Инф-онные технологии и программирование', 'Окно']
friday_para1 = ['0', 'Окно', 'Физра', 'Инф-онные технологии и программирование', 'Цифр-ые сети передачи и методы их защиты', 'Окно']
saturday_para1 = ['0', 'Мультисервисные сети и системы', 'Инф-онные технологии и программирование', 'Линии радиосвязи и методы их защиты', 'Окно', 'Окно']


para_mon0 = [0,1,1,1,1,0]
para_tue0 = [0,1,0,1,1,1]
para_wed0 = [0,0,0,1,1,1]
para_thu0 = [0,1,1,1,1,0]
para_fri0 = [0,0,1,1,1,0]
para_sat0 = [0,1,1,1,0,0]

para_mon1 = [0,1,1,1,1,0]
para_tue1 = [0,1,1,1,0,1]
para_wed1 = [0,1,0,0,0,0]
para_thu1 = [0,1,1,1,1,0]
para_fri1 = [0,0,1,1,1,0]
para_sat1 = [0,1,1,1,0,0]

nedelya = 1

while True:
    try:
        current_datetime = datetime.now()
        time1 = str(current_datetime.hour) + ':' + str(current_datetime.minute)
        my_date = date.today()
        day1 = calendar.day_name[my_date.weekday()]
        nums = int(datetime.utcnow().isocalendar()[1])

        if day1 == 'Monday' and time1 == '3:0':
            nedelya = 1

        if (nums % 2) != 0 and nedelya == 1:
            para_mon = para_mon0.copy()
            para_tue = para_tue0.copy()
            para_wed = para_wed0.copy()
            para_thu = para_thu0.copy()
            para_fri = para_fri0.copy()
            para_sat = para_sat0.copy()

            monday_para = monday_para0.copy()
            tuesday_para = tuesday_para0.copy()
            wednesday_para = wednesday_para0.copy()
            thursday_para = thursday_para0.copy()
            friday_para = friday_para0.copy()
            saturday_para = saturday_para0.copy()

            nedelya = 0

        if (nums % 2) == 0 and nedelya == 1:
            para_mon = para_mon1.copy()
            para_tue = para_tue1.copy()
            para_wed = para_wed1.copy()
            para_thu = para_thu1.copy()
            para_fri = para_fri1.copy()
            para_sat = para_sat1.copy()

            monday_para = monday_para1.copy()
            tuesday_para = tuesday_para1.copy()
            wednesday_para = wednesday_para1.copy()
            thursday_para = thursday_para1.copy()
            friday_para = friday_para1.copy()
            saturday_para = saturday_para1.copy()

            nedelya = 0

            # _________________________Создание клавиатур______________________________

        # Понедельник
        keyboard1 = VkKeyboard(inline=True)
        for i in range(1, 5):
            if para_mon[i] == 1:
                keyboard1.add_callback_button(monday_para[i], VkKeyboardColor.POSITIVE, payload=str(i + 100))
            else:
                keyboard1.add_callback_button(monday_para[i], VkKeyboardColor.NEGATIVE, payload=str(i + 100))
            keyboard1.add_line()
        if para_mon[5] == 1:
            keyboard1.add_callback_button(monday_para[5], VkKeyboardColor.POSITIVE, payload=str(5 + 100))
        else:
            keyboard1.add_callback_button(monday_para[5], VkKeyboardColor.NEGATIVE, payload=str(5 + 100))
        keyboard1.add_line()
        keyboard1.add_callback_button('Назад', VkKeyboardColor.PRIMARY, payload='16')

        # Вторник
        keyboard2 = VkKeyboard(inline=True)
        for i in range(1, 5):
            if para_tue[i] == 1:
                keyboard2.add_callback_button(tuesday_para[i], VkKeyboardColor.POSITIVE, payload=str(i + 200))
            else:
                keyboard2.add_callback_button(tuesday_para[i], VkKeyboardColor.NEGATIVE, payload=str(i + 200))
            keyboard2.add_line()
        if para_tue[5] == 1:
            keyboard2.add_callback_button(tuesday_para[5], VkKeyboardColor.POSITIVE, payload=str(5 + 200))
        else:
            keyboard2.add_callback_button(tuesday_para[5], VkKeyboardColor.NEGATIVE, payload=str(5 + 200))
        keyboard2.add_line()
        keyboard2.add_callback_button('Назад', VkKeyboardColor.PRIMARY, payload='16')

        # Среда
        keyboard3 = VkKeyboard(inline=True)
        for i in range(1, 5):
            if para_wed[i] == 1:
                keyboard3.add_callback_button(wednesday_para[i], VkKeyboardColor.POSITIVE, payload=str(i + 300))
            else:
                keyboard3.add_callback_button(wednesday_para[i], VkKeyboardColor.NEGATIVE, payload=str(i + 300))
            keyboard3.add_line()
        if para_wed[5] == 1:
            keyboard3.add_callback_button(wednesday_para[5], VkKeyboardColor.POSITIVE, payload=str(5 + 300))
        else:
            keyboard3.add_callback_button(wednesday_para[5], VkKeyboardColor.NEGATIVE, payload=str(5 + 300))
        keyboard3.add_line()
        keyboard3.add_callback_button('Назад', VkKeyboardColor.PRIMARY, payload='16')

        # Четверг
        keyboard4 = VkKeyboard(inline=True)
        for i in range(1, 5):
            if para_thu[i] == 1:
                keyboard4.add_callback_button(thursday_para[i], VkKeyboardColor.POSITIVE, payload=str(i + 400))
            else:
                keyboard4.add_callback_button(thursday_para[i], VkKeyboardColor.NEGATIVE, payload=str(i + 400))
            keyboard4.add_line()
        if para_thu[5] == 1:
            keyboard4.add_callback_button(thursday_para[5], VkKeyboardColor.POSITIVE, payload=str(5 + 400))
        else:
            keyboard4.add_callback_button(thursday_para[5], VkKeyboardColor.NEGATIVE, payload=str(5 + 400))
        keyboard4.add_line()
        keyboard4.add_callback_button('Назад', VkKeyboardColor.PRIMARY, payload='16')

        # Пятница
        keyboard5 = VkKeyboard(inline=True)
        for i in range(1, 5):
            if para_fri[i] == 1:
                keyboard5.add_callback_button(friday_para[i], VkKeyboardColor.POSITIVE, payload=str(i + 500))
            else:
                keyboard5.add_callback_button(friday_para[i], VkKeyboardColor.NEGATIVE, payload=str(i + 500))
            keyboard5.add_line()
        if para_fri[5] == 1:
            keyboard5.add_callback_button(friday_para[5], VkKeyboardColor.POSITIVE, payload=str(5 + 500))
        else:
            keyboard5.add_callback_button(friday_para[5], VkKeyboardColor.NEGATIVE, payload=str(5 + 500))
        keyboard5.add_line()
        keyboard5.add_callback_button('Назад', VkKeyboardColor.PRIMARY, payload='16')

        # Суббота
        keyboard6 = VkKeyboard(inline=True)
        for i in range(1, 5):
            if para_sat[i] == 1:
                keyboard6.add_callback_button(saturday_para[i], VkKeyboardColor.POSITIVE, payload=str(i + 600))
            else:
                keyboard6.add_callback_button(saturday_para[i], VkKeyboardColor.NEGATIVE, payload=str(i + 600))
            keyboard6.add_line()
        if para_sat[5] == 1:
            keyboard6.add_callback_button(saturday_para[5], VkKeyboardColor.POSITIVE, payload=str(5 + 600))
        else:
            keyboard6.add_callback_button(saturday_para[5], VkKeyboardColor.NEGATIVE, payload=str(5 + 600))
        keyboard6.add_line()
        keyboard6.add_callback_button('Назад', VkKeyboardColor.PRIMARY, payload='16')


        #Понедельник
        if day1 == 'Monday':
            lol, k = schedule(time1, para_mon, k)
            if lol:
                sender(id, monday_para[lol] + "@q.vvan(.)")
                lol = 0

        #Вторник
        if day1 == 'Tuesday':
            lol, k = schedule(time1, para_tue, k)
            if lol:
                sender(id, name + '\n' +tuesday_para[lol])
                lol = 0

        #Среда
        if day1 == 'Wednesday':
            lol, k = schedule(time1, para_wed, k)
            if lol:
                sender(id, wednesday_para[lol])
                lol = 0

        #Четверг
        if day1 == 'Thursday':
            lol, k = schedule(time1, para_thu, k)
            if lol:
                sender(id, thursday_para[lol])
                lol = 0

        #Пятница
        if day1 == 'Friday':
            lol, k = schedule(time1, para_fri, k)
            if lol:
                sender(id, friday_para[lol])
                lol = 0
        #Суббота
        if day1 == 'Saturday':
            lol, k = schedule(time1, para_sat, k)
            if lol:
                sender(id, saturday_para[lol])
                lol = 0


        messagelist = longpoll.check()
        if messagelist:
            if messagelist[0].type == VkBotEventType.MESSAGE_NEW:
                msg = messagelist[0].object.message['text'].lower()

                if msg == 'неделя':
                    if (nums % 2) != 0:
                        sender(id, str(nums - 4) + ' верхняя(нечетная)')
                    else: sender(id, str(nums - 4) + ' нижняя(четная)')
                if msg == 'диск':
                    sender(id, 'https://drive.google.com/drive/folders/19W93cJFX3UxDoBcQoG-_VYOb4QqLekGb')
                if msg == 'дискорд':
                    sender(id, 'Дискорд нашей группы\nhttps://discord.gg/4MGt7U6Pdf')

                    #____________________________Начало расписания___________________________
                if msg == 'понедельник':
                    keyboard = VkKeyboard(inline=True)
                    for i in range(1,5):
                        if para_mon[i] == 1:
                            keyboard.add_callback_button(monday_para[i], VkKeyboardColor.POSITIVE)
                        else:
                            keyboard.add_callback_button(monday_para[i], VkKeyboardColor.NEGATIVE)
                        keyboard.add_line()
                    if para_mon[5] == 1:
                        keyboard.add_callback_button(monday_para[5], VkKeyboardColor.POSITIVE)
                    else: keyboard.add_callback_button(monday_para[5], VkKeyboardColor.NEGATIVE)
                    send_message(id, "Расписание на понедельник!", keyboard=keyboard.get_keyboard())

                if msg == 'вторник':
                    keyboard = VkKeyboard(inline=True)
                    for i in range(1,5):
                        if para_tue[i] == 1:
                            keyboard.add_callback_button(tuesday_para[i], VkKeyboardColor.POSITIVE)
                        else:
                            keyboard.add_callback_button(tuesday_para[i], VkKeyboardColor.NEGATIVE)
                        keyboard.add_line()
                    if para_tue[5] == 1:
                        keyboard.add_callback_button(tuesday_para[5], VkKeyboardColor.POSITIVE)
                    else: keyboard.add_callback_button(tuesday_para[5], VkKeyboardColor.NEGATIVE)
                    send_message(id, "Расписание на вторник!", keyboard=keyboard.get_keyboard())

                if msg == 'среда':
                    keyboard = VkKeyboard(inline=True)
                    for i in range(1,5):
                        if para_wed[i] == 1:
                            keyboard.add_callback_button(wednesday_para[i], VkKeyboardColor.POSITIVE)
                        else:
                            keyboard.add_callback_button(wednesday_para[i], VkKeyboardColor.NEGATIVE)
                        keyboard.add_line()
                    if para_wed[5] == 1:
                        keyboard.add_callback_button(wednesday_para[5], VkKeyboardColor.POSITIVE)
                    else: keyboard.add_callback_button(wednesday_para[5], VkKeyboardColor.NEGATIVE)
                    send_message(id, "Расписание на среду!", keyboard=keyboard.get_keyboard())

                if msg == 'четверг':
                    keyboard = VkKeyboard(inline=True)
                    for i in range(1,5):
                        if para_thu[i] == 1:
                            keyboard.add_callback_button(thursday_para[i], VkKeyboardColor.POSITIVE)
                        else:
                            keyboard.add_callback_button(thursday_para[i], VkKeyboardColor.NEGATIVE)
                        keyboard.add_line()
                    if para_thu[5] == 1:
                        keyboard.add_callback_button(thursday_para[5], VkKeyboardColor.POSITIVE)
                    else: keyboard.add_callback_button(thursday_para[5], VkKeyboardColor.NEGATIVE)
                    send_message(id, "Расписание на четверг!", keyboard=keyboard.get_keyboard())

                if msg == 'пятница':
                    keyboard = VkKeyboard(inline=True)
                    for i in range(1,5):
                        if para_fri[i] == 1:
                            keyboard.add_callback_button(friday_para[i], VkKeyboardColor.POSITIVE)
                        else:
                            keyboard.add_callback_button(friday_para[i], VkKeyboardColor.NEGATIVE)
                        keyboard.add_line()
                    if para_fri[5] == 1:
                        keyboard.add_callback_button(friday_para[5], VkKeyboardColor.POSITIVE)
                    else: keyboard.add_callback_button(friday_para[5], VkKeyboardColor.NEGATIVE)
                    send_message(id, "Расписание на пятницу!", keyboard=keyboard.get_keyboard())

                if msg == 'суббота':
                    keyboard = VkKeyboard(inline=True)
                    for i in range(1,5):
                        if para_sat[i] == 1:
                            keyboard.add_callback_button(saturday_para[i], VkKeyboardColor.POSITIVE)
                        else:
                            keyboard.add_callback_button(saturday_para[i], VkKeyboardColor.NEGATIVE)
                        keyboard.add_line()
                    if para_sat[5] == 1:
                        keyboard.add_callback_button(saturday_para[5], VkKeyboardColor.POSITIVE)
                    else: keyboard.add_callback_button(saturday_para[5], VkKeyboardColor.NEGATIVE)
                    send_message(id, "Расписание на субботу!", keyboard=keyboard.get_keyboard())

                if msg == 'доб' or msg == 'отм':
                    if msg == 'доб':
                        add_or_not = 1
                    elif msg == 'отм':
                        add_or_not = 0
                    keyboard = VkKeyboard(inline=True)
                    keyboard.add_callback_button('Понедельник', VkKeyboardColor.POSITIVE, payload='1')
                    keyboard.add_callback_button('Вторник', VkKeyboardColor.POSITIVE, payload='2')
                    keyboard.add_line()
                    keyboard.add_callback_button('Среда', VkKeyboardColor.POSITIVE, payload='3')
                    keyboard.add_callback_button('Четверг', VkKeyboardColor.POSITIVE, payload='4')
                    keyboard.add_line()
                    keyboard.add_callback_button('Пятница', VkKeyboardColor.POSITIVE, payload='5')
                    keyboard.add_callback_button('Суббота', VkKeyboardColor.POSITIVE, payload='6')
                    keyboard.add_line()
                    keyboard.add_callback_button('Закрыть', VkKeyboardColor.PRIMARY, payload='0')
                    if msg == 'доб':
                        keyboard.add_callback_button('Отмена', VkKeyboardColor.NEGATIVE, payload='901')
                        send_message(id, "Процесс ДОБАВЛЕНИЯ пар", keyboard=keyboard.get_keyboard())
                    elif msg == 'отм':
                        keyboard.add_callback_button('Добавить', VkKeyboardColor.NEGATIVE, payload='902')
                        send_message(id, "Процесс ОТМЕНЫ пар", keyboard=keyboard.get_keyboard())


            elif messagelist[0].type == VkBotEventType.MESSAGE_EVENT:
                    if messagelist[0].object.payload == 901:
                        add_or_not = 0
                        keyboard = VkKeyboard(inline=True)
                        keyboard.add_callback_button('Понедельник', VkKeyboardColor.POSITIVE, payload='1')
                        keyboard.add_callback_button('Вторник', VkKeyboardColor.POSITIVE, payload='2')
                        keyboard.add_line()
                        keyboard.add_callback_button('Среда', VkKeyboardColor.POSITIVE, payload='3')
                        keyboard.add_callback_button('Четверг', VkKeyboardColor.POSITIVE, payload='4')
                        keyboard.add_line()
                        keyboard.add_callback_button('Пятница', VkKeyboardColor.POSITIVE, payload='5')
                        keyboard.add_callback_button('Суббота', VkKeyboardColor.POSITIVE, payload='6')
                        keyboard.add_line()
                        keyboard.add_callback_button('Закрыть', VkKeyboardColor.PRIMARY, payload='0')
                        keyboard.add_callback_button('Добавить', VkKeyboardColor.NEGATIVE, payload='902')
                        last_id = vk.messages.edit(
                            peer_id=messagelist[0].obj.peer_id,
                            message='Процесс ОТМЕНЫ пар',
                            conversation_message_id=messagelist[0].obj.conversation_message_id,
                            keyboard=(keyboard).get_keyboard())

                    if messagelist[0].object.payload == 902:
                        add_or_not = 1
                        keyboard = VkKeyboard(inline=True)
                        keyboard.add_callback_button('Понедельник', VkKeyboardColor.POSITIVE, payload='1')
                        keyboard.add_callback_button('Вторник', VkKeyboardColor.POSITIVE, payload='2')
                        keyboard.add_line()
                        keyboard.add_callback_button('Среда', VkKeyboardColor.POSITIVE, payload='3')
                        keyboard.add_callback_button('Четверг', VkKeyboardColor.POSITIVE, payload='4')
                        keyboard.add_line()
                        keyboard.add_callback_button('Пятница', VkKeyboardColor.POSITIVE, payload='5')
                        keyboard.add_callback_button('Суббота', VkKeyboardColor.POSITIVE, payload='6')
                        keyboard.add_line()
                        keyboard.add_callback_button('Закрыть', VkKeyboardColor.PRIMARY, payload='0')
                        keyboard.add_callback_button('Отмена', VkKeyboardColor.NEGATIVE, payload='901')
                        last_id = vk.messages.edit(
                            peer_id=messagelist[0].obj.peer_id,
                            message='Процесс ДОБАВЛЕНИЯ пар',
                            conversation_message_id=messagelist[0].obj.conversation_message_id,
                            keyboard=(keyboard).get_keyboard())

                    #Понедельник
                    if messagelist[0].object.payload == 1:
                        last_id = vk.messages.edit(
                            peer_id=messagelist[0].obj.peer_id,
                            message='Понедельник',
                            conversation_message_id=messagelist[0].obj.conversation_message_id,
                            keyboard=(keyboard1).get_keyboard())

                    #Вторник
                    if messagelist[0].object.payload == 2:
                        last_id = vk.messages.edit(
                            peer_id=messagelist[0].obj.peer_id,
                            message='Вторник',
                            conversation_message_id=messagelist[0].obj.conversation_message_id,
                            keyboard=(keyboard2).get_keyboard())

                    #Среда
                    if messagelist[0].object.payload == 3:
                        last_id = vk.messages.edit(
                            peer_id=messagelist[0].obj.peer_id,
                            message='Среда',
                            conversation_message_id=messagelist[0].obj.conversation_message_id,
                            keyboard=(keyboard3).get_keyboard())

                    #Четверг
                    if messagelist[0].object.payload == 4:
                        last_id = vk.messages.edit(
                            peer_id=messagelist[0].obj.peer_id,
                            message='Четверг',
                            conversation_message_id=messagelist[0].obj.conversation_message_id,
                            keyboard=(keyboard4).get_keyboard())

                    #Пятница
                    if messagelist[0].object.payload == 5:
                        last_id = vk.messages.edit(
                            peer_id=messagelist[0].obj.peer_id,
                            message='Пятница',
                            conversation_message_id=messagelist[0].obj.conversation_message_id,
                            keyboard=(keyboard5).get_keyboard())

                    #Суббота
                    if messagelist[0].object.payload == 6:
                        last_id = vk.messages.edit(
                            peer_id=messagelist[0].obj.peer_id,
                            message='Суббота',
                            conversation_message_id=messagelist[0].obj.conversation_message_id,
                            keyboard=(keyboard6).get_keyboard())

                    #Кнопка назад
                    if messagelist[0].object.payload == 16:
                        if add_or_not == 1:
                            qwe = 'Процесс ДОБАВЛЕНИЯ пар'
                        elif add_or_not == 0:
                            qwe = 'Процесс ОТМЕНЫ пар'
                        last_id = vk.messages.edit(
                            peer_id=messagelist[0].obj.peer_id,
                            message=qwe,
                            conversation_message_id=messagelist[0].obj.conversation_message_id,
                            keyboard=(keyboard).get_keyboard())

                    #Кнопка закрыть все
                    if messagelist[0].object.payload == '0':
                        last_id = vk.messages.edit(
                            peer_id=messagelist[0].obj.peer_id,
                            message='Удачи!',
                            conversation_message_id=messagelist[0].obj.conversation_message_id)

                    #Пары понедельника
                    if (messagelist[0].object.payload == 101 or messagelist[0].object.payload == 102 or messagelist[0].object.payload == 103
                        or messagelist[0].object.payload == 104 or messagelist[0].object.payload == 105):
                        word = str(messagelist[0].object.payload)[2]
                        if add_or_not == 1:
                            add_par(para_mon, word)
                        elif add_or_not == 0:
                            otmena_par(para_mon, word)
                        keyboard1 = VkKeyboard(inline=True)

                        for i in range(1, 5):
                            if para_mon[i] == 1:
                                keyboard1.add_callback_button(monday_para[i], VkKeyboardColor.POSITIVE, payload=str(i + 100))
                            else:
                                keyboard1.add_callback_button(monday_para[i], VkKeyboardColor.NEGATIVE, payload=str(i + 100))
                            keyboard1.add_line()
                        if para_mon[5] == 1:
                            keyboard1.add_callback_button(monday_para[5], VkKeyboardColor.POSITIVE, payload=str(5 + 100))
                        else:
                            keyboard1.add_callback_button(monday_para[5], VkKeyboardColor.NEGATIVE, payload=str(5 + 100))
                        keyboard1.add_line()
                        keyboard1.add_callback_button('Назад', VkKeyboardColor.PRIMARY, payload='16')
                        last_id = vk.messages.edit(
                            peer_id=messagelist[0].obj.peer_id,
                            message='Понедельник',
                            conversation_message_id=messagelist[0].obj.conversation_message_id,
                            keyboard=(keyboard1).get_keyboard())

                    #Пары вторника
                    if (messagelist[0].object.payload == 201 or messagelist[0].object.payload == 202 or messagelist[0].object.payload == 203
                        or messagelist[0].object.payload == 204 or messagelist[0].object.payload == 205):
                        word = str(messagelist[0].object.payload)[2]
                        if add_or_not == 1:
                            add_par(para_tue, word)
                        elif add_or_not == 0:
                            otmena_par(para_tue, word)
                        keyboard2 = VkKeyboard(inline=True)
                        for i in range(1, 5):
                            if para_tue[i] == 1:
                                keyboard2.add_callback_button(tuesday_para[i], VkKeyboardColor.POSITIVE, payload=str(i + 200))
                            else:
                                keyboard2.add_callback_button(tuesday_para[i], VkKeyboardColor.NEGATIVE, payload=str(i + 200))
                            keyboard2.add_line()
                        if para_tue[5] == 1:
                            keyboard2.add_callback_button(tuesday_para[5], VkKeyboardColor.POSITIVE, payload=str(5 + 200))
                        else:
                            keyboard2.add_callback_button(tuesday_para[5], VkKeyboardColor.NEGATIVE, payload=str(5 + 200))
                        keyboard2.add_line()
                        keyboard2.add_callback_button('Назад', VkKeyboardColor.PRIMARY, payload='16')
                        last_id = vk.messages.edit(
                            peer_id=messagelist[0].obj.peer_id,
                            message='Вторник',
                            conversation_message_id=messagelist[0].obj.conversation_message_id,
                            keyboard=(keyboard2).get_keyboard())

                    #Пары среда
                    if (messagelist[0].object.payload == 301 or messagelist[0].object.payload == 302 or messagelist[0].object.payload == 303
                        or messagelist[0].object.payload == 304 or messagelist[0].object.payload == 305):
                        word = str(messagelist[0].object.payload)[2]
                        if add_or_not == 1:
                            add_par(para_wed, word)
                        elif add_or_not == 0:
                            otmena_par(para_wed, word)
                        keyboard3 = VkKeyboard(inline=True)
                        for i in range(1, 5):
                            if para_wed[i] == 1:
                                keyboard3.add_callback_button(wednesday_para[i], VkKeyboardColor.POSITIVE, payload=str(i + 300))
                            else:
                                keyboard3.add_callback_button(wednesday_para[i], VkKeyboardColor.NEGATIVE, payload=str(i + 300))
                            keyboard3.add_line()
                        if para_wed[5] == 1:
                            keyboard3.add_callback_button(wednesday_para[5], VkKeyboardColor.POSITIVE, payload=str(5 + 300))
                        else:
                            keyboard3.add_callback_button(wednesday_para[5], VkKeyboardColor.NEGATIVE, payload=str(5 + 300))
                        keyboard3.add_line()
                        keyboard3.add_callback_button('Назад', VkKeyboardColor.PRIMARY, payload='16')
                        last_id = vk.messages.edit(
                            peer_id=messagelist[0].obj.peer_id,
                            message='Среда',
                            conversation_message_id=messagelist[0].obj.conversation_message_id,
                            keyboard=(keyboard3).get_keyboard())

                    #Пары четверг
                    if (messagelist[0].object.payload == 401 or messagelist[0].object.payload == 402 or messagelist[0].object.payload == 403
                        or messagelist[0].object.payload == 404 or messagelist[0].object.payload == 405):
                        word = str(messagelist[0].object.payload)[2]
                        if add_or_not == 1:
                            add_par(para_thu, word)
                        elif add_or_not == 0:
                            otmena_par(para_thu, word)
                        keyboard4 = VkKeyboard(inline=True)
                        for i in range(1, 5):
                            if para_thu[i] == 1:
                                keyboard4.add_callback_button(thursday_para[i], VkKeyboardColor.POSITIVE, payload=str(i + 400))
                            else:
                                keyboard4.add_callback_button(thursday_para[i], VkKeyboardColor.NEGATIVE, payload=str(i + 400))
                            keyboard4.add_line()
                        if para_thu[5] == 1:
                            keyboard4.add_callback_button(thursday_para[5], VkKeyboardColor.POSITIVE, payload=str(5 + 400))
                        else:
                            keyboard4.add_callback_button(thursday_para[5], VkKeyboardColor.NEGATIVE, payload=str(5 + 400))
                        keyboard4.add_line()
                        keyboard4.add_callback_button('Назад', VkKeyboardColor.PRIMARY, payload='16')
                        last_id = vk.messages.edit(
                            peer_id=messagelist[0].obj.peer_id,
                            message='Четверг',
                            conversation_message_id=messagelist[0].obj.conversation_message_id,
                            keyboard=(keyboard4).get_keyboard())


                    #Пары пятница
                    if (messagelist[0].object.payload == 501 or messagelist[0].object.payload == 502 or messagelist[0].object.payload == 503
                        or messagelist[0].object.payload == 504 or messagelist[0].object.payload == 505):
                        word = str(messagelist[0].object.payload)[2]
                        if add_or_not == 1:
                            add_par(para_fri, word)
                        elif add_or_not == 0:
                            otmena_par(para_fri, word)
                        keyboard5 = VkKeyboard(inline=True)
                        for i in range(1, 5):
                            if para_fri[i] == 1:
                                keyboard5.add_callback_button(friday_para[i], VkKeyboardColor.POSITIVE, payload=str(i + 500))
                            else:
                                keyboard5.add_callback_button(friday_para[i], VkKeyboardColor.NEGATIVE, payload=str(i + 500))
                            keyboard5.add_line()
                        if para_fri[5] == 1:
                            keyboard5.add_callback_button(friday_para[5], VkKeyboardColor.POSITIVE, payload=str(5 + 500))
                        else:
                            keyboard5.add_callback_button(friday_para[5], VkKeyboardColor.NEGATIVE, payload=str(5 + 500))
                        keyboard5.add_line()
                        keyboard5.add_callback_button('Назад', VkKeyboardColor.PRIMARY, payload='16')
                        last_id = vk.messages.edit(
                            peer_id=messagelist[0].obj.peer_id,
                            message='Пятница',
                            conversation_message_id=messagelist[0].obj.conversation_message_id,
                            keyboard=(keyboard5).get_keyboard())

                    #Пары Суббота
                    if (messagelist[0].object.payload == 601 or messagelist[0].object.payload == 602 or messagelist[0].object.payload == 603
                        or messagelist[0].object.payload == 604 or messagelist[0].object.payload == 605):
                        word = str(messagelist[0].object.payload)[2]
                        if add_or_not == 1:
                            add_par(para_sat, word)
                        elif add_or_not == 0:
                            otmena_par(para_sat, word)
                        keyboard6 = VkKeyboard(inline=True)
                        for i in range(1, 5):
                            if para_sat[i] == 1:
                                keyboard6.add_callback_button(saturday_para[i], VkKeyboardColor.POSITIVE, payload=str(i + 600))
                            else:
                                keyboard6.add_callback_button(saturday_para[i], VkKeyboardColor.NEGATIVE, payload=str(i + 600))
                            keyboard6.add_line()
                        if para_sat[5] == 1:
                            keyboard6.add_callback_button(saturday_para[5], VkKeyboardColor.POSITIVE, payload=str(5 + 600))
                        else:
                            keyboard6.add_callback_button(saturday_para[5], VkKeyboardColor.NEGATIVE, payload=str(5 + 600))
                        keyboard6.add_line()
                        keyboard6.add_callback_button('Назад', VkKeyboardColor.PRIMARY, payload='16')
                        last_id = vk.messages.edit(
                            peer_id=messagelist[0].obj.peer_id,
                            message='Суббота',
                            conversation_message_id=messagelist[0].obj.conversation_message_id,
                            keyboard=(keyboard6).get_keyboard())

                    r = vk.messages.sendMessageEventAnswer(
                        event_id=messagelist[0].object.event_id,
                        user_id=messagelist[0].object.user_id,
                        peer_id=messagelist[0].object.peer_id,
                        event_data=json.dumps(messagelist[0].object.payload))

    except Exception as lol:
        sender(2, 'Ошибка: ' + str(lol) + '\nВремя: ' + time1)
        continue