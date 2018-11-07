import time
import requests
import math
import random
import Adafruit_DHT
import RPi.GPIO as GPIO

TOKEN = "A1E-xCkKbIOiXnsFpXyIfp0aM02wBO9Ic4"  # Put your TOKEN here
DEVICE_LABEL = "Museu"  # Put your device label here 
VARIABLE_TEMP = "temp"  # Put your first variable label here
VARIABLE_SMOKE = "smoke"
VARIABLE_R = "R"
VARIABLE_G = "G"
VARIABLE_B = "B"

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

RUNNING = True

# Sensor de temperatura
# Define o tipo de sensor
sensor = Adafruit_DHT.DHT11
pino_sensor = 25

# Sensor de fumaca
pino_fumaca = 32
GPIO.setup(pino_fumaca, GPIO.IN)

# LED RGB
# Definindo os pinos
green = 38
red = 40
blue = 15

# pinos como output
GPIO.setup(red, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)

# definindo uma frequencia
Freq = 100

# pinos como pwm
RED = GPIO.PWM(red, Freq)
GREEN = GPIO.PWM(green, Freq)
BLUE = GPIO.PWM(blue, Freq)

def build_payload(VARIABLE_TEMP, VARIABLE_SMOKE, VARIABLE_R, VARIABLE_G, VARIABLE_B):
    # SENSOR DE TEMPERATURA
    print ("*** Lendo os valores de temperatura e umidade");
    # Efetua a leitura do sensor
    umid, temp = Adafruit_DHT.read_retry(sensor, pino_sensor);

    # SENSOR DE FUMACA
    print ("*** Lendo os valores de fumaca");
    smoke = GPIO.input(pino_fumaca)

    # DEFINE A COR DO LED
    print ("*** Mudando cor do led");
    if (temp <= 24 and smoke):
        # LED VERDE
        redValue = 1
        greenValue = 100
        blueValue = 1
    elif (temp > 24 and smoke):
        # LED AMARELO
        redValue = 100
        greenValue = 100
        blueValue = 1
    else:
        # LED VERMELHO
        redValue = 100
        greenValue = 1
        blueValue = 1

    RED.ChangeDutyCycle(redValue)
    GREEN.ChangeDutyCycle(greenValue)
    BLUE.ChangeDutyCycle(blueValue)
    
    payload = {VARIABLE_TEMP: temp, VARIABLE_SMOKE: smoke, VARIABLE_R: redValue, VARIABLE_G: greenValue, VARIABLE_B: blueValue}

    return payload


def post_request(payload):
    # Creates the headers for the HTTP requests
    url = "http://things.ubidots.com"
    url = "{}/api/v1.6/devices/{}".format(url, DEVICE_LABEL)
    headers = {"X-Auth-Token": TOKEN, "Content-Type": "application/json"}

    # Makes the HTTP requests
    status = 400
    attempts = 0
    while status >= 400 and attempts <= 5:
        req = requests.post(url=url, headers=headers, json=payload)
        status = req.status_code
        attempts += 1
        time.sleep(1)

    # Processes results
    if status >= 400:
        print("[ERROR] Could not send data after 5 attempts, please check \
            your token credentials and internet connection")
        return False

    print("[INFO] request made properly, your device is updated")
    return True

def make_get(url, headers):
    # Makes the HTTP requests
    status = 400
    attempts = 0
    while status >= 400 and attempts <= 5:
        res = requests.get(url=url, headers=headers)
        status = res.status_code
        attempts += 1
        time.sleep(1)

    # Processes results
    if status >= 400:
        print("[ERROR] Could not retrieve data after 5 attempts, please check \
            your token credentials and internet connection")
        return False

    return res.json()

    

def get_led(VARIABLE_R, VARIABLE_G, VARIABLE_B):
    # Creates the headers for the HTTP requests
    url = "http://things.ubidots.com"
    url = "{}/api/v1.6/devices/{}".format(url, DEVICE_LABEL)

    redUrl = "{}/{}/lv".format(url, VARIABLE_R)
    greenUrl = "{}/{}/lv".format(url, VARIABLE_G)
    blueUrl = "{}/{}/lv".format(url, VARIABLE_B)
    
    headers = {"X-Auth-Token": TOKEN, "Content-Type": "application/json"}

    redValue = make_get(redUrl, headers)
    greenValue = make_get(greenUrl, headers)
    blueValue = make_get(blueUrl, headers)

    RED.ChangeDutyCycle(redValue)
    GREEN.ChangeDutyCycle(greenValue)
    BLUE.ChangeDutyCycle(blueValue)
    
    print("[INFO] request made properly, your device is updated")
    return True

def main():
    RED.start(1)
    GREEN.start(1)
    BLUE.start(1)
    
    # Get nas cores do LED
    print("[INFO] Attemping to get data")
    get_led(VARIABLE_R, VARIABLE_G, VARIABLE_B)

    # Medir a temperatura e umidade
    payload = build_payload(VARIABLE_TEMP, VARIABLE_SMOKE, VARIABLE_R, VARIABLE_G, VARIABLE_B)

    # Enviar a temperatura e fumaca
    # Enviar as cores do led
    print("[INFO] Attemping to send data")
    print(payload)
    post_request(payload)
    print("[INFO] finished")
    

try:
    if __name__ == '__main__':
        while (RUNNING):
            main()
            time.sleep(3)
except KeyboardInterrupt:
    RUNNING = False
    GPIO.cleanup()
