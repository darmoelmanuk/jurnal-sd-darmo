## Tabel users

* id : INT
* username : VARCHAR(100)
* password : VARCHAR(255)
* role : VARCHAR(20)

## Tabel buku

* id : INT
* judul : VARCHAR(255)
* penulis : VARCHAR(255)
* stok : INT
* kategori_id : INT

## Tabel kategori

* id : INT
* nama_kategori : VARCHAR(100)

## Tabel mahasiswa

* id : INT
* nama : VARCHAR(255)
* nim : VARCHAR(20)

## Tabel peminjaman

* id : INT
* mahasiswa_id : INT
* buku_id : INT
* tanggal_pinjam : DATE
* tanggal_kembali : DATE
* status : VARCHAR(20)
