import tcod as libtcod


class Eyes:
    def __init__(self, colour_name,eye_colour):
        self.eye_colour = eye_colour
        self.colour_name = colour_name

class Skin:
    def __init__(self, colour_name,skin_colour):
        self.skin_colour = skin_colour
        self.colour_name = colour_name

class Hair:
    def __init__(self, colour_name,hair_colour):
        self.hair_colour = hair_colour
        self.colour_name = colour_name

#eye colours
black = Eyes(eye_colour=libtcod.black,colour_name='black')
blue = Eyes(eye_colour=libtcod.blue,colour_name='blue')

#skin colours
white_skin = Skin(skin_colour=libtcod.han,colour_name='tan')
black_skin = Skin(skin_colour=libtcod.black,colour_name='dark brown')

#hair colours
blonde = Skin(skin_colour=libtcod.han,colour_name='tan')
black_hair = Skin(skin_colour=libtcod.black,colour_name='dark brown')

eye_colour_list = [black,blue]
skin_colour_list = [white_skin,black_skin]