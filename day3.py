#If Else
#Assignment Operator
#Logical Operator
#Comparison Operator

# a = 5
# a += 10
# a *= 2
# a /= 10
# a %= 2
# print(a)

# nama = 'Citra'
# nama += ' Kirana'
# print(nama)

# angka = 5
# print(not angka <=5)
# print(angka == 5 or angka < 4) #true

# Comparison operator
# ==
# >=
# <=
# >
# <

#If elif else
# nilai_murid = 80

# if nilai_murid >= 70 :
#     print('Lulus')
# else :
#     print("tidak lulus")

# grade = 2
# if grade >=3.5 :
#     print('Very Satisfactory')
# elif 2.5 <= grade < 3.5:
#     print('Satisfactory')
# else :
#     print('Bad')

#if dalam if
# menu = (input('Pilih menu yang diinginkan \n 1. Belanja \n 2. Belajar \n 3.Exit \n Pilih Menu Nomor : '))
# if(menu.isdigit()==True):
#     if(int(menu)>0 and int(menu)<=3) :
#         check=True
#     else :
#         print('Input salah, Input hanya angka 1 sampai angka 3')
#         print('-----------------------------------------------')
    
# else :
#     print('Input salah, Input hanya angka 1 sampai angka 3')
#     print('-----------------------------------------------')

#While Loop-----------
# angka = 0
# while(angka<=10):
#     print(angka)
#     angka+=1

# angka = 1
# while(angka<=10):
#     print(angka)
#     angka += 1

#For Loop and List
# listItem = list(range(10))
# print(listItem) #mulainya dari 0 tapi bentuknya list dalam satu baris

# listItem = list(range(5,2,-1))
# print(listItem) #keluarnya 5,4,3

# listItem = list(range(1,10,2))
# print(listItem) 

# listItem = [1,2,3,4,5,6,7,8]
# #cara ambil 7
# print(listItem[6])#dari kiri
# #atau
# print(listItem[-2])#dari kanan

# list_makanan =['ayam', 'tahu', 'tempe']
# for makanan in list_makanan :
#     print(makanan) #keluar semua dalam bentuk enter

# for item in list(range(2,10,2)) :
#     print(item) #keluar 2,4,6,8

#Solve bikin nomor urut 1-10
# i = 1
# while (i <= 10) :
#     print (f'Nomor urut {i}')
#     i +=1

# atau
# y = 'Nomor Urut'
# for item in range(1,11):
#     print(y+str(item))

#atau
# for item in list(range(1,11)):
#     print('Nomor Urut ' + str(item))

#For Looping Drawing
#segitiga siku bawah
# out = ''
# for item in list(range(5)): #ngelooping 5 kali 0,1,2,3,4,5
#     out += '*'
#     print(out)

# for i in list(range(5)):
#     for j in list(range(5)):
#         print(i)

# out = ''
# for item in list(range(0,5)): 
#     out += '* \n'
#     print(out)

# for i in list(range(5)):
    # for j in list(range(5)):
    #     print(j)
    # print('--')

# out = ''
# for i in list(range(5)): #iterasi dari kiri ke kanan terus di-enter di looping
#     for j in list(range(5)):
#         out  += '*'
#     out += '\n'
# print(out)

#------------SOLVE1------------------
#segitiga siku atas kanan
# out = ''
# for i in list(range(5,0,-1)): #5,4,3,2,1
#     for j in list(range(0,i)): #iterasi pertama dimulai dari 0 ke 5 ; kedua 0 ke 4
#         out += '*'
#     out  += '\n'
# print(out)

# #------------SOLVE2------------------
# out = ''
# for i in list(range(5,-6,-1)): #5,4,3,2,1
#     for j in list(range(0, abs(i)+1): #iterasi pertama dimulai dari 0 ke 5 ; kedua 0 ke 4
#         out += '*'
#     out  += '\n'
# print(out)