import ASUS.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.ASUS)

GPIO.setup(252,GPIO.OUT)
GPIO.setup(253,GPIO.OUT)
GPIO.setup(164,GPIO.OUT)
GPIO.setup(166,GPIO.OUT)
GPIO.setup(167,GPIO.OUT)
GPIO.setup(257,GPIO.OUT)
GPIO.setup(256,GPIO.OUT)
GPIO.setup(254,GPIO.OUT)
GPIO.setup(165,GPIO.OUT)
GPIO.setup(168,GPIO.OUT)
GPIO.setup(238,GPIO.OUT)
GPIO.setup(185,GPIO.OUT)
GPIO.setup(224,GPIO.OUT)

GPIO.setup(161,GPIO.OUT)
GPIO.setup(160,GPIO.OUT)
GPIO.setup(184,GPIO.OUT)
GPIO.setup(162,GPIO.OUT)
GPIO.setup(163,GPIO.OUT)
GPIO.setup(171,GPIO.OUT)
GPIO.setup(255,GPIO.OUT)
GPIO.setup(251,GPIO.OUT)
GPIO.setup(239,GPIO.OUT)
GPIO.setup(223,GPIO.OUT)
GPIO.setup(187,GPIO.OUT)
GPIO.setup(188,GPIO.OUT)

try:
    while True:
        #open led
        print("open led")
        GPIO.output(252,GPIO.HIGH)
        GPIO.output(253,GPIO.HIGH)
        GPIO.output(164,GPIO.HIGH)
        GPIO.output(166,GPIO.HIGH)
        GPIO.output(167,GPIO.HIGH)
        GPIO.output(257,GPIO.HIGH)
        GPIO.output(256,GPIO.HIGH)
        GPIO.output(254,GPIO.HIGH)
        GPIO.output(165,GPIO.HIGH)
        GPIO.output(168,GPIO.HIGH)
        GPIO.output(238,GPIO.HIGH)
        GPIO.output(185,GPIO.HIGH)
        GPIO.output(224,GPIO.HIGH)

        GPIO.output(161,GPIO.HIGH)
        GPIO.output(160,GPIO.HIGH)
        GPIO.output(184,GPIO.HIGH)
        GPIO.output(162,GPIO.HIGH)
        GPIO.output(163,GPIO.HIGH)
        GPIO.output(171,GPIO.HIGH)
        GPIO.output(255,GPIO.HIGH)
        GPIO.output(251,GPIO.HIGH)
        GPIO.output(239,GPIO.HIGH)
        GPIO.output(223,GPIO.HIGH)
        GPIO.output(187,GPIO.HIGH)
        GPIO.output(188,GPIO.HIGH)
        time.sleep(0.3)  # 500ms
        # close led
        print("close led")
        GPIO.output(252,GPIO.LOW)
        GPIO.output(253,GPIO.LOW)
        GPIO.output(164,GPIO.LOW)
        GPIO.output(166,GPIO.LOW)
        GPIO.output(167,GPIO.LOW)
        GPIO.output(257,GPIO.LOW)
        GPIO.output(256,GPIO.LOW)
        GPIO.output(254,GPIO.LOW)
        GPIO.output(165,GPIO.LOW)
        GPIO.output(168,GPIO.LOW)
        GPIO.output(238,GPIO.LOW)
        GPIO.output(185,GPIO.LOW)
        GPIO.output(224,GPIO.LOW)

        GPIO.output(161,GPIO.LOW)
        GPIO.output(160,GPIO.LOW)
        GPIO.output(184,GPIO.LOW)
        GPIO.output(162,GPIO.LOW)
        GPIO.output(163,GPIO.LOW)
        GPIO.output(171,GPIO.LOW)
        GPIO.output(255,GPIO.LOW)
        GPIO.output(251,GPIO.LOW)
        GPIO.output(239,GPIO.LOW)
        GPIO.output(223,GPIO.LOW)
        GPIO.output(187,GPIO.LOW)
        GPIO.output(188,GPIO.LOW)
        time.sleep(0.3)  # 500ms
except KeyboardInterrupt:
    GPIO.cleanup()
