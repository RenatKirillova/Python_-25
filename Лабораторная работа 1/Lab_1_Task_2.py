# TODO Найдите количество книг, которое можно разместить на дискете
disk_size = 1.44
pages = 100
lines = 50
chars = 25
bytes_per_char = 4

disk_bytes = disk_size * 1024 * 1024
book_bytes = pages * lines * chars * bytes_per_char

a = int(disk_bytes // book_bytes)

print("Количество книг, помещающихся на дискету:", a )
