import matplotlib.pyplot as plt
import numpy as np
img_1=plt.imread("image.jpg")

def my_function_1(img_1):
    
    en_fazla = 0
    en_az = 0

    en_fazla = (img_1[:,:,0].max())
    en_az = (img_1[:,:,0].min())
    dimention = (img_1.ndim)
    shape=(img_1.shape)
    print("Dimention degeri =",dimention)
    print("Shape degeri = ",shape)
    print("En buyuk deger =",en_fazla)
    print("En kucuk deger =",en_az)
my_function_1(img_1)    