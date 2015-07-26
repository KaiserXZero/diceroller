#!/usr/bin/env python
import time
import Skype4Py
import random
import re


def commands(Message, Status):
	if Status == 'SENT' or (Status == 'RECEIVED'):

		if Message.Body == "//*":
			diceroll(Message)

		elif Message.Body == "!ping":
			cmd_ping(Message)

		elif Message.Body == "!rickroll":
			cmd_rickroll(Message)

		elif Message.Body == "!celebrate":
			cmd_celebrate(Message)

		elif Message.Body == "!hammertime":
			cmd_hammertime(Message)

		elif Message.Body == "!credit":
			cmd_credit(Message)

		elif Message.Body == "!help":
			cmd_help(Message)

		elif Message.Body == "!spam":
			cmd_spam(Message)

		elif Message.Body == "!introduce":
			cmd_intro(Message)

		elif Message.Body == '!dice':
			cmd_dice(Message)

		else:
			pass

	else:
		pass


def diceroll(Message):
	dice = '//d20+2d5-1+5-d6'
	removeslashes = re.split('//',dice)
	total = re.split('\+|\-',removeslashes[1])
	posrm = re.split('\+',removeslashes[1])
	posneg = [0 for x in range(len(total))]
	count = 0

	for i in range(len(posrm)):
		negrm = re.split('\-',posrm[i])
		if len(negrm) == 1:
		        posneg[count]=1
		        count = count + 1
		else:
		        for x in range(len(negrm)):
		                if x == 0:
		                        posneg[count] = 1
		                        count = count + 1
		                else:
		                        posneg[count] = -1
		                        count = count + 1

	for z in range(len(total)):
		roll = re.split('d',total[z])
		if roll[0] == '':
		        rollnum = 1
		else:
		        rollnum = roll[0]
		if len(roll) == 2:
		        for y in range(int(rollnum)):
		                max = roll[1]
		                rolling = random.randint(1,int(max))
		else:
		        rolling = roll[0]



def cmd_ping(Message):
	Message.Chat.SendMessage('Robot: Yes, I\'m still alive. :)')
	print "Ping Command Received \n"

def cmd_rickroll(Message):
	Message.Chat.SendMessage('Robot: Never Gonna Give You Up! (dance)')
	time.sleep(0.5)
	Message.Chat.SendMessage('Robot: Never Gonna Let You Down! (dance)')
	time.sleep(0.5)
	Message.Chat.SendMessage('Robot: Never Gonna Run Around and Desert You! (dance)')
	time.sleep(0.5)
	Message.Chat.SendMessage('Robot: Never Gonna Make You Cry! (dance)')
	time.sleep(0.5)
	Message.Chat.SendMessage('Robot: Never Gonna Say Goodbye! (dance)')
	time.sleep(0.5)
	Message.Chat.SendMessage('Robot: Never Gonna Tell A Lie! (dance)')
	time.sleep(0.5)
	Message.Chat.SendMessage('Robot: Or Hurt You! (dance)')
	time.sleep(0.5)
	print "Rick Command Received.\n"

def cmd_celebrate(Message):
	Message.Chat.SendMessage('Robot: Good job!')
	time.sleep(1)
	Message.Chat.SendMessage('Robot: You did great!')
	time.sleep(1)
	Message.Chat.SendMessage('Robot: Keep up the good work!')
	time.sleep(1)
	Message.Chat.SendMessage('Robot: (clap)')
	print "Celebrate Command Received.\n"

def cmd_hammertime(Message):
	Message.Chat.SendMessage('Robot: EVERYONE!')
	time.sleep(1)
	Message.Chat.SendMessage('Robot: EVERYONE STOP WHAT YOU\'RE DOING!')
	time.sleep(1)
	Message.Chat.SendMessage('Robot: DO YOU GUYS EVEN KNOW WHAT TIME IT IS!?!?!?!?!?')
	time.sleep(1)
	Message.Chat.SendMessage('Robot: HAMMERTIME!!!!!!!! (dance)')
	print "Hammer time Command Received.\n"

def cmd_credit(Message):
	Message.Chat.SendMessage('Robot: Hi, I\'m Snayer\'s Bot.')
	Message.Chat.SendMessage('Robot: Everything on me was made by him.')
	Message.Chat.SendMessage('Robot: If you want to further develop me, just ask Snayer!')
	print "Credit Command Received.\n"

def cmd_help(Message):
	Message.Chat.SendMessage('Robot: Type !ping to see if the bot is alive!')
	Message.Chat.SendMessage('Robot: Type !celebrate to have a party!')
	Message.Chat.SendMessage('Robot: Type !rickroll to rick roll someone!')
	Message.Chat.SendMessage('Robot: Type !hammertime to stop, drop, and hammertime!')
	Message.Chat.SendMessage('Robot: Type !credit to see who made me!')
	Message.Chat.SendMessage('Robot: Type !spam for some yummy spam!')
	Message.Chat.SendMessage('Robot: Type !dice for a fun game!')
	print 'Help Command Recieved.\n'

def cmd_spam(Message):
	print 'Spam Command Recieved.\n'
	while True:
		Message.Chat.SendMessage('Robot: SPAM IS YUMMY!')

def cmd_intro(Message):
	Message.Chat.SendMessage('Robot: Hi!')
	time.sleep(2)
	Message.Chat.SendMessage('Robot: My name is Willis.')
	time.sleep(2)
	Message.Chat.SendMessage('Robot: Techincally, I\'m a robot!')
	time.sleep(2)
	Message.Chat.SendMessage('Robot: Type !help to see what I can do. :)')
	print "Introduce Command Received.\n"

def cmd_dice(Message):
	Message.Chat.SendMessage('Robot: Put a bet on numbers 1 through 6.')
	time.sleep(8)
	answer = random.randint(1,6)
	Message.Chat.SendMessage('Robot: *rolls dice*')
	time.sleep(1)
	Message.Chat.SendMessage('Robot: The dice rolled the number:')
	Message.Chat.SendMessage(answer)
	print "Someone's playing dice. \n"

skype = Skype4Py.Skype();
skype.OnMessageStatus = commands

if skype.Client.IsRunning == False:
    skype.Client.Start()
skype.Attach();

print 'Skype Bot currently running on user',skype.CurrentUserHandle, "\n"

while True:
    raw_input('')
