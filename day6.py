
#nomor 1 HW 4 versi mas uga
# duplicate_string
# def duplicate_string(text) :
#     out = ''
#     for i in range (len(text)):
#         for j in range (i+1) : #biar muncul string pertamanya kan semuanya dimulai dari nol
#             out += text[i]
#             j += 1
#     print(out)
# hasilnya :
# ciitttrrrraaaaa

# duplicate_string('citra')

# nomor 1 klo kita input nya ada huruf besar huruf kecil
# def duplicate_string(text) :
#     out = ''
#     lower_text = text.lower()
#     for i in range (len(lower_text)):
#         for j in range (i+1) : #biar muncul string pertamanya kan semuanya dimulai dari nol
#             out += lower_text[i]        
#     print(out)
# duplicate_string('cItRa')
# hasilnya :
# ciitttrrrraaaaa

#nomor 2 duplicate string strip
# text = 'citra'
# out =  ''
# for i in range (len(text)) :
#     for j in range (i+1):
#         if j==0 :
#             out += '-'
#             out += text[i].upper()
#         else :
#             out  += text[i]
#     print(out)text = 'citra'


# def duplicate_string_strip(text):
#     out =  ''
#     for i in range (len(text)) :
#         for j in range (i+1):
#             if j==0 :
#                 out += '-'
#                 out += text[i].upper()
#             else :
#                 out  += text[i]
#         print(out)
# duplicate_string_strip('citra')
#----------Hasilnya-----------
# -C
# -C-Ii
# -C-Ii-Ttt
# -C-Ii-Ttt-Rrrr
# -C-Ii-Ttt-Rrrr-Aaaaa

# def duplicate_string_strip(text):
#     out =  ''
#     for i in range (len(text)) :
#         for j in range (i+1):
#             if j==0 :
#                 out += '-'
#                 out += text[i].upper()
#             else :
#                 out  += text[i]
#     print(out)
# duplicate_string_strip('citra')
#----------Hasilnya-----------
# -C-Ii-Ttt-Rrrr-Aaaaa

#--------function sort ascending
# list_angka = [1,5,6,4,3,2,10,2,11,3,4,6,7]
# for i in range(len(list_angka)):
#     print (i)
# ------------Hasilnya-----------
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# 11
# 12

# inget
# a = 5
# b = 4
# a,b = b,a
# --------Hasilnya----------
# a = 4
# b = 5

# list_angka = [1,5,6,4,3,2,10,2,11,3,4,6,7]
# def sort_ascending(list_angka):
#     for i in range(len(list_angka)):
#         for j in range(i+1,len(list_angka)):
#             if list_angka [i] > list_angka[j] :
#                 list_angka [i], list_angka [j] = list_angka[j],list_angka[i]
#     return list_angka
# print(sort_ascending([1,5,6,4,3,2,10,2,11,3,4,6,7]))

# def sort_descending(list_angka):
#     for i in range(len(list_angka)):
#         for j in range(i+1,len(list_angka)):
#             if list_angka [i] < list_angka[j] :
#                 list_angka [i], list_angka [j] = list_angka[j],list_angka[i]
#     return list_angka
# print(sort_descending([1,5,6,4,3,2,10,2,11,3,4,6,7]))

#Modul3
# def contoh() :
#     print('Halo Dunia!')
# contoh()
#-------------------------------------------------
# Hasilnya 
# Halo Dunia!

# x = 10
# y = 50

# def contoh() :
#     print(x+y)
# contoh()
#-------------------------------------------------
# # Hasilnya 
# 60
# def namaku(nama):
#     print(nama + ' Kyaaa')
# namaku('Citra')
# namaku('Siapa')
#-------------------------------------------------
# Hasilnya
# Citra Kyaaa
# Siapa Kyaaa

# def blender(buah) :
#     print('jus ' + buah)
# # blender('alpukat')
# blender(buah='apel')
# # Hasilnya
# # jus alpukat
# jus apel

# def bayar_parkir(masuk,keluar):
#     total_jam =abs(keluar-masuk)
#     total_biaya = total_jam *3000
#     print(total_biaya)
# bayar_parkir(7,10)
# bayar_parkir(masuk=7,keluar=10)
# #-------------------------------------------------
# Hasilnya
# 9000
# 9000

#Coba di kelas
# bebas ('Anugrah','n')

# def replace_satu_char(text,y):
#     n = text.replace(remove,'',1)
#     print(n)
    
# replace_satu_char('citra','i')
# replace_satu_char(text='citra',remove='i')
# #-------------------------------------------------
# Hasilnya
# ctra
# ctra

# def rock_paper_scissors(p1,p2):
#     if p1 == 'gunting' and p2 == 'batu':
#         print ('P1 loss and P2 win')
#     if p1 == 'gunting' and p2 == 'kertas':
#         print ('P1 win  and P2 loss')
#     if p1 =='batu' and p2 == 'kertas':
#         print ('P1 loss and P2 win')
#     if p1 == 'batu' and p2 == 'gunting':
#         print('PP1 win  and P2 loss')
#     if p1 == 'kertas' and p2 == 'batu':
#         print('P1 win and P2 loss')
#     if p1 == 'kertas' and p2 == 'gunting':
#         print('P1 loss and P2 win'')

# rock_paper_scissors('gunting', 'batu')

# ----------------------------------------------------------------
# def rock_paper_scissors():

#     p1 = input('Masukkan pilihan player  : ')
#     p2 = input('Maukkan pilhan player 2 : ')
#     if p1 == p2 :
#         print ('Draw')
#     if p1 == 'gunting' and p2 == 'batu':
#         print ('P1 loss and P2 win')
#     if p1 == 'gunting' and p2 == 'kertas':
#         print ('P1 win  and P2 loss')
#     if p1 =='batu' and p2 == 'kertas':
#         print ('P1 loss and P2 win')
#     if p1 == 'batu' and p2 == 'gunting':
#         print('PP1 win  and P2 loss')
#     if p1 == 'kertas' and p2 == 'batu':
#         print('P1 win and P2 loss')
#     if p1 == 'kertas' and p2 == 'gunting':
#         print('P1 loss and P2 win')

# rock_paper_scissors()
# # -------------------------------------------------------------------------
# Hasilnya
# Masukkan pilihan player1: gunting
# Masukkan pilihan player2: kertas
# P1 win and P2 loss

# ------------------------------------------------------------------------------------------------------
# def main_suit(p1,p2):
#     p1 = p1.lower()
#     p2 = p2.lower()
#     if p1 == p2 :
#         print ('Hasil Draw')
#     elif (p1 == 'gunting'):
#         if (p2 == 'kertas') :
#             print('P1 win and P2 loss')
#         if (p2 == 'batu') :
#             print('P1 loss and P2 win')
#     elif (p1 == 'batu'):
#         if (p2 == 'kertas') :
#             print('P1 loss and P2 win')
#         if (p2 == 'gunting'):
#             print('P1 win and P2 loss')
#     elif (p1 == 'kertas') :
#         if (p2 == 'batu') :
#             print('P1 win and P2 loss')
#         if (p2 == 'gunting'):
#             print('P1 loss and P2 win')

# pilih1 = input('Masukkan pilihan player1: ')           
# pilih2 = input('Masukkan pilihan player2: ')
# main_suit(pilih1,pilih2)

# Hasilnya-------------------------------------
# Masukkan pilihan player1: kertas
# Masukkan pilihan player2: batu
# P1 win and P2 loss
# ------------------------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------------------------
# Function punya default parameter
# Default parameter merupakan sebuah parameter dari sebuah function
# def perkalian(angka1=5,angka2=2):
#     return angka1 * angka2
# print(perkalian()) # Hasilnya 10
# print(perkalian(angka1=2)) #Hasilnya 4 karena angka 1 udah diganti jadi 2
# ------------------------------------------------------------------------------------------------------


# ------------------------------------------------------------------------------------------------------
# function in function
# def perkalian_2(x):
#     if x < 3 :
#         return 4
#     else :
#         return (x*tujuh())
# def tujuh():
#     return 7
# print(perkalian_2(2)) # karena inputnya 2 < 4 sehingga nge return ke 4
# print(perkalian_2(0)) # karena inputnya 0 < 4 sehingga nge return ke 4
# print(perkalian_2(4)) # karena inputnya 4 sehingga nge return ke 4*7 = 28
# print(perkalian_2(-1)) # karena inputnya -1 < 4 sehingga nge return ke 4
#posisi function nya bisa dimana aja karena dia bakal ngereturn terus selama functionnya masih jalan
# ------------------------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------------------------
# def remove_vowels():
#     kata = input('Masukkan string yang ingin diubah :  ')
#     kata = kata.replace('a','')
#     kata = kata.replace('i','')
#     kata = kata.replace('u','')
#     kata = kata.replace('e','')
#     kata = kata.replace('o','')
#     kata = kata.replace('A','')
#     kata = kata.replace('I','')
#     kata = kata.replace('U','')
#     kata = kata.replace('E','')
#     kata = kata.replace('O','')
#     print(kata)

# remove_vowels()
# # ------------------------------------------------------------------------------------------------------

# # ------------------------------------------------------------------------------------------------------
# def hilangkan_vowels() :
#     sentence = input('Masukkan kata yang diinginkan : ')
#     vowels = ('a','i','u','e','o','A','I','U','E','O')
#     for a in vowels :
#         sentence = sentence.replace(a,'')
#     print(sentence)
# hilangkan_vowels()
# # ------------------------------------------------------------------------------------------------------

# def hilangkan_vowels(sentence) :
    
#     vowels = ('a','i','u','e','o''A','I','U','E','O')
#     for i in vowels :
#         remove = sentence.replace(i,'') #GA BOLEH, karena ga bisa kelooping si sentence nya
#     print (remove)
# hilangkan_vowels('Saya adalah')

# # ------------------------------------------------------------------------------------------------------

#LIST bisa diisi apa 
# #kontainer sementara yang isinya value holding berapapun valuenya
# buah_buah = ['Jeruk','Apel','Semangka', 'Pear','Pisang'] #kurung siku
# buah_buah2 = ('Jeruk','Apel','Semangka') #kurung biasa
# print (type(buah_buah)) #list kurung siku
# print(type(buah_buah2)) #tuple

# print(buah_buah[2]) #pilih semangka
# print(buah_buah[-1]) #pilih pisang dari kanan minus 1
# print(buah_buah[:]) #print semua ['Jeruk', 'Apel', 'Semangka', 'Pear', 'Pisang']
# print(buah_buah[:2]) #['Jeruk', 'Apel']
# print(buah_buah[2:5])#['Semangka', 'Pear', 'Pisang']

# buah_buah[2] = 'Durian'#mengganti Semangka jadi Durian
# print(buah_buah) #jadi udah keganti semangka jadi durian ['Jeruk', 'Apel', 'Durian', 'Pear', 'Pisang']

# #append menambah suatu value ke list yang kita punya
# buah_buah.append('Es Krim') #bakal nambahin di ujung list
# print(buah_buah)  #['Jeruk', 'Apel', 'Durian', 'Pear', 'Pisang', 'Es Krim']

# append, pop, insert
# append nambahin di end ot the list
# insert bisa nambahin dimana
# buah_buah = ['Jeruk','Apel','Semangka', 'Pear','Pisang'] #kurung siku
# buah_buah.pop(2)
# print(buah_buah) #semangka kehapus ['Jeruk', 'Apel', 'Pear', 'Pisang']


# buah_buah = ['Jeruk','Apel','Semangka', 'Pear','Pisang']
# buah_buah.insert(3,'Kurma')
# print(buah_buah)#nambah kurma di string ke 3 inget semua dari nol ['Jeruk', 'Apel', 'Semangka', 'Kurma', 'Pear', 'Pisang']
# # # ------------------------------------------------------------------------------------------------------



list_angka = [2,'Hello', [1,5,'Hai',[9, False]]]
print(list_angka[2][2][0]) # H
# print(list_angka[2][2])#Hai
# print(list_angka[2][2][0])


# check_name (name,alphaber) -> ('Anugerah nurhamid','a') - > True

# def check_nama() :
#     nama = input('Masukkan nama : ')
#     alph = input('Masukkan alphabet : ')
#     if alph.lower() in nama[:]:
#         print(nama, 'terdapat huruf', alph, ' TRUE')
#     else :
#         print(nama, 'tidak terdapat huruf', alph, ' FALSE')
# check_nama()

# #--------------ATAU-------------------------------

# def check_nama(nama,alph) :
#     if alph.lower() in nama[:]:
#         print(nama, 'terdapat huruf', alph, ' TRUE')
#     else :
#         print(nama, 'tidak terdapat huruf', alph, ' TRUE')
# check_nama('citra','a')

# #--------------ATAU-------------------------------
# def check_nama(nama,alph) :
#     print(alph.lower() in nama or alph.upper() in nama) #bisa langsung soalnya hasilnya boolean TRUE atau FALSE
# check_nama('citrA','a')

