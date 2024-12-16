from collections import deque
 # pembuatan queue
queue = deque(['nama','umur','tgllahir'])
print(queue)

#  • append() : untuk menambah elemen dari belakang (tambahBelakang)
#  • appendleft() : untuk menambah elemen dari depan (tambahDepan).
#  • pop() : untuk menghapus elemen dari belakang (hapusBelakang).
#  • popleft() : untuk menghapus elemen dari depan (hapusDepan).
#  • index(ele, beg, end) : untuk mengembalikan indeks pertama dari data yang ditemukan dari
#  posisi beg sampai dengan end.
#  • insert(i, a) : digunakan untuk menyisipkan elemen pada indeks tertentu
#  • remove(e) : untuk menghapus elemen pertama yang ditemukan sesuai nilai elemen
#  • extend(iterable) : untuk menambah elemen berupa list dari belakang (lebih dari satu data)
#  • extendleft(iterable) : untuk menambah elemen berupa list dari depan (lebih dari satu data)
#  • reverse() : untuk membalik isi deque