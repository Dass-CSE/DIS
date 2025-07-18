from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "This Flask app is running with HTTPS (SSL Enabled)!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=443, ssl_context=('cert.pem', 'key.pem'))
