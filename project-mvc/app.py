from controllers.user_controller import run_app
import os

user_name = os.getenv("APP_USER", "Guest")
app_env = os.getenv("APP_ENV", "Development")

print(f"Halo {user_name}! Aplikasi ini berjalan di dalam kontainer Docker.\n")
print(f"Environment : {app_env}\n")
# =====================================================================
from controllers.api_handler import get_users
from views.dashboard_component import (
    render_dashboard,
    fetch_data_from_api
)

# Simulasi State
app_state = {
    "items": [],
    "is_loading": True
}


def update_state(new_data):
    app_state["items"] = new_data
    app_state["is_loading"] = False

if __name__ == "__main__":

    print("Loading data...")

    # Tampilan saat loading
    render_dashboard(
        app_state["items"],
        app_state["is_loading"]
    )

    print()

    # Integrasi Frontend-Backend
    data = fetch_data_from_api(get_users)

    if data:
        update_state(data)

    # Setelah data berhasil diterima
    render_dashboard(
        app_state["items"],
        app_state["is_loading"]
    )

    print()

    # Menjalankan aplikasi MVC sebelumnya
    run_app()