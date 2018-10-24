#extorn ve intorn degerlerini tut.
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
img=mpimg.imread("tct.jpg")
def get_distance(v,w=[1/3,1/3,1/3]):
    a,b,c=v[0],v[1],v[2]
    w1,w2,w3=w[0],w[1],w[2]
    d=((a**2)*w1+(b**2)*w2+(c**2)*w3)**.5
    return d 
my_RGB=[1,2,3]
gray_level=get_distance(my_RGB)
print(gray_level)
my_RGB=[10,20,3]
gray_level=get_distance(my_RGB,[.6,.3,.1])
print(gray_level)
def convert_rgb_to_gray_level(im_1):
    m=im_1.shape[0]
    n=im_1.shape[1]
    im_2=np.zeros((m,n))
    for i in range(m):
        for j in range(n):
            im_2[i,j]=get_distance(im_1[i,j,:])
            
    return im_2
im_2=convert_rgb_to_gray_level(img)
type(im_2)
plt.imshow(im_2,cmap="gray")
plt.show()
def convert_gray_level_to_BW(image_gray_level):
    m=image_gray_level.shape[0]
    n=image_gray_level.shape[1]
    im_bw=np.zeros((m,n))
    for i in range(m):
        for j in range(n):
            if image_gray_level[i,j]>100:
                im_bw[i,j]=1
            else:
                im_bw[i,j]=0
    return im_bw
im_3=convert_gray_level_to_BW(im_2)
plt.subplot(1,3,1),plt.imshow(img)
plt.subplot(1,3,2),plt.imshow(im_2,cmap="gray")
plt.subplot(1,3,3),plt.imshow(im_3,cmap="gray")


def pixel_compenent(img_3):    
    m=img.shape[0]   # black 0  white 1 
    n=img.shape[1]
    external=0
    internal=0
    for i in range (1,m-1):
        for j in range(1,n-1):
            poi=img[i:i+2,j:j+2]
            black=0
            white=0
            for k in range(2):
                for l in range(2):
                    if poi[k][l]==1:
                        black=black+1
                    else:
                        white=white+1
            if(black>white and white>0):
                external=external+1
            elif(white>black and black>0):
                internal=internal+1
                
    print(external)
    print(internal)
