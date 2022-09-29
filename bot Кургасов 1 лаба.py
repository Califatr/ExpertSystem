from email import message
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id
from vk_api.keyboard import VkKeyboard, VkKeyboardColor


# API-ключ созданный ранее
token = "vk1.a.OJ-bsPDyzp9lnVkYECDDoH5WUuQkg1Zg4ct6_VFFTjN8JQWLb1DcWj_LQzUUQUj57MKIxPL7pV0TyOUSexaQACauiCT56A6jWUkul3LH_i0NbiDyeB-zF7vSrNAODmMC4DablMwN4Cnyzb6tjjFL1e1vv3FQFjhsulc3Cq3QkvIAy8eJgBUTph0cjKu5vvWt"

# Авторизуемся как сообщество
vk_session = vk_api.VkApi(token=token)
vk = vk_session.get_api()
def send_message(user_id, message, keyboard=None):
    post = {
        "user_id":user_id,
        "message":message,
        "random_id":0
    }
    if keyboard !=None:
        post["keyboard"] = keyboard.get_keyboard()
    else:
        post = post
    vk_session.method("messages.send", post)
# Работа с сообщениями
longpoll = VkLongPoll(vk_session)
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
    #Слушаем longpoll, если пришло сообщение то:
        user_id = event.user_id
        if event.text == 'Начать': #Если написали заданную фразу
            if event.from_user: #Если написали в ЛС
                keyboard = VkKeyboard(one_time=True)
                keyboard.add_button("Для работы")
                keyboard.add_line()
                keyboard.add_button("Для повседневных поездок")  
                keyboard.add_line()
                keyboard.add_button("Для отдыха и хобби")
                send_message(user_id, "Выберете предназначение автомобиля", keyboard)
        if event.text == 'Для работы': #Если написали заданную фразу
            keyboard = VkKeyboard(one_time=True)
            keyboard.add_button("Коммерческие перевозки")
            keyboard.add_line()
            keyboard.add_button("Личное пользование")
            send_message(user_id, "Выберете тип использования", keyboard)
        if event.text == 'Личное пользование': #Если написали заданную фразу
            keyboard = VkKeyboard(one_time=True)
            keyboard.add_button("Скорость доставки")
            keyboard.add_line()
            keyboard.add_button("Высокая проходимость")  
            send_message(user_id, "Выберете сильную сторону", keyboard)
        if event.text == 'Скорость доставки': 
            send_message(user_id, "Вам подходит Lada Largus")
        if event.text == 'Высокая проходимость': 
            keyboard = VkKeyboard(one_time=True)
            keyboard.add_button("Высокая проходимость - ДА")
            keyboard.add_line()
            keyboard.add_button("Высокая проходимость - НЕТ")
            send_message(user_id, "Выберете тип использования", keyboard) 
        if event.text == 'Высокая проходимость - НЕТ"': 
            send_message(user_id, "Вам подходит Volkswagen Transporter")
        if event.text == 'Высокая проходимость - ДА"': 
            send_message(user_id, "Вам подходит УАЗ Профи")
        if event.text == 'Коммерческие перевозки': #Если написали заданную фразу
            keyboard = VkKeyboard(one_time=True)
            keyboard.add_button("Перевозка пассажиров - ДА")
            keyboard.add_line()
            keyboard.add_button("Перевозка пассажиров - НЕТ")
            send_message(user_id, "Используется для перевозки пассажиров?", keyboard)
        if event.text == 'Перевозка пассажиров - НЕТ': #Если написали заданную фразу
            keyboard = VkKeyboard(one_time=True)
            keyboard.add_button("Крытый кузов - ДА")
            keyboard.add_line()
            keyboard.add_button("Крытый кузов - НЕТ")
            send_message(user_id, "Необходим крытый кузов?", keyboard) 
        if event.text == 'Крытый кузов - ДА': 
            send_message(user_id, "Вам подходит Ford Transit")
        if event.text == 'Крытый кузов - НЕТ"': 
            send_message(user_id, "Вам подходит Газель бортовая") 
        if event.text == 'Перевозка пассажиров - ДА': #Если написали заданную фразу
            keyboard = VkKeyboard(one_time=True)
            keyboard.add_button("Тип перевозки - Городские")
            keyboard.add_line()
            keyboard.add_button("Тип перевозки - Межгород")
            keyboard.add_line()
            keyboard.add_button("Тип перевозки - Смешанные")
            send_message(user_id, "Выберете тип перевозки", keyboard)
        if event.text == 'Тип перевозки - Городские': 
            send_message(user_id, "Вам подходит ПАЗ 3204")
            send_message(user_id, "Вам подходит BAW street")
        if event.text == 'Тип перевозки - Межгород': 
            send_message(user_id, "Вам подходит Mercedes-Benz Sprinter") 
            send_message(user_id, "Вам подходит Hyundai Universe")
        if event.text == 'Тип перевозки - Смешанные': 
            send_message(user_id, "Вам подходит IVECO Daily")
            send_message(user_id, "Вам подходит Marcopolo Bravis") 