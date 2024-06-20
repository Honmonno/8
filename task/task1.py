import random 


s = ["Дмитрий", "Моска", "Хорошо", "Александр", "Алексей", "Англия", "Кот", "Собака","", "Врач", "Токио", "Елена", "Лондон", "Рысь", 
     "Волейбол", "Писать", "Париж", "Максим", "Нью-Йорк", "Лошадь", "Катание на велосипеде", "Читать", "Берлин", "Евгений", "Барселона", 
     "Волк", "Пение", "Покой", "Рим", "Данил", "Сан-Франциско", "Зебра", "Фотография", "Инженер", "Ирина", "Чикаго", "Попугай", "Блондинка", "Гитара", "Пилот", "Мадрид"
    ]

def catch_ball():
    if random.random() <= 0.3:
        return True
    else:
        return False
    
def quest1():
    global quest1
    if catch_ball():
        print("Копьютер бросает мяч: Вы поймали!")
        quest1 = input("Вопрос: Ваше имя? ")
        print("Ответ: ", quest1)
        print(" ")
    else:
        print("Копьютер бросает мяч: Вы не поймали!")
        quest1 = random.choice(s)
        print("Ваше имя?")
        print("Ответ: ", quest1)
        print(" ")
def quest2():
    global quest2
    if catch_ball():
        print("Вы бросаете мяч: Вы поймяли!")
        print("Вопрос: Где вы живете?")
        quest2 = random.choice(s)
        print("Ответ: ", quest2)
        print(" ")
    else:
        print("Вы бросаете мяч: Вы не поймали!")
        quest2 = input("Где вы живете?: ")
        print("Ответ: ", quest2)
        print(" ")
def quest3():
    global quest3
    if catch_ball():
        print("Копьютер бросает мяч: Компьтер поймал!")
        quest3 = input("Вопрос: Как дела компьютера? ")
        print("Ответ: ", quest3)
        print(" ")
    else:
        print("Копьютер бросает мяч: Компьютер не поймал!")
        quest3 = random.choice(s)
        print("Как ваши дела?")
        print("Ответ: ", quest3)
        print(" ")
def quest4():
    global quest4
    if catch_ball():
        print("Вы бросаете мяч: Компьютер поймал!")
        print("Вопрос: Где находится компьютер?")
        quest4 = random.choice(s)
        print("Ответ: ", quest4)
        print(" ")
    else:
        print("Вы бросаете мяч: Компьютер не поймал!")
        quest4 = input("Где находится компьютер?: ")
        print("Ответ: ", quest4)
        print(" ")
def quest5():
    global quest5
    if catch_ball():
        print("Копьютер бросает мяч: Вы поймали!")
        quest5 = input("Вопрос: Какое ваше любимое животное? ")
        print("Ответ: ", quest5)
        print(" ")
    else:
        print("Копьютер бросает мяч: Вы не поймали!")
        quest5 = random.choice(s)
        print("Какое ваше любимое животное?")
        print("Ответ: ", quest5)
        print(" ")
def quest6():
    global quest6
    if catch_ball():
        print("Вы бросаете мяч: Компьютер поймал!")
        print("Вопрос: Какое любимое животное компьютера?")
        quest6 = random.choice(s)
        print("Ответ: ", quest6)
        print(" ")
    else:
        print("Вы бросаете мяч: Компьютер не поймал!")
        quest6 = input("Какое любимое животное компьютера?: ")
        print("Ответ: ", quest6)
        print(" ")
def quest7():
    global quest7
    if catch_ball():
        print("Копьютер бросает мяч: Вы поймали!")
        quest7 = input("Вопрос: Ваше увлечение ")
        print("Ответ: ", quest7)
        print(" ")
    else:
        print("Копьютер бросает мяч: Вы не поймали!")
        quest7 = random.choice(s)
        print("Ваше увлечение?")
        print("Ответ: ", quest7)
        print(" ")
def quest8():
    global quest8
    if catch_ball():
        print("Вы бросаете мяч: Компьютер поймал!")
        print("Вопрос: Увлечение компьютера?")
        quest8 = random.choice(s)
        print("Ответ: ", quest8)
        print(" ")
    else:
        print("Вы бросаете мяч: Компьютер не поймал!")
        quest8 = input("Увлечение компьютера?: ")
        print("Ответ: ", quest8)
        print(" ")


def quest9():
    global quest9
    if catch_ball():
        print("Копьютер бросает мяч: Вы поймали!")
        quest9 = input("Вопрос: Какова ваша мечта? ")
        print("Ответ: ", quest9)
        print(" ")
    else:
        print("Копьютер бросает мяч: Вы не поймали!")
        quest9 = random.choice(s)
        print("Какова ваша мечта?")
        print("Ответ: ", quest9)
        print(" ")
def quest10():
    global quest10
    if catch_ball():
        print("Вы бросаете мяч: Компьютер поймал!")
        print("Вопрос: Какова мечта компьютера?")
        quest10 = random.choice(s)
        print("Ответ: ", quest10)
        print(" ")
    else:
        print("Вы бросаете мяч: Компьютер не поймал!")
        quest10 = input("Какова мечта компьютера?: ")
        print("Ответ: ", quest10)
        print(" ")

def quest11():
    global quest11
    if catch_ball():
        print("Копьютер бросает мяч: Вы поймали!")
        quest11 = input("Вопрос: Куда вы хотели бы поехать? ")
        print("Ответ: ", quest11)
        print(" ")
    else:
        print("Копьютер бросает мяч: Вы не поймали!")
        quest11 = random.choice(s)
        print("Куда вы хотели бы поехать?")
        print("Ответ: ", quest11)
        print(" ")
def quest12():
    global quest12
    if catch_ball():
        print("Вы бросаете мяч: Компьютер поймал!")
        print("Вопрос: Где хотел побывать компьютер?")
        quest12 = random.choice(s)
        print("Ответ: ", quest12)
        print(" ")
    else:
        print("Вы бросаете мяч: Компьютер не поймал!")
        quest12 = input("Где хотел побывать компьютер?: ")
        print("Ответ: ", quest12)
        print(" ")


quest1()
quest2()
quest3()
quest4()
quest5()
quest6()
quest7()
quest8()
quest9()
quest10()
quest11()
quest12()

print("Рассказ человека: ")
print("Привет! Меня зовет", quest1, "я из города", quest3, ", мое любимое животное", quest5, ", мое хобби это", quest7, ", я по професси", quest9, ", я бы хотел побывать в", quest11)
print(" ")

print("Рассказ компьютера: ")
print("Привет! Меня зовет", quest2, "я из города", quest4, ", мое любимое животное", quest6, ", мое хобби это", quest8, ", я по професси ", quest10, "я бы хотел побывать в", quest12)