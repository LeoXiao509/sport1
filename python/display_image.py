# -*- coding: utf-8 -*-
"""
Created on Fri May 24 11:00:41 2024

@author: User
"""
import cv2
print(cv2.__version__)
import numpy as np
import matplotlib.pyplot as plt

#Sobel偵測
#THRESH_BINARY_INV ->白底黑描
def Sobel_edge_detection(f):
    gray = cv2.cvtColor(f, cv2.COLOR_BGR2GRAY)
    grad_x = cv2.Sobel(gray, cv2.CV_32F, 1, 0, ksize=3)
    grad_y = cv2.Sobel(gray, cv2.CV_32F, 0, 1, ksize=3)
    
    magnitude = abs(grad_x) + abs(grad_y)
    g = np.uint8(np.clip(magnitude, 0, 255))
    ret, g = cv2.threshold(g, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    
    return g

#影像銳化
def laplacian(h):
    kernel = np.array([[0,-1,0],[-1,5,-1],[0,-1,0]])
    temp = cv2.filter2D(h, cv2.CV_32F,kernel)
    x = np.uint8(np.clip(temp,0,255))
    
    return x

#膨脹
def Dilated(i):
    global dilated
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (10,10))
    dilated = cv2.dilate(i, kernel)
    y = np.uint8(np.clip(dilated,0,255))
    
    return y

#侵蝕
def Eroded(j):
    global eroded
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (10,10))
    eroded = cv2.erode(j,kernel)
    z = np.uint8(np.clip(eroded,0,255))
    
    return z
    
def main():
    img = cv2.imread("Osaka.jpg", -1)
    img_1 = cv2.imread("cat.jpg",-1)
    
    new_width = 500
    new_height = 400
    
    #引用Sobel偵測
    img1 = Sobel_edge_detection(img)
    resized_img = cv2.resize(img1, (new_width, new_height))
    
    #Canny偵測
    img2 = cv2.Canny(img,50,200)
    resized_img1 = cv2.resize(img2,(new_width,new_height))
   
    #引用影像銳化
    img3 = laplacian(img)
    resized_img2 = cv2.resize(img3,(new_width,new_height))
    
    #引用膨脹
    img4 = Dilated(img_1)
    resized_img3 = cv2.resize(img4,(new_width,new_height))
    
    #引用侵蝕
    img5 = Eroded(img_1)
    resized_img4 = cv2.resize(img5,(new_width,new_height))
    
    
    cv2.imshow("Sobel", resized_img)
    cv2.imshow("Canny", resized_img1)
    cv2.imshow("Laplacian",resized_img2)
    cv2.imshow("Dilate",resized_img3)
    cv2.imshow("Erode",resized_img4)
    
    cv2.waitKey(0)
    
    # 關閉所有 OpenCV 窗口
    cv2.destroyAllWindows()
    
main()


