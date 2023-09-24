x = int(input("Введите произвольное число: "))
y = int(input("Введите пограничное число: "))
if x < y:
    print(f"{x} < {y}")
elif x > y:
    print(f"{x} > {y}")
    if x > y * 3:
        print(f"{x} > {y} более чем в 3 раза")
