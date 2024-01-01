import sys
import pygame
import random
from scripts.entities.animal import Animal
from scripts.entities.plant import Plant
from scripts.entities.dna import DNA

class Simulation:
    ANIMALS_MAX_HEALTH = 100
    ANIMALS_MAX_ENERGY = 100
    ANIMALS_MAX_SIZE = 10
    ANIMALS_MIN_PERCENTAGE_HEALTH_TO_REPRODUCE = .7
    
    PLANTS_MAX_HEALTH = 100
    PLANTS_MAX_ENERGY = 100
    PLANTS_MAX_SIZE = 10

    MAX_ANIMALS = 1000
    MAX_PLANTS = 1000
    SPAWN_NEW_ANIMALS_THRESHOLD = 30  # Threshold below which we start spawning new animals
    
    def __init__(self, width, height, num_animals):
        self.width = width
        self.height = height
    
        num_animals = min(num_animals, self.MAX_ANIMALS)
        self.animals: list[Animal] = [
                    Animal(
                        random.randint(0, width), 
                        random.randint(0, height), 
                        DNA(
                            self.ANIMALS_MAX_SIZE,
                        )
                    ) for _ in range(num_animals)
        ]        
        self.plants: list[Plant] = []
        
        pygame.init()
        pygame.display.set_caption("Evolution Simulation")
        self.screen = pygame.display.set_mode((self.width, height))
        self.clock = pygame.time.Clock()

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    sys.exit()
                
            self.screen.fill((255, 255, 255))  # Fill the screen with a white background
            
            if len(self.animals) < self.SPAWN_NEW_ANIMALS_THRESHOLD:
                self.spawn_animals()

            for animal in self.animals[:]:
                animal.move()                
                if animal.isAlive():
                    for plant in self.plants[:]:
                        if plant.isAlive():
                            if animal.shape.colliderect(plant.shape):
                                self.plants.remove(plant)
                                animal.gainEnergy(100)  #TODO create variable for this
                                animal.heal()
                            else:
                                plant.update()
                                plant.draw(self.screen)
                        else:
                            self.plants.remove(plant)
                            
                    if(animal.calculate_health_ratio() >= self.ANIMALS_MIN_PERCENTAGE_HEALTH_TO_REPRODUCE):
                        if len(self.animals) < self.MAX_ANIMALS and random.random() * animal.calculate_health_ratio() >= self.ANIMALS_MIN_PERCENTAGE_HEALTH_TO_REPRODUCE:
                            self.animals.append(animal.give_birth())
                    
                    animal.draw(self.screen)
                else:
                    self.animals.remove(animal)

            self.spawn_plants()
            
            pygame.display.update()
            self.clock.tick(60)

    def spawn_animals(self):
            # Function to spawn new animals if below threshold
            while len(self.animals) < self.SPAWN_NEW_ANIMALS_THRESHOLD:
                new_animal = Animal(
                    random.randint(0, self.screen.get_width()), 
                    random.randint(0, self.screen.get_height()), 
                    DNA(
                        self.ANIMALS_MAX_SIZE,
                    )
                )
                self.animals.append(new_animal)
                if len(self.animals) >= self.MAX_ANIMALS:
                    break
    
    def spawn_plants(self):
        if len(self.plants) < self.MAX_PLANTS:
            new_plant = Plant(
                random.randint(0, self.screen.get_width()), 
                random.randint(0, self.screen.get_height()),
                DNA(
                    self.PLANTS_MAX_SIZE,
                    color = pygame.Color(random.randint(0, 30), random.randint(50, 150), random.randint(0, 30))
                )
            )
            self.plants.append(new_plant)  