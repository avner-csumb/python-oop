# create a Musician class
# first attributes will be name and genre

# other attributes: instrument, years active, top hit, number of albums

# play concerts, practice, record albums

class Musician(object):
    """A class that creates musicians"""
    def __init__ (self, name, genre, top_hit, is_on_tour):
        self.name = name
        self.genre = genre
        self.top_hit = top_hit
        self.is_on_tour = is_on_tour

    def description(self):
        return ('Hi, I\'m ' + self.name + ' and my number one single was ' + self.top_hit + '.')

    def on_tour(self):
        if self.is_on_tour:
            print('Hey you, check out my tour. It\'s the best. Andy says so.')
        else:
            print('I\'m not tour at the moment. Hope to be soon. Don\'t forget about me.')


beyonce = Musician('Beyonce', 'R&B', 'Lemonade', True)

prince_clone = Musician('Prince', 'R&B', 'Raspberry Beret', False)

mj_clone = Musician('Michael Jackson', 'Pop', 'Thriller', False)

bruno_mars = Musician('Bruno Mars', 'Pop', '24K', True)

# bruno_mars.on_tour()

# print(beyonce.name)
# print(beyonce.name + ' is a musician who plays ' + beyonce.genre + ' music.')

# print('Prince\'s top hit is ' + prince_clone.top_hit + '.')

# beyonce.description()
