# CircuitPython 2.0.0 - Trinket M0
# 16 neopixels on D4

import board
import neopixel
import adafruit_dotstar as dotstar
import time

# built-in dotstar
dot = dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1,
                      brightness=0.1, auto_write=True)

# 16-LED neopixel strip
pixels = neopixel.NeoPixel(board.D4, 16, brightness=0.1,
                           auto_write=False)

def wheel(pos):
    # Input a value 0 to 255 to get a colour value.
    # The colours are a transition r - g - b - back to r.
    if (pos < 0) or (pos > 255):
        return (0, 0, 0)
    if (pos < 85):
        return (int(pos * 3), int(255 - (pos*3)), 0)
    elif (pos < 170):
        pos -= 85
        return (int(255 - pos*3), 0, int(pos*3))
    else:
        pos -= 170
        return (0, int(pos*3), int(255 - pos*3))

def rainbow_cycle(wait):
    for j in range(255):
        for i in range(len(pixels)):
            idx = int ((i * 256 / len(pixels)) + j)
            pixels[i] = wheel(idx & 255)
        pixels.show()
        dot.fill(wheel(j))
        time.sleep(wait)

while True:
    rainbow_cycle(0.001)
