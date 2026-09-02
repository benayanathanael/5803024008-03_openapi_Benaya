# Products API

Tugas Web Service Lab 03: Contract-First API Design.

## Struktur Project

```
.
├── openapi.yaml      # Kontrak API (OpenAPI 3.0.3)
├── app.py            # Backend Flask
├── requirements.txt  # Dependencies
└── .env.example     # Template DATABASE_URL
```

## Setup

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Buat file `.env`:
   ```
   copy .env.example .env
   ```

3. Isi `.env` dengan connection string Neon:
   ```
   DATABASE_URL=postgresql://user:pass@host/neondb?sslmode=require
   ```

## Jalankan Backend

```
python -m flask --app app --env-file .env run
```

Server berjalan di `http://localhost:5000`.

## Endpoint

| Method | Path                  | Fungsi              |
|--------|-----------------------|---------------------|
| GET    | /products             | Ambil semua produk  |
| GET    | /products/{id}        | Ambil satu produk   |
| POST   | /products             | Tambah produk baru  |
| DELETE | /products/{id}        | Hapus produk        |

## Test dengan curl

```bash
# Ambil semua produk
curl http://localhost:5000/products

# Ambil satu produk
curl http://localhost:5000/products/1

# Tambah produk baru
curl -X POST http://localhost:5000/products \
  -H "Content-Type: application/json" \
  -d '{"name":"Monitor","price":1500000,"stock":5}'

# Hapus produk
curl -X DELETE http://localhost:5000/products/4
```

## Database

Menggunakan PostgreSQL Neon. Tabel `products` sudah tersedia dengan struktur:

| Field  | Tipe         |
|--------|--------------|
| id     | integer (PK) |
| name   | varchar(100) |
| price  | numeric(12,2)|
| stock  | integer      |
# 5803024008-03_openapi_Benaya
