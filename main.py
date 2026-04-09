from manager import TaskManager

def main():
    manager = TaskManager(max_workers=2)

    try:
        manager.add_task("Tarea A", 3)
        manager.add_task("Tarea B", 2)
        manager.add_task("Tarea C", 1)
        manager.add_task("Tarea D", 4)

        manager.run()

    except Exception as e:
        print(f"Error general: {e}")

if __name__ == "__main__":
    main()
