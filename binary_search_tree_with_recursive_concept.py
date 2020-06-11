# Binary Search Tree

def binarySearchTree(data, objek):

    def cari(s, n, objek):

        # Index Tengah 
        c = int((n + s) /2)

        # Data Ditemukan
        if data[c] == objek:
            print("=====Pencarian Berhasil=====")
            print(f"Data[{c}] : {data[c]}")

        # Data Tidak Ditemukan
        elif c == n or n < 0 or s > len(data)-2:
            print("Data Tidak Ditemukan!")

        # Data Lebih Besar Dari Objek
        elif data[c] > objek:
            n = c-1
            cari(s, n, objek)
        
        # Data Lebih Kecil Dari Objek
        elif data[c] < objek:
            s = c+1
            cari(s, n ,objek)


    # Inisialisasi
    s = 0               # index awal pencarian
    n = len(data)       # Index Akhir Pencarian

    objek = objek       # Data yang dicari


    cari(s, n , objek) #Lakukan Pencarian


# Client Side

data = [2, 3, 5, 6, 8, 11, 12, 17, 20, 25]      # Data Terurut
objek = 27     # Objek Pencarian

# Lakukan Pencarian
binarySearchTree(data, objek)

     
