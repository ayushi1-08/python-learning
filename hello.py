from fastapi import FastAPI;

api = FastAPI();

all_todos = [
  {"id": 1, "task": "Buy groceries"},
  {"id": 2, "task": "Walk the dog"},
  {"id": 3, "task": "Read a book"},
  {"id": 4, "task": "Write code"},
  {"id": 5, "task": "Exercise"},
  {"id": 6, "task": "Clean the house"},
  {"id": 7, "task": "Prepare dinner"},
]
@api.get("/")
def index():
  return {"message": "Hello World!"}

@api.get("/todos")
def get_todos(first_n: int = None):
  if first_n:
    return all_todos[:first_n]
  else:
    return all_todos

@api.get("/todos/{todo_id}")
def get_todo(todo_id: int):
  for todo in all_todos:
    if todo["id"] == todo_id:
      return todo
  return {"error": "Todo not found"}, 404

@api.post("/todos")
def create_todo(todo: dict):
  new_id = max(todo["id"] for todo in all_todos) + 1 if all_todos else 1
  new_todo = {"id": new_id, "task": "go to the dance classes"}
  all_todos.append(new_todo)
  return todo

@api.put("/todos/{todo_id}")
def update_todo(todo_id: int, updated_todo: dict):
  for todo in all_todos:
    if todo["id"] == todo_id:
      todo["task"] = updated_todo["task"]
      return todo
  return {"error": "Todo not found"}, 404

@api.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
  for todo in all_todos:
    if todo["id"] == todo_id:
      all_todos.remove(todo)
      return {"message": "Todo deleted successfully"}
  return {"error": "Todo not found"}, 404