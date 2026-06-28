# Simulasikan data dari database

users = [
    {"id": 1, "name": "Admin"},
    {"id": 2, "name": "User"}
]

def get_users():
    return {
        "status": "success",
        "data": users
    }