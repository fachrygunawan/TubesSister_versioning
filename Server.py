
import xmlrpc.server # Mengimport modul xmlrpc.server
import datetime # Mengimport modul datetime
server_version = 4.2 # Menetapkan versi server

class VersionServer: # Mendefinisikan kelas VersionServer
    def read_file_as_bytes(self, filename):  # Mendefinisikan fungsi bernama read_file_as_bytes yang menerima satu parameter, yaitu filename
        with open(filename, 'rb') as f:  # Membuka file dengan mode 'rb' (baca dalam bentuk byte)
            return f.read()  # Mengembalikan isi file

    def check_version(self, client_version):  # Mendefinisikan fungsi bernama check_version yang menerima satu parameter, yaitu client_version
        if server_version == client_version:  # Membandingkan client_version dengan server_version 
            return client_version
        else:
            return server_version


    def update_version(self, client_version):  # Mendefinisikan fungsi bernama update_version yang menerima satu parameter, yaitu client_version
        # Memperbarui versi client jika versi server lebih baru
        if client_version < server_version:
            new_file = self.read_file_as_bytes('calc.py')  # Memanggil fungsi read_file_as_bytes dengan parameter 'calc.py'
            return server_version, new_file  # Mengembalikan nilai server_version dan new_file
        else:
            empty_bytes = bytes('')  # Menetapkan empty_bytes dengan sebuah objek bytes kosong
            return client_version, empty_bytes  # Mengembalikan nilai client_version dan empty_bytes

    def get_server_time(self):  # Mendefinisikan fungsi bernama get_server_time
        return str(datetime.datetime.now()) # Mengembalikan waktu saat ini di server

server = xmlrpc.server.SimpleXMLRPCServer(("26.64.160.207", 8000)) # Membuat server XML-RPC yang terhubung ke IP 26.64.160.207 di port 8000
server.register_instance(VersionServer()) # Mendaftarkan kelas VersionServer sebagai instance
server.serve_forever() # Menjalankan server selama-lamanya