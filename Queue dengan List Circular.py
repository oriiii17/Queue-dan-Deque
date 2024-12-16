class ArrayQueue:
    DEFAULT_CAPACITY = 10
    def __init__(self):
        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0
    
    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self): #menampilkan data dengan indeks front
        if self.is_empty():
            print("Empty")
        return self._data[self._front]

    def dequeue(self): #menghapus data indeks front, kemudian indeks front geser satu ke s20 
        if self.is_empty():
            print("Empty")
        answer = self. data[self. front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return answer

    def enqueue(self, e): #menambah data ke list
        if self._size == len(self._data):
            self._resize(2*len(self._data))
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1

    def resize(self, cap): #mengubah ukuran queue pada list
        old = self._data
        self._data = [None] * cap
        walk = self._front
        for k in range(self. size):
            self._data[k] = old[walk]
            walk = (1 + walk) % len(old)
        self._front = 0