# -*- coding: utf-8 -*-
from flask_script import Manager
from app import create_app

app = create_server()
manager = Manager(app)


@manager.command
def runserver():
    """Run in local machine."""
    # context = ('asset/server.crt', 'asset/server.key')
    # app.run(host='0.0.0.0', port=18686, use_reloader=True, ssl_context=context)
    app.run(host='127.0.0.1', port=8080, use_reloader=True, ssl_context=None)

if __name__ == "__main__":
    manager.run(default_command='runserver')
