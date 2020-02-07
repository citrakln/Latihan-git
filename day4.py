#Buat segitiga sama kaki dengan masukin input tinggi 
h = int(input("Masukkan tinggi : "))
for i in range (0,h):
    h-=1 #buat spasi
    print((' ')*h+' * '*(i+1))

# versi mas uga
# size = int(input('Size? '))
# for i in range (size) :
#     for j in range (size-i-1) :
#         print(end=" ")
#     for j in range(i+1):
#         print("x",end = " ")
#     print() #buat enter
    

#Buat segitiga  
# 1   3 5   7   9
# 11 13 15 17
# 19 21 23
# 25 27
# 29

# segitiga siku bawahkiri
# size = int(input('Size? '))
# x = 1
# for i in range (0, size+1):#baris
#     for j in range(0, size) : #kolom
#         print(x, end='\t')
#         x +=2
#     size -=1
#     print('')


# segitiga siku atas kiri versi mas uga
# i = 0
# out =""
# num = 1
# while (i<5):
#     j = 0
#     while (j<(5-i)) :
#         out += str(num) +' '
#         if (i == 0):
#             out += ' '
#         num = num +2
#         j +=1
#     i += 1
#     out += '\n'
# print(out)

# i = 0
# out =""
# num = 1
# while (i<5):
#     j = 0
#     while (j<(5-i)) :
#         out += str(num) +' '
#         if (i == 0):
#             out += ' ' #buat pas awal2 aja waktu cuma satu variabel angka
#         num = num +2
#         j +=1
#     i += 1
#     out += '\n'
# print(out)


# # segitiga siku bawah kiri
# size = int(input('Size? '))
# # x = 1
for i in range (0, size):#baris
    for j in range(0, i+1) : #kolom
        print(' x ',end='')
#         # print(x, end='\t')
#         # x +=2
#     print('')