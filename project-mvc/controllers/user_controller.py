from models.user_model import user_data
from views.user_view import render_user

def run_app():
    render_user(user_data)