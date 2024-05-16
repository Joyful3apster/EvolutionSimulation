import random

# Organisms
ENERGY_TO_HEALTH_RATIO: float = 0.5
HEALTH_TO_ENERGY_RATIO: float = 1 / ENERGY_TO_HEALTH_RATIO
ORGANISM_BASE_ATTACK_POWER: float = 0
ORGANISM_BASE_ENERGY_MAINTANCE: float = 1
ORGANISM_BASE_MOISTURE_PREFERENCE: float = 0.5
ORGANISM_BASE_HEIGHT_PREFERENCE: float = 0.5

# Animals
STARTING_ANIMAL_SPAWNING_CHANCE = 0.001
ANIMAL_BASE_ATTACK_POWER: float = 16
ANIMAL_BASE_ENERGY_MAINTANCE: float = 10
DROWNING_DAMAGE: float = 10

def ANIMAL_STARTING_ATTACK_POWER():
    return ANIMAL_BASE_ATTACK_POWER * random.random()

def ANIMAL_STARTING_HEALTH():
    return PLANT_MAX_HEALTH * random.uniform(0.2, 0.4)


def ANIMAL_STARTING_ENERGY():
    return PLANT_MAX_ENERGY * random.uniform(0.2, 0.4)


def ANIMAL_BASE_MOISTURE_PREFERENCE():
    return random.random()


def ANIMAL_BASE_HEIGHT_PREFERENCE():
    return random.random()

def ANIMAL_STARTING_MUTATION_CHANCE():
    return random.random()

# Plants
STARTING_PLANT_SPAWNING_CHANCE = 0.5
PLANT_MAX_HEALTH: float = 200
PLANT_MAX_ENERGY: float = 100
PLANT_NUTRITION_FACTOR: float = 0.8
PLANT_REPRODUCTION_CHANCE_FACTOR: float = 1
PLANT_BASE_ATTACK_POWER: float = 0
PLANT_REPRODUCTION_ENERGY_COST_FACTOR: float = 0.5
PLANT_OFFSPRING_HEALTH_FACTOR: float = 0
PLANT_OFFSPRING_ENERGY_FACTOR: float = 0.5
PLANT_MIN_REPRODUCTION_HEALTH: float = 0
PLANT_MIN_REPRODUCTION_ENERGY: float = 0.3
PLANT_PHOTOSYNTHESIS_ENERGY_MULTIPLIER: float = 4
PLANT_COAST_ENERGY_MULTIPLIER: float = 3


def PLANT_STARTING_HEALTH():
    return PLANT_MAX_HEALTH * random.uniform(0.8, 1)


def PLANT_STARTING_ENERGY():
    return PLANT_MAX_ENERGY * random.uniform(0.8, 1)


def PLANT_BASE_MOISTURE_PREFERENCE():
    return random.random()


def PLANT_BASE_HEIGHT_PREFERENCE():
    return random.random()

def PLANT_STARTING_MUTATION_CHANCE():
    return random.random()
