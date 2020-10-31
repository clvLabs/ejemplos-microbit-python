'''
micro:bit puede hablar!
'''

import microbit
import speech

MENSAJE1 = "HELLO"
MENSAJE2 = "MY NAME IS MICRO BIT"


def enciende_farol():
  microbit.pin2.write_digital(1)

def apaga_farol():
  microbit.pin2.write_digital(0)


def ejemplo(sonido):
  enciende_farol()
  microbit.display.show(microbit.Image.GHOST)
  speech.say(sonido, speed=100, mouth=200)
  microbit.display.show(microbit.Image.HAPPY)
  apaga_farol()



def canta():
  enciende_farol()
  microbit.display.show(microbit.Image.MUSIC_QUAVERS)

  # The say method attempts to convert English into phonemes.
  speech.say("Puedo cantar!")
  microbit.sleep(1000)
  speech.say("Escuchame!")
  microbit.sleep(1000)

  # Clearing the throat requires the use of phonemes. Changing
  # the pitch and speed also helps create the right effect.
  speech.pronounce("AEAE/HAEMM", pitch=200, speed=100)  # Ahem
  microbit.sleep(1000)

  # Singing requires a phoneme with an annotated pitch for each syllable.
  solfa = [
      "#115DOWWWWWW",   # Doh
      "#103REYYYYYY",   # Re
      "#94MIYYYYYY",    # Mi
      "#88FAOAOAOAOR",  # Fa
      "#78SOHWWWWW",    # Soh
      "#70LAOAOAOAOR",  # La
      "#62TIYYYYYY",    # Ti
      "#58DOWWWWWW",    # Doh
  ]

  # Sing the scale ascending in pitch.
  song = ''.join(solfa)
  speech.sing(song, speed=100)
  # Reverse the list of syllables.
  solfa.reverse()
  song = ''.join(solfa)
  # Sing the scale descending in pitch.
  speech.sing(song, speed=100)

  microbit.display.show(microbit.Image.HAPPY)
  apaga_farol()

# ---------------------------------------------------------------

microbit.display.show(microbit.Image.HAPPY)

while True:

  if microbit.accelerometer.was_gesture("shake"):
    canta()
  elif microbit.button_a.was_pressed():
    ejemplo(MENSAJE1)
  elif microbit.button_b.was_pressed():
    ejemplo(MENSAJE2)

