import os

from flask import Flask, escape, request, redirect, url_for

# from entity.vector import Vector

# myapp = Flask(__name__)
# port = int(os.environ.get("PORT", 8080))


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path,'flask.sqlite')
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/')
    def hello():
        name = escape(request.args.get("name", "World"))

        return f"Hello {name}, I'm a Vector Web Service!\n" \
               f"Send me a Vector to /add /subtract or /multiply\n\n" \
               f"curl'{{domain.com}}/add?vector1=1,2,3&vector2=1,2,3'\n"

    return app
