'''
Demostración práctica de que MicroPython es MUCHO más rápido
 que el editor de bloques JavaScript de Microsoft
'''

'''
Código equivalente en JavaScript blocks
https://makecode.microbit.org/#editor
Resultado: 24ms/iteración (41 it/s)

let count = 0
let elapsed = 0
basic.showIcon(IconNames.Skull)
let lastmillis = control.millis()

basic.forever(function () {
    elapsed = control.millis() - lastmillis
    if (elapsed > 10000) {
        basic.showNumber(Math.round(elapsed/count))
        count = 0
        lastmillis = control.millis()
    } else {
        count += 1
    }
})
'''

'''
Versión MicroPython
Resultado: 0.3ms/iteración (3333 it/s) => 80 VECES MÁS RÁPIDO
'''
import microbit

count = 0
elapsed = 0
microbit.display.show(microbit.Image.SKULL)
lastmillis = microbit.running_time()

while True:
  elapsed = microbit.running_time() - lastmillis
  if elapsed > 10000:
    microbit.display.show(round(elapsed/count, 1))
    count = 0
    lastmillis = microbit.running_time()
  else:
    count += 1
