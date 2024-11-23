# Capstone Project by Perdiansyah Ramadan
# JDCSOL-017-2-ONLINE

data_pasien = [
    {
        'ID Pasien' : '0001',
        'Nama Lengkap' : 'Perdiansyah Ramadan',
        'Umur' : 28,
        'Penyakit' : 'Masuk Angin',
        'Metode Pembayaran' : 'Asuransi'
    },
    {
        'ID Pasien' : '0002',
        'Nama Lengkap' : 'Raidah Fauziah',
        'Umur' : 29,
        'Penyakit' : 'Sakit Gigi',
        'Metode Pembayaran' : 'Mandiri'
    },
    {
        'ID Pasien' : '0003',
        'Nama Lengkap' : 'Muhammad Abdul Muiz',
        'Umur' : 16,
        'Penyakit' : 'Batuk Pilek',
        'Metode Pembayaran' : 'Asuransi'
    }
]

def menu_utama():
    print('------------------------------------------')
    print('Selamat datang di Menu Utama Data Pasien ')
    print('------------------------------------------')
    print('[1] Menampilkan Data Pasien Rumah Sakit')
    print('[2] Menambahkan Data Pasien Rumah Sakit')
    print('[3] Mengubah Data Pasien Rumah Sakit')
    print('[4] Menghapus Data Pasien Rumah Sakit')
    print('[5] Keluar Program (Exit)')
    print('------------------------------------------')    
    while True:
        input_menu_utama = int(input('Silahkan masukan angka (1-5): '))
        if input_menu_utama == 1:
            menampilkan_data_pasien()
            break
        elif input_menu_utama == 2:
            menambahkan_data_pasien()
            break
        elif input_menu_utama == 3:
            mengubah_data_pasien()
            break
        elif input_menu_utama == 4:
            menghapus_data_pasien()
            break
        elif input_menu_utama == 5:
            keluar()
            break
        else:
            print('Data yang dimasukan tidak sesuai')
            
def menampilkan_data_pasien():
    print('------------------------------------------')
    print('Pilihan Menu untuk Menampilkan Data Pasien ')
    print('------------------------------------------')
    print('[1] Tampilkan Seluruh Data Pasien')
    print('[2] Mencari Data Pasien Berdasarkan ID')
    print('[3] Kembali ke Menu Utama')
    print('[4] Keluar Program (Exit)')
    print('----------------------------------------')
    while True:
        input_menu_menampilkan = int(input('Silahkan masukan angka (1-4): '))
        print('------------------------------------------')
        if input_menu_menampilkan == 1:
            print('----------------------------------------------------------------------------')
            print('ID\t| Nama Lengkap   \t| Umur \t| Penyakit \t| Metode Pembayaran')
            print('----------------------------------------------------------------------------')
            for data in data_pasien:
                print(f"{data['ID Pasien']} \t| {data['Nama Lengkap']} \t| {data['Umur']} \t| {data['Penyakit']} \t| {data['Metode Pembayaran']}")
            print('----------------------------------------------------------------------------')
            kembali_menu_utama()
            break
        elif input_menu_menampilkan == 2:
            while True:
                input_validasi_id = input('Masukan ID Pasien yang ingin dicari: ')
                validasi_id = False
                for data in data_pasien:
                    if data['ID Pasien'] == input_validasi_id:
                        print('------------------------------------------')
                        print(f'Data pasien [{input_validasi_id}] ditemukan ')
                        print('------------------------------------------')
                        print(f"[#] ID Pasien         : {data['ID Pasien']}")
                        print(f"[#] Nama Lengkap      : {data['Nama Lengkap']}")
                        print(f"[#] Umur Pasien       : {data['Umur']}")
                        print(f"[#] Penyakit Pasien   : {data['Penyakit']}")
                        print(f"[#] Metode Pembayaran : {data['Metode Pembayaran']}")
                        print('------------------------------------------')
                        validasi_id = True
                        kembali_menu_utama()
                        break
                if validasi_id == False:
                    print('Data tidak ditemukan')
                else:
                    break
            break
        elif input_menu_menampilkan == 3:
            kembali_menu_utama()
            break
        elif input_menu_menampilkan == 4:
            keluar()
            break
        else:
            print('Data yang dimasukan tidak sesuai')

def menambahkan_data_pasien():
    print('------------------------------------------')
    print('Pilihan Menu untuk Menambahkan Data Pasien')
    print('------------------------------------------')
    print('[1] Menambahkan Data Pasien Baru')
    print('[2] Kembali ke Menu Utama')
    print('[3] Keluar Program (Exit)')
    print('----------------------------------------')
    while True:
        input_menu_menambahkan = int(input('Silahkan masukan angka (1-3): '))
        print('------------------------------------------')
        if input_menu_menambahkan == 1:
            while True:
                input_id = input("Masukkan ID Pasien: ")
                validasi_id = False
                for data in data_pasien:
                    if data['ID Pasien'] == input_id:
                        print('Data telah terdaftar, mohon masukan data lain')
                        validasi_id = True
                        break
                if validasi_id == False:
                    input_nama = input("Masukkan Nama Lengkap Pasien: ")
                    input_umur = input("Masukkan Umur Pasien: ")
                    input_penyakit = input("Masukkan Penyakit/Keluhan Pasien: ")
                    
                    input_metode_pembayaran = input("Masukkan Metode Pembayaran yang digunakan (Asuransi/Mandiri): ")

                    print('------------------------------------------')
                    print('Data pasien yang ingin ditambahkan')
                    print(f"ID Pasien        : {input_id}")
                    print(f"Nama Lengkap     : {input_nama}")
                    print(f"Umur             : {input_umur}")
                    print(f"Penyakit/Keluhan : {input_penyakit}")
                    print(f"Metode Pembayaran: {input_metode_pembayaran}")
                    print('------------------------------------------')
                    input_simpan_data = input('Apakah anda yakin ingin menambahkan data diatas? (ya/tidak): ')
                    if input_simpan_data == 'ya':
                        data_pasien.append({
                            'ID Pasien' : input_id,
                            'Nama Lengkap' : input_nama,
                            'Umur' : input_umur,
                            'Penyakit' : input_penyakit,
                            'Metode Pembayaran' : input_metode_pembayaran
                        })
                        print('Selamat, data berhasil ditambahkan!')
                        kembali_menu_utama()
                        break
                    elif input_simpan_data == 'tidak':
                        kembali_menu_utama()
                        break
            break
        elif input_menu_menambahkan == 2:
            kembali_menu_utama()
            break
        elif input_menu_menambahkan == 3:
            keluar()
            break
        else:
            print('Data yang dimasukan tidak sesuai')

def mengubah_data_pasien():
    while True:
        input_validasi_id = input('Masukan ID Pasien yang ingin diubah: ')
        validasi_id = False
        for data in data_pasien:
            if data['ID Pasien'] == input_validasi_id:
                validasi_id = True
                print('----------------------------------')
                print(' **** Data Pasien ditemukan ****  ')
                print('----------------------------------')
                print(f"[1] ID Pasien           : {data['ID Pasien']}")
                print(f"[2] Nama Lengkap Pasien : {data['Nama Lengkap']}")
                print(f"[3] Umur Pasien         : {data['Umur']}")
                print(f"[4] Penyakit            : {data['Penyakit']}")
                print(f"[5] Metode Pembayaran   : {data['Metode Pembayaran']}")
                print('----------------------------------')
                while True:
                    input_menu_ubah_data = int(input('Pilih kolom yang ingin diubah (1-5): '))
                    if input_menu_ubah_data == 1:
                        data_id_lama = data['ID Pasien']
                        input_id_baru = input('Masukan ID baru: ')
                        data['ID Pasien'] = input_id_baru
                        print(f'ID sudah diubah dari {data_id_lama} menjadi {input_id_baru}')
                        kembali_menu_utama()
                        break
                    elif input_menu_ubah_data == 2:
                        data_nama_lama = data['Nama Lengkap']
                        input_nama_baru = input('Masukan Nama Lengkap baru: ')
                        data['Nama Lengkap'] = input_nama_baru
                        print(f'Nama Lengkap sudah diubah dari {data_nama_lama} menjadi {input_nama_baru}')
                        kembali_menu_utama()
                        break
                    elif input_menu_ubah_data == 3:
                        data_umur_lama = data['Umur']
                        input_umur_baru = input('Masukan Umur baru: ')
                        data['Umur'] = input_umur_baru
                        print(f'Umur sudah diubah dari {data_umur_lama} menjadi {input_umur_baru}')
                        kembali_menu_utama()
                        break
                    elif input_menu_ubah_data == 4:
                        data_penyakit_lama = data['Penyakit']
                        input_penyakit_baru = input('Masukan Penyakit baru: ')
                        data['Penyakit'] = input_penyakit_baru
                        print(f'Penyakit sudah diubah dari {data_penyakit_lama} menjadi {input_penyakit_baru}')
                        kembali_menu_utama()
                        break
                    elif input_menu_ubah_data == 5:
                        data_metode_pembayaran_lama = data['Metode Pembayaran']
                        input_metode_pembayaran_baru = input('Masukan Metode Pembayaran baru: ')
                        data['Metode Pembayaran'] = input_metode_pembayaran_baru
                        print(f'Metode Pembayaran sudah diubah dari {data_metode_pembayaran_lama} menjadi {input_metode_pembayaran_baru}')
                        kembali_menu_utama()
                        break
                    else:
                        print('Inputan tidak sesuai')
                        break
        if validasi_id == False:
            print('Data tidak ditemukan, silahkan coba lagi')
        else:
            break

def menghapus_data_pasien():
    while True:
        input_validasi_id = input('Masukan ID Pasien yang ingin dihapus: ')
        validasi_id = False
        for data in data_pasien:
            if data['ID Pasien'] == input_validasi_id:
                validasi_id = True
                print('----------------------------------')
                print(' **** Data Pasien ditemukan ****  ')
                print('----------------------------------')
                print(f"[1] ID Pasien           : {data['ID Pasien']}")
                print(f"[2] Nama Lengkap Pasien : {data['Nama Lengkap']}")
                print(f"[3] Umur Pasien         : {data['Umur']}")
                print(f"[4] Penyakit            : {data['Penyakit']}")
                print(f"[5] Metode Pembayaran   : {data['Metode Pembayaran']}")
                print('----------------------------------')
                konfirmasi_hapus_data = input('Apakah kamu yakin ingin menghapus data tersebut? (ya/tidak): ')
                if konfirmasi_hapus_data == 'ya':
                    data_pasien.remove(data)
                    print(f'Data {input_validasi_id} telah berhasil dihapus')
                    kembali_menu_utama()
                    break
                elif konfirmasi_hapus_data == 'tidak':
                    kembali_menu_utama()
                    break
                else:
                    print('Inputan tidak sesuai')
                break
        if validasi_id == False:
            print('Data tidak ditemukan')
        else:
            break

def kembali_menu_utama():
    while True:
        input_kembali_menu_utama = input('Apakah ingin kembali ke menu utama? (ya/tidak): ')
        if input_kembali_menu_utama == 'ya':
            menu_utama()
            break
        elif input_kembali_menu_utama == 'tidak':
            print('Anda telah keluar, terima kasih telah mencoba program ini!')
            break
        else:
            print('Data yang dimasukan tidak sesuai')

def keluar():
    while True:
        input_keluar = input('Apakah ingin keluar program? (ya/tidak): ')
        if input_keluar == 'ya':
            print('Anda telah keluar, terima kasih telah mencoba program ini!')
            break
        elif input_keluar == 'tidak':
            menu_utama()
            break
        else:
            print('Data yang dimasukan tidak sesuai')

#--------------
menu_utama()
