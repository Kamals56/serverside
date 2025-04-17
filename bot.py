import random
command = "sum 50 50 60".lower()
functionality = command.split(' ')



if len(functionality) == 3 and functionality[0] == "random" and functionality[1].isdigit() and functionality[2].isdigit():
    num1 = int(functionality[1])
    num2 = int(functionality[2])
    random_number = random.randint(num1, num2)
    print(random_number)

elif len(functionality) == 4 and functionality[0] == "random" and functionality[1].isdigit() and functionality[2].isdigit() and functionality[3].isdigit():
    num1 = int(functionality[1])
    num2 = int(functionality[2])
    count = int(functionality[3])

    random_numbers = [random.randint(num1, num2) for _ in range(count)]
    #print(" & ".join(map(str, random_numbers)))
    result = ""
    for i in range(len(random_numbers)):
        result += str(random_numbers[i]) + " & "
    print(result[:-3])

elif functionality[0] == "random"and len(functionality>4):
    print("Exterminate! Too many parameters!")

elif functionality[0] == "random"and len(functionality <3 ):
    print("Exterminate! Too few parameters!")

if len(functionality) == 3 and functionality[0] == "sum":
    if functionality[1].isdigit() and functionality[2].isdigit():
        num1 = int(functionality[1])
        num2 = int(functionality[2])
        result = num1 + num2
        print(result)
        
    else:
        print("Exterminate! Only digits are allowed!")
elif functionality[0] == "sum" and len(functionality) > 3:
    print("Exterminate! Too many parameters!")
elif functionality[0] == "sum" and len(functionality) < 3:
    print("Exterminate! Too few parameters!")


if functionality[0] == "help":
    help = ("When asking chatbot random <minNumber> <maxNumber>, it gives a random number between the two numbers. So, for example, random 0 20 should give a random number between 0 and 20.\nA third parameter can also be passed to it, which defines how many random numbers it generates. So the syntax should be like random <minNumber> <maxNumber> <howMany>. So, for example, random 0 20 2 gives back 2 random numbers. The output should be something like this: Random numbers 13 & 4. \nTo sum two numbers you can do sum <number1> <number2> it should sum up the numbers. So, for example, sum 160 20  should return back 180. ")
    print(help)
