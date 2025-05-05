# 🌾 Sistem Pakar Diagnosa Penyakit Padi

[![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GUI Ready](https://img.shields.io/badge/GUI-Tkinter-blueviolet)](https://docs.python.org/3/library/tkinter.html)

## 📌 Deskripsi

Repositori ini berisi tugas ke-4 dari pertemuan ke-5 mata kuliah **Sistem Pakar**, yang bertujuan untuk membuat sistem pakar berbasis GUI (Graphical User Interface) untuk **mendiagnosa penyakit pada tanaman padi**. Aplikasi ini menggunakan **Python** dengan library `tkinter` untuk antarmuka dan **Prolog** sebagai basis pengetahuan.

> Penggunaan GUI memberikan pengalaman pengguna yang lebih baik dan merupakan syarat penilaian tambahan dalam tugas ini.

## 📷 Tampilan Antarmuka

![Screenshot GUI]("Screenshot (198).png")  
*Contoh tampilan pertanyaan dalam GUI (ganti dengan screenshot asli)*

## 📌 Fitur Utama

- Antarmuka grafis menggunakan Tkinter
- Diagnosa berbasis gejala dengan pendekatan rule-based
- Integrasi dengan basis pengetahuan menggunakan Prolog
- Deteksi 4 penyakit padi utama
- Tampilan hasil diagnosa yang jelas dan informatif

## 🛠 Teknologi yang Digunakan

- Python 3.13
- Tkinter (GUI)
- SWI-Prolog (Basis Pengetahuan)
- Pyswip (untuk integrasi Python ↔ Prolog)

## 📁 Struktur Folder
TUGAS_PRAKKB/
├── basis_pengetahuan.pl # File basis pengetahuan Prolog
├── hasil_diagnosa.py # Tampilan hasil diagnosa
├── main_app.py # File utama aplikasi (GUI)
├── pertanyaan_padi.py # Daftar pertanyaan/gejala
├── pycache/ # Cache Python


## 🚀 Cara Menjalankan

1. Pastikan Python 3 sudah terpasang.
2. Jalankan program utama dengan perintah:

```bash
python main_app.py
```
3. Ikuti pertanyaan yang muncul.
4. Diagnosa akan ditampilkan di akhir berdasarkan gejala yang dipilih.

##🧾 Lisensi
Proyek ini dibuat hanya untuk kebutuhan akademik. Gunakan dan modifikasi sesuai kebutuhan.
