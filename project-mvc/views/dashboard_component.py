def render_dashboard(data_list, is_loading):
    print("--- DASHBOARD APLIKASI ---")

    if is_loading:
        print("Mohon Tunggu...")
        return

    if not data_list:
        print("[!] Data Kosong. Silakan sinkronisasi dengan Backend.")
    else:
        for item in data_list:
            print(f"- Item ID: {item['id']} | Nama: {item['name']}")
            
def fetch_data_from_api(api_function):

    print("[System] Mencoba menghubungkan ke API...")

    try:

        response = api_function()

        if response["status"] == "success":
            return response["data"]

        raise Exception(response.get("message", "Terjadi kesalahan pada server."))

    except Exception as e:

        print("[ERROR]")
        print("Integrasi Frontend-Backend gagal.")
        print(f"Penyebab : {e}")
        print("Silakan coba beberapa saat lagi.\n")

        return None