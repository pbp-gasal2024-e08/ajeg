### Kelompok E08
**Anggota:**	
- Thorbert Anson Shi 		        (2306221900)
- Andreas Timothy 			        (2306259963)
- Meinhard Christian 		        (2306275733)
- Daffa Rayhan Ananda 		        (2306152235)
- Ananda Joy Pratiwi Pasha Patoding (2206811190)
- Muhammad Nadzim Tahara 		    (2306275430)

### Nama Aplikasi	: AJEG 
**Deskripsi Aplikasi	:** 
AJEG adalah kepanjangan dari Ajengan Gede (Menekankan pada makanan dalam porsi besar  atau kuliner yang mengenyangkan). Ajengan berasal dari bahasa bali yang berarti ‘Makanan’. AJEG adalah platform berbasis web yang menawarkan informasi lengkap mengenai kuliner dengan porsi besar atau makanan yang mengenyangkan di Bali. Aplikasi ini bertujuan untuk membantu pengguna menemukan restoran, warung, atau tempat makan yang menyajikan makanan dengan porsi besar yang lezat dan sesuai dengan preferensi mereka. Aplikasi ini menarik wisatawan dan warga lokal yang mencari hidangan mengenyangkan dan otentik. AJEG juga membantu mempromosikan restoran dan warung lokal dengan memberikan platform untuk menjangkau lebih banyak pelanggan.

Referensi arti nama ajengan: https://id.glosbe.com/ban/id/ajengan#:~:text=Periksa%20terjemahan%20dari%20%22ajengan%22%20dalam%20kamus%20Glosbe%20Bali,ngastawa%20indik%20pakaryan%2C%20ajengan%2C%20panganggo%2C%20umah%2C%20lan%20karahayuan.

### Modul Aplikasi AJEG
## Questions and Answers (QnA)
> By: Daffa Rayhan Ananda

Modul QnA adalah modul yang memungkinkan pengguna untuk memberikan suatu pertanyaan terhadap sebuah produk. Berikut adalah alur utama yang akan diimplementasikan dalam modul Checkout.

#### 1. Melihat Pertanyaan
Pengguna atau admin dapat melihat seluruh pertanyaan yang ada terhadap suatu produk. 

#### 2. Memberi Pertanyaan
Pengguna yang sudah terautentikasi dapat menambahkan pertanyaan terhadap produk dari suatu toko.

#### 3. Memjawab Pertanyaan
 Admin pada toko yang bersangkutan dapat menjawab setiap pertanyaan yang ada.

### Fitur Utama
- *Tinjau Pertanyaan*: Melihat seluruh pertanyaan yang ada.
- *Tanya*: Memberikan suatu pertanyaan.
- *Jawab*: Menjawab suatu pertanyaan.

# Checkout
> By: Muhammad Nadzim Tahara
> NPM: 2306275430

Modul Checkout ini dirancang untuk menangani proses checkout makanan dan minuman, mulai dari pemilihan item hingga penyimpanan riwayat pembelian pengguna. Modul ini bertujuan untuk memfasilitasi pengalaman pengguna dalam memesan, membayar, dan melihat pesanan yang sudah dilakukan. Berikut adalah alur utama yang akan diimplementasikan dalam modul Checkout:

###  1. Pemilihan Item
Pengguna dapat memilih item makanan dan minuman yang tersedia di dalam sistem. Item akan ditambahkan ke dalam keranjang belanja (cart) yang bersifat sementara sebelum di-checkout.

### 2. Proses Checkout
Setelah pengguna selesai memilih item, mereka akan diarahkan ke halaman checkout. Di halaman ini, pengguna dapat:

- Meninjau daftar item yang akan dibeli.
- Memilih metode pembayaran yang diinginkan: transfer bank, e-wallet, atau cash on delivery.
- Mengonfirmasi rincian pesanan, termasuk total harga, diskon voucher, dan biaya pengiriman jika ada.

### 3. Pembayaran
Setelah pesanan dikonfirmasi, pengguna akan diarahkan ke halaman pembayaran sesuai dengan metode pembayaran yang dipilih. Proses ini akan disimulasikan.

### 4. Konfirmasi Pesanan
Setelah pembayaran berhasil atau diterima, sistem akan mengirimkan konfirmasi pesanan kepada pengguna. Pesanan ini akan disimpan ke dalam sistem sebagai riwayat pembelian pengguna.

### 5. Riwayat Pembelian
Pengguna dapat mengakses halaman History atau Riwayat Pembelian untuk melihat daftar pesanan yang sudah pernah dilakukan, termasuk rincian seperti tanggal pembelian, item yang dibeli, total biaya, dan status pembayaran.

## Fitur Utama:
- *Keranjang Belanja*: Mengelola item yang dipilih sebelum checkout.
- *Opsi Pembayaran*: Integrasi dengan berbagai metode pembayaran.
- *Validasi Pesanan*: Memastikan ketersediaan item dan verifikasi harga.
- *Konfirmasi Pembelian*: Mengirimkan notifikasi setelah pembelian selesai.
- *Riwayat Pembelian*: Menyimpan dan menampilkan histori transaksi.

## Voucher
> By: Ananda Joy Pratiwi Pasha Patoding

Modul Voucher memungkinkan pengguna untuk mendapatkan potongan harga saat berbelanja di aplikasi AJEG. Berikut adalah alur utama yang akan diimplementasikan:

### 1. Melihat Voucher
Pengguna dapat melihat daftar voucher yang tersedia, termasuk kode, deskripsi, dan tanggal berlaku.

### 2. Mengklaim Voucher
Pengguna dapat mengklaim voucher dengan memasukkan kode voucher yang ingin digunakan. Voucher akan disimpan dalam akun pengguna.

### 3. Menggunakan Voucher
Saat checkout, pengguna dapat memilih voucher yang telah diklaim untuk mendapatkan diskon pada total harga pesanan.

## Fitur Utama:
- *Daftar Voucher*: Melihat semua voucher yang tersedia.
- *Klaim Voucher*: Mengklaim voucher untuk digunakan.
- *Penggunaan Voucher*: Menerapkan voucher saat checkout.

Modul ini bertujuan untuk memberikan bonus kepada pengguna agar lebih sering berbelanja di AJEG.