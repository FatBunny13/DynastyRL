import tcod as libtcod

from components.fighter import Fighter, Species
from entity import Entity

orc = Species(hp_bonus=1,defense_bonus=1,power_bonus=1,name='Orc')
troll = Species(hp_bonus=2,defense_bonus=2,power_bonus=2,name='Troll')
human = Species(hp_bonus=16,defense_bonus=1,power_bonus=10,name='Human')