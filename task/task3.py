def money_max(money, procent, years):
    drop = money * (1 + (procent * 100) / 100) ** years
    print("Общая сумма: ", drop)

money = (input("Введите сумму денег: "))
procent = float(input("Введите процент: "))
years = int(input("Введите количество лет: "))

money_max(money, procent, years)

