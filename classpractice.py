class KittyCat:
    def __init__(self, id='None', prop='None', iprop=0):
        self.id = id
        self.prop = prop
        self.iprop = iprop
    
    def getID(self):
        area = 1+1
        return self.id, area

    def getSProp(self):
        return self.prop

    def getIProp(self):
        return self.iprop

    def takeAction(self):
        return 'jumps in the air'

daisy = KittyCat('72','Cool',10)

print(daisy.getID())

print('The cat with ID ' + str(daisy.getID()) + ' took action ' + daisy.takeAction())