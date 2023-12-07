from flask import Flask
import socket
import RPi.GPIO as GPIO
import time
import pygame
GPIO.setwarnings(False)
      
app = Flask(__name__)

@app.route('/')
def hello():
    GPIO.output(motor1, False)
    GPIO.output(motor2, True)
    time.sleep(2)
    GPIO.output(motor1, False)
    GPIO.output(motor2, False)
    return "hello"

@app.route('/vibration')
def vibration():
    return "vibration"

@app.route('/speaker')
def speaker():
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue
    return "speaker"
           

if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM)
    motor1 = 14
    motor2 = 15
    
    GPIO.setup(motor1, GPIO.OUT)
    GPIO.setup(motor2, GPIO.OUT)
    
    pygame.mixer.init()
    pygame.mixer.music.load("/home/raspberrypi/Junee/ALERT.wav")
    app.run(host = "192.168.211.38", port = 9999, debug = True)
