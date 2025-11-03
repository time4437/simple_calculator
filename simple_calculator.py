print("Выберите язык/Change language:", "1 - Русский", "2 - English", sep = "\n")
language = input()

if language == "1":
    print("\n")
    print("Язык установлен!")
    print("\n")
    print("Выберите тип калькулятора:", "1 - простой, арифметический", "2 - геометрический", sep="\n")
    type_of_calculator = input()
    print("\n")
    if type_of_calculator == "1":
        number1 = int(input("Введите первое число:"))
        print("\n")
        print("Введите арифметическое действие:", "1 - сложение", "2 - вычитание", "3 - умножение", "4 - деление", "5 - возведение в степень", sep = "\n")
        action = input()
        print("\n")
        number2 = int(input("Введите второе число:"))
        if action == "1":
            print("\n")
            print("Ответ:", number1 + number2)
            one = input()
        elif action == "2": 
            print("\n")
            print("Ответ:", number1 - number2)
            one = input()
        elif action == "3":
            print("\n")
            print("Ответ:", number1 * number2)
            one = input()
        elif action == "4":
            print("\n")
            print("Ответ:", number1 / number2)
            one = input()
        elif action == "5":
            print("\n")
            print("Ответ:", number1 ** number2)
            one = input()
    elif type_of_calculator == "2":
        print("Какой параметр фигуры вы хотите найти?", "1 - Периметр (P)", "2 - Площадь (S)", sep="\n")
        figure_parameter = input("")
        if figure_parameter == "1":
            print("Введите фигуру, периметр которой нужно найти.", "1 - квадрат", "2 - прямоугольник", "3 - треугольник", sep="\n")
            figure = input()
            if figure == "1":
                print("Введите длину одной стороны:")
                first_side = int(input())
                print("Ответ:", first_side * 4)
                one = input()
            elif figure == "2":
                print("Введите длинну первой стороны:")
                first_side = int(input())
                print("Введите длинну второй стороны:")
                second_side = int(input())
                print("Ответ:", 2 * (first_side + second_side))
                one = input()
            elif figure == "3":
                print("Введите длинну первой стороны:")
                first_side = int(input())
                print("Введите длинну второй стороны:")
                second_side = int(input())
                print("Введите длинну третьей стороны:")
                third_side = int(input())
                print("Ответ:", first_side + second_side + third_side)
                one = input()
        elif figure_parameter == "2":
            print("Введите фигуру, площадь которой нужно найти.", "1 - квадрат", "2 - прямоугольник", "3 - треугольник", sep="\n")
            figure = input()
            if figure == "1":
                print("Введите длину одной стороны:")
                first_side = int(input())
                print("Ответ:", first_side ** 2)
                one = input()
            elif figure == "2":
                print("Введите длинну первой стороны:")
                first_side = int(input())
                print("Введите длинну второй стороны:")
                second_side = int(input())
                print("Ответ:", first_side * second_side)
                one = input()
            #elif figure == "3"
elif language == "2":
    print("\n")
    print("Language installed!")
    print("\n")
    print("Select calculator type:", "1 - simple, arithmetic", "2 - geometric", sep="\n")
    type_of_calculator = input()
    print("\n")
    if type_of_calculator == "1":
        number1 = int(input("Enter the first number:"))
        print("\n")
        print("Enter the arithmetic operation:", "1 - addition", "2 - subtraction", "3 - multiplication", "4 - division", "5 - exponentiation", sep = "\n")
        action = input()
        print("\n")
        number2 = int(input("Enter the second number:"))
        if action == "1":
            print("\n")
            print("Answer:", number1 + number2)
            one = input()
        elif action == "2": 
            print("\n")
            print("Answer:", number1 - number2)
            one = input()
        elif action == "3":
            print("\n")
            print("Answer:", number1 * number2)
            one = input()
        elif action == "4":
            print("\n")
            print("Answer:", number1 / number2)
            one = input()
        elif action == "5":
            print("\n")
            print("Answer:", number1 ** number2)
            one = input()
    elif type_of_calculator == "2":
        print("What figure parameter do you want to find?", "1 - Perimeter (P)", "2 - Area of ​​the figure (S)", sep="\n")
        figure_parameter = input("")
        if figure_parameter == "1":
            print("Enter the shape whose perimeter you want to find.", "1 - square", "2 - rectangle", "3 - triangle", sep="\n")
            figure = input()
            if figure == "1":
                print("Enter the length of one side:")
                first_side = int(input())
                print("Answer:", first_side * 4)
                one = input()
            elif figure == "2":
                print("Enter the leight of the first side:")
                first_side = int(input())
                print("Enter the length of the second side:")
                second_side = int(input())
                print("Answer:", 2 * (first_side + second_side))
                one = input()
            elif figure == "3":
                print("Enter the leight of the first side:")
                first_side = int(input())
                print("Enter the leight of the second side:")
                second_side = int(input())
                print("Enter the length of the third side:")
                third_side = int(input())
                print("Answer:", first_side + second_side + third_side)
                one = input()
        elif figure_parameter == "2":
            print("Enter the shape whose area you want to find:", "1 - square", "2 - rectangle", "3 - triangle", sep="\n")
            figure = input()
            if figure == "1":
                print("Enter the length of one side:")
                first_side = int(input())
                print("Ответ:", first_side ** 2)
                one = input()
            elif figure == "2":
                print("Enter the leight of the first side:")
                first_side = int(input())
                print("Enter the leight of the second side:")
                second_side = int(input())
                print("Answer:", first_side * second_side)
                one = input()
            #elif figure == "3"
