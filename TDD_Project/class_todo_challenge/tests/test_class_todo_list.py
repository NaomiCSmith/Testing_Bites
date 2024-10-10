from lib.class_todo_list import *

def test_class_todo_list_instantiates():
    todolist = TodoList()
    assert todolist.todo_list == []

