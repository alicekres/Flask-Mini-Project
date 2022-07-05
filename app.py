from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

facts = [
    {'id': 1, 'fact': "A happy cat holds her tail high and steady."}, 
    {'id': 2, 'fact': "The Maine Coone is the only native American long haired breed."}, 
    {'id': 3, 'fact': "Cats are often lactose intolerant, so stop givin them milk!"}, 
    {'id': 4, 'fact': "Cats do not think that they are little people. They think that we are big cats. This influences their behavior in many ways."}, 
    {'id': 5, 'fact': "A cat's whiskers are thought to be a kind of radar, which helps a cat gauge the space it intends to walk through."}, {'id': 6, 'fact': "The worlds richest cat is worth $13 million after his human passed away and left her fortune to him."}, 
    {'id': 7, 'fact': "A cat can sprint at about thirty-one miles per hour."}]

@app.route('/')
def hello():
    return f'Hello world!'

@app.route('/facts', methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return jsonify(facts)
    elif request.method == "POST":
        data = request.json
        last_id = facts[-1]['id']
        data['id'] = last_id + 1
        facts.append(data)
        return 'New fact was added!', 201

@app.route('/facts/<int:fact_id>')
def show(fact_id):
    try:
        return next(fact for fact in facts if fact['id'] == fact_id)
    except:
        raise Exception(f"We don't have that many facts about cats yet! Maybe you can add one!")

if __name__ == "__main__":
    app.run()
