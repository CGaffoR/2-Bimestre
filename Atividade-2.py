class Time:
    def __init__(self, name, players = []):
        self.name = name
        self.players = players
    def addPlayer(self, name):
        players = self.players
        players.append(name)    
    def showTime(self):
        for index,player in enumerate(self.players):
            print(f'Jogador[{index+1}] - {player}')
time1 = Time('GGEZ')
time1.addPlayer('carlos')
time1.addPlayer('leo')
time1.addPlayer('matheus')
time1.addPlayer('ryan')
time1.addPlayer('jean')
time1.showTime()