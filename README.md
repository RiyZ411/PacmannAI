# Project Python Pacmannn
- Nama : Riyan Zaenal Arifin
- Email : riyanzaenal411@gmail.com
## Latar Belakang Masalah
Andi adalah seorang pemilik supermarket besar di salah satu kota di Indonesia. Andi memiliki rencana untuk melakukan perbaikan proses bisnis, yaitu Andi akan membuat sistem kasir yang self-service di supermarket miliknya. Sehingga customer bisa langsung memasukkan item yang dibeli, jumlah item yang dibeli, dan harga item yang dibeli dan fitur yang lain. Sehingga customer yang tidak berada di kota tersebut bisa membeli barang dari supermarket tersebut. Setelah Andi melakukan riset, ternyata Andi memiliki masalah, yaitu Andi membutuhkan Programmer untuk membuatkan fitur-fitur agar bisa sistem kasir self-service di supermarket itu bisa berjalan dengan lancar
## Penjelasan Requirements/Objective
  Penjeasan bisa dilihat di https://docs.google.com/document/d/1TyWrKr4xPFJu3IFwt4vUW5gLXgbNRcQjSYkpGVc376I/preview#heading=h.xni05nwx4sb6
### Penjelasan Flowchart
  ![Flowchart](https://github.com/RiyZ411/Pacmannn/blob/main/Gambar/python.jpg)
### Penjelasan Fungsi
#### transaction.py
   Transaction.py berisi class Transaction yang di dalamnya terdapat beberapa fungsi. Berikut penjelasan fungsi dari class tersebut:
    
    import pandas as pd

    class Transaction:
      def __init__(self):
        """
        Inisialisasi penyimpanan data
        ............................
        self.simpan_item sebagai penyimpanan item/barang (dictionary)
        ............................
        """
        self.simpan_item = {}

      def add_item(self, nama_item, jumlah_item, harga_per_item):
        """
        Fungsi untuk menambah item/barang
        ..........................
        Parameter:
        nama_item (str) akan didefinisikan sebagai key
        jumlah_item (int) dan harga_per_item (int) didefinisikan sebagai value
        ..........................

        """
        self.simpan_item[nama_item] = [jumlah_item, harga_per_item]

      def update_item_name(self, nama_item, update_nama_item):
        """
        Fungsi untuk mengubah nama item/barang
        ................................
        Parameter:
        nama_item (str) untuk mencari nama item/barang yang ingin diubah namanya
        update_nama_item (str) sebagai nama item/barang yang baru dari nama_item
        ................................
        """
        self.simpan_item[update_nama_item] = self.simpan_item[nama_item]
        del self.simpan_item[nama_item]
        print(f'Nama item/barang {nama_item} berhasil diubah menjadi {update_nama_item}')
        print(f'\nItem yang dibeli adalah: {self.simpan_item}')


      def update_item_qty(self, nama_item, update_jumlah_item):
        """
        Fungsi untuk mengubah jumlah item/barang
        ................................
        Parameter:
        nama_item (str) untuk mencari nama item/barang yang ingin diubah jumlahnya
        update_jumlah_item (int) sebagai jumlah item/barang yang baru dari nama_item
        ................................
        """
        for x, y in self.simpan_item.items():
          try:
            if x == nama_item:
              y[0] = update_jumlah_item
              print(f'\nJumlah item/barang {nama_item} berhasil diubah menjadi {update_jumlah_item}')
              print(f'\nItem yang dibeli adalah: {self.simpan_item}')
          except:
            raise Exception('Maaf, item tidak ditemukan')


      def update_item_price(self, nama_item, update_harga_item):
        """
        Fungsi untuk mengubah hara peritem/barang
        .........................................
        nama_item (str) untuk mencari nama item/barang yang ingin diubah jumlahnya
        update_harga_item (int) sebagai harga item/barang yang baru dari nama_item
        .........................................
        """
        for x, y in self.simpan_item.items():
          try:
            if x == nama_item:
              y[1] = update_harga_item
              print(f'\nHarga item/barang {nama_item} berhasil diubah menjadi {update_harga_item}')
              print(f'\nItem yang dibeli adalah: {self.simpan_item}')
          except:
            raise Exception('Maaf, item tidak ditemukan')

      def delete_item(self, nama_item):
        """
        Fungsi untuk menghapus item/barang
        ..................................
        Parameter:
        nama_item (str) untuk mencari nama item/barang yang ingin dihapus
        ..................................
        """
        del self.simpan_item[nama_item]
        print(f'\nItem/barang {nama_item} berhasil dihapus')
        print(f'\nItem yang dibeli adalah: {self.simpan_item}')


      def reset_transaction(self):
        """
        Fungsi untuk menghapus seluruh item/barang
        """
        self.simpan_item.clear()
        print('Semua item berhasil di delete')
        print(f'\nItem yang dibeli adalah: {self.simpan_item}')

      def check_order(self):
        """
        Fungsi untuk mengecek dan menampilkan total harga peritem/barang
        """
        while True:
          if len(self.simpan_item) == 0:
            print(f'\nItem yang dibeli adalah: {self.simpan_item}')
            print('Maaf, item belum ditambah. Silahkan tambah item dulu!')
            return
          else:
            a = 0
            for x, y in self.simpan_item.items():
              x = a
              a+=1
              if type(x) != str and type(y[0]) != int and type(y[1]) != int:
                print(f'\nPesanan {a} Terdapat kesalahan input data')
              else:
                print(f'Pesanan {a} sudah benar')
            print(f'\nItem yang dibeli adalah: {self.simpan_item}')
            print('\n')
            item = pd.DataFrame.from_dict(self.simpan_item, orient ='index', columns=['Jumlah Item', 'Harga/Item'])
            item = item.reset_index()
            item.rename(columns = {'index':'Nama Item'}, inplace = True)
            item['Total Harga'] = item['Jumlah Item'] * item['Harga/Item']
            print(item)
            break

      def total_price(self):
        """
        Fungsi untuk melihat total uang yang harus dibayar 
        dan diskon yang diperoleh customer
        """
        while True:
          if len(self.simpan_item) == 0:
            print(f'\nItem yang dibeli adalah: {self.simpan_item}')
            print('Maaf, item belum ditambah. Silahkan tambah item dulu!')
            return
          else:
            print(f'\nItem yang dibeli adalah: {self.simpan_item}')
            print('\n')
            item = pd.DataFrame.from_dict(self.simpan_item, orient ='index', columns=['Jumlah Item', 'Harga/Item'])
            item = item.reset_index()
            item.rename(columns = {'index':'Nama Item'}, inplace = True)
            item['Total Harga'] = item['Jumlah Item'] * item['Harga/Item']
            print(item)
            Total = item['Total Harga'].sum()
            print(f'\nTotal yang harus dibayarkan!: {Total}')
            if 200000 < Total <= 300000:
              total = Total-(Total * 0.05)
              print('\nSelamat, Anda mendapatkan diskon sebesar 5%')
              print(f'\nTotal yang harus dibayar setelah mendapat diskon!: {total}')
            elif 300000 < Total <= 500000:
              total = Total-(Total * 0.08)
              print('\nSelamat, Anda mendapatkan diskon sebesar 8%')
              print(f'\nTotal yang harus dibayar setelah mendapat diskon!: {total}')
            elif Total > 500000:
              total = Total-(Total * 0.1)
              print('\nSelamat, Anda mendapatkan diskon sebesar 10%')
              print(f'\nTotal yang harus dibayar setelah mendapat diskon!: {total}')
            else:
              print('Maaf, Anda tidak mendapatkan diskon')
          break
#### main.py
  main.py merupakan file interface agar pembeli tidak perlu melakukan penulisan object dari fungsi. File tersebut hanya berisi 1 fungsi sebagai main.

    from transaction import Transaction

    ts = Transaction()

    def main():
      """
      Fungsi sebagai interface agar pembeli tidak perlu ngoding
      """
      while True:
        print('\t\n\n\nSELAMAT DATANG DI TOKO KAMI\n')
        print('Silahkan Pilih Menu di Bawah Ini')
        print('1. Tambah Item/Barang')
        print('2. Ubah Item/Barang')
        print('3. Hapus Item/Barang')
        print('4. Check Item/Barang')
        print('5. Total Bayar')
        print('0. Batal')
        try:
          a = int(input('Masukan Pilihan Angka: '))
          if type(a) == int:
            if a == 1:
              while True:
                while True:
                  try:
                    a = str(input('Nama item/barang : '))
                    b = int(input('Jumlah item/barang : '))
                    c = int(input('Harga per item/barang : '))
                    if type(a) == str and type(b) == int and type(c) == int:
                      ts.add_item(a, b, c)
                      break
                  except:
                    print('\nMohon ulangi!. Pastikan:\n*Nama item harus huruf!\n*Jumlah item harus bilangan bulat!\n*Harga item harus bilangan bulat!\n')
                print(f'\nItem yang dibeli adalah: {ts.simpan_item}')
                d = int(input('\nKetik selain 0 untuk tambah item dan ketik 0 jika sudah!: '))
                if d == 0 and type(d) == int:
                  break
            elif a == 2:
              if len(ts.simpan_item) >= 1:
                while True:
                  try:
                    print('\n1. Ubah Nama Item/Barang')
                    print('2. Ubah Jumlah Item/Barang')
                    print('3. Ubah Harga Peritem/Barang')
                    print('0. Kembali')
                    b = int(input('Masukan Pilihan Angka: '))
                    if b == 1:
                      while True:
                        print(f'\nItem yang dibeli adalah: {ts.simpan_item}')
                        e = str(input('Masukan nama item yang ingin diubah!: '))
                        try:
                          if e in ts.simpan_item:
                            f = str(input('Masukan perubahan nama item!: '))
                            ts.update_item_name(e, f)
                            break
                        except:
                          print('Mohon ulangi!. Pastikan nama item sudah sesuai dan ada di daftar belanja!')
                    elif b == 2:
                      while True:
                        print(f'\nItem yang dibeli adalah: {ts.simpan_item}')
                        g = str(input('Masukan nama item yang ingin diubah jumlahnya!: '))
                        try:
                          if g in ts.simpan_item:
                            h = int(input('Masukan jumlah item terbaru!: '))
                            if type(h) == int:
                              ts.update_item_qty(g, h)
                              break
                        except:
                          print('\nMohon ulangi!. Pastikan: \n*nama item sudah sesuai dan ada di daftar belanja!\n*Pastikan jumlah item berupa bilangan bulat')
                    elif b == 3:
                      while True:
                        print(f'\nItem yang dibeli adalah: {ts.simpan_item}')
                        i = str(input('Masukan nama item yang ingin diubah harganya!: '))
                        try:
                          if g in ts.simpan_item:
                            j = int(input('Masukan harga peritem terbaru!: '))
                            if type(j) == int:
                              ts.update_item_price(i, j)
                              break
                        except:
                          print('\nMohon ulangi!. Pastikan: \n*nama item sudah sesuai dan ada di daftar belanja!\n*Pastikan harga item berupa bilangan bulat')
                    elif b == 0:
                      break
                    else:
                      print('\nMohon ulangi!. Pastikan:\n*Bilangan yang Anda masukan bilangan bulat 1-4!')
                  except:
                    print('\nMohon ulangi!. Pastikan:\n*Bilangan yang Anda masukan bilangan bulat!')
              else:
                print('Maaf, item/barang belum ditambahkan. Silahkan pilih menu tambah item/barang!')
            elif a == 3:
              if len(ts.simpan_item) >= 1:
                while True:
                  try:
                    print('\n1. Hapus satu Item/Barang')
                    print('2. Hapus seluruh Item/Barang')
                    print('0. Kembali')
                    c = int(input('Masukan Pilihan Angka: '))
                    if c == 1:
                      while True:
                        print(f'\nItem yang dibeli adalah: {ts.simpan_item}')
                        k = str(input('Masukan nama item yang ingin dihapus!: '))
                        if k in ts.simpan_item:
                          ts.delete_item(k)
                          break
                        else:
                          print('Mohon ulangi. Pastikan nama item/barang sudah benar')
                    elif c == 2:
                      ts.reset_transaction()
                    elif c == 0:
                      break
                    else:
                      print('\nMohon ulangi!. Pastikan:\n*Bilangan yang Anda masukan bilangan bulat 1-3!')
                  except:
                    print('\nMohon ulangi!. Pastikan:\n*Bilangan yang Anda masukan bilangan bulat!')

              else:
                print('Maaf, item/barang belum ditambahkan. Silahkan pilih menu tambah item/barang!')
            elif a == 4:
              ts.check_order()
            elif a == 5:
              ts.total_price()
            elif a == 0:
              break
            else:
              print('Mohon ulangi!. Pastikan:\n*Bilangan yang Anda masukan bilangan bulat 1-6!')
        except:
          print('Mohon ulangi!. Pastikan:\n*Bilangan yang Anda masukan bilangan bulat!')

    main()
## Alur penggunaan file python
1. Download file transaction.py di repository Pacmann
2. Download file main.py di repository Pacmann
3. Buka file main.py
4. Import module transaction ke dalam file main.py
5. Jalankan program
## Test Case
- Test 1

![pilih](https://github.com/RiyZ411/Pacmannn/blob/main/Gambar/pilih.png)
![pilih1](https://github.com/RiyZ411/Pacmannn/blob/main/Gambar/pilih%201.png)
- Test 2
![pilih](https://github.com/RiyZ411/Pacmannn/blob/main/Gambar/pilih.png)
- Test 3
![pilih](https://github.com/RiyZ411/Pacmannn/blob/main/Gambar/pilih.png)
- Test 4
![pilih](https://github.com/RiyZ411/Pacmannn/blob/main/Gambar/pilih.png)
## Conclusion




