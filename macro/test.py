import pyfirmata
import time
from tkinter import *
from tkinter.ttk import *
from tkinter import ttk

board = pyfirmata.Arduino('COM3')

it = pyfirmata.util.Iterator(board)
it.start()

board.digital[2].mode = pyfirmata.INPUT



while True:
    
    sw = board.digital[2].read()
    if sw is True:
        board.digital[13].write(1)
    else:
        board.digital[13].write(0)
    time.sleep(0.1)