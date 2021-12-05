print("---------- Praktikum ----------")
print()
print("Program Daftar Nilai\n")

Data_Mahasiswa = {} 

def garis():
    print(71*"=")

def header():
    garis()
    print("| {0:^2} | {1:^7} | {2:^18} | {3:^5} | {4:^5} | {5:^5} | {6:^7} |".format("No", "NIM", "Nama", "Tugas", "UTS", "UAS", "Akhir"))
    garis()

def tidakAdaData(): 
    header()          
    print("|{0:^69}|".format("TIDAK ADA DATA!!! Silahkan Tambah Data Terlebih Dahulu"))
    garis()

def tambah():
    print("Tambah Data")
    nim        = input("NIM         : ")
    nama       = input("Nama        : ")
    nilaiTugas = int(input("Nilai Tugas : "))
    nilaiUTS   = int(input("Nilai UTS   : "))
    nilaiUAS   = int(input("Nilai UAS   : "))
    nilaiAkhir = (nilaiTugas * 30/100) + (nilaiUTS * 35/100) + (nilaiUAS * 35/100)
    Data_Mahasiswa[nim] = [nama, nilaiTugas, nilaiUTS, nilaiUAS, nilaiAkhir]
    print(f"Berhasil menambahkan data '{nim}' dengan NAMA : {nama}")

def lihat():
    print("Daftar Mahasiswa")
    if len(Data_Mahasiswa) <= 0:  
        tidakAdaData()
    else:
        no = 0
        header()
        for data in Data_Mahasiswa.items():
            no += 1 
            print(f"| {no:>2} | {data[1][0]:<7} | {data[0]:<18} | {data[1][1]:>5} | {data[1][2]:>5} | {data[1][3]:>5} | {data[1][4]:>7.2f} |")               
        garis() 

def ubah():
    print("Ubah Data Mahasiswa berdasarkan Nim")
    if len(Data_Mahasiswa) <= 0:  
        tidakAdaData()

    else:
        nim = input("Masukan Nim : ") 
        if nim in Data_Mahasiswa.keys():
            print(f"Nim        = {nim}")
            print(f"NAMA         = {Data_Mahasiswa[nim][0]}")
            print(f"Nilai Tugas = {Data_Mahasiswa[nim][1]}")
            print(f"Nilai UTS   = {Data_Mahasiswa[nim][2]}")
            print(f"Nilai UAS   = {Data_Mahasiswa[nim][3]}")
            print(25*"=")
            print("1. Nim\n2. NAMA\n3. Nilai\n0. Kembali")
            tanya = int(input("Apa yang ingin diubah? [1-3] : "))
            if tanya == 1:
                _nim = input("Masukan Nim Baru : ")
                Data_Mahasiswa[_nim] = Data_Mahasiswa.pop(nim)
                print("Berhasil merubah Nim! ")

            elif tanya == 2:
                _nama = input("Masukan Nama Baru : ")
                Data_Mahasiswa[nama][0] = _nama
                print("Berhasil merubah NAMA!")

            elif tanya == 3:
                _nilaiTugas = int(input("Masukan Nilai Tugas Baru : "))
                _nilaiUTS = int(input("Masukan Nilai UTS Baru : "))
                _nilaiUAS = int(input("Masukan Nilai UAS Baru : "))
                _nilaiAkhir = _nilaiTugas * 30/100 + _nilaiUTS * 35/100 + _nilaiUAS * 35/100
                Data_Mahasiswa[nim][1:4] = _nilaiTugas, _nilaiUTS, _nilaiUAS, _nilaiAkhir
                print("Berhasil merubah data nilai!")
            elif tanya == 0:
                pass
            
            else:
                print(f"Pilihan {tanya} tidak ada! Silahkan masukan [1-3]")

        else:
            print(f"Data {nim} tidak ditemukan!") 

def hapus():
    print("Hapus Data Mahasiswa berdasarkan Nim")
    if len(Data_Mahasiswa) <= 0:  
        tidakAdaData()

    else:
        nim = input("Masukan nim : ")
        if(nim in Data_Mahasiswa):
            del Data_Mahasiswa[nim]
            print(f"Data {nama} berhasil dihapus!")
        else:
            print(f"Data {nim} tidak ditemukan!")

loop = True
while loop:
    print()
    print(71*"-")
    print(25*"-", "Program Input Nilai", 25*"-")
    print(71*"-")
    menu = input("[(T)ambah, (L)ihat, (U)bah, (H)apus, (K)eluar]: ")
    print()

    if menu == "T" or menu == "t":     
        tambah()

    elif menu == "L" or menu == "l":
        lihat()

    elif menu == "U" or menu == "u":
        ubah() 

    elif menu == "H" or menu == "h":
        hapus()

    elif menu == "K" or menu == "k":
        print("Program selesai")
        print()
        loop = False 

    else:
        print(f"Menu '{menu}' tidak ada!")