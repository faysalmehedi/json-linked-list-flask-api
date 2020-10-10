import json
from flask import Flask, request 

from linked_list import SinglyLinkedList 


app = Flask(__name__)

def make_json():
    new_data = {}
    p = new_linked_list.head
    i = 0

    while p is not None:
        key = f'node_{i}'
        new_data[key] = p.key
        i += 1
        p = p.next
    return new_data

@app.route('/')
def hello_world():
    return "Hello Wold!"


@app.route('/api/v1/insert', methods=['POST'])
def insert():
    data = json.loads(request.data)
    
    for value in data.values():
        new_linked_list.push_back(value)

    return data


@app.route('/api/v1/getall')
def getall():

    new_data = make_json()

    json_format = json.dumps(new_data, indent=2)
    return json_format


@app.route('/api/v1/print')
def print():

    new_data = make_json()

    with open('result.json', 'w') as f:
        json.dump(new_data, f, indent=2)

    return 'Print Done! Data saved in Json format to "result.json"'



if __name__ == '__main__':

    new_linked_list = SinglyLinkedList()

    app.run()
