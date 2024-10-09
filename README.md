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