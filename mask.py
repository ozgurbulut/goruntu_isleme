import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
img=mpimg.imread("image.jpg")
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


plt.subplot(1,3,1),plt.imshow(img)
plt.subplot(1,3,2),plt.imshow(im_2,cmap="gray")

def get_default_mask_for_mean():
    #ortalamayı bulduracak
    return np.array([1,1,1,1,1,1,1,1,1]).reshape(3,3)/9    
def apply_msk(part_of_image):
    mask = get_default_mask_for_mean()
    return sum(sum(part_of_image*mask))
def get_mean_filter(img1):

    #img1 = plt.imread("image.jpg")
    #img2 = np.zeros((m,n))
    m = img1.shape[0]
    n = img1.shape[1]
    img2=np.zeros((m,n))
    for i in range(1,m-1):
        for j in range(1,n-1):
            poi =img1[i-1:i+2,j-1:j+2]
            img2[i,j] = apply_msk(poi)
    return img2


img3= get_mean_filter(im_2)
plt.imshow(im_2)
plt.imshow(img3,cmap="gray")
