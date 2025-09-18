def task_manager(tasks_dict=None):
    tasks_dict = {}

    def add_task(name, status="incomplete"):
        tasks_dict[name] = status

    def get_tasks():
        """
        Returns a copy of the tasks dictionary to prevent external modification.
        while not entirely functional (tasks_dict gets modified by other functions),
        it prevents the user from modifying it directly.
        it's been used this way to work with the way the provided example script
        is written in the exercise itself.
        """
        return dict(tasks_dict)

    def complete_task(name):
        tasks_dict[name] = "complete"

    return {
        "add_task": add_task,
        "get_tasks": get_tasks,
        "complete_task": complete_task,
    }
