import matplotlib.pyplot as plt
import numpy as np
import random
#soru 1 a nın cevabı
def matris_create_28_by_28with_0_1():
    img = np.zeros((28,28))
    for i in range(28):
        for j in range(28):
            img[i,j] = random.randrange(0,2)
    return(img)
#soru 1 b nin cevabı
plt.imshow(matris_create_28_by_28with_0_1(),plt.cm.gray)
def MBR_create_28_by_28_with_0_1(matris_a):
    m = matris_a.shape[0]
    n = matris_a.shape[1]
    x_min = m
    x_max = 0 #baslangıç değerleri olası en olumsuz durum
    y_min = n
    y_max = 0
    for i in range(m):
        for j in range(n):
            if(matris_a[i,j]==1 and x_min>i):#resim/matris uzerinden
                x_min = i                    #x_min... guncelleniyor
            if(matris_a[i,j]==1 and x_max<i):
                x_min = i
            if(matris_a[i,j]==1 and y_min>j):
                x_min = j
            if(matris_a[i,j]==1 and y_max<j):
                x_min = j
    return(x_min,x_max,y_min,y_max)
print(MBR_create_28_by_28_with_0_1(matris_create_28_by_28with_0_1()))
#birinci soru c nin cevabı
def get_similarity(character_a,character_b):
    m= character_a.shape[0]
    n = character_a.shape[1]
    my_similarity = 0
    for i in range(m):
        for j in range(n):
            my_similarity = my_similarity + character_a[i,j] * character_b[i,j]
    return my_similarity
c_1 = matris_create_28_by_28with_0_1()
c_2 = matris_create_28_by_28with_0_1()
get_similarity(c_1,c_2)

#d nin cevabı
def get_similarty_for_100_characters(kac_karakter=100):
    characters = []
    for i in range(kac_karakter):
        new_char = matris_create_28_by_28with_0_1()
        characters.append(new_char)
    for i in range(kac_karakter):
        benzerlik =get_similarity(characters[0],characters[i])
        print("0 -- "+str(i)+" --- ",benzerlik)
    return my_similarity
get_similarty_for_100_characters()
