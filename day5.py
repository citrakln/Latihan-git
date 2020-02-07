#for list
#inget dalam range semuanya dimulai dari 0
# for i in range (3) :
#     for j in range(3) :
#         print(i)

# Hasilnya
# 0
# 0
# 0
# 1
# 1
# 1
# 2
# 2
# 2

# for i in range (3) :
#     for j in range (3) :
#         print (i*' + ')

# Hasilnya



#  +
#  +
#  +
#  +  +
#  +  +
#  +  +

# out = ''
# for i in range (3) :
#     for j in range (3) :
#         out += str(i)
#     out+='\n'
# print(out)
# Hasilnya
# 000
# 111
# 222

# out = ''
# for i in range (3) :
#     for j in range (3) :
#         out += str(j)
#     out+='\n'
# print(out)
# Hasilnya
# 012
# 012
# 012

# out = ''
# for i in range (3):
#     for j in range (4) :
#         out += str(i+1)
#     out += '\n'
# print(out)

#FUNCTION

# def contoh () :
#     print('Aku adalah seorang kapiten')
# #function akan berjalan kalo kita excecute
# contoh() #cara manggilnya nama function apa ()
# Hasilnya
# Aku adalah seorang kapiten


# angka1 = 5
# angka2 = 10
# def pertambahan():
#     print(angka1+angka2)
# pertambahan()
# Hasilnya
# 15

#Function juga punya parameter
# def fullName(FirstName, LastName) :
#     print(FirstName + ' ' +LastName)
# fullName('Citra', 'Kirana') #Kalo diisi yang pertama aja ga bisa soalnya dia butuh 2 parameter
# Hasilnya
# Citra Kirana

#di function ada fungsi return dan ??/
# def pertambahan(x,y):
#     total = x + y
#     return total#return itu bisa mencetak nilai dan nilainya bakal bisa dipanggil dalam function untuk manggilnya tinggal di print
# pertambahan(7,5)# kaya gini ga ada outputnya 
#jadi cara ngeluarin outputnya tinggal ngeprnt ajah
# print(pertambahan(7,5))
# Hasilnya
# 12
# print(total) #ga akan keluar karena total sudah ada dalam fungsi

def lima():
    return 5

def kali(x):
    if(x<3) :
        return 1
    else :
        return (x*lima())

# print(kali(5))
# Hasilnya
# 25
print(kali(1))

