import copy
import random

class Hat:

    def __init__(self, **args):
        self.args = args
        self.contents = [[k]*v for k,v in args.items()] # Add incoming dictionary to list
        self.contents = [x for y in self.contents for x in y] # Turn list of lists to list
    '''
    def draw(self, amount):
        self.amount = amount
        rand_draw_list = []
        if amount >= len(self.contents):
            return self.contents
        else:
             rand_draw_list.append(random.sample(self.contents, amount)) # Randomly select items from original list and append them to new list
        rand_draw_list = [x for y in rand_draw_list for x in y]
        return rand_draw_list
    '''
    def draw(self, amount):
        rand_draw_list = []
        if amount >= len(self.contents):
            return self.contents
        for i in range(amount):
            drawn_balls = self.contents.pop(random.randrange(len(self.contents)))
            rand_draw_list.append(drawn_balls)
        return rand_draw_list
    
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    '''
    list_expected_balls = [[k]*v for k,v in expected_balls.items()] # Add incoming dictionary to list
    list_expected_balls = [x for y in list_expected_balls for x in y] # Turn list of lists to list

    for i in range(num_experiments):
        copy_of_hat = copy.deepcopy(hat)
        drawn_list = copy_of_hat.draw(num_balls_drawn)
        if drawn_list in list_expected_balls:
            count += 1
    
    return count/num_experiments
    '''
    count = 0

    for x in range(num_experiments):
      copy_of_hat = copy.deepcopy(hat)
      drawn_list = copy_of_hat.draw(num_balls_drawn)
      success = True
      for k, v in expected_balls.items():
        if drawn_list.count(k) < v:
          success = False
          break
      if success:
        count += 1

    return count / num_experiments

experiment(Hat, {"blue":2,"green":1}, 4, 1000)#hat2 = Hat(red=5, orange=4)
#hat = Hat(yellow=3, blue=2, green=4)
#hat2.draw(5)
#hat3 = Hat(red=5, orange=4, black=1, blue=0, pink=2, striped=9)
#hat3.draw(7)