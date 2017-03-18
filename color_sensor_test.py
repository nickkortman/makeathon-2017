import TCS34725 as colorSensor
import Adafruit_BBIO.GPIO as gpio
import time
import numpy as np

LED_PIN = "P9_14"

BLUE_THRESHOLD = 0.1

TARGET_COLOR = [0.30, 0.55, 0.78] # Blue tape

gpio.setup(LED_PIN, gpio.OUT)

color_sensor = colorSensor.TCS34725()

while True:
    raw_data = color_sensor.get_raw_data()
    raw_data_np = np.array(raw_data[0:3])
    mag = np.linalg.norm(raw_data_np)
    norm_rd = raw_data_np / mag
    print(norm_rd)
    dist = TARGET_COLOR - norm_rd
    dist_norm = np.linalg.norm(dist)
    print(dist_norm)
    if (dist_norm < BLUE_THRESHOLD):
        gpio.output(LED_PIN, gpio.HIGH)
    else:
        gpio.output(LED_PIN, gpio.LOW)
    time.sleep(0.1)