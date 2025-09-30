def atur_genap_ganjil(daftar_angka):
    genap = []
    ganjil = []

    for angka in daftar_angka:
        if angka % 2 == 0:  # Cek jika angka genap
            genap.append(angka)
        else:  # Jika tidak, berarti angka ganjil
            ganjil.append(angka)

    # Menggabungkan list genap dan ganjil
    return genap + ganjil

# Meminta input dari user
input_str = input("Masukkan daftar angka, dipisahkan oleh spasi: ")

try:
    # Mengubah string input menjadi list of integer
    list_angka = [int(x) for x in input_str.split()]

    # Panggil fungsi untuk mengurutkan
    list_terurut = atur_genap_ganjil(list_angka)

    # Cetak hasilnya
    print("Daftar angka yang sudah diurutkan:", list_terurut)

except ValueError:
    print("Input tidak valid. Pastikan Anda hanya memasukkan angka.")