import copy
import random

class Hat:

    def __init__(self, **args):
        self.args = args
        self.contents = [[k]*v for k,v in args.items()] # Add incoming dictionary to list
        self.contents = [x for y in self.contents for x in y] # Turn list of lists to list

    def draw(self, amount):
        self.amount = amount
        rand_draw_list = []
        if amount > len(self.contents):
            return self.contents
        else:
            return rand_draw_list.append(random.sample(self.contents, amount)) # Randomly select items from original list and append them to new list


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    balls_drawn = []
    balls_drawn.append(random.sample(hat, num_balls_drawn))
    count = 0
    
    return 
        


hat1 = Hat(yellow=3, blue=2, green=4)
hat1.draw(5)
experiment(Hat, {"yellow":2,"green":1}, 5, 2000)
#hat2 = Hat(red=5, orange=4)
#hat2.draw(5)
#hat3 = Hat(red=5, orange=4, black=1, blue=0, pink=2, striped=9)
#hat3.draw(7)