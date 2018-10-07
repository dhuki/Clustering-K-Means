#   NAMA    : DHUKI DWI RACHMAN
#   KELAS   : IF39-13
#   NIM     : 1301154265
#   Menggunakan Cluster dengan K = 8

import xlrd
import matplotlib.pyplot as plt
import random
import math


#Membuat class yang berfungsi untuk membuat object yang mempunyai 3 attribute
#yaitu attribute x , y , dan cluster

class data :

    def __init__(self, x, y, cluster):
        self.x = x
        self.y = y
        self.cluster = cluster

    def __eq__(self, other):                                #fungsi untuk membandingkan attribute antar object
        """Override the default Equals behavior"""
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):                                #fungsi untuk membandingkan attribute antar object
        """Override the default Unequal behavior"""
        return self.x != other.x or self.y != other.y

#===========================================================

#Men-convert file excel ke variable list pada program

arraydata = list()
book = xlrd.open_workbook("TestsetTugas2.xlsx")
sh = book.sheet_by_index(0)
for i in range(sh.nrows):
    tempdata = data(sh.cell_value(i, 0), sh.cell_value(i, 1), 0)

    arraydata.append(tempdata)

#===========================================================

#Menampilkan persebaran data pada TestsetTugas2.xlsx melalu grafik 2D

for i in range(len(arraydata)):
    plt.scatter(arraydata[i].x,arraydata[i].y, marker = 'o', c="red")

plt.show()

#===========================================================


#Menggunakan cluster dengan 8 titik sesuai dengan hasil perhitungan yang dianggap paling optimal
#dari beberapa cluster yang ada menurut metode Elbow yang telah dilakukan pada data Train

k1 = data(33, 23 ,1)
k2 = data(33.1079787234, 8.85531914894, 2)
k3 = data(19.3659638554, 6.86957831325, 3)
k4 = data(9.39407894737, 19.9230263158, 4)
k5 = data(21.6230769231, 23.0282051282, 5)
k6 = data(9.44473684211, 4.12368421053, 6)
k7 = data(10.9717105263, 10.4013157895, 7)
k8 = data(9.09436619718, 25.7422535211, 8)

#===========================================================


j = 0

while j != 100 :

    #Perhitungan euclidean/jarak dari 1 titik ke tiap clusternya
    #Jarak yang terkecil dari tiap cluster akan masuk ke clusternya

    for i in range(len(arraydata)):

        tempK1 = math.sqrt((((k1.x - arraydata[i].x) ** 2) + ((k1.y - arraydata[i].y) ** 2)))
        tempK2 = math.sqrt((((k2.x - arraydata[i].x) ** 2) + ((k2.y - arraydata[i].y) ** 2)))
        tempK3 = math.sqrt((((k3.x - arraydata[i].x) ** 2) + ((k3.y - arraydata[i].y) ** 2)))
        tempK4 = math.sqrt((((k4.x - arraydata[i].x) ** 2) + ((k4.y - arraydata[i].y) ** 2)))
        tempK5 = math.sqrt((((k5.x - arraydata[i].x) ** 2) + ((k5.y - arraydata[i].y) ** 2)))
        tempK6 = math.sqrt((((k6.x - arraydata[i].x) ** 2) + ((k6.y - arraydata[i].y) ** 2)))
        tempK7 = math.sqrt((((k7.x - arraydata[i].x) ** 2) + ((k7.y - arraydata[i].y) ** 2)))
        tempK8 = math.sqrt((((k8.x - arraydata[i].x) ** 2) + ((k8.y - arraydata[i].y) ** 2)))

        temp = min(tempK1, tempK2, tempK3, tempK4, tempK5, tempK6, tempK7, tempK8)

        if (temp == tempK1):

            arraydata[i].cluster = 1

        elif (temp == tempK2):

            arraydata[i].cluster = 2

        elif (temp == tempK3):

            arraydata[i].cluster = 3

        elif (temp == tempK4):

            arraydata[i].cluster = 4

        elif (temp == tempK5):

            arraydata[i].cluster = 5

        elif (temp == tempK6):

            arraydata[i].cluster = 6

        elif (temp == tempK7):

            arraydata[i].cluster = 7

        elif (temp == tempK8):

            arraydata[i].cluster = 8

    j += 1

    #========================================================================

#Membuat grafik baru dengan area - area nya bedasarkan warna dari cluster

x1 = list()
y1 = list()

x2 = list()
y2 = list()

x3 = list()
y3 = list()

x4 = list()
y4 = list()

x5 = list()
y5 = list()

x6 = list()
y6 = list()

x7 = list()
y7 = list()

x8 = list()
y8 = list()


for i in range (len(arraydata)):
    if (arraydata[i].cluster == 1):
        x1.append(arraydata[i].x)
        y1.append(arraydata[i].y)
    elif (arraydata[i].cluster == 2):
        x2.append(arraydata[i].x)
        y2.append(arraydata[i].y)
    elif (arraydata[i].cluster == 3):
        x3.append(arraydata[i].x)
        y3.append(arraydata[i].y)
    elif (arraydata[i].cluster == 4):
        x4.append(arraydata[i].x)
        y4.append(arraydata[i].y)
    elif (arraydata[i].cluster == 5):
        x5.append(arraydata[i].x)
        y5.append(arraydata[i].y)
    elif (arraydata[i].cluster == 6):
        x6.append(arraydata[i].x)
        y6.append(arraydata[i].y)
    elif (arraydata[i].cluster == 7):
        x7.append(arraydata[i].x)
        y7.append(arraydata[i].y)
    elif (arraydata[i].cluster == 8):
        x8.append(arraydata[i].x)
        y8.append(arraydata[i].y)

cluster_1 = plt.scatter(x1,y1,color='red')
cluster_2 = plt.scatter(x2,y2,color='blue')
cluster_3 = plt.scatter(x3,y3,color='green')
cluster_4 = plt.scatter(x4,y4,color='black')
cluster_5 = plt.scatter(x5,y5,color='yellow')
cluster_6 = plt.scatter(x6,y6,color='violet')
cluster_7 = plt.scatter(x7,y7,color='brown')
cluster_8 = plt.scatter(x8,y8,color='pink')

plt.legend((cluster_1,cluster_2,cluster_3,cluster_4,cluster_5,cluster_6, cluster_7, cluster_8),
           ('cluster 1 ','cluster 2','cluster 3','cluster 4','cluster 5', 'cluster 6', 'cluster 7', 'cluster 8'),
           loc='upper center',
           ncol=6,
           fontsize=8,
           bbox_to_anchor=(0.5, -0.05))

plt.show()

#===========================================================


#Memindahkan hasil dari clustering ke file berbentuk .txt

handle = open("TestTugas2.txt","w")

for i in range(len(arraydata)):
    handle.write(str(arraydata[i].x)+" "+str(arraydata[i].y)+" "+str(arraydata[i].cluster)+"\n")

handle.close

#===========================================================