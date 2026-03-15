# Program Nilai & Predikat Mahasiswa

Program Python untuk menginput, memproses, dan memvisualisasikan nilai mahasiswa secara interaktif menggunakan `matplotlib`.

---

## Daftar Isi

- [Cara Menjalankan](#cara-menjalankan)
- [Penjelasan Konsep Array](#1-penjelasan-konsep-array)
- [Analisis Kompleksitas](#2-analisis-kompleksitas)
- [Refleksi Pembelajaran](#3-refleksi-pembelajaran)

---

## Cara Menjalankan

### Prasyarat

Pastikan Python dan library berikut sudah terinstal:

```bash
pip install matplotlib numpy
```

### Menjalankan Program

```bash
python program_nilai.py
```

Program akan meminta input data untuk setiap mahasiswa secara berurutan:

```
Data Mahasiswa ke-1

Nama Mahasiswa :
NIM            :
Nilai Tugas    :
Nilai UTS      :
Nilai UAS      :
```

### Output yang Dihasilkan

- Tabel rekap nilai di terminal
- Ringkasan nilai tertinggi, terendah, dan data kelulusan
- Tiga grafik visualisasi yang otomatis tersimpan sebagai `grafik_nilai.png`

### Tampilan Input di Terminal

> 📸 *Letakkan screenshot tampilan input terminal di sini*

![Tampilan Input Terminal](images/input_terminal.png)

### Tampilan Rekap Tabel di Terminal

> 📸 *Letakkan screenshot tampilan tabel rekap nilai di sini*

![Tampilan Rekap Tabel](images/rekap_tabel.png)

---

## 1. Penjelasan Konsep Array

Program ini menggunakan **list** sebagai implementasi array di Python. List digunakan untuk menyimpan dan mengelola data lebih dari satu mahasiswa secara terstruktur.

### List of Dictionary

`mahasiswa_list` adalah array utama yang menyimpan setiap mahasiswa sebagai sebuah dictionary:

```python
mahasiswa_list = []  # array kosong

mahasiswa_list.append({
    "No"       : i,
    "Nama"     : nama,
    "NIM"      : nim,
    "Tugas"    : tugas,
    "UTS"      : uts,
    "UAS"      : uas,
    "Rata-rata": round(rata_rata, 2),
    "Grade"    : grade,
    "Predikat" : predikat,
    "Status"   : status,
})
```

Setiap elemen array berisi satu record mahasiswa lengkap. Pendekatan ini memudahkan akses data berdasarkan nama key, misalnya `mhs["Nama"]` atau `mhs["Rata-rata"]`.

### List Comprehension untuk Ekstraksi Data

Saat data dibutuhkan untuk grafik, array dipecah menjadi list-list terpisah menggunakan **list comprehension**:

```python
nama_list  = [mhs["Nama"]      for mhs in mahasiswa_list]
rata_list  = [mhs["Rata-rata"] for mhs in mahasiswa_list]
tugas_list = [mhs["Tugas"]     for mhs in mahasiswa_list]
uts_list   = [mhs["UTS"]       for mhs in mahasiswa_list]
uas_list   = [mhs["UAS"]       for mhs in mahasiswa_list]
```

Teknik ini menghasilkan array satu dimensi yang siap dikonsumsi oleh `matplotlib` tanpa perlu loop manual.

### Operasi Array yang Digunakan

| Operasi | Sintaks | Keterangan |
|---|---|---|
| Inisialisasi | `mahasiswa_list = []` | Membuat array kosong |
| Tambah elemen | `mahasiswa_list.append({...})` | Menambah data di akhir array |
| Iterasi | `for mhs in mahasiswa_list` | Membaca seluruh elemen |
| Akses elemen | `mhs["Nama"]` | Akses berdasarkan key |
| Pencarian nilai | `max()`, `min()` | Mencari nilai ekstrem |
| Hitung kemunculan | `.count("LULUS")` | Menghitung elemen tertentu |

---

## 2. Analisis Kompleksitas

### Kompleksitas Waktu

| Bagian Program | Kompleksitas | Keterangan |
|---|---|---|
| Input data mahasiswa | O(n) | Loop sebanyak n mahasiswa |
| Validasi nilai (`while True`) | O(1) per mahasiswa | Maksimal input ulang konstan |
| Kalkulasi rata-rata & grade | O(1) per mahasiswa | Operasi aritmatika tetap |
| `append` ke list | O(1) amortized | Penambahan elemen di akhir list |
| Cetak rekap tabel | O(n) | Iterasi seluruh list |
| List comprehension grafik | O(n) per list | Ekstraksi 5 list = 5 × O(n) |
| `max()` dan `min()` | O(n) | Scan seluruh elemen |
| Render grafik matplotlib | O(n) | Sebanding jumlah data |
| **Total keseluruhan** | **O(n)** | Didominasi operasi linear |

### Kompleksitas Ruang

| Struktur Data | Ruang | Keterangan |
|---|---|---|
| `mahasiswa_list` | O(n) | Menyimpan n record mahasiswa |
| List grafik (5 list) | O(n) | Masing-masing sepanjang n |
| Variabel sementara | O(1) | `rata_rata`, `grade`, dll. |
| **Total** | **O(n)** | Linear terhadap jumlah mahasiswa |

Program ini sangat efisien karena tidak menggunakan nested loop maupun struktur data berlapis, sehingga kompleksitas waktu dan ruang keduanya tetap **O(n)** — linear dan sebanding langsung dengan jumlah mahasiswa yang diinput.

---

## 3. Refleksi Pembelajaran

### Apa yang Dipelajari

Program ini mencakup beberapa konsep pemrograman yang saling berkaitan. Pertama, penggunaan **array (list)** sebagai struktur data utama untuk menyimpan kumpulan data yang homogen — dalam hal ini data mahasiswa. Memahami bahwa array bukan sekadar tempat penyimpanan, melainkan fondasi untuk seluruh operasi berikutnya seperti pencarian, kalkulasi, dan visualisasi.

Kedua, kombinasi **`for` loop dan `while` loop** dalam satu program mengajarkan kapan harus mengulang sejumlah tetap iterasi (jumlah mahasiswa) dan kapan harus mengulang sampai kondisi terpenuhi (validasi input). Keduanya punya tujuan berbeda dan tidak bisa saling menggantikan begitu saja.

Ketiga, konsep **pemisahan tanggung jawab** — bagian input, bagian pemrosesan, dan bagian output dipisahkan dengan jelas. Data dikumpulkan dulu semuanya, baru kemudian ditampilkan dan divisualisasikan. Pendekatan ini membuat program lebih mudah dibaca, diuji, dan dikembangkan.

### Tantangan yang Ditemui

Kesalahan paling umum dalam program ini adalah **masalah indentasi** — blok `while True` yang seharusnya berada di dalam `for` loop justru berada di luar, sehingga hanya mahasiswa terakhir yang mendapat input nilai. Ini adalah contoh nyata bagaimana satu tab indentasi yang salah bisa mengubah seluruh logika program secara drastis tanpa menimbulkan error sama sekali dari Python.

### Pengembangan Selanjutnya

Program ini masih bisa dikembangkan lebih lanjut, misalnya dengan:

- Menyimpan data ke file **CSV atau database** agar data tidak hilang setelah program ditutup
- Menambahkan fitur **pencarian dan pengurutan** berdasarkan nama atau nilai
- Membuat **antarmuka grafis** menggunakan library seperti `tkinter` atau framework web
- Menambahkan **ekspor laporan** dalam format PDF atau Excel

---

## Struktur Program

```
program_nilai.py
│
├── Input Data (for loop)
│   ├── Nama & NIM
│   └── Nilai Tugas, UTS, UAS (dengan validasi while loop)
│
├── Pemrosesan
│   ├── Hitung rata-rata
│   ├── Tentukan grade & predikat
│   └── Simpan ke mahasiswa_list
│
├── Output Tabel
│   └── Cetak rekap ke terminal
│
└── Visualisasi Grafik
    ├── Grafik 1 — Nilai per komponen (grouped bar)
    ├── Grafik 2 — Rata-rata dengan highlight min & max
    └── Grafik 3 — Pie chart data kelulusan
```

---

## Hasil Visualisasi Grafik

### Grafik 1 — Nilai per Komponen

> 📸 *Letakkan screenshot grafik nilai per komponen (grouped bar) di sini*

![Grafik Nilai per Komponen](images/grafik_komponen.png)

### Grafik 2 — Rata-rata Nilai (Min & Max)

> 📸 *Letakkan screenshot grafik rata-rata dengan highlight min & max di sini*

![Grafik Rata-rata Nilai](images/grafik_rata_rata.png)

### Grafik 3 — Data Kelulusan

> 📸 *Letakkan screenshot pie chart data kelulusan di sini*

![Grafik Data Kelulusan](images/grafik_kelulusan.png)

### Tampilan Lengkap Semua Grafik

> 📸 *Letakkan screenshot keseluruhan tampilan grafik (`grafik_nilai.png`) di sini*

![Grafik Lengkap](grafik_nilai.png)

---

## Ketentuan Penilaian Grade

| Rata-rata | Grade | Predikat | Status |
|---|---|---|---|
| ≥ 85 | A | Sangat Baik | LULUS |
| ≥ 75 | B | Baik | LULUS |
| ≥ 60 | C | Cukup | LULUS |
| < 60 | D | Kurang | TIDAK LULUS |
