import os
import openai
import json
from subprocess import run

# On the following line, enter your API key (between the "")
openai.api_key = ""

header = '''
     _                  _          _    ___
    | | __ _ _ ____   _(_)___     / \  |_ _|
 _  | |/ _` | '__\ \ / / / __|   / _ \  | |
| |_| | (_| | |   \ V /| \__ \  / ___ \ | |
 \___/ \__,_|_|    \_/ |_|___/ /_/   \_\___|

Initial Release Date: 12/11/2022
API: openai ChatGPT(davinci gpt 3)
Current Version: 0.3.7
Updated: 2023-02-20-13-12-34
Author: Paul Johnston
Description: Provides ChatGPT functionality in the terminal when needed.
(Feels like a co-pilot.)

to exit, type 'quit' or 'q' and hit enter

'''

run(["lolcat"], input=header, text=True)

def RE():
   divider = '---------------------------------------------------------------------'
   USERREQUEST = input(": ")
   if (USERREQUEST =="q" or USERREQUEST =="quit" or USERREQUEST == "exit"):
        quit()

   if USERREQUEST == "":
       print("")
   else:
        response = openai.Completion.create(model="text-davinci-003", prompt=USERREQUEST, temperature=0, max_tokens=2000)
        run(["lolcat"], input=divider, text=True)
        output = response["choices"][0]["text"]
        print(output+" \n \n")
        run(["lolcat"], input=divider, text=True)

infinitelooper = 0

while infinitelooper == 0:
	RE()
