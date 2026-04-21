from flask import Flask, request, jsonify

app = Flask(__name__)

# Simulasi database sederhana
buku = {
    "1": {"judul": "Algoritma", "stok": 5},
    "2": {"judul": "Basis Data", "stok": 3}
}

peminjaman = []

@app.route('/pinjam', methods=['POST'])
def pinjam_buku():
    data = request.json
    id_buku = data.get("id_buku")
    id_user = data.get("id_user")

    if id_buku not in buku:
        return jsonify({"message": "Buku tidak ditemukan"}), 404

    if buku[id_buku]["stok"] <= 0:
        return jsonify({"message": "Stok habis"}), 400

    # kurangi stok
    buku[id_buku]["stok"] -= 1

    # simpan data peminjaman
    peminjaman.append({
        "id_user": id_user,
        "id_buku": id_buku,
        "status": "dipinjam"
    })

    return jsonify({
        "message": "Peminjaman berhasil",
        "sisa_stok": buku[id_buku]["stok"]
    })

@app.route('/')
def home():
    return "Server Backend Perpustakaan Berjalan"

if __name__ == '__main__':
    app.run(debug=True)