import tkinter as tk
from tkinter import simpledialog
import os



n = 0
name = ""
def set_class():
    ROOT = tk.Tk()
    ROOT.withdraw()
    name = simpledialog.askstring(title="Get Class nema",
                                  prompt="Masukan Jenis Sayur:")
    n = 0
    os.mkdir(name)
    return name,n
# the input dialog
# check it out
import cv2 
name,n = set_class()
key = cv2. waitKey(1)
webcam = cv2.VideoCapture(0)

while True:
    try:
        check, frame = webcam.read()
        print(check) #prints true as long as the webcam is running
        print(frame) #prints matrix values of each framecd 
        cv2.imshow("Capturing", frame)
        key = cv2.waitKey(1)
        if key == ord('s'): 
            
            cv2.imwrite(filename=name+"/"+name + "-"+ str(n)+".jpg", img=frame)
            #cv2.imwrite(name+'.jpg', img=frame)
            n += 1
            
        elif key == ord('q'):
            print("Turning off camera.")
            webcam.release()
            print("Camera off.")
            print("Program ended.")
            cv2.destroyAllWindows()
            break
        elif key == ord('n'):
            name,n = set_class()
    except(KeyboardInterrupt):
        print("Turning off camera.")
        webcam.release()
        print("Camera off.")
        print("Program ended.")
        cv2.destroyAllWindows()
        break
    