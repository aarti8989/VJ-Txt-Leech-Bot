from flask import Flask
app = Flask(__utkarsh__)

@app.route('/')
def hello_world():
    return 'Tech VJ'


if __name__ == "__main__":
    app.run()
