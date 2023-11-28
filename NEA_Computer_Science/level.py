class Level:
	def __init__(self, levelID, gameID, levelNumber, levelName, description):
		self.levelID = levelID
		self.gameID = gameID
		self.levelNumber = levelNumber
		self.levelName = levelName
		self.description = description

	def GetLevelID(self):
		return self.levelID

	def GetGameID(self):
		return self.gameID

	def GetLevelNumber(self):
		return self.levelNumber

	def GetLevelName(self):
		return self.levelName

	def GetDescription(self):
		return self.description