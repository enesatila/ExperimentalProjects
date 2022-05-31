#          Python Başlangıç

#           Print Komutu
#          Ekrana Yazdırır

print("merhaba")  #out merhaba
print("naber")    # out naber
 
# Ekrana 3 tane değer yan yana yazdırmak için , kullanılılır
 
print("murat",14,"coşkun")
# out murat 14 çoşkun

# Alt alta satır atlamak için \n kullanılır

print("Mustafa\nMurat\nCoşkun")
"""
Mustafa
Murat     out
Coşkun
"""
# Boşluk olan yerlere herhangi birşey eklemek için ,sep = " "

print("19","09","1993")               # out 19 09 1993
print("19","09","1993",sep = "/")     # out 19/09/1993
print("19","09","1993",sep = ".")     # out 19.09.1993

# .format fonksyonuyla süslü parantez doldurma
print("{} + {} = {}".format(2,3,2+3)) #out 2 + 3 = 5 
print("{} + {} = {}".format("ali","mehmet","mustafa"))
# out ali + mehmet = mustafa
print("{} + {} = {}".format("alp",12,"a"))
# out SyntaxError: unexpected EOF while parsing
# Hatayı düzeltmek için "12" yazılmalı

# Paythondaki veri tipleri ve Değişken tanımlama

# Değişken tanımlama işlemi = ile yapılır
a = 3 #int tam satr yyı
b = 3.14 #float ondalıklı sayı
c = "Python" # sazı 
d = [1,2,3,4,5,6] # list liste
e = (1,2,3,4,5) # tupple demet
f = {"elma":1,"armut":2,"kiraz":3} # dict sözlük
g = True # bool 

# Type() fonksyonuyla değişken tipini öğrenme

print(type(a)) # out <class 'int'> tam sayı
print(type(b)) # out <class 'float'> ondalıklı sayı
print(type(c)) # out <class 'str'> yazı
print(type(d)) # out <class 'list'> liste
print(type(e)) # out <class 'tuple'> demet
print(type(f)) # out <class 'dict'> sözlük
print(type(g)) # out <class 'bool'> bool

print(a,b,c) # out 3 3.14 Python

del(a,b,c,d,e,f,g) # del() fonksyonu değişkenleri siler


#  Matematik Operatörleri

print(3 + 4)  # out 7    Toplama
print(10 - 3) # out 7    Çıkartma
print(10 * 2) # out 20   Çarpma
print(10 / 4) # out 2.5  Bölme
print(2 ** 5) # out 32   Üs alma
print(10 // 7) #out 1    tamsayı bolmesi //
print(10 % 7) # out 3    bölümden kalan %

#            Alıştırmalar
a = 5
b = 10
c = 2 
d = b/c*a
e = c**a
print(a*c+b) #out 20
print(d)     #out 25.0
print(e)     #out 32

a = "Python"
b = "Proglamlama"
c = "Dili"
d = a + b + c 
print(a+b+c) # out PythonProglamlamaDili
print(d)     # out PythonProglamlamaDili
print(a * 5) # out PythonPythonPythonPythonPython

print("*" * 1)# *
print("*" * 2)# **
print("*" * 3)# ***
print("*" * 4)# ****
print("*" * 5)# *****
print("*" * 6)# ******   out
print("*" * 5)# *****
print("*" * 4)# ****
print("*" * 3)# ***
print("*" * 2)# **
print("*" * 1)# *


# Stringlerle listelerin indexlenmesi

a = "Python"
b = [1,2,3,4,5,6,7,8,9,0]
"""
Pyton'da indexler 0 dan başlar b listesinin
1. terimi 0. index
2. terimi 1. index
10. terimi 9.index
"""
print(b[0]) # out 1
print(b[1]) # out 2
print(b[2]) # out 3
print(b[3]) # out 4
print(b[4]) # out 5
print(b[5]) # out 6
print(b[6]) # out 7
print(b[7]) # out 8
print(b[8]) # out 9
print(b[9]) # out 0

# len() fonksyonu eleman sayısını verir
print(len(a)) # out 6
print(len(b)) # out 10

print(len(a)-1) # out 5 sonindeksi almak için

# indexlerde belirli kısımları almak 
print(a[0:2]) # 0 dan 2. indexe kadar out Py
print(a[2:]) #out thon 2 den başla sonuna kadar git
print(a[:4]) # out Pyth baştan başla 4. ye kadar git
print(b[2:]) # out [3, 4, 5, 6, 7, 8, 9, 0]
print(b[0:6:2]) # out [1, 3, 5] baştan 6 ya kadar 2 atlayark

#    Sözlüklerin yapısı anahtar kilit uyumu

a = {"Elma":3,"Armut":4,"Kiraz":5}
print(a["Elma"]) # out 3
print(a["Armut"]) # out 4
print(a["Kiraz"]) # out 5
print(a["Çilek"]) # out Keyerror

#       Kullanıcıdan İnput almak
#     input fonksyonu kullanılır

yaş = input("Yaşınızı Giriniz:")
print("Yaşınız",yaş)

a = input("a:") # a = 5
b = input("b:") # b = 6
c = input("c:") # c = 7
print("Toplam",a+b+c) # out 567
# Değerleri str biçiminde aldığı için yan yana yazmıştır
print(type(a)) # out <class 'str'>
print(type(b)) # out <class 'str'>
print(type(c)) # out <class 'str'>

# Değişlen tipini değiştirmek için kullanılan yöntem

a = int(input("a:")) # a = 5
b = int(input("b:")) # a = 6
c = int(input("c:")) # a = 7
print("Toplam",a+b+c) # out Toplam 18

# Değişkenleri integer'a çevirdiğimiz için matematiksel toplama yaptı

a = float(input("Ondalıklı bir a değeri giriniz:")) # a=3.1
b = float(input("Ondalıklı bir b değeri giriniz:")) # b=4.2
c = float(input("Ondalıklı bir c değeri giriniz:")) # c=5.3
print("Çarpım",a+b+c) #  Out Çarpım 12.600000000000001

#         Koşul Durumları
#     if den sonraki satırda Tab boşluğuyla çalışır
yaş = int(input("Yaşınızı giriniz:"))
if yaş < 18:
    print("Mekana giremezsiniz")
else:
    print("Mekana Hoşgeldiniz")

"""
18 den küçük bir değer için True değer
oluşacağı için print("Mekana Giremezsiniz") çalışır.

18 den büyük bir değer için False değer
oluşacağı için print("Mekana Giremezsiniz") çalışır.

else bloğu sadece ve sadece 
if bloğu false olduğunda çalışır
"""
"""
<  Küçükse              True
>  Büyükse              True
<= Küçük eşitse         True
>= Büyük eşitse         True
== İki değerimiz eşitse True
!= Eşit değilse         True
"""
"""
if koşul durumu oluşturur
else koşulun
elif koşul ekler
"""
işlem = int(input("Seçmek İstediğiniz İşlemi Giriniz :"))
if işlem == 1 :
    print("İşlem 1 i Seçtiniz...")
elif işlem == 2 :
    print("İşlem 2'yi Seçtiniz....")
elif işlem == 3 :
    print("İşlem 3'ü Seçtiniz...")
else :
    print("Geçersiz İşlem seçtiniz")
"""
Eğer işlemi 1 seçersen 1. print çalışır.

Eğer işlem 2 yi seçersen 1. işlem False olduğundan
1. elif fonksyonu True olur ve 2. print çalışır.

Eğer işlem 3 ü seçersen if ve 1. elif fonksyonları 
False olur ve 2.elif fonksyonu True olur 
ve 3. print çalışır.

Eğer bu 3 işlemden farklı bir işlem seçmeye 
çalışırsan if ve elifler False olur else fonksyou
True değer alır ve 4. print çalışır.
"""

# Mantıksal Bağlaçlar

a = 3
b = 4

if a==3 and b==4 :
    print("Evet")
else:
    print("Hayır")
# out Evet
"""
And bağlacı iki koşulun birden True olması
durumunda çalışır ve 1. printi yazdırır.
"""
a = 3
b = 4

if a==3 and b==5:
    print("Evet")
else:
    print("Hayır")    
# out Hayır

a = 3
b = 4
if a==3 or b==5:
    print("Evet")
else:
    print("Hayır")
# out Evet
"""
Or bağlacı harhangi iki koşuldan 
en az birinin True olması durumunda 
çalışır ve 1. print i çalıştırır.
"""

a = 3
b = 4
c = 5
if a==3 or b==5 or c==3:
    print("Evet") 
else:
    print("hayır")
# out incalid syntax

# and ve or operatörleri sadece iki koşulla çalışır.

if (not(3==4)):
    print("Evet")
# out Evet

"""
not bağlacı koşul True ise False ya
False ise True ye çevirir.

3==4 koşulu False değerlidir
başındaki not bağlacı değerini True ya çevirir
dolayısıyla if operatörü print i çalıştırır.
"""
# Pythonda Döngü yapıları
"""
While döngüsü koluşumuz True olduğu sürece 
sürekli bloğunu döndürmeye devam eder.
koşul False olduğu anda döngü sona erer.
"""

i = 0
while i<10:
    print("i:",i)
    i = i + 1   # i + = 1 aynı işlemdir.

"""
i: 0
i: 1    döngü olduğu için i = 10 
i: 2    olana kadar tekrarlandı
i: 3    i = 10 koşulu False yaptı
i: 4    döngü durdu.
i: 5
i: 6
i: 7
i: 8
i: 9
"""

i = 0
while i < 10:
    print("i:",i)
    i += 2
"""
i: 0
i: 2
i: 4        out
i: 6
i: 8
"""
i = 1
while i < 2000:
    print("i:",i)
    i *= 2
"""
i: 1
i: 2
i: 4      i değerlerini 2 ile çarparak ilerledi
i: 8
i: 16
i: 32
i: 64          out
i: 128
i: 256
i: 512
i: 1024
"""
# Döngülerde kullanılan Break Continue
# Break döngüyü sonlandırmak
# Continue döngünün başına dönmek

i = 0

while i < 10 :
    if i == 5 :
        break
    print("i:",i)
    i += 1
"""    
i: 0 out
i: 1   i == 5 olduğunda if true olduğu için
i: 2   break çalıştı ve döngü durdu.
i: 3  
i: 4
"""

i = 0
while (i < 10):
    if i ==3 or i==5:
        i +=1
        continue
    print("i:",i)
    i +=1
"""
i: 0    i = 3 olana kadar füzgün bir şekilde
i: 1    çalıştı 3 olduktan sonra if koşulu True
i: 2    değer aldığı için continue yi çalıştırdı
i: 4    continue ise işlemi en başa döndürüp
i: 6    print'in çalışmasını engelledi ve işlem 
i: 7    4 den devam etti. 5 de de if True oldu
i: 8    aynı şekilde 6 dan devam ettiği için  
i: 9    3 ve 5 değerlerini out kısmında göremeyiz.
"""
"""
*
**
***
****
*****
******    SONSUZ DÖNGÜYE GİRMEMEYE DİKKAT ET!
*****
****
***
**
*
"""
# For Döngüsü
"""
For döngüsüyle herhangi bir listenin
sözlüğün veya tupple in üzerinde rahatlıkla gezebiliyoruz.
"""
a = [1,2,3,4,5,6]

for eleman in a:
    print(eleman)

"""
1   biz for eleman in a derken 
2   aslında listenin üstinde gezinmek istediğimizi
3   belirtiyoruz ve her bir eleman sırayla yazılıyor.
4   
5
6   out
"""
 
b = "Python"
for karakter in b:
    print(karakter)
"""
P     
y     her bir karakter sırayla yazılıyor
t
h
o
n
"""
# Range Fonksyonu

for sayı in range(0,5):
    print(sayı)

"""
0
1
2    0 dan başla ve 5 e kadar git anlamına
3    gelen ve menzil belirten bir fonksyon.
4
"""
for sayı in range(10,50,10):
    print(sayı)
"""
10
20    10 dan 50 ye kadar 10 ar 10 ar git
30
40
"""
# Fonksyon tanımlama olayları
"""
Her bir fonksyon belirli bir bloğa sahiptir.
Biz bu blogda fonksyonun yapması gereken işlemleri
tnımlıyoruz. Ve eğer biz fonksyona herhangi bir 
değer göndeirsek bu fonksyonların input ları
yani parametreleri olmuş oluyor. Göndermiş olduğumuz
değerlere göre fonksyon yapması gereken işlemleri
yapıyor ve dışarı bir çıktı veriyor.g
"""

def selamla():
    print("Merhaba")
    print("Nasılsın")
    
# fonksyonu çağırmak için
selamla()
#  out  Merhaba
#       Nasılsın
# input göndermek için

def selamla(isim):
    print("Merhaba",isim)


selamla("Alp")
# out Merhaba Alp


# fonksyona varsayılan değer atamak
# eğer fonksyona isim gönderilmezse varsayılan değer çalışır

def selamla (isim = "İsimsiz"):
    print("Merhaba",isim)
    
selamla() 
# out Merhaba İsimsiz

def toplama(a,b,c):
    print("Toplam:",a+b+c)
    
toplama(3,4,5)
# out Toplam: 12

# fonksyonun içindeki değeri çağrıldığı yere döndürme

def toplama(a,b,c):
    return a + b + c
toplam = toplama(3,4,5)
print(toplam)
#out 12

def toplama(a,b,c):
    print("Toplam:",a+b+c)
    
a = toplama(3,4,5)
print(a)
#Toplam: 12
#None return kullanarak fonksyondan çıktı elde edebiliriz


  # Bağzı methodlar
liste = [1,2,3,4,5,6]
a ="araba"

a = a.replace("a","o")
print(a)
# orobo

# nesne yönelimli programlama

class Account:
    def __init__(self,isim,numara,bakiye):
        self.isim = isim
        self.numara = numara
        self.bakiye = bakiye
    def hesapbilgileri(self):
        print("İsim :",self.isim)
        print("Numara :",self.numara)
        print("Bakiye :",self.bakiye)
        def paracek(self,miktar):
            if self.bakiye - miktar < 0:
                print("Bakiyeniz Yeterli Değil...")
            else:
                self.bakiye -= miktar
                print("Yeni Bakiye :",self.bakiye)
                def parayatır(self,miktar):
                    self.bakiye += miktar
                    print("Yeni Bakiye :",self.bakiye)
          
account = Account("Alpgiray Demirtaş",10190052,1000)  
    
account.hesapbilgileri()      








































































































































