from task import Task
import threading
from queue import Queue

class TaskManager:
    def __init__(self, max_workers=3):
        self.tasks = Queue()
        self.max_workers = max_workers

    def add_task(self, name, duration):
        if duration < 0:
            raise ValueError("Duración inválida")

        task = Task(name, duration)
        self.tasks.put(task)

    def worker(self):
        while not self.tasks.empty():
            task = self.tasks.get()
            task.run(self.on_task_start, self.on_task_finish)
            self.tasks.task_done()

    def on_task_start(self, task_name):
        print(f"[EVENTO] Iniciando tarea: {task_name}")

    def on_task_finish(self, task_name):
        print(f"[EVENTO] Tarea finalizada: {task_name}")

    def run(self):
        threads = []

        for _ in range(self.max_workers):
            t = threading.Thread(target=self.worker)
            t.start()
            threads.append(t)

        for t in threads:
            t.join()

        print("Todas las tareas procesadas")
