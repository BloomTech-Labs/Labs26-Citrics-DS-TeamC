# web_app/__init__.py

from flask import Flask
from app.routes.home_routes import home_routes

# TODO: uncomment when we start utilizing tests
# from app.routes.test_routes import test_routes


def create_app():
    '''
    Creates our flask app!
    '''
    app = Flask(__name__)
    # prevents jsonify from reordering our data in ways we don't want
    app.config['JSON_SORT_KEYS'] = False
    # register the home_routes file
    app.register_blueprint(home_routes)
    # app.register_blueprint(test_routes)   # TODO
    return app


if __name__ == "__main__":
    # instantiate the flask app
    my_app = create_app()
    my_app.run(debug=True)