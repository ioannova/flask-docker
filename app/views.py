from app import app

@app.route('/')
def home():
    return "hello world!"

@app.route('/nelson')
def nelson():
    return "Olá Nelson"
