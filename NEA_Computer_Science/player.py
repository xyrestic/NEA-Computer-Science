class Player:
	def __init__(self, playerID, name, academicLevel, confidenceLevel):
		self.playerID = playerID
		self.name = name
		self.academicLevel = academicLevel
		self.confidenceLevel = confidenceLevel
		self.revisionMethod = ''
		self.preferredMathTopics = []
		
	def SetRevisionMethod(self, revisionMethod):
		self.revisionMethod = revisionMethod
		
	def AddMathTopic(self, topic):
		self.preferredMathTopics.append(topic)
		
	def GetPlayerID(self):
		return self.playerID
		
	def GetName(self):
		return self.name
		
	def GetAcademicLevel(self):
		return self.academicLevel
		
	def GetConfidenceLevel(self):
		return self.confidenceLevel
		
	def GetRevisionMethod(self):
		return self.revisionMethod
		
	def GetPreferredMathTopics(self):
		return self.preferredMathTopics