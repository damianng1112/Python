#---------------------------------------------

class Coach:

        def __init__(self, title, licence):
            self._title = title
            self._licence = licence

        def getTitle(self):
            return self._title

        def getLicence(self):
            return self._licence

        def setLicence(self, licence):
            self._licence = licence

class Player:

    def __init__(self, position, gamesPlayed):
        self._position = position
        self.__gamesPlayed = gamesPlayed


    def getPosition(self):
        return self._position

    def getGamesPlayed(self):
        return self.__gamesPlayed

    def setGamesPlayed(self, gamesPlayed):
        self.__gamesPlayed = gamesPlayed
    # Extended Class


class PlayerCoach(Coach, Player):

    def __init__(self, name, title, licence, position, gamesPlayed):
        Coach.__init__(self, title, licence)
        Player.__init__(self, position, gamesPlayed)
        self.__name = name

    def incrementGamesPlayed(self):
        gamesPlayed = super().getGamesPlayed()
        super().setGamesPlayed(gamesPlayed+1)

    def getName(self):
        return self.__name

    def setTitle(self, title):
        self._title = title