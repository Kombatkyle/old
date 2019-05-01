#!/usr/bin/env python3
'''
test
'''
def fav():
    '''
    test
    '''

    favs = [26, 52, 4, 498, 102]
    favs1 = sorted(favs)


    for fa in favs1:

        if fa < 11:
            print("You need the basic package for channel {}".format(fa))

        elif fa < 41 and fa > 10:
            print("You need the standard package for channel {}".format(fa))

        elif fa < 101 and fa > 40:
            print("You need the premium package for channel {}".format(fa))

        elif fa < 201 and fa > 100:
            print("You need the HD package for channel {}".format(fa))

        elif fa < 601 and fa > 200:
            print("You need the Expensive extras package for channel {}".format(fa))
fav()
