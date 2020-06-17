# import the necessary packages
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

host = "http://netflix.com"

# load the image
print("[INFO] starting video stream...")
vs = VideoStream(src=0).start()
time.sleep(2.0)
print("[INFO] loading network...")
model = load_model("sayur.model")

fps = FPS().start()
while True:
    frame = vs.read()

    # pre-process the image for classification
    image = cv2.resize(frame, (28, 28))
    image = image.astype("float") / 255.0
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)

    
    # classify the input image
    
    (veg) = model.predict(image)[0].copy()
    name = ["Kentang","Kubis","Mentimun","Terung","Tomat","Wortel"]
    veg = veg.tolist()
    probMax = veg.index(max(veg))
    label = name[probMax]
    proba = max(veg)

    label = "{}: {:.2f}%".format(label, proba * 100)

    #Get price
    price = harga.get_harga(name[probMax])
    
    #cek koneksi 
    konek = 'connected' if connection.connect(host) else 'no internet!' 
    
    # draw the label on the image
    output = imutils.resize(frame, width=400)
    cv2.putText(frame, label, (10, 25),  cv2.FONT_HERSHEY_SIMPLEX,
        0.7, (0, 255, 0), 2)
    cv2.putText(frame, "Berat : 6 Kg", (10,50), cv2.FONT_HERSHEY_SIMPLEX, 
        0.7, (0, 255, 0), 2)
    cv2.putText(frame, "Harga : Rp." + str(price), (10,75), cv2.FONT_HERSHEY_SIMPLEX, 
        0.7, (0, 255, 0), 2)
    cv2.putText(frame, konek, (10,100), cv2.FONT_HERSHEY_SIMPLEX, 
        0.7, (0, 255, 0), 2)
    fps.update()

    # show the output image
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF

    # if the `q` key was pressed, break from the loop
    if key == ord("q"):
        break

# stop the timer and display FPS information
fps.stop()
print("[INFO] elasped time: {:.2f}".format(fps.elapsed()))
print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))

# do a bit of cleanup
cv2.destroyAllWindows()
vs.stop()