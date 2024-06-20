def reverse(number): 
    reverse_num = "" 
    for num in str(number): 
        reverse_num = num + reverse_num 
    print(reverse_num)

number = input("Введите число: ") 
if number == number[::-1]: 
    print("Число является палиндромом") 
else: 
    print("Число не является палиндромом")

    n1 = int(input("Введите целое число: "))

digit = n1 % 10
n2 = digit


n1 = n1 // 10

while n1 > 0:
    
    digit = n1 % 10
    
    n1 = n1 // 10
    
    n2 = n2 * 10
    
    n2 = n2 + digit

print('"Обратное" ему число:', n2)