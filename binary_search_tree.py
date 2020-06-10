# Binary Search Tree

def binarySearchTree(data, objek):
    
    # Inisialisasi
    i = "1"             # Indikator Perulangan
    s = 0               # index awal pencarian
    n = len(data)       # Index Akhir Pencarian

    objek = objek       # Data yang dicari

    # Memulai Pencarian
    while i == "1":

        # Index Tengah 
        c = int((n + s) /2)

        # Data Ditemukan
        if data[c] == objek:
            print("=====Pencarian Berhasil=====")
            print(f"Data[{c}] : {data[c]}")
            i = "0"         # Stop Pencarian
        
        # Data Lebih Besar Dari Objek
        elif data[c] > objek:
            n = c-1
        
        # Data Lebih Kecil Dari Objek
        elif data[c] < objek:
            s = c+1


# Client Side

data = [2, 3, 5, 6, 8, 11, 12, 17, 20, 25]      # Data Terurut
objek = 6       # Objek Pencarian

# Lakukan Pencarian
binarySearchTree(data, objek)

     
