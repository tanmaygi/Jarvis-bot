def greet(bot_name, birth_year):
    print('Hello! My name is ' + bot_name + '.')
    print('I was created in ' + birth_year + '.')


def remind_name():
    print('Please, remind me your name.')
    name = input()
    print('What a great name you have, ' + name + '!')


def guess_age():
    print('Let me guess your age.')
    print('Enter remainders of dividing your age by 3, 5 and 7.')

    rem3 = int(input())
    rem5 = int(input())
    rem7 = int(input())
    age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105

    print("Your age is " + str(age) + "; that's a good time to start programming!")


def count():
    print('Now I will prove to you that I can count to any number you want.')

    num = int(input())
    curr = 0
    while curr <= num:
        print(curr, '!')
        curr = curr + 1


def test():
    print("Let's test your programming knowledge.")
    # write your code here
    print("What do we use to define a block of code in Python language?")
    options = []
    option_1 = "1. Key"
    option_2 = "2. Brackets"
    option_3 = "3. Indentations"
    option_4 = "4. None"
    print("option_1")
    print("option_2")
    print("option_3")
    print("option_4")
    answer = input()
    if answer == "option_3":
        print("Completed, have a nice day!")
    else:
        print("Please, try again.")
    
    print('Completed, have a nice day!')


def end():
    print('Congratulations, have a nice day!')


greet('Aid', '2020')  # change it as you need
remind_name()
guess_age()
count()
test()
end()