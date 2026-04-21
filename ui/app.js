function pinjamBuku() {
    const id_user = document.getElementById("id_user").value;
    const id_buku = document.getElementById("id_buku").value;

    if (!id_user || !id_buku) {
        showNotif("Semua field harus diisi!", "danger");
        return;
    }

    fetch("http://127.0.0.1:5000/pinjam", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            id_user: id_user,
            id_buku: id_buku
        })
    })
    .then(response => response.json())
    .then(data => {
        if (data.message === "Peminjaman berhasil") {
            showNotif(data.message + " | Sisa stok: " + data.sisa_stok, "success");
        } else {
            showNotif(data.message, "danger");
        }
    })
    .catch(error => {
        console.error(error);
        showNotif("Terjadi kesalahan pada server!", "danger");
    });
}

// fungsi notifikasi
function showNotif(message, type) {
    const notif = document.getElementById("notif");
    notif.className = "alert alert-" + type + " mt-3";
    notif.classList.remove("d-none");
    notif.innerHTML = message;
}