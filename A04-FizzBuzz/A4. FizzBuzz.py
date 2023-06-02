n1 = int(input("Número inicial do intervalo: "))
n2 = int(input("Número final do intervalo: "))

if n2 <= n1:
    print("O número final deve ser maior que o número inicial.")
else:
    for num in range(n1, n2 + 1):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)