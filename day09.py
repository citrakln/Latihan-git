# def function(a,b):
#     return {'Ada apa' : [1,[1,[]],3]}
# Decision = {'testing':[1,3,[1,[1,function('Hello',3)]]]}
# Decision['testing'][2][1][1]('Ada Apa')[1][0] # hasilnya 1

a = [1,2,3,4,5,3,5,5,6,8,2,0,3,1,5,7,9,0,5,2,4,6,8,7,7,9,3,1]

from math import floor, pow, sqrt, ceil
def bubblesort(list) :
    for i in range (len(list)-1,0,-1):
        for j in range(i) :
            if list[j] > list[j+1] :
                list[j],list[j+1]=list[j+1],list[j]
    return list

def mean_list(list):
    return sum(list)/len(list)

def median_list(list) :
    list = bubblesort(list)
    # kondisi buat jumlah list yang genap
    if len(list) %2 == 0 :
        return (list[(len(list))//2-1]+ list[len(list)//2])/2
    else :
        return list[(len(list)//2)]

def mode_list(list) :
    ind = set(list) # set itu uniq artinya nilai yang sama akan hilang
    counter = {} # kita bikin dictionary , buat nge-count(menghitung)
    modus = []
    for i in ind :
        z = 0
        for j in list :
            if i == j :
                z+= 1
        counter[i] = z  #jadi dictionary yang ada isinya contohnya {1:2,2:4,3:0,dst}
    max_count = max(counter.values()) # bakal menghitung nilai maksimum dari value di dictionary counter
    for k in counter :
        if counter[k] == max_count : # counter[k] bacanya value dari dictionary counter index ke k
            modus.append(k) # bakal bikin list modus key k apa aja yang punya maks value 
    if len(modus) == len(set(list)):
        modus = []
    return modus
    
def variance_List(list):
    z = 0
    mean = mean_list(list)
    for i in list :
        z += pow((i-mean),2)
    return z/(len(list)-1)

def std_dec(list):
    z = 0
    mean = mean_list(list)
    for i in list :
        z += pow((i-mean),2)
    return sqrt(z/(len(list)-1))

def sample_statistic(list, type=''): # type artinya ngetik apa?
    if type == 'mean':
        return mean_list(list)
    if type == 'stddev' :
        return std_dec(list)
    if type == 'median' :
        return median_list(list)
    if type == 'variance':
        return variance_List(list)
    if type == 'mode':
        return mode_list(list)
    else :
        return 'Input tidak sesuai'

print(sample_statistic(a,'mean'))
print(sample_statistic(a,'stddev'))
print(sample_statistic(a,'mode'))
print(sample_statistic(a,'median'))
print(sample_statistic(a,'variance'))
