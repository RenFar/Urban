
def send_email(message, recipient, *, sender = "university.help@gmail.com"):
    recip = str(recipient)
    send = str(sender)

    check_dog_rec = recip.find("@")
    check_dog_sen = send.find("@")
    check_com_rec = recip.endswith('.com')
    check_com_sen = send.endswith('.com')
    check_ru_rec = recip.endswith('.ru')
    check_ru_sen = send.endswith('.ru')
    check_net_rec = recip.endswith('.net')
    check_net_sen = send.endswith('.net')

    if check_dog_sen == -1 or check_dog_rec == -1:
        print(f"Невозможно отправить письмо с адреса -  {sender} на адрес - {recipient}")
    elif check_com_rec == 0 and check_ru_rec == 0 and check_net_rec == 0:
        print(f"Невозможно отправить письмо с адреса -  {sender} на адрес - {recipient}")
    elif check_com_sen == 0 and check_ru_sen == 0  and check_net_rec == 0 and check_net_sen == 0:

        print(f"Невозможно отправить письмо с адреса -  {sender} на адрес - {recipient}")

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





