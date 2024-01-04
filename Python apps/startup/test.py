
# importing libraries
import cv2
import numpy as np
window = "window"
# Create a VideoCapture object and read from input file
cap = cv2.VideoCapture('SRS.mp4')
cv2.namedWindow(window, cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty(window, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
cv2.resizeWindow(window, 1600, 900)
# Check if camera opened successfully
if (cap.isOpened()== False):
    print("Error opening video file")
 
# Read until video is completed
while(cap.isOpened()):
     
# Capture frame-by-frame
    ret, frame = cap.read()
    if ret == True:
    # Display the resulting frame
        cv2.imshow('window', frame)
         
    # Press Q on keyboard to exit
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
 
# Break the loop
    else:
        break
 
# When everything done, release
# the video capture object
cap.release()
 
# Closes all the frames
cv2.destroyAllWindows()