class Queue:
    def __init__(self):
        self.qlist = list()

    def isEmpty(self):
        return len(self.qlist) == 0

    def __len__(self):
        return len(self.qlist)

    def enqueue(self, data):
        self.qlist.append(data)

    def dequeue(self):
        if self.isEmpty():
            print('Queue kosong. Tidak ada data yang dapat di-dequeue.')
            return None 
        else:
            return self.qlist.pop(0)

    def display(self):
        if self.isEmpty():
            print('Queue kosong. Tidak ada data yang dapat ditampilkan.')
        else:
            print("Isi Queue (Depan -> Belakang): [", end="") 
            for item in self.qlist:
                print(item, end=' ')
            print("]")

    def deleteAll(self):
        self.qlist.clear() 

myQueue = Queue()

cek = True

while cek:
    print()
    print("----- PILIHAN MENU ANDA -----")
    print("1. Tambah Elemen pada Queue")
    print("2. Tampil Elemen dalam Queue")
    print("3. Hapus Elemen dalam Queue")
    print("4. Hapus Seluruh data dalam Queue")
    print("------------------------------")
    print("0. Keluar")
    print()

    try:
        pil = int(input("Masukkan pilihan anda: ")) 
    except ValueError:
        print("Input pilihan harus berupa angka. Silakan coba lagi.")
        continue 

    if pil == 1:
        try:
            jum = int(input("Masukkan jumlah data yang ingin diinputkan: "))
        except ValueError:
            print("Input jumlah data harus berupa angka.")
            continue

        if jum > 0:
            i = 1
            while i <= jum:
                data = input(f"Masukkan data ke-{i} yang ingin diinput: ")
                myQueue.enqueue(data)
                i += 1
        else:
            print("Jumlah data minimal 1 !!!")

    elif pil == 2:
        print("Isi Queue: ", end="") 
        myQueue.display()

    elif pil == 3:
        data_dihapus = myQueue.dequeue() 
        
        if data_dihapus is not None:
            print(f"Data '{data_dihapus}' telah dihapus.")

    elif pil == 4: 
        myQueue.deleteAll()
        print("Semua data dalam Queue telah dihapus.")
        
    elif pil == 0:
        print("Bye Troopers... \n")
        break

    else:
        print("Pilihan tidak ada")