'''
Copiado de: https://github.com/bbcmicrobit/micropython/tree/master/examples
'''
import microbit
import random

def led_dance():
  dots = [ [0]*5, [0]*5, [0]*5, [0]*5, [0]*5 ]
  while True:
    dots[random.randrange(5)][random.randrange(5)] = 9
    for i in range(5):
      for j in range(5):
        microbit.display.set_pixel(i, j, dots[i][j])
        if random.random() < 0.2 or dots[i][j] > 4:
          dots[i][j] = max(dots[i][j] - 1, 0)
    microbit.sleep(microbit.display.read_light_level() * 5)

led_dance()
