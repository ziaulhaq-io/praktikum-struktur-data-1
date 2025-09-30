import os
from queue import LifoQueue
from collections import deque

print()
Maxsize = int(input("Masukkan Jumlah data yang ingin ditambahkan : "))

DequeStack = deque()
LifoStack = LifoQueue(maxsize=Maxsize)

cek = True

while cek:
    os.system('cls')
    print('-Masukkan Pilihan anda-')
    print('1. Stack dengan Deque')
    print('2. Stack dengan LifoQueue')
    print('0. Keluar')
    
    pil = int(input('masukkan pilihan anda: '))
    
    if pil == 1:
        os.system('cls')
        i = 1
        temp = True
        while temp:
            print('-Masukkan Pilihan anda-')
            print('1. Tambah Data dengan Deque')
            print('2. Hapus Data Deque')
            print('3. Tampil Data Deque')
            print('4. Jumlah Data Deque')
            print('0. Keluar')
            pilMenu = int(input('masukkan pilihan anda: '))
            
            if pilMenu == 1:
                if len(DequeStack) <= Maxsize:
                    while i <= Maxsize:
                        item = input(f'Masukkan data ke-{i}: ')
                        DequeStack.append(item)
                        i += 1
                else:
                    print('Data tidak bisa ditambah. Stack sudah penuh!!')
            
            elif pilMenu == 2:
                if len(DequeStack) != 0:
                    print(f'Elemen terakhir: {DequeStack.pop()} telah dihapus!!')
                else:
                    print('Stack kosong. Tidak ada elemen untuk dihapus!!')
            
            elif pilMenu == 3:
                print('Data dalam Stack adalah:')
                print(DequeStack)
            
            elif pilMenu == 4:
                print(f'Jumlah Data dalam Stack = {len(DequeStack)}')
                
            else:
                pilMenu = False
                break
    
    elif pil == 2:
        os.system('cls')
        temp = True
        while temp:
            print()
            print('-Masukkan Pilihan anda-')
            print('1. Tambah Data dengan LifoQueue')
            print('2. Hapus Data LifoQueue')
            print('3. Tampil Data LifoQueue')
            print('4. Jumlah Data LifoQueue')
            print('0. Keluar')
            pilMenu = int(input('masukkan pilihan anda: '))
            print()
            if pilMenu == 1:
                if LifoStack.qsize() == 0:
                    i = 1
                else:
                    i = LifoStack.qsize() + 1
                    
                if LifoStack.full() == False:
                    while i <= Maxsize:
                        item = input(f'Masukkan data ke-{i}: ')
                        LifoStack.put(item)
                        i += 1
                    i=1
                else:
                    print('Data tidak bisa ditambah. Stack Sudah penuh!!')
            
            elif pilMenu == 2:
                if LifoStack.empty() == False:
                    print(f'Elemen terakhir: {LifoStack.get()} telah dihapus!!')
                else:
                    print('Stack kosong. Tidak ada elemen untuk dihapus!!')
            
            elif pilMenu == 3:
                isi = list(LifoStack.queue)
                print('Data dalam Stack adalah:')
                print(isi)
                
            elif pilMenu == 4:
                print(f'Jumlah Data dalam Stack = {LifoStack.qsize()}')

            elif pilMenu == 0:
                pilMenu = False
                break
    elif pil == 0:
        pil = False
        break
    
    else:
        print('Pilihan tidak ada')
        input("\nTekan ENTER untuk melanjutkan...")
        os.system('cls')