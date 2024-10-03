# As a user
# So that I can keep track of my tasks
# I want a program that I can add todo tasks to and see a list of them.

# As a user
# So that I can focus on tasks to complete
# I want to mark tasks as complete and have them disappear from the list.

class TaskTracker:
    def __init__(self):
        self.task_list = []
    
    def add_tasks(self, task):
        self.task_list.append(task)

    def list_tasks(self):
        return self.task_list

    def mark_tasks_complete(self, task):
        self.task_list.remove(task)
        return (f"Task completed. Pending tasks: {self.task_list}")
        