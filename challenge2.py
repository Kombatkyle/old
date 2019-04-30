#!/usr/bin/env python3

def fav():

    fav_chan_num = int(input("Please Enter your Favorite Channel Number: "))

    if fav_chan_num < 11:
        print("You need the basic package")

    elif fav_chan_num < 41 and fav_chan_num > 10:
        print(" You need the standard package")

    elif fav_chan_num < 101 and fav_chan_num > 40:
        print("You need the premium package")

    elif fav_chan_num < 201 and fav_chan_num > 100:
        print(" You need the HD package")

    elif fav_chan_num < 601 and fav_chan_num > 200:
        print("You need the Expensive extras package")

    else:
        print("Please enter a valid channel number between 1 and 600")
        fav()

fav()
