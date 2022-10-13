#mastery application
#store skill in a text file
#10000 hours to become master at specific skill
 

import os
import time
from Skill import Skill
import shelve
import smtplib
import progressbar


#instance variables
currentSkills = []
gmail_user = 'apple@gmail.com'
gmail_password = 'password123'

#stylistic methods
#print an app banner
def printHeader():
	print("\n| It takes 10000 hours to master a craft |")
	print("|  mstr.y helps you get one step closer  |")
	animated_bar(15)
	print()

#output the current skills and time invested
def printSkills():
	message = "| Your Skills Update From MSTRY | \n"

	for x in range(0, len(currentSkills)):
			message += "\n" + str(x+1) + "."
			message += currentSkills[x].getSkill()
			print("\n" + str(x+1) + ".")
			print(currentSkills[x].getSkill())
	return message

#print a navigation menu
def navigation():
	print("\n| Would you like to... |")
	print("| 1. Add a skill ")
	print("| 2. Update a skill ")
	print("| 3. Clear all skills (!)")
	print("| 4. Exit ")
	return input("| > ")

# create progress bar function.
def animated_bar(interval):
    widgets = ['|   loading skills... ', progressbar.AnimatedMarker()]
    bar = progressbar.ProgressBar(widgets=widgets).start()
      
    for i in range(interval):
        time.sleep(0.1)
        bar.update(i)

#functional methods
#get the skill from the user
def addSkill():
	skillName = input("\n| What skill would like to master? > ")
	skillTime = 0;
	#error handling
	while True:
		try:
			skillTime = int(input("\n| How much time have you invested into " + skillName + " (in hours) > "))
			break
		except: 
			print("| Please Enter A Number| ")

	currentSkills.append(Skill(skillName, skillTime))

#update a current skill
def updateSkill():
	option = input("\n| Which skill did you invest time mastering? (1-" + str(len(currentSkills)) + ") > ")
	#todo: implement binary search debug
	print(option)
	for x in range(0, len(currentSkills)):

		if (option.lower() == currentSkills[x].skillName.lower()) or (option[0].lower() == str(x+1)):
			currentSkills[x].investTime() 

#user experience methods
#prompt the user to begin adding skills
def promptUser():
	#check if user has no skills
	if len(currentSkills) == 0:
		print("\n| It looks like you currently have no skills...")
		option = input("\n| Would you like to start developing a skill? (y/n) > " )
		
		if option[0].lower() == 'y':
			addSkill()

#the main loop
def mainMenu():
	addUpdate = 'add'
	forEmail = ""

	while addUpdate[0].lower() != 'e' and addUpdate[0].lower() != '4':
		forEmail = printSkills()
		addUpdate = navigation()

		if addUpdate[0].lower() == 'a' or addUpdate[0].lower() == '1':
			addSkill()
		elif addUpdate[0].lower() == 'u' or addUpdate[0].lower() == '2':
			updateSkill()
		elif addUpdate[0].lower() == 'c' or addUpdate[0].lower() == '3':
			clearSkills()
		else:
			print("\n| Thank you! |")
			return

#back end methods
#storing the skill data onto the machine
def storeSkills():
	skillData = shelve.open('mydata')
	skillData['mySkills'] = currentSkills
	skillData.close()

#loading the skill data from the machine
def loadSkills():
	try:
		#user interface
		print('successful load from last run')
		#open our database file
		skillData = shelve.open('mydata')
		tempSkills = skillData['mySkills']
		skillData.close()
		return tempSkills

	except:
		print('you currently have no skills saved')
		return []

#clearing all saved data
def clearSkills():
	print("\n| Are You Sure You Want To Reset Your Progress? (This Can Not Be Undone) |")
	certainty = input("> ")

	if certainty[0].lower() == 'y':
		currentSkills.clear()
		os.remove('mydata.db')
		storeSkills()
	else:
		print("\n| Close Call |")

#main function
def main():
	temp = loadSkills()
	#load saved data from last run
	for x in range(len(temp)):
		currentSkills.append(temp[x])

	#the main loop of the program
	printHeader()
	promptUser()
	mainMenu()

	#save after run
	storeSkills()

if __name__ == "__main__":
	main()