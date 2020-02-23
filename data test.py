# USAGE
# python test_network.py --model santa_not_santa.model --image images/examples/santa_01.png

# import the necessary packages
from keras.preprocessing.image import img_to_array
from keras.models import load_model
from imutils.video import VideoStream
from imutils.video import FPS
import time
import numpy as np
import argparse
import imutils
import cv2

def sort(array,b):
    # we minus 1 because we are always comparing the current value with the next value
    lengthOfArray = len(array) - 1
    # numbe of rounds will be the total length - 1, for array with length 5, we will do 4 rounds: 0 and 1, 1 and 2, 2 and 3, 3 and 4.
    for i in range(lengthOfArray):
        # at each round, we compare the current j with the next value
        for j in range(lengthOfArray - i):
            # only swap their positions if left value < right value as we aim to move all the small values to the back
            if array[j] < array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                b[j], b[j + 1] = b[j + 1], b[j]

    return array
# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-m", "--model", required=True,
	help="path to trained model model")

args = vars(ap.parse_args())

# load the image
print("[INFO] starting video stream...")
vs = VideoStream(src=0).start()
time.sleep(2.0)
print("[INFO] loading network...")
model = load_model(args["model"])

fps = FPS().start()
while True:
    frame = vs.read()

    # pre-process the image for classification
    image = cv2.resize(frame, (28, 28))
    image = image.astype("float") / 255.0
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)

    # load the trained convolutional neural network
    
    # classify the input image
    #(Chilo, Coccinella, Leptocorisa) = model.predict(image)[0]
    (bug) = model.predict(image)[0].copy()
    name = ["cabbage","carrot","cucumber","potato","tomato"]
    #name = ["Chilo suppressalis","Coccinella septempunctata","Leptocorisa acuta","Mantis sp","Nephotettix virescens","Nilaparvata lugens"]
    # build the label
    sort(bug,name)

    label = name[0]
    proba = bug[0]

    label = "{}: {:.2f}%".format(label, proba * 100)

    # draw the label on the image
    output = imutils.resize(frame, width=400)
    cv2.putText(frame, label, (10, 25),  cv2.FONT_HERSHEY_SIMPLEX,
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