import smbus
from max30105 import MAX30105, HeartRate
import gpiod
import time
import multiprocessing as mp

red = 0
green  = 0
blue = 0
max30105 = 0
buzz = 0
p=0
q=0

def display_heartrate(beat, bpm, avg_bpm):
    global q
    print("{} BPM: {:.2f}  AVG: {:.2f}".format("<3" if beat else "  ",
          bpm, avg_bpm))
    manage_leds(beat, bpm, avg_bpm)
    q.put([beat, bpm])

    display_temp()

def manage_leds(beat, bpm, avg_bpm):
    global red, green, blue
    if ((bpm <50 and bpm > 10) or bpm > 130):
        blue.set_values([1])
        red.set_values([0])
        green.set_values([0])
    if bpm >= 50 and bpm <= 130:
        blue.set_values([0])
        red.set_values([1])
        green.set_values([0])
    if bpm <= 10:
        blue.set_values([0])
        red.set_values([0])
        green.set_values([1])

def manage_buzzer(q):
    global buzz
    tm = 0.3
    while True:
        beat, bpm = q.get()
        if beat:
            if ((bpm <50 and bpm > 10) or bpm > 130):
                freq = 900
            elif bpm >= 50 and bpm <= 130:
                freq = 1200
            elif bpm <= 10:
                freq = 600
            for i in range(int(tm * freq)):
                buzz.set_values([1])
                buzz.set_values([0])
                time.sleep(1/freq)

def display_temp():
    global max30105
    print("   Temperature: ", max30105.get_temperature(), " *C")

def set_slot_mode(max30105):
    max30105._max30105.set('LED_MODE_CONTROL', slot1='red')
    max30105._max30105.set('LED_MODE_CONTROL', slot2='ir')
    max30105._max30105.set('LED_MODE_CONTROL', slot3='green')
    max30105._max30105.set('LED_MODE_CONTROL', slot4='off')

def main():
    global red, green, blue, max30105, buzz, p, q

    # chip = gpiod.Chip('gpiochip0')
    

    max30105 = MAX30105()
    max30105.setup(leds_enable=2)

    max30105.set_led_pulse_amplitude(1, 0.2)
    max30105.set_led_pulse_amplitude(2, 12.5)
    max30105.set_led_pulse_amplitude(3, 0)

    set_slot_mode(max30105)

    # # max30105.set_slot_mode(1, 'red')
    # max30105.set_slot_mode(2, 'ir')
    # max30105.set_slot_mode(3, 'off')
    # max30105.set_slot_mode(4, 'off')

    chip = gpiod.chip('gpiochip0')


    config = gpiod.line_request()
    config.consumer = "foobar"
    config.request_type = gpiod.line_request.DIRECTION_OUTPUT

    red = chip.get_lines([16]) # zdrowe
    red.request(config)

    green = chip.get_lines([21]) # smierc
    green.request(config)

    blue = chip.get_lines([20]) # niezdrowe
    blue.request(config)

    buzz = chip.get_lines([23]) # ping
    buzz.request(config)

    # buzz.set_values([1]) # TODO przeniesc do watku???
    # time.sleep(1)
    # buzz.set_values([0])

    hr = HeartRate(max30105)

    q = mp.Queue()
    p = mp.Process(target = manage_buzzer, args = (q, ))
    p.start()

    delay = 10

    # print("Starting readings in {} seconds...\n".format(delay))
    # time.sleep(delay)

    try:
        hr.on_beat(display_heartrate, average_over=4)
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    main()
    print("o tam byczq???")
