import muser as ms

import random

basenotes = ["a", "a#", "b", "c", "c#", "d", "d#", "e", "f", "f#", "g", "g#"]
octaves = ["", "2", "*", "3", "4", "5"]

durations = (1, 2, 4, 8, 16)

all_notes = tuple((note + octave, duration) for octave in octaves for note in basenotes for duration in durations)

random_notes1 = random.sample(all_notes, 4)
random_notes2 = random.sample(all_notes, 4)
random_notes3 = random.sample(all_notes, 4)
# random_notes4 = random.sample(all_notes, 4)
print(random_notes1)
#print(random_notes2)

notes = (
            (
                random_notes1
            ),
            (
                random_notes2
            ), #('b2*', -4)
            (
                random_notes3
            ), #('b2*', -4)
            # (
            #     random_notes4
            # )
        )
#octaves = ["", "2", "*", "3"]


muser = ms.Muser ()
muser.generate (notes)
