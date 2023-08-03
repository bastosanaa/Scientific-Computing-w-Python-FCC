import copy
import random
# Consider using the modules imported above.

class Hat: 

#{"red": 2, "blue": 1}
    def __init__(self, **balls):
        self.contents = []
        for key, value in balls.items():
            for ball in range(int(value)):
                self.contents.append(key)


    def draw(self, drawn):
        balls_drawn = []

        if drawn < len(self.contents):
            for draw in range(int(drawn)):
                choosen = random.choice(self.contents)
                balls_drawn.append(choosen)
                self.contents.remove(choosen)
            return balls_drawn
        return self.contents


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    event = 0

    for experiments in range(num_experiments):
        hatcopy = copy.deepcopy(hat)
        drawn = (hatcopy.draw(num_balls_drawn))
        for key, value in expected_balls.items():
            counting = drawn.count(key)
            if value <= counting:
                exp = True
            else:
                exp = False
                break
        if exp:
            event += 1
    
    print(key, counting, value)

    probability = event/num_experiments
    return probability
    