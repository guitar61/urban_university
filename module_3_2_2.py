def send_email(message, recipient, sender="university.help@gmail.com"):
    if ("@" not in recipient or "@" not in sender or
            (".com" not in recipient and ".net" not in recipient and ".ru" not in recipient) or
            (".com" not in sender and ".net" not in sender and ".ru" not in sender)):
        print(f"It is impossible to send a letter from the address {sender} to the address {recipient} .")

    else:
        if sender == recipient:
            print("“ You can’t send a letter to yourself! ”")
        elif sender == "university.help@gmail.com":
            print(f"The letter was successfully sent from the address {sender} to the address {recipient} .")
        else:
            print(f"NON-STANDARD SENDER! The letter was sent from the address {sender} to the address {recipient} .")


send_email('This is a communication check message', 'vasyok1337@gmail.com')

send_email('You see this message as the best student of the course!', 'urban.fan@mail.ru',
           sender='urban.info@gmail.com')
send_email('Please correct the assignment', 'urban.student@mail.ru',
           sender='urban.teacher@mail.uk')
send_email('Reminding myself about the webinar', 'urban.teacher@mail.ru',
           sender='urban.teacher@mail.ru')
