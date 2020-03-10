import cv2
import numpy as np
from matplotlib import pyplot as plt
import time
# import auxiliar as aux
import math


def ponto_fuga (p1, p2, q1, q2):
    m1 = (p2[1]-p1[1])/(p2[0]-p1[0])
    m2 = (q2[1]-q1[1])/(q2[0]-q1[0])
    h1 = p1[1] - m1*p1[0]
    h2 = q1[1] - m2*q1[0]
    
    x_fuga = (h2-h1)/(m1-m2)
    y_fuga = m1*x_fuga +h1
    
    return (x_fuga, y_fuga)


cap = cv2.VideoCapture("v1.mp4")


while(True):


    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    array0 = np.array(250)
    array1 = np.array(255)
    mask = cv2.inRange(gray, array0, array1)  


    tela = cv2.bitwise_and(gray,gray,mask=mask)

    print(tela.shape)

    # a,b,c = tela.shape

    hough_img_rgb2 = cv2.cvtColor(tela, cv2.COLOR_GRAY2BGR)
    min = 100
    max = 200
    frame2 = cv2.Canny(hough_img_rgb2, min, max)

    # a,b,c = tela.shape

    # for i in range(a):
    #     # Faz uma linha ligando o ponto inicial ao ponto final, com a cor vermelha (BGR)
    #     cv2.line(hough_img_rgb2, (lines[i][0][0], lines[i][0][1]), (lines[i][0][2], lines[i][0][3]), (0, 0, 255), 5, cv2.LINE_AA)


    cv2.imshow("video", frame2 )

    

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
