from flask import Flask

app = Flask(__name__)

@app.route('/retrieve_recommendation', methods=['GET'])
def retrieve_recommendation():
    return "Hello World!"

if __name__ == '__main__':
    app.run()
