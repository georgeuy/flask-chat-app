import os
from flask import Flask
from flask_socketio import SocketIO, emit, join_room, leave_room

socketio = SocketIO(cors_allowed_origins='*')

app = Flask(
    __name__,
    static_folder='../static',  # Ruta relativa a __init__.py
    static_url_path='/static'
)   # URL para acceder a los archivos estáticos)


def create_app(config_class):

    app.config.from_object(config_class)

    # Iniciatizar SocketIO
    socketio.init_app(app)

    from .api import api
    app.register_blueprint(api)

    return app, socketio
