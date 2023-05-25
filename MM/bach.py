import muser as ms
import time

import random

class Bach:
    basenotes = ["a", "a#", "b", "c", "c#", "d", "d#", "e", "f", "f#", "g", "g#"]
    octaves = ["", "2", "*", "3", "4", "5"]
    random_notes = []
    durations = (1, 2, 4, 8)

    def __init__(self):
        self.all_notes = tuple((note + octave, duration) for octave in self.octaves for note in self.basenotes for duration in self.durations)

    def generate_random_notes(self):
        return random.sample(self.all_notes, 4)
    
    def gen(self):
        self.random_notes = self.generate_random_notes() 
        print(self.random_notes)

        self.notes = ((self.random_notes),(self.random_notes))
        return self.notes
    
    def gener(self):
        selected_notes = self.generate_random_notes()

        for generation in range(4):
            print(f"Generation {generation + 1}: {selected_notes}")

            muser = ms.Muser()
            muser.generate(selected_notes)

            print("Hello user, take a listen to the newly generated audio file...")
            time.sleep(1)

            user_input = int(input("What sequence do you want to continue in the next generation? (0-3): "))
            selected_notes = selected_notes + selected_notes[user_input]

        return selected_notes

b = Bach()
notes = b.gen()
muser = ms.Muser ()
muser.generate (notes)

print("Hello user, take a listen to the newly generated audio file...")
time.sleep(1)
input = int(input("What sequence do you want to continue in next generation? (0-4)"))
print(notes[input])
print(input)