class TicTacTO():

    arrGameMap = [
        ['1', '2', '3'],
        ['4', '5', '6'],
        ['7', '8', '9']
    ]

    def __createMap(self):
        return f"""
        | {self.arrGameMap[0][0]} | {self.arrGameMap[0][1]} | {self.arrGameMap[0][2]} |
        -------------
        | {self.arrGameMap[1][0]} | {self.arrGameMap[1][1]} | {self.arrGameMap[1][2]} |
        ------------
        | {self.arrGameMap[2][0]} | {self.arrGameMap[2][1]} | {self.arrGameMap[2][2]} |
        """

    def showMap(self):
        print(self.__createMap())

    def setOandX(self, value: str, character: chr):  # character = o or x
        if value == '1':
            self.arrGameMap[0][0] = character
        if value == '2':
            self.arrGameMap[0][1] = character
        if value == '3':
            self.arrGameMap[0][2] = character
        if value == '4':
            self.arrGameMap[1][0] = character
        if value == '5':
            self.arrGameMap[1][1] = character
        if value == '6':
            self.arrGameMap[1][2] = character
        if value == '7':
            self.arrGameMap[2][0] = character
        if value == '8':
            self.arrGameMap[2][1] = character
        if value == '9':
            self.arrGameMap[2][2] = character

    def winner(self):
        if self.arrGameMap[0][0] == self.arrGameMap[0][1] == self.arrGameMap[0][2]:
            return self.arrGameMap[0][0]
        elif self.arrGameMap[1][0] == self.arrGameMap[1][1] == self.arrGameMap[1][2]:
            return self.arrGameMap[1][0]
        elif self.arrGameMap[2][0] == self.arrGameMap[2][1] == self.arrGameMap[2][2]:
            return self.arrGameMap[2][0]
        elif self.arrGameMap[0][0] == self.arrGameMap[1][1] == self.arrGameMap[2][2]:
            return self.arrGameMap[0][0]
        elif self.arrGameMap[0][2] == self.arrGameMap[1][1] == self.arrGameMap[2][0]:
            return self.arrGameMap[0][2]
        elif self.arrGameMap[0][0] == self.arrGameMap[1][0] == self.arrGameMap[2][0]:
            return self.arrGameMap[0][0]
        elif self.arrGameMap[0][1] == self.arrGameMap[1][1] == self.arrGameMap[2][1]:
            return self.arrGameMap[0][1]
        elif self.arrGameMap[0][2] == self.arrGameMap[1][2] == self.arrGameMap[2][2]:
            return self.arrGameMap[0][2]
        return "z"
