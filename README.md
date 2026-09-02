# Products API

Tugas Web Service Lab 03: Contract-First API Design.

## Deskripsi

API untuk mengelola data products menggunakan Flask, OpenAPI 3.0.3, dan PostgreSQL Neon.

## Teknologi

- Python
- Flask
- psycopg (PostgreSQL driver)
- PostgreSQL Neon
- OpenAPI 3.0.3

## Endpoint

| Method | Path                  | Fungsi              |
|--------|-----------------------|---------------------|
| GET    | /products             | Ambil semua produk  |
| GET    | /products/{id}        | Ambil satu produk   |
| POST   | /products             | Tambah produk baru  |
| DELETE | /products/{id}        | Hapus produk        |

## Menjalankan Project

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Buat file `.env`:
   ```bash
   copy .env.example .env
   ```

3. Isi `.env` dengan connection string Neon.

4. Jalankan Flask:
   ```bash
   python -m flask --app app --env-file .env run
   ```

Server berjalan di `http://localhost:5000`.

## Environment

`DATABASE_URL` disimpan di file `.env` dan tidak dimasukkan ke repository.

## OpenAPI

Spesifikasi API terdapat pada file `openapi.yaml`.

## Database

Menggunakan PostgreSQL Neon. Tabel `products` sudah tersedia dengan struktur:

| Field  | Tipe         |
|--------|--------------|
| id     | integer (PK) |
| name   | varchar(100) |
| price  | numeric(12,2)|
| stock  | integer      |
