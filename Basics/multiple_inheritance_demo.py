"""
1. Multiple inheritance - A class can inherit attribute and methods from more than one class
2. Method Resolution order (MRO) - Search is done first in current class, then the search continues into parent classes in depth-first, left-right fashion without searching the same class twice.
"""

class MoveCharacter:
    def move_fwd(self):
        print("Move forward 1 step")

    def move_bwd(self):
        print("Move backward 1 step")

class JumpCharacter:
    def jump_1level(self):
        print("Jump character 1 level")

    def jump_2level(self):
        print("Jump Character 2 level")

class Pokemon(MoveCharacter,JumpCharacter,):
    def move_bwd(self):
        print("Pokemon moving")

p = Pokemon()
p.move_fwd()
p.jump_1level()
print(Pokemon.mro())

# class Micky(MoveCharacter,JumpCharacter):
#     pass
# m = Micky()
# m.move_fwd()
# m.move_bwd()
