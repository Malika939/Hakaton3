import datetime

class LogUp:
    def main(self):
        log = input("Введите логин : ")
        pass1 = input("Введите пароль : ")
        pass2 = input("Повторите пароль : ")
        n = int()
        n = len(log)
        past_date = datetime.datetime.today() - datetime.timedelta(days=14)
        if n < 5:
            while (True):
                if n < 5:
                    print ("Ваш логин слишшком короткий, введите лог длиной больше 5и : ")
                    log = input("Повторите попытку : ")
                    n = len(log)
                else:
                    break
        while (True):
            n = len(pass1)
            if n < 8:
                pass1 = input ("Ваш пароль слишшком простой, введите пароль длиной больше 8и : ")
            else:
                if pass1 != pass2:
                    pass2 = input ("Пароли не совпадают, повторите попытку : ")
                else:
                    open_file = open (f'/home/timurchik/Документы/log.txt', 'w')
                    open_file.write(f'Login : {log} \n Password : {pass2}')
                    print (f'Пользователь успешно регистрирован в {past_date}!')
                    break


myClass = LogUp()
myClass.main()