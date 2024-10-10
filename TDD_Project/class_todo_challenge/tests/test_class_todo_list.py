from lib.class_todo_list import *

def test_class_todo_list_instantiates():
    todolist = TodoList()
    assert todolist.todo_list == []

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