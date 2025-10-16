tiles = [
    [
        'Wall', 'Wall', 'Wall'
    ],
    [
        'Wall', 'Ground', 'Ground', 'Wall'
    ],
    [
        'Wall', 'Player', 'Wall', 'Ground', 'Wall'
    ],
    [
        'Wall', 'Ground', 'Ground', 'Wall'
    ],
    [
        'Wall', 'Wall', 'Wall'
    ],
]

npcs = ['Zach', 'Harry', 'Lleo']
mobs = ['Many', 'Tree' ,'Quail']
wallImages = {
    'default': ''
}

groundImages = {
    'default':''
}

objectImages = {
    'default':''
}

npcImages = {
    'Zach':''
}

mobImages = {
    'Many':''
}

class Wall:
    def __init__(self, row, col, name = 'default'):
        self.row = row
        self.col = col
        self.name = name
    def loop(self):
        pass

class Ground:
    def __init__(self, row, col, name = 'default'):
        self.row = row
        self.col = col
        self.name = name
    def loop(self):
        pass

class Object:
    def __init__(self, row, col, name):
        self.row = row
        self.col = col
        self.name = name
    
    def interact():
        pass

    def loop(self):
        pass

class NPC:
    def __init__(self, row, col, name):
        self.row = row
        self.col = col
        self.name = name

    def interact():
        pass

    def loop(self):
        pass

class Mob:
    def __init__(self, row, col, name):
        self.row = row
        self.col = col
        self.name = name

    def loop(self):
        pass