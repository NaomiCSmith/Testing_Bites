from lib.task_tracker import *

def test_class_initialises():
    tracker = TaskTracker()
    assert tracker.task_list == []

def test_add_tasks_shopping():
    tracker = TaskTracker()
    tracker.add_tasks("Food shopping")
    assert tracker.task_list == ["Food shopping"]

def test_add_tasks_karaoke_everest():
    tracker = TaskTracker()
    tracker.add_tasks("Sing karaoke")
    tracker.add_tasks("Climb Mount Everest")
    assert tracker.task_list == ["Sing karaoke", "Climb Mount Everest"]

def test_list_tasks_shopping_dentist():
    tracker = TaskTracker()
    tracker.add_tasks("Food shopping")
    tracker.add_tasks("Visit dentist")
    assert tracker.list_tasks() == ["Food shopping", "Visit dentist"]

def test_list_tasks_cat_dog():
    tracker = TaskTracker()
    tracker.add_tasks("Walk the dog")
    tracker.add_tasks("Feed the cat")
    assert tracker.list_tasks() == ["Walk the dog", "Feed the cat"]

def test_completed_tasks_completed_and_removed_cake():
    tracker = TaskTracker() 
    tracker.add_tasks("Do cold yoga")
    tracker.add_tasks("Eat cake")
    assert tracker.mark_tasks_complete("Eat cake") == (f"Task completed. Pending tasks: {tracker.task_list}")

def test_completed_tasks_completed_and_removed_cheese():
    tracker = TaskTracker() 
    tracker.add_tasks("Eat grapes")
    tracker.add_tasks("Eat cheese")
    tracker.add_tasks("Drink wine")
    tracker.add_tasks("Pretend to be a Greek God")
    assert tracker.mark_tasks_complete("Eat cheese") == (f"Task completed. Pending tasks: {tracker.task_list}") 