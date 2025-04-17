
dictionary = {}
def chat(command):
    command = "set name kamal".lower()
    parts = command.split(' ')

    action, key, value = parts
    if len(parts) != 3:
        return "invalid command"

    if len(parts) == 3 and parts[1] == "set":
        dictionary[key] = value
        return f"{key}: {value} saved to dictionary"
    print(dictionary)

    todo_dict = {}  # Global dictionary for terms and definitions
todo_items = {}  # Global dictionary for todo items

@client.event
async def on_message(message):
    global todo_dict, todo_items  # Import the global dictionaries

    # Set term with definition
    if message.content.startswith("csm_101_aleksi set"):
        parts = message.content.split(" ", 3)
        if len(parts) == 4:
            term, definition = parts[2], parts[3]
            todo_dict[term] = definition
            await message.channel.send(f"Term '{term}' set.")
        elif len(parts) == 2:
            term = parts[1]
            if term in todo_dict:
                del todo_dict[term]
                await message.channel.send(f"Term '{term}' removed.")
            else:
                await message.channel.send("Term not found.")
        else:
            await message.channel.send("Invalid format. Use 'set <term> <definition>'")

    # Get term definition
    elif message.content.startswith("csm_101_aleksi get"):
        term = message.content.split(" ", 2)[2]
        if term in todo_dict:
            await message.channel.send(todo_dict[term])
        else:
            await message.channel.send("I do not know this")

    # Add todo item
    elif message.content.startswith("csm_101_aleksi todo"):
        todo_item = message.content[15:]  # Extract the todo item
        if len(todo_items) >= 5:
            await message.channel.send("Too many items!")
        else:
            todo_items[len(todo_items) + 1] = todo_item
            await message.channel.send(f"Added todo: {todo_item}")

    # Show all todo items
    elif message.content == "csm_101_aleksi todo":
        if todo_items:
            todo_list = "\n".join([f"{key}: {value}" for key, value in todo_items.items()])
            await message.channel.send(f"Todo list:\n{todo_list}")
        else:
            await message.channel.send("No todo items.")

    # Remove todo item
    elif message.content.startswith("csm_101_aleksi todoremove"):
        parts = message.content.split(" ", 2)
        if len(parts) == 2 and parts[1].isdigit():
            item_number = int(parts[1])
            if item_number in todo_items:
                del todo_items[item_number]
                await message.channel.send(f"Todo item {item_number} removed.")
            else:
                await message.channel.send("No item with this number")
        else:
            await message.channel.send("Invalid number.")

    # Help command
    elif message.content == "csm_101_aleksi help":
        help_text = """
        Commands:
        - set <term> <definition>: Set a term with a definition.
        - get <term>: Get the definition of a term.
        - set <term>: Remove a term.
        - todo <todo item>: Add a todo item.
        - todo: View all todo items.
        - todoremove <number>: Remove a todo item by its number.
        """
        await message.channel.send(help_text)
""""