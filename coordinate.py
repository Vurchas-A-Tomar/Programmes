class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Finds quadrant of the point given
    def find_quadrant(self):
        output = ''
        if self.x and self.y == 0:
            output = 'Origin'
        elif self.y == 0:
            if abs(self.x) == self.x:
                output = 'Above and Parallel to the x-axis'
            else:
                output = 'Below and Parallel to the x-axis'
        elif self.x == 0:
            if abs(self.y) == self.y:
                output = 'Above and Parallel to the y-axis'
            else:
                output = 'Below and Parallel to the y-axis'
        elif abs(self.x) == self.x:
            if abs(self.y) == self.y:
                output = 'Quadrant 1'
            else:
                output = 'Quadrant 4'
        elif abs(self.y) == self.y:
            if abs(self.x) != self.x :
                output = 'Quadrant 2'
        else:
            output = 'Quadrant 3'

        return output


try:
    type_input = int(input('''If you want to find the quadrant of this point, type (1)
If you want to find a random point in a certain quadrant, type (2)
: '''))

    if type_input == 1:
        x, y = input('Enter the Coordinates (Enter a comma after each point): ').split(',')
        x = int(x)
        y = int(y)
        print(f'{x},{y}')
        point = Point(x, y)
        print(point.find_quadrant())

except TypeError:
    print('Invalid Input, enter a point')
except ValueError:
    print('Invalid Input, enter appropriately')

# -----------------------------------------------------------------------------------------------------------------------