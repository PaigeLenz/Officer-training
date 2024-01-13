from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/getReposts', methods=['GET'])
def get_reposts():
    return "100 reposts"

@app.route('/getLikes', methods=['GET'])
def get_likes():
    return "200 likes"

@app.route('/getBookmarks', methods=['GET'])
def get_bookmarks():
    return "300 bookmarks"

if __name__ == "__main__":
    app.run(debug=True)