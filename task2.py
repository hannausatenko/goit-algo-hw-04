def total_salary(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            salaries = []
            for line in file:
                name, salary = line.strip().split(',')
                salaries.append(int(salary))

            total = sum(salaries)
            average = total / len(salaries) if salaries else 0
            return total, average
    except FileNotFoundError:
        print(f"Файл {path} не знайдено.")
        return 0, 0
    except Exception as e:
        print(f"Сталася помилка: {e}")
        return 0, 0

path_to_file = "salary.txt"
total, average = total_salary(path_to_file)
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")