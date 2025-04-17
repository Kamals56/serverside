import sys
# This is mainly taken from https://discordpy.readthedocs.io/en/stable/quickstart.html
# To make the file watch for changes (the script is restarted each time you save the file),
# npm package nodemon can be used:
# 1: Install npm if you do not have it yet:
#    sudo apt update
#    sudo apt install npm
# 2. To install nodemon: sudo npm i -g nodemon
# 3: To run the file: nodemon --exec python3 bottemplate.py

discordToken = "" # Your bot token here (https://discord.com/developers/applications/ and tab Bot -> Token -> Reset Token -> Copy the token here)
name = "" # Your bot name here


if (discordToken == ""): sys.exit("ERROR: Please set the discord token.")
if (name == ""): sys.exit("ERROR: Please set the name of the bot.")

# To use this package, install: pip3 install discord.py
import discord
import random

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
dictionary = {}
todo_list = {}

@client.event
async def on_ready():
  print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
  if message.author == client.user: return # We don't want to reply to ourselves

  # RULE: To not flood the channel with responses from multiple bots,
  # we only respond to messages that start with our name

  if message.content.startswith(name):
    print(f"{message.author} says: {message.content}")

    msg =message.content[len(name):].strip()
    print(f"msg comtains: {msg}")

    functionality = msg.split(' ')
    # 1.1 set term
    if len(functionality) == 3 and functionality[0] == "set":
      key = functionality[1]
      value = " ".join(functionality[2:]) #got help from friend in this
      dictionary[key] = value
      print(f"{key}' is : {value}")
      await message.channel.send(f"{key} is: {value}")
    
    # 1.2 get term
    elif len(functionality) == 2 and functionality[0] == "get":
      key = functionality[1]
      if key in dictionary:
        print(f"The {key} is {dictionary[key]}")
        await message.channel.send(f"The {key} is {dictionary[key]}")
      else:
        print("I donot know this")
        await message.channel.send("I donot know this")
    # 1.3 remove term
    elif len(functionality) == 2 and functionality[0] == "set":
      key = functionality[1]
      if key in dictionary:
        del dictionary[key]
        print(f"Term {key} removed")
        await message.channel.send(f"Term {key} removed")
    # 2.1 todo adding
    elif functionality[0] == "todo" and len(functionality) > 1:
      if len(todo_list) < 5:
        todo_item = " ".join(functionality[1:])
        todo_list[len(todo_list)+ 1] = todo_item
        print(f"Added to-do item: {todo_item}")
        await message.channel.send(f"Added to-do item: {todo_item}")

    # 2.3 todo limiting
      else:
        print("Too many items")
        await message.channel.send("Too many items")

    # 2.2 todo listing
    elif functionality[0] == "todo":
      if len(todo_list) == 0:
        print("No todo items")
        await message.channel.send("No todo items.")
      else:
        todo_items = "\n".join([f"{key}: {value}" for key, value in todo_list.items()])
        print(f"Todo items:\n{todo_items}")
        await message.channel.send(f"Todo items:\n{todo_items}")

    # 2.4 todo removal
    elif functionality[0] == "todoremove" and len(functionality) == 2 and functionality[1].isdigit():
      item_number = int(functionality[1])
      if item_number in todo_list:
        removed_item = todo_list.pop(item_number)
        print(f"Removed to-do item: {removed_item}")
        await message.channel.send(f"Removed to-do item: {removed_item}")
      else:
        print("No item with this number")
        await message.channel.send("No item with this number")

    # 2.5 improved help
    elif functionality[0] == "help":
      help_message = (
          "Available commands:\n"
          "1. todo <item> : Adds a to-do item.\n"
          "2. todo Displays all to-do items.\n"
          "3. todoremove <number> : Removes a to-do item by number.\n"
          "4. random <minNumber> <maxNumber> : Generates a random number between min and max.\n"
          "5. random <minNumber> <maxNumber> <howMany> : Generates howMany random numbers.\n"
          "6. sum <number1> <number2> : Sums two numbers.\n"
          "7. set <term> <definition> : Sets a term with its definition.\n"
          "8. get <term>: Retrieves the definition of a term.\n"
          "9. remove <term>: Removes a term from the dictionary.\n"
            )
      print(help_message)
      await message.channel.send(help_message)


    else:
      print("Invalid command")
      await message.channel.send("Invalid command")


  #[] 1.1 random
    if len(functionality) == 3 and functionality[0] == "random":
      if functionality[1].isdigit() and functionality[2].isdigit():
        num1 = int(functionality[1])
        num2 = int(functionality[2])
        random_number = random.randint(num1, num2) #got help from chatgpt about this randint
        print(F"your random number is: {random_number}")
        await message.channel.send(F"Your random number is: {random_number}")
  #[] 2.6 error checking: random with no digit
      else:
        print("Exterminate! Only digits are allowed!")
        await message.channel.send("Exterminate! Only digits are allowed!")

  #[] 1.2 improved random
    elif len(functionality) == 4 and functionality[0] == "random":
      if functionality[1].isdigit() and functionality[2].isdigit() and functionality[3].isdigit():
        num1 = int(functionality[1])
        num2 = int(functionality[2])
        count = int(functionality[3])

        random_numbers = [random.randint(num1, num2) for _ in range(count)]
        #print(" & ".join(map(str, random_numbers)))
        result = ""
        for i in range(len(random_numbers)): #got help from you in class
          result += str(random_numbers[i]) + " & "
        print(F"Here are your random numbers: {result[:-3]}")
        await message.channel.send(F"Here are your random numbers: {result[:-3]}")

  #[] 2.6 error checking: random with no digit
      else:
        print("Exterminate! Only digits are allowed!")
        await message.channel.send("Exterminate! Only digits are allowed!")    

  #[] 2.1 error checking: too many parameters with random
    elif functionality[0] == "random"and len(functionality) >4:
      print("Exterminate! Too many parameters!")
      await message.channel.send("Exterminate! Too many parameters!")

  #[] 2.2 error checking: too few parameters with random
    elif functionality[0] == "random"and len(functionality) <3:
      print("Exterminate! Too few parameters!")
      await message.channel.send("Exterminate! Too few parameters!")  

  #[] 1.3 sum
    elif len(functionality) == 3 and functionality[0] == "sum":
      if functionality[1].isdigit() and functionality[2].isdigit():
        num1 = int(functionality[1])
        num2 = int(functionality[2])
        result = num1 + num2
        print(result)
        await message.channel.send(F"The sum is: {result}")

  #[] 2.5 error checking: sum with no digit
      else:
        print("Exterminate! Only digits are allowed!")
        await message.channel.send("Exterminate! Only digits are allowed!")

  #[] 2.3 error checking: too many parameters with sum
    elif functionality[0] == "sum" and len(functionality) > 3:
      print("Exterminate! Too many parameters!")
      await message.channel.send("Exterminate! Too many parameters!")

  #[] 2.4 error checking: too few parameters with sum
    elif functionality[0] == "sum" and len(functionality) < 3:
     print("Exterminate! Too few parameters!")
     await message.channel.send("Exterminate! Too few parameters!")

  #[] 1.4 help
    elif functionality[0] == "help1":
      help = ("When asking chatbot random <minNumber> <maxNumber>, it gives a random number between the two numbers. So, for example, random 0 20 should give a random number between 0 and 20.\nA third parameter can also be passed to it, which defines how many random numbers it generates. So the syntax should be like random <minNumber> <maxNumber> <howMany>. So, for example, random 0 20 2 gives back 2 random numbers. The output should be something like this: Random numbers 13 & 4. \nTo sum two numbers you can do sum <number1> <number2> it should sum up the numbers. So, for example, sum 160 20  should return back 180. ")
      print(help)
      await message.channel.send(help)


    if message.content.startswith(f'{name} hello'):
      await message.channel.send('Hello! I am ALIVE?')

client.run(discordToken)