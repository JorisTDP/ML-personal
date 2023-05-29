import random
import pysynth as ps
import muser as ms

# Definieer de noten en duur van de muzikale building blocks
building_blocks = [
    [("c", 4), ("d", 4), ("e", 4), ("f", 4)],
    [("g", 4), ("a", 4), ("b", 4), ("c^", 4)],
    [("c^", 4), ("b", 4), ("a", 4), ("g", 4)],
    [("f", 4), ("e", 4), ("d", 4), ("c", 4)]
]

# Functie om een willekeurige compositie te genereren
def generate_random_composition():
    composition = []
    for _ in range(4):
        building_block = random.choice(building_blocks)
        composition.extend(building_block)
    return composition

# Functie om de gegenereerde compositie af te spelen
def play_composition(composition):
    notes = []
    for note, duration in composition:
        notes.append((note, duration * 4))  # Duur wordt vermenigvuldigd met 4 voor pysynth
    # ps.make_wav(notes, fn="composition.wav")
    # ps.make_wav(notes)  # Speel de compositie af

# Functie om de gebruiker een keuze te laten maken
def select_building_block(compositions):
    print("Kies een building block:")
    for i, composition in enumerate(compositions):
        print(f"{i + 1}. {composition}")
    choice = int(input("Selecteer een nummer: ")) - 1
    return compositions[choice]

# Hoofdprogramma
def main():
    population_size = 4
    generations = 5

    # Genereren van de initiele populatie
    population = []
    for _ in range(population_size):
        composition = generate_random_composition()
        population.append(composition)

    for _ in range(generations):
        print(f"Generation: {_ + 1}")
        for i, composition in enumerate(population):
            print(f"\nCompositie {i + 1}:")
            play_composition(composition)

        selected_composition = select_building_block(population)
        population = [selected_composition] * population_size

    print("Voltooide compositie:")
    print(selected_composition[1])
    #play_composition(selected_composition)

if __name__ == "__main__":
    main()
