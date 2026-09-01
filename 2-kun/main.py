# python data types

# type is help our check data type


# python has many data types includes text, number, boolean and complex(list, set, dict, tuple)
#  number = int, float, complex


# strings
name = "komiljon"# it's only single line work
name2 = 'odil' #it's only single line

# for two line we use 3 " "quotation mark(qo'shtirnoq)"
two_line = """
komiljon roziyev 16 yoshda 
"""


# numeric raqamlar , butun sonlar(int), o'nli sonlar(float), mavhum(complex)

age = 12



complexnumber = 12 + 3j # complex number is a imaginery and it's only j one work there


# we have boolean data type
# it has only two value it's true or false
print(type(true))	 #for check
1 > 5 #1 isn't greater than 5	
 

 # we have two value this bool = boolean
# true (rost) false(yolg'on)

# indexlash
a = 'hello world'
a[0:5] #index doim 0dan boshlanadi + : qirqib olish uchun ishlatilinadi
print(a)

# ro'yxatlar turli xil narsalarni 1ta joyda yig'ish

# list[] is mutable (o'zgaruvchan)swap qila olamiz va qo'sha olamiz

diffirent_type_in_oneplace = ['komiljon', True, 12, [1,2,3]]
diffirent_type_in_oneplace.append('roziyev')
print(komiljon)

# kortejlar("ro'yxatlar") is immutable oddiy qavsdan foydalanamiz
tuple1 = (1, 2, "komiljon")#static ma'lumotlar uchun eng zo'ri

# to'plamlar(set) umuman tartibsiz va takroriy qiymatni hech qachon qabul qilmaydi
toplam = {1 ,2, 2, 'komiljon'}	

 # dictionary lug'at = kalit va qiymat
lugat = {1: "komiljon", 2: "roziyev"}

lugat.values() #qiymatlar valuelarni ajratib olish uchun
lugat.keys() # faqat kalitlar 1 2 birinchi kalit keladi ushani olish uchun
lugat.items()# kalit + qiymatni olish

print(lugat)

