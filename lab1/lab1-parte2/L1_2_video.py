import time
import numpy as np
import cv2 as cv

cap = cv.VideoCapture('video.mp4')
print("a velocidade é dada de 0 a 10, sendo 5 a velocidade normal.")
velocidade = int(input("digite a velocidade de 1 a 10: "))/5
print("para sair digite Q")
while(cap.isOpened()):
    ret, frame = cap.read()
    
    if ret==True:
        # show the frame
        cv.imshow('frame',frame)

        #wait next frame by 40ms - 25fps
        time.sleep((1/25.0)*(1/velocidade)) 
        
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
               
cap.release()
cv.destroyAllWindows()
