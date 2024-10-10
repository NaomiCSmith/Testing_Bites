from lib.class_todo import *
from lib.class_todo_list import *


def test_class_todo_list_adds_one_todo_to_list():
    todolist = TodoList()
    todolist.add("check on the hippos")
    assert todolist.todo_list == ["check on the hippos"]

def test_class_todo_list_adds_multiple_todos_to_list():
    todolist = TodoList()
    todolist.add("Eat grapes")
    todolist.add("Put grapes in barrel")
    todolist.add("Ferment grapes")
    todolist.add("Drink grapes")
    assert todolist.todo_list == ["Eat grapes", "Put grapes in barrel", "Ferment grapes", "Drink grapes"]

def test_class_todo_list_returns_list_of_incomplete_todos():
    todolist = TodoList()
    todolist.add(Todo("Chillin' out"))
    todolist.add(Todo("Maxin'"))
    todolist.todo_list[1].mark_complete()
    todolist.add(Todo("Relaxin' all cool"))
    incomplete_tasks = [todo.task for todo in todolist.incomplete()]
    assert incomplete_tasks == ["Chillin' out", "Relaxin' all cool"]

def test_class_todo_list_returns_list_of_complete_todos():
    todolist = TodoList()
    todolist.add(Todo("Puzzle wednesday"))
    todolist.add(Todo("Pizza thursday"))
    todolist.add(Todo("Waterpainting friday"))
    todolist.todo_list[2].mark_complete()
    todolist.todo_list[0].mark_complete()
    complete_tasks = [todo.task for todo in todolist.complete()]
    assert complete_tasks == ["Puzzle wednesday", "Waterpainting friday"]

def test_class_todo_list_mark_all_complete():
    todolist = TodoList()
    todolist.add(Todo("Balance beam"))
    todolist.add(Todo("Uneven bars"))
    todolist.add(Todo("Vault"))
    todolist.add(Todo("Floor"))
    todolist.todo_list[0].mark_complete()
    todolist.todo_list[1].mark_complete()
    todolist.todo_list[2].mark_complete()
    todolist.todo_list[3].mark_complete()
    complete_tasks = [todo.task for todo in todolist.complete()]
    assert complete_tasks == ["Balance beam", "Uneven bars", "Vault", "Floor"]



