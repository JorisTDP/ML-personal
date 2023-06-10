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

    length = 4 # building blocks
    population_size = 3
    population = []

    octaves = ["", "2", "*", "3", "4", "5"]
    random_notes = []
    durations = (2, 4, 8)

    def __init__(self):
        self.all_notes = tuple((note + octave, duration) for octave in self.octaves for note in self.basenotes for duration in self.durations)

    def generate_random_notes(self):
        rand = random.sample(self.all_notes, 4)
        return [rand]

    def getPopSize(self):
        return self.population_size

    def generate_bb(self):
        self.building_blocks.extend(self.generate_random_notes()) #add random notes to building blocks
        #print(self.building_blocks)
        composition = []
        for i in range(self.length):
            building_block = random.choice(self.building_blocks)
            composition.extend(building_block)
        return composition
    
    def evaluate_fitness(self, song):
        # Custom fitness evaluation heuristic
        # fitness is based on the number of unique notes
        unique_notes = set(song)
        return len(unique_notes)
    
    def best_parent(self, selected_song):
        # Selection on basis of unique notes
        size = 2
        contestants = random.sample(selected_song, size)
        #print(contestants)
        best_contestant = max(contestants, key=self.evaluate_fitness)
        return best_contestant

    def crossover(self, parent1, parent2):
        # Single-point crossover
        crossover = random.randint(1, self.length - 1)
        child = parent1[:crossover] + parent2[crossover:]
        return child

    def mutate(self, song): #TO DOOOOOOOOOOOOOO
        # Randomly select one position in the song and replace it with a random note
        l = list(song)
        for i in range(4):
            mutation_pos = random.randint(0, len(song) - 1)
            l[mutation_pos] = random.choice(random.choice(self.building_blocks))
        return l

    def gen(self):
        comp = []
        for i in range(self.population_size):
            p = self.generate_bb() #generate random notes using building blocks
            self.population.append(p)
            pop = ((p),(p))
            comp.append(pop)

        print(comp)
        return comp

    def genNext(self):
        next_gen = []

        user_input = int(input("Select a song index to continue in the next generation (0-2): "))
     
        selected_song = self.population[user_input]
        self.population = []
        #next_gen.append(best_parent)

        for i in range(self.population_size):
            mutated_child = self.mutate(selected_song)
            self.population.append(mutated_child)
            pop = ((mutated_child),(mutated_child))
            next_gen.append(pop)

        print("Previous------------")
        print(self.population[0])
        print("NEW------------")
        print(next_gen[0])
        #next_gen = tuple(next_gen)
        return next_gen
    
    def main(self):

        for generation in range(4):

            print("Hello user, take a listen to the newly generated audio files...")
            time.sleep(1)

            #user_input = int(input("What sequence do you want to continue in next generation? (1-4)"))

            muser = ms.Muser()
            notes = self.genNext()

            #notes = tuple(notes)
            #print(f"NOTES: {notes}")
            for i in range(self.population_size):
                #print(f"Song{i}:")
                muser.generate(notes[i], "song" + str(i) + ".wav")
            # muser.generate(notes)
            for i in range(3):
                print(f"Song{i}:")
                print(notes[i][0])
                print("-----------------------------------------------")   

b = Bach()
notes = b.gen()
#print(f"NOTES STARTTTTT{notes}")
muser = ms.Muser ()

for i in range(3):
    print(f"Song{i}:")
    muser.generate(notes[i], "song" + str(i) + ".wav")

for i in range(3):
    print(f"Song{i}:")
    print(notes[i][0])
    print("-----------------------------------------------")   
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