from flask import Flask

app = Flask(__name__)

@app.route('/',methods=["GET","POST"])
def index():
    return "CI CD Pipeline has been established for Starting the AlgoTrade Project"

if __name__ == "__main__":
    app.run(debug=True)