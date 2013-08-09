a = [
        'Aardvark', 'Hyena',
        'Albatross',    'Jaguar',
        'Alligator',    'Jay',
        'Alpaca',   'Jellyfish',
        'American_Bison',   'Kangaroo',
        'Ant',  'Koala',
        'Anteater', 'Lemur',
        'Antelope', 'Leopard',
        'Ape',  'Lion',
        'Armadillo',    'Llama',
        'Baboon',   'Lobster',
        'Badger',   'Locust',
        'Barracuda',    'Manatee',
        'Bat',  'Marten',
        'Bear', 'Meerkat',
        'Beaver',   'Mink',
        'Bee',  'Mole',
        'Bison',    'Monkey',
        'Buffalo',  'Moose',
        'Butterfly',    'Mouse',
        'Camel',    'Mule',
        'Caribou',  'Narwhal',
        'Cat',  'Octopus',
        'Caterpillar',  'Ostrich',
        'Chamois',  'Otter',
        'Cheetah',  'Owl',
        'Chicken',  'Ox',
        'Chimpanzee',   'Oyster',
        'Chinchilla',   'Panda',
        'Chough',   'Panther',
        'Clam', 'Parrot',
        'Cobra',    'Penguin',
        'Cod',  'Pig',
        'Cow',  'Pigeon',
        'Coyote',   'Pony',
        'Crab', 'Porcupine',
        'Crane',    'Porpoise',
        'Crocodile',    'Quail',
        'Crow', 'Rabbit',
        'Deer', 'Raccoon',
        'Dinosaur', 'Rail',
        'Dog',  'Ram',
        'Dolphin',  'Rat',
        'Dove', 'Raven',
        'Dragonfly',    'Reindeer',
        'Duck', 'Rhinoceros',
        'Dugong',   'Salamander',
        'Eagle',    'Salmon',
        'Eel',  'Scorpion',
        'Elephant', 'Seahorse',
        'Elk',  'Seal',
        'Emu',  'Shark',
        'Falcon',   'Sheep',
        'Ferret',   'Shrimp',
        'Finch',    'Snail',
        'Fish', 'Snake',
        'Flamingo', 'Squid',
        'Fly',  'Squirrel',
        'Fox',  'Stingray',
        'Frog', 'Swan',
        'Gerbil',   'Tiger',
        'Giraffe',  'Toad',
        'Goat', 'Turkey',
        'Goose',    'Turtle',
        'Gorilla',  'Wallaby',
        'Hamster',  'Walrus',
        'Hare', 'Weasel',
        'Hawk', 'Whale',
        'Hedgehog', 'Wolf',
        'Heron',    'Wolverine',
        'Hippopotamus', 'Wombat',
        'Horse', 'Mosquito'
    ]


class base_except(Exception):
    def __init__(self, val):
        self.value = val
    def __str__(self):
        return repr(self.value)

for animal in a:
    exec("class {}: pass".format(animal))
    globals()[animal] = type("".format(animal), (base_except,), dict())
