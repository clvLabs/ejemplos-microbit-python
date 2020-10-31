'''
Ejemplo básico de uso de música
'''

import microbit
import music
import random

IMAGES = [
  microbit.Image.SMILE,
  microbit.Image.SKULL,
]

def makeshow(image, sound):
    microbit.pin1.write_digital(1)
    microbit.display.show(image)
    music.play(sound, wait=True)
    microbit.pin1.write_digital(0)


microbit.display.show(microbit.Image.HAPPY)
music.play(music.POWER_UP, wait=True)

while True:
  if microbit.button_a.is_pressed():
    makeshow(microbit.Image.GHOST, music.PRELUDE)

  if microbit.button_b.is_pressed():
    makeshow(microbit.Image.SKULL, music.DADADADUM)

  if microbit.pin2.read_analog() > 300:
    makeshow(microbit.Image.UMBRELLA, music.ODE)
