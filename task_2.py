# TODO Найдите количество книг, которое можно разместить на дискете
disk_bytes = 1.44 * 1024 * 1024  # 1 509 949.44 байт

pages = 100
lines_per_page = 50
families_per_line = 25
bytes_per_family = 4


book_size = pages * lines_per_page * families_per_line * bytes_per_family


books_fit = int(disk_bytes // book_size)

print("Количество книг, помещающихся на дискету:", books_fit)
