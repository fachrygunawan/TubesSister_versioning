# import modul client xmlrpc, modul base64, dan modul os
import xmlrpc.client
import base64
import os

# Membuat client XML-RPC yang terhubung ke IP 26.64.160.207 di port 8000
client = xmlrpc.client.ServerProxy("http://26.64.160.207:8000")

# definisikan sebuah fungsi untuk membaca sebuah variabel dari sebuah file
def read_variable(filename, variable_name):
    # buka file dalam mode baca
    with open(filename, 'r') as f:
        # jalankan isi file sebagai kode python
        exec(f.read())
        # kembalikan nilai variabel yang ditentukan dalam file
        return locals()[variable_name]

# definisikan sebuah fungsi untuk mengubah sebuah file dengan mengganti nilai sebuah variabel yang ditentukan
def modify_file(filename, variable_name, new_value):
    # ubah nilai baru menjadi string
    new_value_str = str(new_value)
    # buka file dalam mode tulis
    with open(filename, 'w') as f:
        # tulis nilai baru variabel ke file
        f.write(f"{variable_name} = {new_value_str}")

# definisikan sebuah fungsi untuk menulis data ke sebuah file
def write_to_file(filename, data):
    # buka file dalam mode tulis, menggunakan encoding utf-8 dan mengabaikan errors
    with open(filename, 'w', encoding='utf-8', errors='ignore') as f:
        # tulis data ke file
        f.write(data)

# definisikan sebuah fungsi untuk memeriksa versi klien terhadap versi server
def check_version(version):
    # periksa versi dengan menjalankan metode check_version server dan mengirimkan versi klien
    result = client.check_version(version)
    # jika hasil lebih besar dari versi klien, berarti ada versi baru tersedia di server
    if result > version:
        # memberitahu pengguna bahwa ada versi baru tersedia
        print(f"Client Version {version} Outdated, Server version is {result}\n")
        # tanya pengguna apakah mereka ingin memperbarui versi
        update = input("A new version is available. Would you like to update? (y/n) ")
        # jika pengguna ingin memperbarui
        if update == "y":
            # jalankan metode update_version server untuk mendapatkan versi baru dan file kalkulator baru
            new_version, new_file = client.update_version(version)
            # tulis file kalkulator baru ke file di komputer klien
            write_to_file('new_calc.py', str(new_file))
            # modify the client's version file to update the version number
            modify_file('Version.py', 'version', new_version)
            # inform the user that the update was successful
            print(f"Update successful to : {new_version}")
        # jika pengguna tidak ingin memperbarui
        else:
            # memberitahu pengguna bahwa pembaruan ditolak
            print("Version update declined")
    # jika hasil tidak lebih besar dari versi klien, berarti versi klien sudah up to date
    else:
        print("Version Up to date")

# mendefinisikan sebuah fungsi untuk mendapatkan waktu dari server
def get_server_time():
    # jalankan metode get_server_time server dan simpan hasilnya dalam variabel
    time = client.get_server_time()
    # cetak waktu server
    print(f"Server time: {time}")

# buat loop menampilkan menu 
while True:
    # membaca versi klien dari file versi
    client_version = read_variable('Version.py', 'version')
    # menu
    print("Menu:")
    print("1. Check version")
    print("2. Get server time")
    print("3. Open old calculator")
    # jika file kalkulator baru ada di komputer klien, tambahkan pilihan untuk membukanya
    if os.path.exists('new_calc.py'):
        print("4. Open new calculator")
    print("0. Exit")

    # membaca pilihan pengguna dari command line
    choice = input("Enter your choice: ")

    if choice == "1":
        check_version(client_version) # memeriksa versi klien dengan versi di server
    elif choice == "2":
        get_server_time() # mengambil waktu yang ada di server
    elif choice == "3":
        # buka file kalkulator lama dan jalankan isinya
        with open('old_calc.py', 'r') as f:
            exec(f.read())
    elif choice == "4":
        # jika file kalkulator baru ada di komputer klien
        if os.path.exists('new_calc.py'):
            # buka file kalkulator baru dan jalankan isinya
            with open('new_calc.py', 'r') as f:
                exec(f.read())
    elif choice == "0":
        # keluar dari loop 
        break
    else:
        # jika pengguna memasukkan pilihan yang tidak valid
        print("Invalid choice")
