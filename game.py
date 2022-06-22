#!/usr/bin/python3


class PlayField:
    def __init__(self):
        self.rows = [1, 3, 5, 7]
    def __str__(self):
        return str(self.rows)


class Game:
    ''' Docstring '''

    def __init__(self):
        ''' Constructor '''
        self.field = PlayField()
        self.log = []
        self.curPlayerNo = 1

    def move(self, _move):
        row_str = _move[0]

        if not row_str.isdigit():
            return (False, 'Move is not a number')
        row = int(row_str)
        if row>3:
            return (False, 'Too big row')
        if len(_move)<2:
            return (False, 'Too short move')
        if not _move[1].isdigit():
            return (False, 'Second digit in move is not a number')
        number = int(_move[1])
        if self.field.rows[row]<number:
            return (False, 'Too big number in a row')

        self.field.rows[row] -= number
        print(f'Move was made by Player {self.curPlayerNo}')

        if self.curPlayerNo == 1:
            self.curPlayerNo = 2
        else:
            self.curPlayerNo = 1

        return (True, 'OK')

    @property
    def ends(self):
        return sum(self.field.rows)==0


if __name__ == '__main__':
    print('Creating PlayField')
    g = Game()
    print(f'Total Game field is : {g.field}')
    print(sum(g.field.rows))
    while True:
        mv = input('Input your move: ')
        if mv == 'stop':
            break
        #print(g.move(mv))
        print(f'Now field is: {g.field} Game ends:{g.ends}')
        if g.ends:
            break
    print(f'Game is over. Player {g.curPlayerNo} win.')
