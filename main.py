from flask import Flask

app = Flask(__name__, static_folder='static', static_url_path='')


@app.route('/')
def galaxy():
    return app.send_static_file('index.html')


if __name__ == '__main__':
    app.run(threaded=True, host="0.0.0.0", port=5000)