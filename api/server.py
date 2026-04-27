from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# 🔥 database sementara (dummy)
buku = {
    "1": {"judul": "Algoritma", "stok": 5},
    "2": {"judul": "Basis Data", "stok": 3}
}

@app.route('/pinjam', methods=['POST'])
def pinjam():
    data = request.get_json()

    # validasi
    if not data:
        return jsonify({"message": "Data tidak dikirim"})

    id_user = data.get("id_user")
    id_buku = data.get("id_buku")

    if not id_user or not id_buku:
        return jsonify({"message": "Data tidak lengkap"})

    if id_buku not in buku:
        return jsonify({"message": "Buku tidak ditemukan"})

    if buku[id_buku]["stok"] <= 0:
        return jsonify({"message": "Stok habis"})

    # proses pinjam
    buku[id_buku]["stok"] -= 1

    return jsonify({
        "message": "Peminjaman berhasil",
        "sisa_stok": buku[id_buku]["stok"]
    })


@app.route('/')
def home():
    return "Server Backend Perpustakaan Berjalan"


if __name__ == '__main__':
    app.run(debug=True)
    print("update backend v2")