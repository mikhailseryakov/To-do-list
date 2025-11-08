import os
from datetime import datetime
import csv

# Файл для хранения задач
TASKS_FILE = "tasks.txt"

def load_tasks():
    """Загружает задачи из файла при запуске программы."""
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r", encoding="utf-8") as f:
            lines = f.read().splitlines()
            # Фильтруем пустые строки
            return [line for line in lines if line.strip()]
    return []

def save_tasks(tasks):
    """Сохраняет текущий список задач в файл."""
    with open(TASKS_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(tasks))

def add_task(tasks):
    """Добавляет новую задачу в список."""
    task = input("Введите задачу: ").strip()
    if task:
        tasks.append(f"{task} | {datetime.now().strftime('%Y-%m-%d %H:%M')}")
        print("Задача добавлена!")
    else:
        print("Задача не может быть пустой!")

def view_tasks(tasks):
    """Показывает все задачи с нумерацией."""
    if tasks:
        print("\nВаши задачи:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    else:
        print("Список задач пуст!")

def delete_task(tasks):
    """Удаляет задачу по номеру."""
    if not tasks:
        print("Список задач пуст!")
        return

    try:
        num = int(input("Номер задачи для удаления: ")) - 1
        if 0 <= num < len(tasks):
            removed = tasks.pop(num)
            print(f"Задача удалена: {removed}")
        else:
            print("Нет задачи с таким номером!")
    except ValueError:
        print("Введите число!")

def search_tasks(tasks):
    query = input("Поиск: ").lower()
    found = [task for task in tasks if query in task.lower()]
    if found:
        print("Найденные задачи:")
        for task in found:
            print(f"!  {task}")
    else:
        print("Ничего не найдено!")

def clear_all_tasks(tasks):
    """Очищает весь список задач."""
    if tasks:
        confirm = input("Удалить все задачи? (y/n): ").lower()
        if confirm == "y":
            tasks.clear()
            print("Все задачи удалены!")
        else:
            print("Отмена.")
    else:
        print("Список уже пуст!")

def export_to_csv(tasks):
    with open("tasks.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Задача", "Дата"])
        for task in tasks:
            parts = task.split(" | ")
            writer.writerow([parts[0], parts[1]])
    print("Экспорт в tasks.csv завершён!")

def main():
    """Основная функция программы."""
    tasks = load_tasks()
    print("Добро пожаловать в To‑Do List!")

    while True:
        print("\n--- Меню ---")
        print("1. Добавить задачу")
        print("2. Посмотреть задачи")
        print("3. Удалить задачу")
        print("4. Очистить все задачи")
        print("5. Поиск задач")
        print("6. Экспорт в CSV")
        print("7. Выход")

        choice = input("Выберите действие (1–7): ").strip()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            clear_all_tasks(tasks)
        elif choice == "5":
            search_tasks(tasks)
        elif choice == "6":
            export_to_csv(tasks)
        elif choice == "7":
            save_tasks(tasks)
            print("Задачи сохранены! До свидания!")
            break
        else:
            print("Неверный ввод! Попробуйте снова.")

if __name__ == "__main__":
    main()