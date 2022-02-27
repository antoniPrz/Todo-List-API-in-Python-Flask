from flask import Flask , jsonify, request, json
app = Flask(__name__)


todos = [
  {"label": "primera tarea", "done":False},
  {"label": "segunda tarea", "done":False},
  {"label": "tercera tarea", "done":False},
]



@app.route('/todos', methods=['GET'])
def hello_world():
    todos_json = jsonify(todos)
    return todos_json
    

@app.route('/todos' , methods=['POST'])
def add_new_todo():
    request_body = request.data
    incoming_todos = json.loads(request_body)
    global todos
    todos = [*todos ,incoming_todos]
    todos_json = jsonify(todos)
    return todos_json

@app.route('/todos/<int:position>',methods= ['DELETE'])
def delete_todo(position):
    global todos
    todos.pop(position)
    todos_json = jsonify(todos)
    return todos_json


    
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)