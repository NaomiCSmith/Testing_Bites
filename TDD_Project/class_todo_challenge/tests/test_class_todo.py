from lib.class_todo import *

def test_class_todo_instantiates():
    todo = Todo("spring clean")
    assert todo.complete == False

def test_todo_mark_complete():
    todo = Todo("spring clean")
    todo.mark_complete()
    assert todo.complete == True