import os
from flask import Flask
from . import auth, master

def create_app(test_config=None):
    # create and configure
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev'
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello world'

    app.register_blueprint(auth.bp)
    app.register_blueprint(master.bp)
    app.add_url_rule('/', endpoint='index')

    return app
