#create skill object
class Skill:
	def __init__(self, skillName, skillTime):
		self.skillName = skillName
		self.skillTime = skillTime

	def getSkill(self):
		plural = "hours"
		if (self.skillTime == 1):
			plural = "hour"

		message = ("\n| " + self.skillName + ": " + str(self.skillTime) + " " + plural + " invested.")
		#print progress
		message += ("\n| You're Progress: " + str(((self.skillTime/100))) + "%")
		#print time left
		duration = int(10000 - self.skillTime)
		message += ("\n| Hours left to obtain mstr.y: " + str(duration) + " hours\n")
		return message

	def investTime(self):
		self.skillTime += int(input("\nHow much time did you invest into " + self.skillName + " (in hours) > "))