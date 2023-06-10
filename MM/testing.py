import random

class MusicGenerator:
    notes = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]
    song_length = 8
    population_size = 6

    def __init__(self):
        self.population = self.generate_initial_population()

    def generate_initial_population(self):
        population = []
        for _ in range(self.population_size):
            song = [random.choice(self.notes) for _ in range(self.song_length)]
            population.append(song)
        return population

    def evaluate_fitness(self, song):
        # Custom fitness evaluation heuristic
        # In this example, fitness is based on the number of unique notes in the song
        unique_notes = set(song)
        return len(unique_notes)

    def select_parent(self):
        # Tournament selection
        tournament_size = 2
        tournament_contestants = random.sample(self.population, tournament_size)
        best_contestant = max(tournament_contestants, key=self.evaluate_fitness)
        return best_contestant

    def crossover(self, parent1, parent2):
        # Single-point crossover
        crossover_point = random.randint(1, self.song_length - 1)
        child = parent1[:crossover_point] + parent2[crossover_point:]
        return child

    def mutate(self, song):
        # Randomly select one position in the song and replace it with a random note
        mutation_position = random.randint(0, self.song_length - 1)
        song[mutation_position] = random.choice(self.notes)
        return song

    def generate_next_generation(self):
        next_generation = []

        # Allow the user to select a song to continue in the next generation
        user_input = int(input("Select a song index to continue in the next generation (0-5): "))
        selected_song = self.population[user_input]
        next_generation.append(selected_song)

        # Generate offspring for the remaining population
        for _ in range(self.population_size - 1):
            parent1 = self.select_parent()
            parent2 = self.select_parent()
            child = self.crossover(parent1, parent2)
            child = self.mutate(child)
            next_generation.append(child)

        self.population = next_generation

    def run(self):
        for generation in range(4):
            print(f"Generation {generation + 1}:")
            for index, song in enumerate(self.population):
                print(f"Song {index}: {song}")
            self.generate_next_generation()

music_generator = MusicGenerator()
music_generator.run()

