from LinearFunctions import *
from os import system


menu = '''

enter your function form or it's number.
if you wish to exit, type "exit":

1: y = mx + b
2: y - y1 = m(x - x1)
3: ax + by = c

'''
while True:
    system('clear')
    usr_cmd = input(f'{menu}> ').replace(' ', '')

    if usr_cmd == '1' or usr_cmd == 'y=mx+b':
        print('\n\n' + SlopeIntercept(input('please enter your function: ')).info() + '\n\n')
        input('press [enter] to continue')
    elif usr_cmd == '2' or usr_cmd == 'y-y1=m(x-x1)':
        print('\n\n' + PointSlope(input('please enter your function: ')).info() + '\n\n')
        input('press [enter] to continue')
    elif usr_cmd == '3' or usr_cmd == 'ax+by=c':
        print('\n\n' + Standard(input('please enter your function: ')).info() + '\n\n')
        input('press [enter] to continue')
    elif usr_cmd == 'exit':
        system('clear')
        quit()
    else:
        print('This option is invalid, please enter a valid input or type "exit" for quitting.')
        input('press [enter] to continue')
