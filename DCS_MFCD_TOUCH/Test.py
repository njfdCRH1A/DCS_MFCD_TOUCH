from pynput.keyboard import Key, Controller
import matplotlib.pyplot as plt

image = plt.imread('UI\\TEST\\button.png')
plt.imshow(image)
plt.show()

import time
keyboard = Controller()
time.sleep(5)
keyboard.press('1')
keyboard.release('1')