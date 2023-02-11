#import os
import openai
#import json
from subprocess import run
#import pyttsx3  #python text to speach - consider upgrading to google tts (requires internet)  this one can run offline (but the openai wont work)

#define globals
#engine = pyttsx3.init()

# Enter your API Key
api_key = ""

header = '''
   _                  _             _ 
  (_) __ _ _ ____   _(_)___    __ _(_)
  | |/ _` | '__\ \ / / / __|  / _` | |
  | | (_| | |   \ V /| \__ \ | (_| | |
 _/ |\__,_|_|    \_/ |_|___/  \__,_|_|
|__/                                  

Initial Date: December 11, 2022
Last Updated: Feb 11, 2023
Version: 0.0.7
Author: Paul Johnston
Github: https://github.com/nocturnalguru/jarvis
Description: A terminal co-pilot powered by openai (davinci).
Simply add your API key and away you go.
For those who work in the terminal and just need an easy way to ask their questions without constantly being asked to login.

To exit type 'q' or 'quit' or 'exit'

'''

run(["lolcat"], input=header, text=True)


def RE():
    #define a few vars
    divider = '---------------------------------------------------------------------'
    #take in the input
    USERREQUEST = input(": ")
    if (USERREQUEST =="q" or USERREQUEST =="quit" or USERREQUEST == "exit"):
        quit()
    response = openai.Completion.create(model="text-davinci-003", prompt=USERREQUEST, temperature=0, max_tokens=2000)
    run(["lolcat"], input=divider, text=True)
    output = response["choices"][0]["text"]
    print(output+" \n \n")
    run(["lolcat"], input=divider, text=True)
    #voice  output - uncomment 2 lines below - note,  you need to wait till the speaking is complete to enter another command.
    #engine.say(output)
    #engine.runAndWait()


infinitelooper = 0

while infinitelooper == 0:
	RE()
