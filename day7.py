# def hello() :
#     print('Hello')

# def function():
#     return[1,2,hello] 
# #print tidak memiliki value karena langsung excecute print
# #return menghasilkan sebuah value dimana value tersebut dapat dipanggil kapanpun
# #cara ngambil list hello di function
# function()[2]() #jadi function()[2] itu nunjukin indexnya, () yang terakhir buat nge excecute

#IMPORTANT from list
#Cara ambil dari sebuah list, cara mengganti list, setelah diganti lalu diambil sebuah list
#function harus diexcecute setelah def

# #Matrix 2 dimensi
# produk = [
#     ['Jeruk',2000],
#     ['Apel',3000],
#     ['Pear',4000]
# ]
# print(produk[2][1]) #Hasilnya ambil index 2 dari 2 jadinya 4000
#----------------------------------------------------------------------------------------------------------------
# produk = [
#     ['Jeruk',2000],
#     ['Apel',3000],
#     ['Pear',4000]
# ]
# cart = [
#     [0,3],
#     [1,4],
#     [2,5]
# ]
#proses pengambilan produk untuk dikalikan dengan cart jadi index 0 dikali 3, index 1 dikali 4 index 2 dikali 5
# out =""
# for i in range (len(cart)) :
#     index = cart[i][0] #untuk ngambil 0,1,2
#     out += str(i+1) + '. ' + produk[index][0]+ ' Rp ' + str(produk[index][1]) + ' dikali '+ str(cart[i][1]) + ' =  Rp ' + str((produk[i][1])*(cart[i][1])) + '\n'
# print(out)
#----------------------------------------------------------------------------------------------------------------
# Hasilnya :
# 1. Jeruk Rp 2000 dikali 3 =  Rp 6000
# 2. Apel Rp 3000 dikali 4 =  Rp 12000
# 3. Pear Rp 4000 dikali 5 =  Rp 20000

#yang diatas si index sebenernya buat ngambil i jadi ga pake index gpp
# out =""
# for i in range (len(cart)) :
#     out += str(i+1) + '. ' + produk[i][0]+ ' Rp ' + str(produk[i][1]) + ' dikali '+ str(cart[i][1]) + ' =  Rp ' + str((produk[i][1])*(cart[i][1])) + '\n'
# print(out)
#----------------------------------------------------------------------------------------------------------------
# Hasilnya :
# 1. Jeruk Rp 2000 dikali 3 =  Rp 6000
# 2. Apel Rp 3000 dikali 4 =  Rp 12000
# 3. Pear Rp 4000 dikali 5 =  Rp 20000

#Dictionary
# penulisannya harus kurung kurawal {}, bisa dubah2, indexing/indexed(bisa ngakses ke indexnya langsung)
# {}, changeable, indexing/indexed
# have key and value
#-----------------------------------------------------------------------------
# nama = {
#     'depan' : 'Citra', #Key1 dan Value1
#     'belakang' : 'Kirana' #Key2 dan Value2
# }
# #gimana caranya manggil anugrah
# print(nama ['depan']) #hasilnya Citra
# print(nama['belakang']) #hasilnya Kirana

# #cara ubahnya sama kaya list
# nama['depan'] = 'anugerah' #bedanya sama list yang dipanggil bukan index tapi key nya
# print(nama['depan']) #print nya berubah jadi anugerah
# print(nama) #print {'depan': 'anugerah', 'belakang': 'Kirana'}
# print(nama['depan','belakang'])
#-----------------------------------------------------------------------------

#TUPPLE
#unchangeable, () kurung biasa

# variable_tuple = (1,2,3,4,5,6,9,8)
# # print(type(variable_tuple)) #masuk ke kelas tupple dan tupple ga bisa diubah sama sekali
# a = ('citra', [1,True], {'nama' : 'Citra'})
# #cara ngeprint True
# print(a[1][1])
# #cara ngeprint False
# a[1][1] = False #index pertama dari list yang adalah True diganti dengan False
# print(a) #hasil list di dalam tupple akan berubah
# #hasil print nya : ('citra', [1, False], {'nama': 'Citra'})
# a[1].append('Kya') #nambahin list di tupple
# print(a) 
# #hasil print nya : ('citra', [1, False, 'Kya'], {'nama': 'Citra'})
# a[2]['nama'] = 'Kyaa'# buat ngeubah 'Citra' jadi 'Kyaa'
# print(a)
#hasilnya ('citra', [1, False, 'Kya'], {'nama': 'Kyaa'})
#-----------------------------------------------------------------------------
#SETS
#Unique, ga ad duplicate
#Sama2 kurung kurawal tapi langsung value ga ada key
# ini_set = {'apel','jeruk','mangga'}
# print(type(ini_set))

# #buat ngeprint item
# for item in ini_set :
#     print(item)
# #hasilnya
# # mangga
# # apel
# # jeruk

# print('pisang' in ini_set) #False
# #nambahin set
# ini_set.add('pisang')
# ini_set.add('mangga')
#print(ini_set)
# hasilnya random {'mangga', 'apel', 'pisang', 'jeruk'}
#-----------------------------------------------------------------------------
#LIST COMPREHENSION
# list_num = [1,2,3,4,5]
# list_num = [item * 2 for item in list_num] #bacanya for item in list_num, itemnya bakal dikali 2
# print(list_num)
# Hasilnya :
# [2, 4, 6, 8, 10]

# def perkalian(num) :
#     return num*3
# list_num = [1,2,3,4,5]
# list_num = [perkalian(item) for item in list_num]#jai pertamanya kita nulis algoritma for blablabla baru depannya dipangiil functionnya
# print(list_num)
# # Hasilnya :
# [3, 6, 9, 12, 15]
#-----------------------------------------------------------------------------
#LAMBDA COMPREHENSION
# lambda adalah baris kode untuk memanggil function yang simpel
# def perkalian(number) :
#     return number *2
# x = lambda number: number*2 #nulis kondisi dulu number: number*2
# print(x(5))
#hasilnya 10

#Penulisan function
# def perkalian(a,b):
#     return a*b
# print(perkalian(3,4))
# Hasilnya 12

#Penulisan lambda
# x = lambda a,b : a*b
# print(x(3,4))
# Hasilnya 12

# def function(n) :
#     return lambda a : a*n
# dikali2 = function(2)
# print(dikali2(11))
# Hasilnya 22

#FizzBuzz
# Kelipatan3 Fizz
# Kelipatan 5 Buzz
# Kelipatan 3 dan 5, KPK nya FizzBuzz
# def fizzBuzz (num) :
#     for i in range( 1 ,num+1 ):
#         if ( i % 15 == 0 ) :
#             print('FizzBuzz')
#         elif (i % 3 == 0 ) :
#             print('Fizz')
#         elif (i % 5 == 0 ) :
#             print('Buzz')
#         else :
#             print(i)

# fizzBuzz(20)
# -----------------------------------------------------
#Fibonacci
#bisa buat gambling, saham buat nentuin pattern trading
# barisan ini berawal dari 0 dan 1, kemudian angka berikutnya didapat dengan cara menambahkan kedua bilangan yang berurutan sebelumnya.
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946...
# def fibo(urut):
#     listData = [1,1] #ngedefine dulu 2 angka pertama
#     for i in range(2,urut):
#         listData.append(listData[i-2] + listData[i-1])
#     return listData[urut-1]
# print(fibo(8))

# -----------------------------------------------------
# # import math 
# def reverseList(theList) :
#     for i in range( 0 , math.floor(len(theList)/2)) : #math floor angka dibulatin ke bawah
#         tempList = theList[i]
#         theList[i] = theList [len(theList)-1-i]
#         theList[len(theList) - 1 - i ] = tempList
#     return theList
# print(reverseList([1,2,3,4,5,6,7,8]))

# -----------------------------------------------------
#BUBBLESORT
# karena buih air 
#bubble karena ada pindah dari bawah ke atas

#SORT list from small to large number
# x = [20,40,10,50]
# def bubbleSort (list) :
#     for i in range(len(list), 0 , -1) :
#         for j in range(0 ,i-1) :
#             if (list [j] > list [j + 1 ]) :
#                 temp = list [j]
#                 list[j] = list [j + 1]
#                 list[j + 1] = temp
#     return list
# print(bubbleSort(x))
# -----------------------------------------------------
# MEAN
#itu rata2
# x = [10,20,30,40]
# def getMean(list) :
#     sum = 0
#     for item in list: #buat ngejumlahin semua nilai yg ada di List
#         sum += item
#     mean = sum / len(list) #sum list dibagi sama jumlah data nya
#     return mean
# print(getMean(x))
# # -----------------------------------------------------
# # MEDIA
# #itu nilai tengah setelah diurutin
# x = [1 2 3 2 5 2 7 2]
# def getMedian (list)
#     list.sort () #ngurutin dulu dari bawah 
#     median = 0 
#     if (len(list) % 2 != 0 ) : #!= bacanya tidak sama dengan nol
#         median = list[floor(len (list) / 2)]
#     else :
#         mid1 = list[(int(len(list)/2))-1]
#         mid2 = list[(int(len(list)/2))1]
#     median = (mid1 + mid2) /2
#     return median
# print(getMedian (x))

# # -----------------------------------------------------
# x = [1,2,3,2,5,2,7,2]
# def getMode(list):
#     countList = [] #berapa banyak misalnya berapa banyak angka 1 berapa banyak angka 2,dst
#     for num in list :
#         check = False
#         for list1 in countList :
#             if (list1[0] == num) :
#                 list1[1] += 1
#                 check = True
#         if (check == False) :
#             countList.append([num,0])

#     maxFrequency = 0
#     modes =[]
#     for list1 in countList :
#         if (list1[1]>maxFrequency) :
#             modes = [list1[0]]
#             maxFrequency = list1[1]
#         elif(list1[1]== maxFrequency):
#             modes.append(list1[0])
#     if((len(modes)==len(countList))) :
#         modes = []
#     return modes

# print(getMode(x))
