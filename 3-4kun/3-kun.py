name = "komiljon roZiyev"
txt = "I love apples, apple are my favorite fruit"

# 1. capitalize() - Birinchi belgini bosh harfga (uppercase) o'tkazadi
x = name.capitalize()
print(x)  # "Komiljon roziyev"


# 2. casefold() - Barcha harflarni kichik (lowercase) qiladi (lower() ga qaraganda tajovuzkorroq va xalqaro belgilarni ham kichraytiradi)
a = name.casefold()
print(a)  # "komiljon roziyev"


# 3. lower() - Barcha harflarni kichik belgilarga o'tkazadi
l = name.lower()
print(l)  # "komiljon roziyev"


# 4. upper() - Barcha harflarni bosh harfga (uppercase) o'tkazadi
u = name.upper()
print(u)  # "KOMILJON ROZIYEV"


# 5. title() - Har bir so'zning birinchi harfini bosh harf qiladi
t = name.title()
print(t)  # "Komiljon Roziyev"


# 6. swapcase() - Kichik harflarni katta, kattalarni kichik qiladi
s = name.swapcase()
print(s)  # "KOMILJON ROzIYEV"


# 7. center() - Satrni ko'rsatilgan kenglik markaziga joylashtiradi (bo'sh joy yoki ko'rsatilgan belgi bilan)
c = name.center(30, "*")
print(c)  # "*******komiljon roZiyev*******"


# 8. ljust() - Satrni chap tomondan berilgan kenglikda tekislaydi
lj = name.ljust(25, "-")
print(lj)  # "komiljon roZiyev---------"


# 9. rjust() - Satrni o'ng tomondan berilgan kenglikda tekislaydi
rj = name.rjust(25, "-")
print(rj)  # "---------komiljon roZiyev"


# 10. zfill() - Satr boshiga berilgan uzunlikka yetguncha nol (0) biriktiradi
z = name.zfill(20)
print(z)  # "0000komiljon roZiyev"


# 11. count() - Ko'rsatilgan qiymat satrda necha marta takrorlanganini hisoblaydi
fin = txt.count("apple")
print(fin)  # 2


# 12. encode() - Satrni kodlangan (encoded) ko'rinishga (bytes) o'tkazadi (masalan: UTF-8)
en = name.encode()
print(en)  # b'komiljon roZiyev'


# 13. startswith() - Satr ko'rsatilgan qiymat bilan boshlansa True qaytaradi
st = name.startswith("kom")
print(st)  # True


# 14. endswith() - Satr ko'rsatilgan qiymat bilan tugasa True qaytaradi
xtx = name.endswith("v")
print(xtx)  # True


# 15. find() - Qiymatni qidiradi va birinchi uchragan indeksini qaytaradi (topilmasa -1 qaytaradi)
f = name.find("roZiyev")
print(f)  # 9


# 16. rfind() - Qiymatni o'ngdan (oxiridan) qidiradi va oxirgi uchragan indeksni qaytaradi (topilmasa -1)
rf = txt.rfind("apple")
print(rf)  # 15


# 17. index() - Qiymatni qidiradi va indeksini qaytaradi (topilmasa xatolik/ValueError beradi)
zxz = name.index("roZiyev")
print(zxz)  # 9


# 18. rindex() - Qiymatni o'ngdan qidiradi va indeksini qaytaradi (topilmasa xatolik beradi)
ri = txt.rindex("apple")
print(ri)  # 15


# 19. format() - Satr ichidagi o'zgaruvchilarni ({}) belgilangan tartibda joylashtiradi
fmt = "Mening ismim {}, yoshim {}".format("Komiljon", 22)
print(fmt)  # "Mening ismim Komiljon, yoshim 22"


# 20. format_map() - Lug'at (dictionary) elementlari orqali satrni formatlaydi
data = {"name": "Komiljon", "age": 22}
fm = "Ismi: {name}, Yoshi: {age}".format_map(data)
print(fm)  # "Ismi: Komiljon, Yoshi: 22"


# 21. isalnum() - Satr faqat harf va raqamlardan iborat bo'lsa True qaytaradi
print("Komil123".isalnum())  # True
print("Komil 123".isalnum())  # False (bo'sh joy bor)


# 22. isalpha() - Satr faqat harflardan iborat bo'lsa True qaytaradi
print("Komiljon".isalpha())  # True


# 23. isascii() - Satr barcha belgilari ASCII belgilari bo'lsa True qaytaradi
print("Komiljon".isascii())  # True


# 24. isdecimal() - Satr faqat o'nlik raqamlardan (0-9) iborat bo'lsa True qaytaradi
print("12345".isdecimal())  # True


# 25. isdigit() - Satr faqat raqamli belgilardan (shu jumladan daraja raqamlaridan) iborat bo'lsa True
print("12345".isdigit())  # True
print("²".isdigit())  # True


# 26. isnumeric() - Satr faqat sonli qiymatlardan (rim raqamlari, kasrlar va h.k) iborat bo'lsa True
print("12345".isnumeric())  # True
print("½".isnumeric())  # True


# 27. isidentifier() - Satr to'g'ri o'zgaruvchi nomi (identifier) bo'la olsa True qaytaradi
print("my_var".isidentifier())  # True
print("1var".isidentifier())  # False (raqam bilan boshlanmaydi)


# 28. islower() - Satrdagi barcha harflar kichik bo'lsa True qaytaradi
print("komiljon".islower())  # True


# 29. isupper() - Satrdagi barcha harflar bosh harf bo'lsa True qaytaradi
print("KOMILJON".isupper())  # True


# 30. isprintable() - Satrdagi barcha belgilar ekranga chop etiladigan bo'lsa True (masalan, \n emas)
print("Hello!\nWorld".isprintable())  # False


# 31. isspace() - Satr faqat bo'sh joylardan (spaces) iborat bo'lsa True
print("   ".isspace())  # True


# 32. istitle() - Satrdagi har bir so'z bosh harf bilan boshlangan bo'lsa True
print("Komiljon Roziyev".istitle())  # True


# 33. join() - Iterable (ro'yxat va h.k.) elementlarini satr ajratuvchisi bilan birlashtiradi
words = ["Komiljon", "Roziyev"]
j = " ".join(words)
print(j)  # "Komiljon Roziyev"


# 34. strip() - Satrning ikki chetidagi bo'sh joylarni (yoki ko'rsatilgan belgilarni) olib tashlaydi
st = "   Komiljon   ".strip()
print(st)  # "Komiljon"


# 35. lstrip() - Satrning chap belgilari/bo'sh joylarini olib tashlaydi
ls = "   Komiljon   ".lstrip()
print(ls)  # "Komiljon   "


# 36. rstrip() - Satrning o'ng belgilari/bo'sh joylarini olib tashlaydi
rs = "   Komiljon   ".rstrip()
print(rs)  # "   Komiljon"


# 37. partition() - Satrni berilgan belgi bo'yicha 3 qismdan iborat tuple-ga ajratadi
p = name.partition("roZiyev")
print(p)  # ('komiljon ', 'roZiyev', '')


# 38. rpartition() - Satrni berilgan belgi bo'yicha o'ng tomondan 3 qismli tuple-ga ajratadi
rp = txt.rpartition("apple")
print(rp)  # ('I love apples, ', 'apple', ' are my favorite fruit')


# 39. replace() - Satrdagi ko'rsatilgan qiymatni boshqasiga almashtiradi
rep = name.replace("roZiyev", "Roziyev")
print(rep)  # "komiljon Roziyev"


# 40. split() - Satrni ko'rsatilgan ajratgich bo'yicha bo'lib, ro'yxat (list) qiladi
sp = name.split(" ")
print(sp)  # ['komiljon', 'roZiyev']


# 41. rsplit() - Satrni o me'yorda o'ng tomondan ko'rsatilgan martagacha bo mezon bo'yicha bo'ladi
rsp = txt.rsplit(", ", 1)
print(rsp)  # ['I love apples', 'apple are my favorite fruit']


# 42. splitlines() - Satrni qator o'tkazish belgilari (\n) bo'yicha bo'lib ro'yxat qiladi
lines = "1-qator\n2-qator".splitlines()
print(lines)  # ['1-qator', '2-qator']


# 43. expandtabs() - Satrdagi tab (\t) belgilarini ko'rsatilgan bo'sh joy miqdoriga almashtiradi
tab_txt = "K\to\tm\ti\tl"
print(tab_txt.expandtabs(4))  # "K   o   m   i   l"


# 44. maketrans() va translate() - Belgilarni boshqa belgilarga almashtirish jadvalini tuzadi va almashtiradi
trans_table = str.maketrans("K", "Q")
print("Komil".translate(trans_table))  # "Qomil"


# 45. removeprefix() - Satr boshidagi berilgan prefiksni (agar mavjud bo'lsa) olib tashlaydi
pref = "https://google.com".removeprefix("https://")
print(pref)  # "google.com"


# 46. removesuffix() - Satr oxiridagi berilgan suffiksni (agar mavjud bo'lsa) olib tashlaydi
suff = "filename.pdf".removesuffix(".pdf")
print(suff)  # "filename"

