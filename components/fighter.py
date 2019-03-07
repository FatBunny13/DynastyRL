import tcod as libtcod

from game_messages import Message

class Species:
    def __init__(self,hp_bonus,defense_bonus,power_bonus,name):
        self.hp_bonus = hp_bonus
        self.defense_bonus = defense_bonus
        self.power_bonus = power_bonus
        self.name = name


class Fighter:
    def __init__(self, hp, defense, power, xp=0):
        self.base_max_hp = hp
        self.hp = hp
        self.base_defense = defense
        self.base_power = power
        self.xp = xp

    @property
    def max_hp(self):
        if self.owner and self.owner.equipment:
            bonus = self.owner.equipment.max_hp_bonus
        else:
            bonus = 0

        return self.base_max_hp + self.owner.species.hp_bonus + bonus

    @property
    def power(self):
        if self.owner and self.owner.equipment:
            bonus = self.owner.equipment.power_bonus
        else:
            bonus = 0

        return self.base_power + self.owner.species.power_bonus + bonus

    @property
    def defense(self):
        if self.owner and self.owner.equipment:
            bonus = self.owner.equipment.defense_bonus
        else:
            bonus = 0

        return self.base_defense + self.owner.species.defense_bonus + bonus

    def take_damage(self, amount):
        results = []

        self.hp -= amount

        if self.hp <= 0:
            results.append({'dead': self.owner, 'xp': self.xp})

        return results

    def heal(self, amount):
        self.hp += amount

        if self.hp > self.max_hp:
            self.hp = self.max_hp

    def attack(self, target):
        results = []

        damage = self.power - target.fighter.defense

        if damage > 0:
            results.append({'message': Message('{0} attacks {1} the {2} {3} for {4} hit points.'.format(
                self.owner.name.capitalize(), target.name,target.profession,target.species.name,str(damage)), libtcod.white)})
            results.extend(target.fighter.take_damage(damage))
        else:
            results.append({'message': Message('{0} attacks {1} the {2} {3} but does no damage.'.format(
                self.owner.name.capitalize(), target.name,target.profession,target.species.name,), libtcod.white)})

        return results
