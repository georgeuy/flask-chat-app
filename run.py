import os

from dotenv import load_dotenv
load_dotenv('.env', verbose=True, override=True)

from application import create_app

config_class = os.getenv('CONFIG_CLASS')

app, socketio = create_app(config_class=config_class)

if __name__ == '__main__':

    socketio.run(
        app, 
        debug=os.getenv('FLASK_DEBUG').lower() in ('true','1'),
        host=os.getenv('FLASK_RUN_HOST'),
        port=int(os.getenv('FLASK_RUN_PORT')))
