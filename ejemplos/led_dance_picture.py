import microbit
import music
import random

BUTTON_DEBOUNCE_TIME = 200
ROWS = 5
COLS = 5
MAX_BRIGHTNESS = 9
MIN_BRIGHTNESS = 1
SHOW_SLEEP = 1000
FADE_SLEEP = 150
FAST_FADE_TO = 7
FADE_CHANCE = 0.1
SCR = [ [0]*COLS, [0]*COLS, [0]*COLS, [0]*COLS, [0]*COLS ]

MIN_LIGHT_SPEED_FACTOR = 1
MAX_LIGHT_SPEED_FACTOR = 5
LIGHT_SPEED_FACTOR = 1
LIGHT_SPEED_MULTIPLIER = 5
LIGHT_SPEED_STEP = 1

IMAGES = [
  microbit.Image.HEART,
  microbit.Image.HEART_SMALL,
  microbit.Image.HAPPY,
  microbit.Image.SMILE,
  microbit.Image.SAD,
  microbit.Image.CONFUSED,
  microbit.Image.ANGRY,
  microbit.Image.ASLEEP,
  microbit.Image.SURPRISED,
  microbit.Image.SILLY,
  microbit.Image.FABULOUS,
  microbit.Image.MEH,
  microbit.Image.YES,
  microbit.Image.NO,
  microbit.Image.TRIANGLE,
  microbit.Image.TRIANGLE_LEFT,
  microbit.Image.CHESSBOARD,
  microbit.Image.DIAMOND,
  microbit.Image.DIAMOND_SMALL,
  microbit.Image.SQUARE,
  microbit.Image.SQUARE_SMALL,
  microbit.Image.RABBIT,
  microbit.Image.COW,
  microbit.Image.MUSIC_CROTCHET,
  microbit.Image.MUSIC_QUAVER,
  microbit.Image.MUSIC_QUAVERS,
  microbit.Image.PITCHFORK,
  microbit.Image.XMAS,
  microbit.Image.PACMAN,
  microbit.Image.TARGET,
  microbit.Image.TSHIRT,
  microbit.Image.ROLLERSKATE,
  microbit.Image.DUCK,
  microbit.Image.HOUSE,
  microbit.Image.TORTOISE,
  microbit.Image.BUTTERFLY,
  microbit.Image.STICKFIGURE,
  microbit.Image.GHOST,
  microbit.Image.SWORD,
  microbit.Image.GIRAFFE,
  microbit.Image.SKULL,
  microbit.Image.UMBRELLA,
  microbit.Image.SNAKE,
]

TOTAL_IMAGES = len(IMAGES)
MAX_IMAGE = TOTAL_IMAGES-1
CURR_IMAGE = random.randrange(TOTAL_IMAGES)


def read_image():
  for x in range(COLS):
    for y in range(ROWS):
      SCR[y][x] = microbit.display.get_pixel(x, y)


def fade_image():
  sleeptime = SHOW_SLEEP
  while sleeptime:
    microbit.sleep(10)
    sleeptime -= 10
    if check_keys():
      return False

  some_lit = True
  while some_lit:
    if check_keys():
      return False

    some_lit = False
    for x in range(COLS):
      for y in range(ROWS):
        if SCR[y][x]:
          SCR[y][x] = max(SCR[y][x] - 1, MIN_BRIGHTNESS)
          microbit.display.set_pixel(x, y, SCR[y][x])
          if SCR[y][x] > MIN_BRIGHTNESS:
            some_lit = True

    sleeptime = FADE_SLEEP
    while sleeptime:
      microbit.sleep(10)
      sleeptime -= 10
      if check_keys():
        return False

  return True


def check_keys():
  global CURR_IMAGE, LIGHT_SPEED_FACTOR
  up = False
  down = False

  if microbit.button_a.is_pressed():
    microbit.sleep(BUTTON_DEBOUNCE_TIME)
    down = True
  elif microbit.button_b.is_pressed():
    microbit.sleep(BUTTON_DEBOUNCE_TIME)
    up = True
  elif microbit.accelerometer.was_gesture("shake"):
    music.play(music.JUMP_UP, wait=False)
    randomize_image()
    CURR_IMAGE = random.randrange(TOTAL_IMAGES)
    return True
  elif microbit.accelerometer.is_gesture("left"):
    if LIGHT_SPEED_FACTOR < MAX_LIGHT_SPEED_FACTOR:
      LIGHT_SPEED_FACTOR = LIGHT_SPEED_FACTOR+LIGHT_SPEED_STEP
      microbit.display.scroll(str(MAX_LIGHT_SPEED_FACTOR-LIGHT_SPEED_FACTOR+1),delay=50)
      return False
  elif microbit.accelerometer.is_gesture("right"):
    if LIGHT_SPEED_FACTOR > MIN_LIGHT_SPEED_FACTOR:
      LIGHT_SPEED_FACTOR = LIGHT_SPEED_FACTOR-LIGHT_SPEED_STEP
      microbit.display.scroll(str(MAX_LIGHT_SPEED_FACTOR-LIGHT_SPEED_FACTOR+1),delay=50)
      return False


  if down:
    CURR_IMAGE = CURR_IMAGE-1
    if CURR_IMAGE < 0:
      CURR_IMAGE = MAX_IMAGE
    return True
  elif up:
    CURR_IMAGE = CURR_IMAGE+1
    if CURR_IMAGE > MAX_IMAGE:
      CURR_IMAGE = 0
    return True

  return False


def led_dance():
  while True:
    if check_keys():
      return

    rand_row = random.randrange(ROWS)
    rand_col = random.randrange(COLS)
    if SCR[rand_row][rand_col] > 0:
      SCR[rand_row][rand_col] = MAX_BRIGHTNESS
      for x in range(COLS):
        for y in range(ROWS):
          if SCR[y][x]:
            microbit.display.set_pixel(x, y, SCR[y][x])
            if random.random() < FADE_CHANCE or SCR[y][x] > FAST_FADE_TO:
              SCR[y][x] = max(SCR[y][x] - 1, MIN_BRIGHTNESS)

      microbit.sleep(microbit.display.read_light_level() * (LIGHT_SPEED_FACTOR*LIGHT_SPEED_MULTIPLIER))


def show_image():
  ok = False
  while not ok:
    microbit.display.show(IMAGES[CURR_IMAGE])
    read_image()
    ok = fade_image()

def randomize_image():
  for i in IMAGES:
    if random.random() < 0.3:
      microbit.display.show(i)
      microbit.sleep(50)

# -------------------------------------------

music.play(music.POWER_UP, wait=False)

randomize_image()
CURR_IMAGE = 2   # smile

while True:
  show_image()
  led_dance()
