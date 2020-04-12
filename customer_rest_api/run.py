from app import app


if __name__ == '__main__':
    port = port=app.config.get('PORT')
    host = app.config.get('HOST')
    debug = debug=app.config.get('DEBUG')

    app.run(host=host, port=port, debug=debug)