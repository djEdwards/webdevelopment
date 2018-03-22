
import time
import datetime
import sys




username = input('Hello I am the computer friend but you can call me not siri. Whats your name? ')

# QUESTION 1

convo1=input('why hello '+username+' how are you today? good or bad? ')

if  convo1 =="good":
	time.sleep(1)
	whyWasDayGood=input('why execellent '+username+' Why was your day good?' )
	time.sleep(1)
	print('nice!')


if  convo1 =="bad":
	time.sleep(1)
	whyWasDayGood=input('Aw man :( '+username+' Why was your day bad??? ')
	time.sleep(1)
	print('aww.')
	time.sleep(1)
	print('its ok you have me now.')
	
else:
	print('you didnt type in a valid response. good bye')
	sys.exit()





# QUESTION 1
convo2=input('So hows the weather today '+username+' is it sunny? rainy or cloudy? ')

if  convo2 =="sunny":
	time.sleep(1)
	print('really? you think is sunny? Becuase I looking outside right now and its looking pretty gloomy')
	time.sleep(3)
	lying=input('yeah you feel pretty stupid right now huh? Just admit it, yes or no. Were you lying or not '+username+" ")
	if lying == 'yes':
		print('I knew it, Im leaving. Bye. '+username)
		sys.exit()
	if lying == 'yno':
		print('oh, awkwards... sorry about that '+username)
		sys.exit()


if  convo2 =="rainy":
	time.sleep(1)
	rainrain=input('rain, rain go away come back... do you know the rest')
	if rainrain == 'come back another day ':
		print('wow '+username+' you have skills')
	else:
		print('yikes, guess you dont. huh.')
	time.sleep(1)

if  convo2 =="cloudy":
	time.sleep(1)
	print('usual bay area weather am I right??')
	time.sleep(1)
else:
	print('you didnt type in a valid response. good bye')
	sys.exit()

#QUESTION 3
game=input('do you want to play a game? yee or nah? ')

if game == "yee":
	time.sleep(1)
	print('Good! The name of the game is called stop talking to a computer and talk to some real people. Think you could play?')

if game == "nah":
	time.sleep(1)
	print('Aw man.')
	time.sleep(1)
	print('powering down now good bye!')
	sys.exit()

else:
	print('you didnt type in a valid response. good bye')
	sys.exit()





# if quitormenu == "menu":

# 	print("routing to the menu")

# 	time.sleep(5)#provides for a delay in the excution of the code. 
# 	             #I did this to simulate a computer processing



# print("math(1)")  #menu here<<<
# print("random facts(1)")
# print("date and time(3)") 



# userchoice = input('please enter the catogory of you question (1-3)')


# if userchoice == "1":

# 	print("math stuff here")

# if userchoice == "2":

# 	print("random facts my guy!")

# if userchoice == "3":
 
# 	now = datetime.datetime.now()
# 	print ("Current date and time : ")
# 	print (now.strftime("%Y-%m-%d %H:%M:%S"))