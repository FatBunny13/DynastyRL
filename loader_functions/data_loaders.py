import os

import shelve

def save_level(player,entities,game_map,dungeon_level):
   with shelve.open('level{0}{1}'.format(player.name,dungeon_level), 'n') as data_file:
       data_file['entities'] = entities
       data_file['game_map'] = game_map

def load_level(player,dungeon_level):
    if not os.path.isfile('level{0}{1}.dat'.format(player.name,dungeon_level)):
        raise FileNotFoundError

    with shelve.open('level{0}{1}'.format(player.name, dungeon_level), 'r') as data_file:
        entities = data_file['entities']
        game_map = data_file['game_map']

        return entities, game_map

def load_entities(player,dungeon_level):
    if not os.path.isfile('level{0}{1}.dat'.format(player.name,dungeon_level)):
        raise FileNotFoundError

    with shelve.open('level{0}{1}'.format(player.name, dungeon_level), 'r') as data_file:
        entities = data_file['entities']

        return entities

def save_game(player, entities, game_map, message_log, game_state):
    with shelve.open('savegame.dat', 'n') as data_file:
        data_file['player_index'] = entities.index(player)
        data_file['entities'] = entities
        data_file['game_map'] = game_map
        data_file['message_log'] = message_log
        data_file['game_state'] = game_state


def load_game():
    if not os.path.isfile('savegame.dat'):
        raise FileNotFoundError

    with shelve.open('savegame.dat', 'r') as data_file:
        player_index = data_file['player_index']
        entities = data_file['entities']
        game_map = data_file['game_map']
        message_log = data_file['message_log']
        game_state = data_file['game_state']

    player = entities[player_index]

    return player, entities, game_map, message_log, game_state
