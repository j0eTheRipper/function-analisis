class LinearFunctions:
    def __init__(self, function):
        self.function = function.replace(' ', '').split('=')
        self.slope = 0
        self.x_intercept = 0
        self.y_intercept = 0

    @staticmethod
    def parse_sign(value, inverse=False):
        if inverse:
            return f'- {value}' if value > 0 else f'+ {abs(value)}'
        else:
            return f'+ {value}' if value > 0 else f'- {abs(value)}'

    @staticmethod
    def parse_value(value):
        if value == '+':
            return 1
        elif value == '-':
            return -1

        rounded = round(float(value), 2)

        if rounded == int(rounded):
            return int(rounded)
        else:
            return rounded

    @staticmethod
    def mx(slope, char='x'):
        if slope == 0:
            return ''
        elif slope == 1:
            return f'{char}'
        elif slope == -1:
            return f'-{char}'
        else:
            return f'{slope}{char}'

    def get_slope(self, m):
        if m == '':
            self.slope = 1
        elif m == '-':
            self.slope = -1
        else:
            self.slope = self.parse_value(m)

        return self.slope

    def get_intercept(self, intercept):
        pass

    def to_point_slope(self):
        pass

    def to_slope_intercept(self):
        pass

    def to_standard(self):
        pass

    def info(self):
        return f'''Forms of the function:
Standard ==> {self.to_standard()}
Slope intercept ==> {self.to_slope_intercept()}
Point slope ==> {self.to_point_slope()}

     𝛑𝛑𝛑𝛑𝛑𝛑𝛑𝛑𝛑𝛑𝛑𝛑𝛑𝛑𝛑𝛑𝛑𝛑𝛑𝛑𝛑𝛑𝛑𝛑

Information about the function:
Slope ==> {self.slope}
x-intercept ==> {self.get_intercept('x')}
y-intercept ==> {self.get_intercept('y')}
'''

    def __repr__(self):
        return '='.join(self.function)


class PointSlope(LinearFunctions):
    def __init__(self, function):
        super().__init__(function)
        self.slope = self.get_slope(self.function[1].split('(')[0])
        self.x1 = - self.parse_value(self.function[1].split('x')[1].replace(')', ''))
        self.y1 = - self.parse_value(self.function[0].replace('y', ''))

    def get_intercept(self, intercept):
        """Getting the intercepts of the function"""
        if intercept == 'x':
            self.x_intercept = (- self.y1 + self.slope * self.x1) / self.slope
            return self.x_intercept
        elif intercept == 'y':
            self.y_intercept = - self.slope * self.x1 + self.y1
            return self.y_intercept

    def to_slope_intercept(self):
        b = - (self.slope * self.x1) + self.y1
        return SlopeIntercept(f'y = {self.mx(self.slope)} {self.parse_sign(b)}')

    def to_standard(self):
        a = self.slope * self.x1
        c = -a + self.y1
        return Standard(f'{self.mx(- self.slope)} + y = {c}')

    def to_point_slope(self):
        return self

    def __str__(self):
        return f'y {self.parse_sign(self.y1, True)} = {self.mx(self.slope, "(x")} {self.parse_sign(self.x1, True)})'


class SlopeIntercept(LinearFunctions):
    def __init__(self, function):
        super().__init__(function)
        self.slope = self.get_slope(self.function[1].split('x')[0])

    def get_intercept(self, intercept):
        self.y_intercept = self.parse_value(self.function[1].split('x')[1].replace(' ', ''))

        if intercept == 'x':
            self.x_intercept = - self.y_intercept / self.slope
            return self.x_intercept
        elif intercept == 'y':
            return self.y_intercept

    def to_point_slope(self):
        self.get_intercept('y')

        x = abs(self.y_intercept) + 1
        y = (self.slope * x) + self.y_intercept

        return PointSlope(f'y {self.parse_sign(y, True)} = {self.mx(self.slope, "(")}x {self.parse_sign(x, True)})')

    def to_standard(self):
        return Standard(f'{- self.slope}x + y = {self.get_intercept("y")}')

    def to_slope_intercept(self):
        return self

    def __str__(self):
        return f'y = {self.mx(self.slope)} {self.parse_sign(self.get_intercept("y"))}'


class Standard(LinearFunctions):
    def __init__(self, function):
        super().__init__(function)
        self.a = self.parse_value(self.function[0].split('x')[0])
        self.b = self.parse_value(self.function[0].split('x')[1][:-1:])
        self.c = self.parse_value(self.function[1])
        self.slope = - self.a / self.b

    def get_intercept(self, intercept):
        if intercept == 'x':
            return self.c / self.a
        elif intercept == 'y':
            return self.c / self.b

    def to_slope_intercept(self):
        b = self.c / self.b
        if b < 0:
            b = f'- {abs(b)}'
        elif b > 0:
            b = f'+ {abs(b)}'

        return SlopeIntercept(f'y = {- self.a / self.b}x {b}')

    def to_point_slope(self):
        return self.to_slope_intercept().to_point_slope()

    def to_standard(self):
        return self

    def __str__(self):
        return f'{self.mx(self.a, "x")} + {self.mx(self.b, "y")} = {self.c}'
