import random

# Simulasikan data dari database
users = [
    {"id": 1, "name": "Admin"},
    {"id": 2, "name": "User"}
]


def get_users():

    # Simulasi server sibuk
    if random.randint(1, 4) == 1:
        return {
            "status": "error",
            "message": "Server sedang sibuk, silakan coba lagi."
        }

    return {
        "status": "success",
        "data": users
    }