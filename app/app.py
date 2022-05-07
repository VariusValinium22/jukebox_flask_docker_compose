from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World - Docker in VS Code!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')


from flask import Flask, current_app

app = Flask(__name__)

with app.app_context():
    # within this block, current_app points to app.
    print (current_app.name)