class Queue: #single linked list circular head dantail
    def __init__(self):
        self._head=None
        self._tail=None
        self._size= 0

    def __len__(self):
        return self._size

    def isEmpty(self):
        return self._size == 0

    def enqueue(self,e): #tambahbelakang
        baru = Node(e, None)
        if self.isEmpty()==True:
            self._head= baru
            self._tail= baru
            self._tail._next = self._tail
            self._head._next = self._head
        else:
            self._tail._next = baru
            self._tail= baru
            self._tail._next = self._head
            self._size+= 1
        #print("Datamasuk ke queue!")
 
    def first(self): #menampilkandata di head
        if self.isEmpty == True:
            return "Queue kosong!"
        else:
            return self._head._element

    def last(self): #menampilkandata di tail
        if self.isEmpty == True:
            return "Queue kosong!"
        else:
            return self._tail._element
 
    def dequeue(self): #hapus depan
        if self.isEmpty()==False:
            d =""
            if self._head._next==None:
                d =self._head._element
                self._head=None
                self._tail=None
            else:
                hapus =self._head
                d =hapus._element
                self._head= self._head._next
                self._tail._next = self._head
                hapus._next = None
            del hapus
            self._size-= 1
            #print(d," dihapus!")
        else:
            print("Queue kosong!")
        return d
     
    def printAll(self):
        if self.isEmpty() == False:
            bantu = self._head
            while(True):
                print(bantu._element, " ", end='')
                bantu = bantu._next
                if(bantu == self._tail._next):
                    break
            print()
        else:
            print("Kosong")

#main program
myqueue = Queue()
myqueue.enqueue("1")
myqueue.enqueue("2")
myqueue.enqueue("3")
myqueue.printAll()
myqueue.dequeue()
myqueue.printAll()
myqueue.dequeue()
myqueue.printAll()