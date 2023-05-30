import muser as ms
import time

import random

class Bach:
    basenotes = ["a", "a#", "b", "c", "c#", "d", "d#", "e", "f", "f#", "g", "g#"]

    building_blocks = [
    [("c", 4), ("d", 4), ("e", 4), ("f", 4)],
    [("g", 4), ("a", 4), ("b", 4), ("c#", 4)],
    [("c#", 4), ("b", 4), ("a", 4), ("g", 4)],
    [("f", 4), ("e", 4), ("d", 4), ("c", 4)],
    [("d", 4), ("f", 4), ("a", 4), ("c#", 4)],
    [("g", 4), ("b", 4), ("d", 4), ("f#", 4)],
    [("e", 4), ("g", 4), ("b", 4), ("d#", 4)],
    [("a", 4), ("c#", 4), ("e", 4), ("g#", 4)]
    ]

    finalnotes = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

    octaves = ["", "2", "*", "3", "4", "5"]
    random_notes = []
    durations = (2, 4, 8)

    def __init__(self):
        self.all_notes = tuple((note + octave, duration) for octave in self.octaves for note in self.basenotes for duration in self.durations)

    def generate_random_notes(self):
        rand = random.sample(self.all_notes, 4)
        return [rand]

    def generate_bb(self):
        self.building_blocks.extend(self.generate_random_notes()) #add random notes to building blocks
        print(self.building_blocks)
        composition = []
        for _ in range(4):
            building_block = random.choice(self.building_blocks)
            composition.extend(building_block)
        return composition
    
    def gen(self):
        self.random_notes = self.generate_bb() #generate random notes using building blocks
        #print(self.random_notes)

        for i in range(len(self.finalnotes)): #Use finalnotes if there are any
            if self.finalnotes[i] != 0:
                self.random_notes[i] = self.finalnotes[i]

        self.notes = ((self.random_notes),(self.random_notes)) 
        return self.notes
    
    def main(self):

        for generation in range(4):

            print("Hello user, take a listen to the newly generated audio file...")
            time.sleep(1)

            user_input = int(input("What sequence do you want to continue in next generation? (1-4)"))
            self.finalnotes[( (user_input - 1) * 4):(user_input*4)] = self.notes[0][( (user_input - 1) * 4):(user_input*4)]
            print("finalnotes:")
            print(self.finalnotes)

            muser = ms.Muser()
            notes = self.gen()
            print(notes)
            muser.generate(notes)

b = Bach()
notes = b.gen()
muser = ms.Muser ()
muser.generate (notes)

b.main()


# print("Hello user, take a listen to the newly generated audio file...")
# time.sleep(1)
# input = int(input("What sequence do you want to continue in next generation? (1-4)"))
# print(notes[0])
# print(input)
# finalnotes = notes[0][( (input - 1) * 4):(input*4)]
# print(finalnotes)
#notes[0][4:8] = finalcomp
#print(notes[0]) 