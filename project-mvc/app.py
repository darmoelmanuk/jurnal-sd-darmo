from controllers.user_controller import run_app
import os

user_name = os.getenv("APP_USER", "Guest")
app_env = os.getenv("APP_ENV", "Development")

print(f"Halo {user_name}! Aplikasi ini berjalan di dalam kontainer Docker.\n")
print(f"Environment : {app_env}\n")

if __name__ == "__main__":
    run_app()