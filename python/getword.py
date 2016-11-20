#!flask/bin/python
from flask import Flask, jsonify

app = Flask(__name__)

words = [
    {
        'id': 1,
        'title': u'Womanizer',
        'description': u'man who pursues many women',
        'learned': False
    },
    {
        'id': 2,
        'title': u'Hustler',
        'description': u'man who cheats',
        'learned': False
    }
]

@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_words():
    return jsonify({'words': words})

if __name__ == '__main__':
    app.run(debug=True)