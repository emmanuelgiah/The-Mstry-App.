import os
import time
from Skill import Skill
import shelve
import smtplib

gmail_user = 'google@gmail.com'
gmail_password = 'password123'

#get the current skills and time invested
def printSkills(currentSkills):
	message = "| Your Skills Update From MSTRY | \n"

	for x in range(0, len(currentSkills)):
			message += "\n" + str(x+1) + "."
			message += currentSkills[x].getSkill()
			print("\n" + str(x+1) + ".")
			print(currentSkills[x].getSkill())
	return message

#loading the skill data from the machine
def loadSkills():
	#user interface
	print('successful load from last run')
	#open our database file
	skillData = shelve.open('mydata')
	tempSkills = skillData['mySkills']
	skillData.close()
	return tempSkills

#email reminder of progress
def sendEmail(message):
	sent_from = gmail_user
	to = 'google@gmail.com'

	try:
	    smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
	    smtp_server.ehlo()
	    smtp_server.login(gmail_user, gmail_password)
	    smtp_server.sendmail(sent_from, to, message)
	    smtp_server.close()
	    print ("\nEmail sent successfully!")
	except Exception as ex:
	    print ("\nSomething went wrong….",ex)

#the bot is running on loop
def main():
	updateFrequency = input('| How Often Would You Like Email Updates (d/w/m) > ' )
	timeInterval = 24 * 3600
	if updateFrequency[0].lower() == 'w':
		timeInterval *= 7
	elif updateFrequency[0].lower() == 'm':
		timeInterval *= 30

	while True:
		skills = loadSkills()
		update = printSkills(skills)
		sendEmail(update)

		time.sleep(timeInterval)

if __name__ == '__main__':
	main()