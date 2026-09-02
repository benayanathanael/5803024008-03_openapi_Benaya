"""
Backend Flask — Products API
"""
import os
import psycopg
from flask import Flask, jsonify

app = Flask(__name__)


def get_db_connection():
    """Membuat koneksi ke database Neon PostgreSQL."""
    return psycopg.connect(os.environ["DATABASE_URL"])


@app.get("/")
def home():
    """Cek apakah server hidup."""
    return jsonify({"status": "ok", "message": "Products API is running"})


@app.get("/products")
def get_products():
    """Mengambil semua produk dari database."""
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, name, price, stock FROM products ORDER BY id")
    rows = cur.fetchall()
    cur.close()
    conn.close()

    products = [
        {"id": r[0], "name": r[1], "price": float(r[2]), "stock": r[3]}
        for r in rows
    ]
    return jsonify(products)


@app.get("/products/<int:product_id>")
def get_product_by_id(product_id):
    """Mengambil satu produk berdasarkan ID."""
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        "SELECT id, name, price, stock FROM products WHERE id = %s",
        (product_id,),
    )
    row = cur.fetchone()
    cur.close()
    conn.close()

    if row is None:
        return jsonify({"error": "Product not found"}), 404

    product = {
        "id": row[0],
        "name": row[1],
        "price": float(row[2]),
        "stock": row[3],
    }
    return jsonify(product)


@app.post("/products")
def create_product():
    """Menambah produk baru ke database."""
    from flask import request

    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400

    data = request.get_json()

    for field in ("name", "price", "stock"):
        if field not in data:
            return jsonify({"error": f"{field} is required"}), 400

    conn = get_db_connection()
    cur = conn.cursor()
    try:
        cur.execute(
            "INSERT INTO products (name, price, stock) VALUES (%s, %s, %s) "
            "RETURNING id, name, price, stock",
            (data["name"], data["price"], data["stock"]),
        )
        row = cur.fetchone()
        conn.commit()
    except Exception:
        conn.rollback()
        return jsonify({"error": "Invalid input"}), 400
    finally:
        cur.close()
        conn.close()

    product = {
        "id": row[0],
        "name": row[1],
        "price": float(row[2]),
        "stock": row[3],
    }
    return jsonify(product), 201


@app.delete("/products/<int:product_id>")
def delete_product(product_id):
    """Menghapus satu produk berdasarkan ID."""
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("SELECT id FROM products WHERE id = %s", (product_id,))
    if cur.fetchone() is None:
        cur.close()
        conn.close()
        return jsonify({"error": "Product not found"}), 404

    cur.execute("DELETE FROM products WHERE id = %s", (product_id,))
    conn.commit()
    cur.close()
    conn.close()

    return "", 204
