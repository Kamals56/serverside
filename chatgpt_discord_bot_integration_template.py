import os
from dotenv import load_dotenv
load_dotenv()
import sys
# This is mainly taken from https://discordpy.readthedocs.io/en/stable/quickstart.html
# To make the file watch for changes (the script is restarted each time you save the file),
# npm package nodemon can be used:
# 1: Install npm if you do not have it yet:
#    sudo apt update
#    sudo apt install npm
# 2. To install nodemon: sudo npm i -g nodemon
# 3: To run the file: nodemon --exec python3 bottemplate.py

# Your bot token here (https://discord.com/developers/applications/ and tab Bot -> Token -> Reset Token -> Copy the token here)

discord_token = os.getenv("discord_token")
# Your bot name here
name = "csm101_kamal_lamichhane"
# OpenAI API key here
openai_key = os.getenv("OPENAI_API_KEY") 

if (discord_token == ""): sys.exit("ERROR: Please set the discord token.")
if (name == ""): sys.exit("ERROR: Please set the name of the bot.")
if (openai_key == ""): sys.exit("ERROR: Please set the openai key.")

# To use this package, install: pip3 install discord.py
import discord
import requests
import json

###
# ASSIGNMENT 1 BEGINS
###

class ChatGPT():
  def __init__(self, key):
    self.key = key
    self.headers = {
      "Authorization": "Bearer " + key,
      "Content-Type": "application/json"
    }
  
  def generate_chat_response(self, prompt):
    try:
      print(f"Generating chat response for: {prompt}")

      # Endpoint URL, found from the ChatGPT API documentation: https://platform.openai.com/docs/api-reference/chat
      url = "https://api.openai.com/v1/chat/completions"

      # JSON data for the request
      data = {
        "messages": [
          {
            "role": "user",
            "content": prompt
          }
        ],
        "max_tokens": 200,
        "temperature": 1,
        "model": "gpt-4o"
      }

      # Call the endpoint and return the response (chat response)
      response = requests.post(url, headers=self.headers, data=json.dumps(data))
      r_json = response.json()
      return r_json["choices"][0]["message"]["content"]
    except Exception as e:
      print("\n!!!!! ERROR IN CHAT RESPONSE !!!!!")
      print(e)
      try: print(r_json)
      except: pass
      return None
  
  def generate_image_url(self, prompt):
    try:
      print(f"Generating image url for: {prompt}")
      
      # TODO: Find the endpoint url from the ChatGPT API Documentation for image generation and set it here
      url = "https://api.openai.com/v1/images/generations"

      # TODO: Set the JSON data for the request here, you could use most of the keys and values provided in the API example
      # TODO: Set "size" to "256x256" and "quality" to "standard" to not spend the whole budget ;)
      # TODO: Set the key "prompt" to pass the variable prompt as the value
      data = {
        "model": "dall-e-3",
        "prompt": prompt,
        "n": 1,
        "size": '1024x1024',
        "quality": "standard"
      }

      # Call the endpoint and return the response (image URL)
      response = requests.post(url, headers=self.headers, data=json.dumps(data))
      r_json = response.json()
      return r_json["data"][0]["url"]
    except Exception as e:
      print("\n!!!!! ERROR IN IMAGE GENERATION !!!!!")
      print(e)
      try: print(r_json)
      except: pass
      return None
  
  def generate_audio_file(self, prompt):
    try:
      print(f"Generating audio file (text to speech) for: {prompt}")
      
      # TODO: Find the endpoint url from the ChatGPT API Documentation for audio generation (create speech) and set it here
      url = "https://api.openai.com/v1/audio/speech"

      # TODO: Set the JSON data for the request here, you could use the keys and values provided in the API example
      # TODO: Set the key "input" to pass the variable prompt as the value
      data = {
        "model": "tts-1",
        "input": prompt,
        "voice": "alloy",
        "speed": 2
      }

      # Call the endpoint and store the resulting file as output.mp3
      # Return the path to the stored file (output.mp3)
      response = requests.post(url, headers=self.headers, json=data)
      response.raise_for_status()
      output_file_path = "output.mp3"
      with open(output_file_path, 'wb') as f:
        f.write(response.content)
      return output_file_path
    except Exception as e:
      print("\n!!!!! ERROR IN AUDIO GENERATION !!!!!")
      print(e)
      try: print(response)
      except: pass
      return None

# These demonstrate how to use the chat generation, image url generation, and audio file generation functions of the ChatGPT class
# TODO: Make sure that the functions here work first before proceeding to assignment 2, as these functions are used in assignment 2
gpt = ChatGPT(openai_key)
# Comment out the lines below once the functions above all work
""""
chat_response = gpt.generate_chat_response("Hello")
print(f"Chat response: {chat_response}\n")
image_url = gpt.generate_image_url("Classroom with 3 teachers")
print(f"Image url: {image_url}\n")
audio_file = gpt.generate_audio_file("Classroom with 3 teachers")
print(f"Audio url: {audio_file}\n")
"""
# Comment out till this line

###
# / ASSIGNMENT 1 ENDS
###

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

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

    ###
    # ASSIGNMENT 2 BEGINS
    ###

    #######
    # CHAT
    # 
    # For example: "your_bot_name ask How to create a loop in Python?"
    if message.content.startswith(f'{name} ask'):
      # TODO: Replace (remove) "botname ask " from message.content
      # we will have:
      # message.content = " csm

      prompt = message.content.replace(name + " ask ", "")
      print("Ask:")
      print("prompt")

      # TODO: Call the function gpt.generate_chat_response(prompt) to generate the text response and save the returned response in a variable
      response = gpt.generate_chat_response(prompt)
      # TODO: Send the message to the channel, example code commented out below
      await message.channel.send(response)
      return

    #######
    # IMAGE GENERATION
    # 
    # For example: "your_bot_name image Student coding server-side programming exercises"
    if message.content.startswith(f'{name} image'):
      # TODO: Replace (remove) "botname image " from message.content
      prompt = message.content.replace(name + " ask ", "")

      # TODO: Call the function gpt.generate_image_url(prompt) to generate the image and save the returned image url in a variable
      url = gpt.generate_image_url(prompt)
      # TODO: Embed the image in Discord message and submit it to the channel

      # Example embed code below commented out
      embed = discord.Embed(title = "Generated image for prompt " + prompt, url=url)
      embed.set_thumbnail(url=url)
      await message.channel.send(embed=embed)
      return
    
    #######
    # AUDIO TRANSCRIPTION
    # 
    # For example: "your_bot_name audio Not very long sentence."
    if message.content.startswith(f'{name} audio'):
      # TODO: Replace (remove) "botname audio " from message.content
      prompt = message.content.replace(name + " audio ", "")

      # TODO: Call the function gpt.generate_audio_file(prompt) to generate the image file and save the returned file path in a variable

      # TODO: Send the audio file to the channel
      # Example code below commented out
      file_path = gpt.generate_audio_file(prompt)
      await message.channel.send(prompt, file=discord.File(file_path))
      return

    ###
    # / ASSIGNMENT 2 ENDS
    ###

client.run(discord_token)