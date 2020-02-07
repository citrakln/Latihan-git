# # Variabel

# # nama ='citra' # string
# # tanggal_lahir = 32 # integer
# # Status = True #Boolean
# # decimal = 3.6 #float

# # print(type(nama))
# # print(type(tanggal_lahir))
# # print(type(Status))
# # print(type(decimal))

# #Operasi Aritmatika

# angka_1 = 5
# angka_2 = 10
# angka_3 = '10'
# angka_4 = '15'

# print(angka_1+angka_2)
# print(angka_1/angka_2)
# print(angka_1*angka_3) #bakal nampilin angka_1 5kali
# print(int(angka_3)+angka_1)
# print(angka_3+str(angka_1)) #bakal nampilin 105
# print(angka_2%angka_1) #sisa bagi yaitu 0

# nama = input("Masukkan nama: ")
# gender = input("Masukkan jenis kelamin")
# #untuk menghasilkan satu baris Nama saya Citra, Perempuan
# print(f'Nama saya {nama}, {gender}')
# # print('Nama saya' + (nama) + (gender))

# IMPORT MATH----------
# import math
# #ceil(bulatin keatas), pow(pangkat), floor(bulatin ke bawah), sqrt
# angka_1 = 5
# angka_2 = 12

# # print(math.ceil(angka_2/angka_1))
# # print(math.floor(angka_2/angka_1))
# # print(math.sqrt(angka_2))
# print(math.pow(angka_2,5))

#Strings-------------
# nama = 'citra! kirana# lestari'
# nama_split = nama.split('!')[1]
# nama_split2 =nama.split('!')[0]
# print(nama_split + nama_split2)

# # print(nama.split('a'))
# # print(nama.split(' '))
# # print(nama.index('a'))
# # print(len(nama))
# # print(nama.lower())
# # print(nama.upper())
# # print(nama.capitalize())

# print(nama.split)

# # STRINGS--------------

# single_quotation = 'anugerah nurhamid'
# double_quotation = "anugerah nurhamid"
# multiple_quotation = "let's go to the jungle"

# print(multiple_quotation)

#EXERCISE 1-----------

# a = 5
# b = 6

# #cara membuat a jadi 6, b jadi  5

# # temp = a #buat temporary
# # a = b
# # b = temp

# #atau 
# a,b = b,a

# print(a)
# print(b)

# #STRING INDEXING--------------
# nama = "I'm Citra K L Nainggolan"
# print(nama[1:5]) #indeks 1 sampai 5
# print(nama[:]) #semua indeks
# print(nama[5:]) #indeks 5 sampai akhir

#MODUL2-----------------------------

#Assignment operators----------------
# UsiaAndi = 40
# UsiaAndi += 2
# print(UsiaAndi)
# UsiaAndi **= 2
# print(UsiaAndi)

# #If else, else if(bisa ditulis elif)---------------------------
# a = 50

# if a>50 : 
#     print('Good')
# else :
#     print('Bad')


#-------------------------------
# a = 60
# if a>=60: 
#     print('Good')
# elif a<60 :
#     print('Bad')
# else :
#     print('Not defined') #kalau bukan integer

#Soal dari Mas Uga--------------------
#Masukkan angka pertama 
#Masukkan angka kedua
#Mau melakukan apa?(*,/,-,+,%)
#hasil angka 1 (*,/,-,+,%) angka 2

# angka1 = input('Angka pertama : ')
# angka2 = input('Angka kedua : ')
# apa = input("mau melakukan apa? (+,-,*,/,%) ")

# if (apa == "+"): 
#     print(int(angka1)+int(angka2))
# elif (apa == "-"): 
#     print(int(angka1)-int(angka2))
# elif (apa == "*"): 
#     print(int(angka1)*int(angka2))
# elif (apa == "/"): 
#     print(int(angka1)/int(angka2))
# elif (apa == "%"): 
#     print(int(angka1)%int(angka2))
# else :
#     print('Unidentified')

#tulis ulang dari modul2
# x = 5
# y = '5'

# print(x == y)
# print(x > int(y))
# print(x >= int(y))
# print(x < int(y))
# print(x <= int(y))

#logical operators lainnya
x = 5
y = '5'
z = 6

print(x==int(y) and int(y)<z)
print(x==int(y) or int(y)<z)
print(not(x==int(y) or int(y)<z))