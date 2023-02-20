# Requirements
### - lolcat (not 100% necessary)

Note: Development computer already had lolcat installed using apt package manager (ubuntu)
example: sudo apt install lolcat

alternatively, you can use the python version and install with pip
pip install lolcat
*haven't tested pip version (it's a port) - but assuming it works, it just might need some adjusting.  May not require OS module

### - openai

Note: Obviously if you want to connect we will need to install the openai module :)
example: pip install openai


---------------------------------------------------------------------
: how to install subprocess for python script
---------------------------------------------------------------------


Subprocess is a module in the Python Standard Library that allows you to spawn new processes, connect to their input/output/error pipes, and obtain their return codes.

To install subprocess, you can use pip:

pip install subprocess

Alternatively, you can install it from the source code:

git clone https://github.com/python/cpython.git

cd cpython/Lib/subprocess

python setup.py install

Once installed, you can import the module in your Python script and use it to spawn new processes. 
 

---------------------------------------------------------------------
: 




## Optional / Future

Note: Working on adding morgan freemans voice to Jarvis.  Was testing with alternative TTS scripts (just to get it working) but I didn't
like how I had to wait until Jarvis finished speaking before I could ask another question.  The longer the answer, the longer it would take.

Commented it out.  Perhaps there is a way to break out and continue.  Like a 'shutup' command. :)
