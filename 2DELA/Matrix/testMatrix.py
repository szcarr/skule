#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2017-18 Richard Hull and contributors
# See LICENSE.rst for details.

import time
import argparse

from numpy import matrix

from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.legacy import text
from luma.core.legacy.font import proportional, LCD_FONT

import prints

grid = {

}

#with canvas(device) as draw:
#draw.point((xcoord, ycoord), fill=color)

def demo(w, h, block_orientation, rotate): #is main
    #everySingleLEDOnce(w, h, block_orientation, rotate)
    addLED(w, h, block_orientation, rotate)



def setLED():
        print("Thread entered grid update.")
        parser = argparse.ArgumentParser(description='matrix_demo arguments',
            formatter_class=argparse.ArgumentDefaultsHelpFormatter)

        parser.add_argument('--width', type=int, default=8, help='Width')
        parser.add_argument('--height', type=int, default=8, help='height')
        parser.add_argument('--block-orientation', type=int, default=-90, choices=[0, 90, -90], help='Corrects block orientation when wired vertically')
        parser.add_argument('--rotate', type=int, default=0, choices=[0, 1, 2, 3], help='Rotation factor')

        args = parser.parse_args()

        try:
            demo(args.width, args.height, args.block_orientation, args.rotate)
        except KeyboardInterrupt:
            pass
        except Exception as e:
            print(e)

def everySingleLEDOnce(w, h, block_orientation, rotate):
    serial = spi(port=0, device=0, gpio=noop())
    device = max7219(serial, width=w, height=h, rotate=rotate, block_orientation=block_orientation)

    for x in range(w):
        for y in range(h):
            print(x,y)
            with canvas(device) as draw:
                draw.point((x, y), fill="white")
                time.sleep(1)      

def addLED(w, h, block_orientation, rotate):
    prints.conditionalPrint(prints.matrixPrint, "In addLED()")
    serial = spi(port=0, device=0, gpio=noop())
    device = max7219(serial, width=w, height=h, rotate=rotate, block_orientation=block_orientation)
    ledList = []
    for x in range(w):
        for y in range(h):
            ledList.append(tuple((x, y)))
            with canvas(device) as draw:
                for e in range(len(ledList)):
                    hei = str(ledList[e][0]) + " " + str(ledList[e][1])
                    prints.conditionalPrint(prints.matrixPrint, hei)
                    draw.point((ledList[e][0], ledList[e][1]), fill="white")
                    time.sleep(0.1)

def convertCoordinateToInt(coordinates):

    '''
    <coordinate> 'x y'
    '''

    lst = str(coordinates).split(" ")
    return int(lst[0]), int(lst[1])

#setLED()