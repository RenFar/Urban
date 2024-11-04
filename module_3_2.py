
def send_email(message, recipient, *, sender = "university.help@gmail.com"):
    recip = str(recipient)
    send = str(sender)

    dog ='@'
    com = '.com'
    ru = '.ru'
    net = '.net'
    check_dog_rec = recip.find(dog)
    check_dog_sen = send.find(dog)
    check_com_rec = recip.find(com)
    check_com_sen = send.find(com)
    check_ru_rec = recip.find(ru)
    check_ru_sen = send.find(ru)
    check_net_rec = recip.find(net)
    check_net_sen = send.find(net)
    check_dog = True
    check_rec = True
    check_sen = True
    if check_dog_sen == -1 or check_dog_rec == -1:
        check_dog = False
    elif check_com_rec == -1 and check_ru_rec == -1 and check_net_rec == -1:
        check_rec = False
    elif check_com_sen == -1 and check_ru_sen == -1  and check_net_rec == -1 and check_net_sen == -1:
        check_sen = False
        if check_dog == False or check_rec == False or check_sen == False:
            print(f"Невозможно отправить письмо с адреса -  {sender} на адрес - {recipient}")
        else:
            print()
    else:
        if recip == send:
            print('Нельзя отправить письмо самому себе!')
        elif send == "university.help@gmail.com":
            print(f"Письмо успешно отправлено с адреса  -  {send} на адрес - {recip}")
        else:
            print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса  -  {send} на адрес - {recip}")


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')

send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')

send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')

send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')





