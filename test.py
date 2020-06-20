import lcddriver
from time import *
 
lcd = lcddriver.lcd()
lcd.lcd_clear()
 
import time
import sys
from keras.preprocessing.image import img_to_array
from keras.models import load_model
from imutils.video import VideoStream
from imutils.video import FPS
import time
import numpy as np
import connection
import get_hargadb as harga
import imutils
import cv2


EMULATE_HX711=False

referenceUnit = -447

if not EMULATE_HX711:
    import RPi.GPIO as GPIO
    from hx711 import HX711
else:
    from emulated_hx711 import HX711

def cleanAndExit():
    print("Cleaning...")
    
    if not EMULATE_HX711:
        GPIO.cleanup()
    break
    fps.stop()
    print("[INFO] elasped time: {:.2f}".format(fps.elapsed()))
    print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))

    # do a bit of cleanup
    cv2.destroyAllWindows()
    vs.stop()
    print("Bye!")
    sys.exit()

hx = HX711(5, 6)


hx.set_reading_format("MSB", "MSB")


hx.set_reference_unit(referenceUnit)

hx.reset()

hx.tare()
print("[INFO] starting video stream...")
vs = VideoStream(src=0).start()
time.sleep(2.0)
print("[INFO] loading network...")
model = load_model("sayur.model")

fps = FPS().start()

print("Tare done! Add weight now...")

harga = 6000
while True:
    try:
        frame = vs.read()

        # pre-process the image for classification
        image = cv2.resize(frame, (28, 28))
        image = image.astype("float") / 255.0
        image = img_to_array(image)
        image = np.expand_dims(image, axis=0)

        val = hx.get_weight(5)
        print(val)
        (veg) = model.predict(image)[0].copy()
        name = ["Kentang","Kubis","Mentimun","Terung","Tomat","Wortel"]
        veg = veg.tolist()
        probMax = veg.index(max(veg))
        label = name[probMax]
        proba = max(veg)

        label = "{}: {:.2f}%".format(label, proba * 100)

        #Get price
        price = harga.get_harga(name[probMax])
    

        lcd.lcd_display_string("Berat : "+str(int(val))+" g           ", 1)
        lcd.lcd_display_string("Jenis Sayur : " + label, 2)
        lcd.lcd_display_string("Harga/kg : Rp. " + str(price)+ "      ", 3)
        lcd.lcd_display_string("Total : Rp."+str(harga*int(harga)/1000) + "    ", 4)


        hx.power_down()
        hx.power_up()
        time.sleep(0.1)
        fps.update()

        # show the output image
        cv2.imshow("Frame", frame)
    except (KeyboardInterrupt, SystemExit):
        cleanAndExit()
