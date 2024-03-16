#fh = open('salary.txt', 'w')
#fh.write("Alex Korp,3000\nNikita Borisenko,2000\nSitarama Raju,1000")
#fh.close()

#fh = open('salary.txt', 'r')
#all_file = fh.read()
#print(all_file)
#fh.close()

import pathlib
import sys
def total_salary_2(path):
    # відкриваємо для читання відомість зп із файла salary.txt
    try:
        with open(path, "r", encoding="utf-8") as fh:
            total = 0
            count = 0
            for line in fh:
                lines = line.strip().split(',')
                salary = int(lines[1])
                total += salary
                count += 1
            average = total / count
            return total, average
    except FileNotFoundError:
        return "Не вдалося знайти файл"

total, average = total_salary_2("salary.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")