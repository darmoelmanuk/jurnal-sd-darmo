from controllers.user_controller import run_app
from views.dashboard_component import render_dashboard

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

    # Kondisi loading
    render_dashboard(app_state["items"], app_state["is_loading"])

    mock_data = [
        {"id": 101, "name": "Produk A"},
        {"id": 102, "name": "Produk B"}
    ]

    update_state(mock_data)

    print()

    # Setelah loading selesai
    render_dashboard(app_state["items"], app_state["is_loading"])

    print()

    # Aplikasi sebelumnya tetap berjalan
    run_app()