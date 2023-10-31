# TODO Найдите количество книг, которое можно разместить на дискете

volume = 1.44
pages = 100
lines = 50
symbols = 25
symbolone = 4

size = volume*1024*1024

books = size // (pages*lines*symbols*symbolone)

print("Количество книг, помещающихся на дискету:", int(books))
