import time

class Task:
    def __init__(self, name, duration):
        self.name = name
        self.duration = duration

    def run(self, on_start=None, on_finish=None):
        try:
            if on_start:
                on_start(self.name)

            time.sleep(self.duration)

            if on_finish:
                on_finish(self.name)

        except Exception as e:
            print(f"Error en tarea {self.name}: {e}")
