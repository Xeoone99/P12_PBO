# P12 - Sistem Registrasi Mahasiswa (Implementasi SOLID & Kualitas Kode)

**Disusun oleh:**
* **Nama:** Muhammad Iqbal Nur Salim
* **NIM:** 2411102441302

---

## Deskripsi Proyek

Proyek ini merupakan hasil *refactoring* dari sistem pendaftaran mahasiswa yang mengimplementasikan prinsip Pemrograman Berorientasi Objek (PBO) secara menyeluruh. Fokus utama proyek adalah memastikan kode memenuhi prinsip **SOLID** (terutama **Dependency Inversion Principle** melalui penggunaan *Interface* `IValidationRule`) dan meningkatkan **kualitas kode** melalui dokumentasi dan pelacakan aktivitas.

## Fitur dan Implementasi Teknis

Proyek ini telah diperbarui untuk mencakup dua elemen penting dalam pengembangan perangkat lunak modern:

### 1. Dokumentasi Kode (Docstring)
Semua *class* (`RegistrationService`) dan *method* utama (termasuk pada *interface* `IValidationRule` dan *rule* turunannya) dilengkapi dengan **Docstring** menggunakan format **Google Style**. Dokumentasi ini menjelaskan fungsi, parameter (`Args`), dan nilai kembalian (`Returns`) dari setiap komponen, yang esensial untuk kolaborasi tim.

### 2. Pelacakan Aktivitas (Logging)
Seluruh fungsi `print()` di dalam `RegistrationService` dan *rule* validasi telah diganti dengan modul **`logging`** Python.
* Digunakan level **`INFO`** untuk mencatat proses normal dan sukses.
* Digunakan level **`WARNING`** dan **`ERROR`** untuk mencatat kegagalan validasi (misalnya SKS melebihi batas) atau kesalahan dalam alur registrasi.
Implementasi ini memisahkan jejak sistem dari *output* pengguna akhir, memudahkan *debugging*.

## Struktur Proyek

## Cara Menjalankan

1.  Pastikan Anda telah menginstal Python 3.
2.  Buka terminal atau Command Prompt dan masuk ke direktori proyek ini.
3.  Jalankan file utama:
    ```bash
    python main_app.py
    ```
    Output akan menampilkan log terstruktur yang berisi pesan **INFO** (sukses), **WARNING**, dan **ERROR** (gagal) secara berurutan.

## Version Control

Riwayat *commit* pada repositori ini mencerminkan alur kerja yang teratur, mulai dari penambahan Docstring, implementasi Logging, hingga finalisasi proyek dan dokumentasi.
