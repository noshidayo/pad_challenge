from random import randint

mainAttributes = []
subAttributes = []
team = {}
ATTRIBUTES = {
	0: 'None',
	1: 'Fire',
	2: 'Water',
	3: 'Wood',
	4: 'Light',
	5: 'Dark'
}

class Monster:
	mainAttribute = None
	subAttribute = None

	def __init__(self, mainAtt, subAtt):
		self.mainAttribute = mainAtt
		self.subAttribute = subAtt

	def __repr__(self):
		return '%s/%s' % (ATTRIBUTES[self.mainAttribute], ATTRIBUTES[self.subAttribute])

	@staticmethod
	def randomCardTyping():
		monster = Monster(randint(1,5), randint(0,5))
		return monster

	@staticmethod
	def randomTeam(monsterCount=5):
		monsterTeam = []
		for x in range(0,monsterCount):
			monsterTeam.append(Monster.randomCardTyping())
		return monsterTeam


print("Choose between 1 and 5 monsters to be randomized:")
while True:
	monsterCount = input()

	if monsterCount == '':
		monsterCount = 5
		break
	else:
		try:
			monsterCount = int(monsterCount)
			if monsterCount <= 0 or monsterCount >5:
				raise ValueError()
		except ValueError:
			print("Not a valid number, please try again.")
			continue
		break

print("Try and make a team that contains monsters with the following types:")
print(Monster.randomTeam(monsterCount))

