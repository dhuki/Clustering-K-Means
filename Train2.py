#   NAMA    : DHUKI DWI RACHMAN
#   KELAS   : IF39-13
#   NIM     : 1301154265
#   Percobaan Pertama dengan K = 6

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
book = xlrd.open_workbook("TrainsetTugas2.xlsx")
sh = book.sheet_by_index(0)
for i in range(sh.nrows):
    tempdata = data(sh.cell_value(i, 0), sh.cell_value(i, 1), 0)

    arraydata.append(tempdata)

#===========================================================

#Menampilkan persebaran data pada TrainsetTugas2.xlsx melalu grafik 2D

for i in range(len(arraydata)):
    plt.scatter(arraydata[i].x,arraydata[i].y, marker = 'o', c="red")

plt.show()

#===========================================================


# [ALTERNATIF 1] Mendeklarsikan nilai cluster pertama sesuai dengan data yang optimal yang terlihat dari grafik awal

k1 = data(33,23,0)
k2 = data(33,7,0)
k3 = data(16,7,0)
k4 = data(10,20,0)
k5 = data(23,23,0)
k6 = data(6,3,0)

#===========================================================

# [ALTERNATIF 2] Mendeklarasikan nilai cluster pertama sesuai dengan data ke-random[0 - 687] sebagai awal acuan dari
#nilai cluster yang optimal pada akhirnya

# k1 = data(arraydata[int(random.uniform(0, 687))].x, arraydata[int(random.uniform(0, 687))].y, 0)
# k2 = data(arraydata[int(random.uniform(0, 687))].x, arraydata[int(random.uniform(0, 687))].y, 0)
# k3 = data(arraydata[int(random.uniform(0, 687))].x, arraydata[int(random.uniform(0, 687))].y, 0)
# k4 = data(arraydata[int(random.uniform(0, 687))].x, arraydata[int(random.uniform(0, 687))].y, 0)
# k5 = data(arraydata[int(random.uniform(0, 687))].x, arraydata[int(random.uniform(0, 687))].y, 0)
# k6 = data(arraydata[int(random.uniform(0, 687))].x, arraydata[int(random.uniform(0, 687))].y, 0)

#===========================================================

#Mendeklarasikan variabel - variable yang akan digunakan

#Variabel list yang digunakan untuk menampung sementara tiap data sesuai dengan jarak terdekat ke clusternya

clusterK1 = list()
clusterK2 = list()
clusterK3 = list()
clusterK4 = list()
clusterK5 = list()
clusterK6 = list()

#===========================================================



while 1:

    #Variabel yang digunakan untuk membandingkan perubahan cluster

    Clusterbaru1 = k1
    Clusterbaru2 = k2
    Clusterbaru3 = k3
    Clusterbaru4 = k4
    Clusterbaru5 = k5
    Clusterbaru6 = k6

    #===========================================================

    #Variabel yang digunakan untuk menampung total jumlah attribute x dan y dari masing - masing cluster
    #untuk dicari nilai rata - rata nya sebagai nilai cluster baru
    #Digunakan juga untuk mereset total attribute x dan y dari cluster sebelumnya

    jumlahX1 = 0
    jumlahY1 = 0
    jumlahX2 = 0
    jumlahY2 = 0
    jumlahX3 = 0
    jumlahY3 = 0
    jumlahX4 = 0
    jumlahY4 = 0
    jumlahX5 = 0
    jumlahY5 = 0
    jumlahX6 = 0
    jumlahY6 = 0

    #===========================================================

    #Digunakan untuk mereset isi array cluster menjadi kosong kembali setelah pemakaian cluster sebelumnya
    #untuk menampung data cluster baru lagi

    clusterK1 = []
    clusterK2 = []
    clusterK3 = []
    clusterK4 = []
    clusterK5 = []
    clusterK6 = []

    #===========================================================


    #Perhitungan euclidean/jarak dari 1 titik ke tiap clusternya
    #Jarak yang terkecil dari tiap cluster akan masuk ke clusternya

    for i in range(len(arraydata)):
        tempK1 = math.sqrt((((k1.x - arraydata[i].x) ** 2) + ((k1.y - arraydata[i].y) ** 2)))
        tempK2 = math.sqrt((((k2.x - arraydata[i].x) ** 2) + ((k2.y - arraydata[i].y) ** 2)))
        tempK3 = math.sqrt((((k3.x - arraydata[i].x) ** 2) + ((k3.y - arraydata[i].y) ** 2)))
        tempK4 = math.sqrt((((k4.x - arraydata[i].x) ** 2) + ((k4.y - arraydata[i].y) ** 2)))
        tempK5 = math.sqrt((((k5.x - arraydata[i].x) ** 2) + ((k5.y - arraydata[i].y) ** 2)))
        tempK6 = math.sqrt((((k6.x - arraydata[i].x) ** 2) + ((k6.y - arraydata[i].y) ** 2)))

        temp = min(tempK1, tempK2, tempK3, tempK4, tempK5, tempK6)

        if (temp == tempK1):

            clusterK1.append(data(arraydata[i].x, arraydata[i].y, 1))

            jumlahX1 += k1.x
            jumlahY1 += k1.y

            arraydata[i].cluster = 1

        elif (temp == tempK2):

            clusterK2.append(data(arraydata[i].x, arraydata[i].y, 2))

            jumlahX2 += arraydata[i].x
            jumlahY2 += arraydata[i].y

            arraydata[i].cluster = 2

        elif (temp == tempK3):

            clusterK3.append(data(arraydata[i].x, arraydata[i].y, 3))

            jumlahX3 += arraydata[i].x
            jumlahY3 += arraydata[i].y

            arraydata[i].cluster = 3

        elif (temp == tempK4):

            clusterK4.append(data(arraydata[i].x, arraydata[i].y, 4))

            jumlahX4 += arraydata[i].x
            jumlahY4 += arraydata[i].y

            arraydata[i].cluster = 4

        elif (temp == tempK5):

            clusterK5.append(data(arraydata[i].x, arraydata[i].y, 5))

            jumlahX5 += arraydata[i].x
            jumlahY5 += arraydata[i].y

            arraydata[i].cluster = 5

        elif (temp == tempK6):

            clusterK6.append(data(arraydata[i].x, arraydata[i].y, 6))

            jumlahX6 += arraydata[i].x
            jumlahY6 += arraydata[i].y

            arraydata[i].cluster = 6

        #========================================================================

    #Pembuatan cluster baru dari data yang sebelumnya telah di clustering-kan

    k1 = data(jumlahX1 / len(clusterK1), jumlahY1 / len(clusterK1), 1)
    k2 = data(jumlahX2 / len(clusterK2), jumlahY2 / len(clusterK2), 2)
    k3 = data(jumlahX3 / len(clusterK3), jumlahY3 / len(clusterK3), 3)
    k4 = data(jumlahX4 / len(clusterK4), jumlahY4 / len(clusterK4), 4)
    k5 = data(jumlahX5 / len(clusterK5), jumlahY5 / len(clusterK5), 5)
    k6 = data(jumlahX6 / len(clusterK6), jumlahY6 / len(clusterK6), 6)

    #===========================================================

    #Kondisi jika kluster baru sama dengan kluster lama maka akan keluar dari perulangan

    if (k1 == Clusterbaru1 and k2 == Clusterbaru2 and k3 == Clusterbaru3 and k4 == Clusterbaru4 and
                k5 == Clusterbaru5 and k6 == Clusterbaru6):
        break

    #===========================================================

#Digunakan untuk mengoutputkan cluster yang sudah tidak berubah lagi dari sebelumnya

print "k1 -> x = "+str(k1.x)+" , "+"y = "+str(k1.y)
print "k2 -> x = "+str(k2.x)+" , "+"y = "+str(k2.y)
print "k3 -> x = "+str(k3.x)+" , "+"y = "+str(k3.y)
print "k4 -> x = "+str(k4.x)+" , "+"y = "+str(k4.y)
print "k5 -> x = "+str(k5.x)+" , "+"y = "+str(k5.y)
print "k6 -> x = "+str(k6.x)+" , "+"y = "+str(k6.y)

#===========================================================

#Menghitung sum square error

total = 0

for i in range(6):
    if (i == 1):
        for j in range(len(clusterK1)):
            total += (((k1.x - clusterK1[i].x) ** 2) + ((k1.y - clusterK1[i].y) **2))
    elif (i == 2):
        for j in range(len(clusterK2)):
            total += (((k2.x - clusterK2[i].x) ** 2) + ((k2.y - clusterK2[i].y) **2))
    elif (i == 3):
        for j in range(len(clusterK3)):
            total += (((k3.x - clusterK3[i].x) ** 2) + ((k3.y - clusterK3[i].y) **2))
    elif (i == 4):
        for j in range(len(clusterK4)):
            total += (((k4.x - clusterK4[i].x) ** 2) + ((k4.y - clusterK4[i].y) **2))
    elif (i == 5):
        for j in range(len(clusterK5)):
            total += (((k5.x - clusterK5[i].x) ** 2) + ((k5.y - clusterK5[i].y) **2))
    elif (i == 6):
        for j in range(len(clusterK6)):
            total += (((k6.x - clusterK6[i].x) ** 2) + ((k6.y - clusterK6[i].y) **2))

print "\n" + " total sum square error : " +str(total)

#===========================================================

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


cluster_1 = plt.scatter(x1,y1,color='red')
cluster_2 = plt.scatter(x2,y2,color='blue')
cluster_3 = plt.scatter(x3,y3,color='green')
cluster_4 = plt.scatter(x4,y4,color='black')
cluster_5 = plt.scatter(x5,y5,color='yellow')
cluster_6 = plt.scatter(x6,y6,color='violet')

plt.legend((cluster_1,cluster_2,cluster_3,cluster_4,cluster_5,cluster_6),
           ('cluster 1 ','cluster 2','cluster 3','cluster 4','cluster 5', 'cluster 6'),
           loc='upper center',
           ncol=6,
           fontsize=8,
           bbox_to_anchor=(0.5, -0.05))

plt.show()

#===========================================================


#Memindahkan hasil dari clustering ke file berbentuk .txt

handle = open("TrainTugas2.txt","w")

for i in range(len(arraydata)):
    handle.write(str(arraydata[i].x)+" "+str(arraydata[i].y)+" "+str(arraydata[i].cluster)+"\n")

handle.close

#===========================================================
