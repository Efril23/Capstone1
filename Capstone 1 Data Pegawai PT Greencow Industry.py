# Data Pegawai PT Greencow Industry

listPegawai = [
    {
        'nama': 'Feryzal Putera',
        'nip': '71012281',
        'status': 'Tetap',
        'grade': 'E',
        'gaji': 25800000		
    },
    {
        'nama': 'Intan Mayasari',
        'nip': '85327238',
        'status': 'Tetap',
        'grade': 'D', 
        'gaji': 15750000
    },
    {
        'nama': 'Satrio Pinandito',
        'nip': '96410516',
        'status': 'Kontrak',
        'grade': 'C',
        'gaji': 6970000
    },
    {
        'nama': 'Septia Lupita',
        'nip': '98033394',
        'status': 'Kontrak',
        'grade': 'C',
        'gaji': 5750000
    },
    {
        'nama': 'Anisa Aprilia',
        'nip': '90010900',
        'status': 'Tetap',
        'grade': 'D',
        'gaji': 9965000
    },
    {
        'nama': 'Arif Mumtaz',
        'nip': '87547310',
        'status': 'Tetap',
        'grade': 'E',
        'gaji': 19378000
    }
]

laporanPegawai = []

from prettytable import PrettyTable

def menampilkanDataPegawai():
    table = PrettyTable()
    table.field_names = ['Index', 'Nama', 'NIP', 'Status', 'Grade', 'Gaji']

    for i, pegawai in enumerate(listPegawai):
        table.add_row([i, pegawai['nama'], pegawai['nip'], pegawai['status'], pegawai['grade'], pegawai['gaji']])

    print(table)

def cariPegawaiByNip(nip):
    for pegawai in listPegawai:
        if pegawai['nip'] == nip:
            return pegawai
    return None


def reportDataPegawai():
    while True:
        pilihanMenu = input('''
            1. Report Seluruh Data Pegawai
            2. Report Data Pegawai by NIP
            3. Kembali ke Menu Utama

            Masukkan angka pilihan Sub Menu yang ingin dijalankan : ''')

        if pilihanMenu == '1':
            menampilkanDataPegawai()
        elif pilihanMenu == '2':
            nip = input('Masukkan NIP pegawai : ')
            hasilPencarian = cariPegawaiByNip(nip)
            if hasilPencarian:
                print(f"Data Pegawai dengan NIP {nip}: {hasilPencarian}")
            else:
                print(f"Tidak ada data pegawai dengan NIP {nip}")
        elif pilihanMenu == '3':
            break
        else:
            print("Pilihan tidak valid. Silakan pilih 1, 2, atau 3.")

def menambahDataPegawai():
    while True:
        pilihanMenu = input('''
            1. Tambah Data Pegawai
            2. Kembali ke Menu Utama
          
            Masukkan angka pilihan Sub Menu yang ingin dijalankan : ''')

        if pilihanMenu == '1':
            nip = input('Masukkan NIP pegawai : ')

            if not nip.isdigit() or len(nip) != 8:
                print("Format NIP tidak valid. NIP harus berupa 8 digit angka.")
                continue  

            hasilPencarian = cariPegawaiByNip(nip)
            if hasilPencarian:
                print(f"Data Pegawai dengan NIP {nip} sudah ada")
            else:
                namaPegawai = input('Masukkan Nama Pegawai : ')
                nipPegawai = nip  
                statusPegawai = input('Masukkan Status Pegawai : ')
                gradePegawai = input('Masukkan Grade Pegawai : ')

                if gradePegawai not in ['A', 'B', 'C', 'D', 'E']:
                    print("Grade tidak valid. Pilih antara A, B, C, D, atau E.")
                    continue  
                
                while True:
                    try:
                        gajiPegawai = int(input('Masukkan Gaji Pegawai : '))
                        if gajiPegawai < 0:
                            print("Gaji Pegawai harus berupa angka non-negatif.")
                            continue
                        break  

                    except ValueError:
                        print("Masukkan gaji dalam bentuk angka.")

                listPegawai.append({
                    'nama': namaPegawai,
                    'nip': nipPegawai,
                    'status': statusPegawai,
                    'grade': gradePegawai,
                    'gaji': gajiPegawai
                })

                checker = input('Data akan disimpan? (ya/tidak) = ')
                if checker.lower() == 'ya':
                    print("Data Pegawai sudah tersimpan")
                elif checker.lower() == 'tidak':
                    print("Data Pegawai tidak disimpan")
                else:
                    print("Pilihan tidak valid. Silakan pilih ya atau tidak.")
        elif pilihanMenu == '2':
            break
        else:
            print("Pilihan tidak valid. Silakan pilih 1 atau 2.")

def menghapusDataPegawai():
    while True:
        pilihanMenu = input('''
            1. Hapus Data Pegawai by NIP
            2. Kembali ke Menu Utama
          
            Masukkan angka pilihan Sub Menu yang ingin dijalankan : ''')

        if pilihanMenu == '1':
            nip = input('Masukkan NIP pegawai : ')
            hasilPencarian = cariPegawaiByNip(nip)
            if hasilPencarian:
                checker = input('Data akan dihapus? (ya/tidak) = ')
                if checker.lower() == 'ya':
                    listPegawai.remove(hasilPencarian)
                    print("Data Pegawai telah berhasil dihapus")
                elif checker.lower() == 'tidak':
                    print("Data Pegawai batal dihapus")
                else:
                    print("Pilihan tidak valid. Silakan pilih ya atau tidak.")
            else:
                print(f"Tidak ada data pegawai dengan NIP {nip}")
        elif pilihanMenu == '2':
            break
        else:
            print("Pilihan tidak valid. Silakan pilih 1 atau 2.")

def mengubahDataPegawai():
    while True:
        pilihanMenu = input('''
            1. Ubah Data Pegawai
            2. Kembali ke Menu Utama
          
            Masukkan angka pilihan Sub Menu yang ingin dijalankan : ''')

        if pilihanMenu == '1':
            nip = input('Masukkan NIP pegawai yang ingin diubah : ')
            hasilPencarian = cariPegawaiByNip(nip)
            
            if hasilPencarian:
                print(f"Data Pegawai dengan NIP {nip}: {hasilPencarian}")
                checker = input('Data akan diubah? (ya/tidak) = ')
                
                if checker.lower() == 'ya':
                    while True:
                        pilihanKolom = input('''
                            1. Nama
                            2. NIP
                            3. Status
                            4. Grade
                            5. Gaji
                            
                            Masukkan pilihan Kolom Data Pegawai yang ingin diubah (1-5) atau tekan 'Enter' untuk selesai: ''')

                        if pilihanKolom == '1':
                            hasilPencarian['nama'] = input('Masukkan Nama Pegawai baru: ')
                        elif pilihanKolom == '2':
                            hasilPencarian['nip'] = input('Masukkan NIP Pegawai baru: ')
                        elif pilihanKolom == '3':
                            hasilPencarian['status'] = input('Masukkan Status Pegawai baru: ')
                        elif pilihanKolom == '4':
                            gradeBaru = input('Masukkan Grade Pegawai baru: ')
                            if gradeBaru not in ['A', 'B', 'C', 'D', 'E']:
                                print("Grade tidak valid. Pilih antara A, B, C, D, atau E.")
                                continue
                            hasilPencarian['grade'] = gradeBaru
                        elif pilihanKolom == '5':
                            while True:
                                try:
                                    gajiBaru = int(input('Masukkan Gaji Pegawai baru: '))
                                    if gajiBaru < 0:
                                        print("Gaji Pegawai harus berupa angka non-negatif.")
                                        continue
                                    hasilPencarian['gaji'] = gajiBaru
                                    break
                                except ValueError:
                                    print("Masukkan gaji dalam bentuk angka.")
                        elif pilihanKolom == '':
                            print("Perubahan data Pegawai berhasil disimpan")
                            break
                        else:
                            print("Pilihan tidak valid. Silakan pilih 1-5 atau tekan 'Enter'.")
                else:
                    print("Perubahan data Pegawai tidak disimpan")
            else:
                print(f"Tidak ada data pegawai dengan NIP {nip}")
        elif pilihanMenu == '2':
            break
        else:
            print("Pilihan tidak valid. Silakan pilih 1 atau 2.")

def menghitungDataPegawai():
    while True:
        pilihanMenu = input('''
            1. Hitung Jumlah Pegawai
            2. Hitung Total Gaji Pegawai
            3. Hitung Average Gaji Pegawai
            4. Kembali ke Menu Utama

            Masukkan angka pilihan Sub Menu yang ingin dijalankan : ''')

        if pilihanMenu == '1':
            hitungJumlahPegawai()
        elif pilihanMenu == '2':
            hitungTotalGajiPegawai()
        elif pilihanMenu == '3':
            hitungAverageGajiPegawai()
        elif pilihanMenu == '4':
            break
        else:
            print("Pilihan tidak valid. Silakan pilih 1, 2, 3, atau 4.")

def hitungJumlahPegawai():
    total_pegawai = len(listPegawai)
    if total_pegawai == 0:
        print("Tidak ada data pegawai.")
    else:
        print(f"Total Pegawai: {total_pegawai}")

def hitungTotalGajiPegawai():
    total_gaji = sum(pegawai['gaji'] for pegawai in listPegawai)
    if total_gaji == 0:
        print("Tidak ada data gaji pegawai.")
    else:
        print(f"Total Gaji: {total_gaji}")

def hitungAverageGajiPegawai():
    total_pegawai = len(listPegawai)
    total_gaji = sum(pegawai['gaji'] for pegawai in listPegawai)

    if total_pegawai == 0:
        print("Tidak ada data pegawai.")
    else:
        average_gaji = total_gaji / total_pegawai
        print(f"Average Gaji: {average_gaji}")


while True :
    pilihanMenu = input('''
        Selamat Datang di PT Greencow Industry

        Data Pegawai PT Greencow Industry:
        1. Report Data Pegawai
        2. Menambah Data Pegawai
        3. Menghapus Data Pegawai
        4. Mengubah Data Pegawai
        5. Menghitung Data Pegawai
        6. Exit Program

        Masukkan angka pilihan Menu yang ingin dijalankan : ''')

    if(pilihanMenu == '1') :
        reportDataPegawai()
    elif(pilihanMenu == '2') :
        menambahDataPegawai()
    elif(pilihanMenu == '3') :
        menghapusDataPegawai()
    elif(pilihanMenu == '4') :
        mengubahDataPegawai ()
    elif(pilihanMenu == '5') :
        menghitungDataPegawai ()
    elif(pilihanMenu == '6') :
        break
    else:
        print("Pilihan menu tidak valid. Silakan pilih 1, 2, 3, 4, 5, atau 6.")
