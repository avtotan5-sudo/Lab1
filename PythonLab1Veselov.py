# Проверка ввода row и col
while True:
    try:
        row = int(input("Введите колличество строк матрицы: "))
        col = int(input("Введите колличество столбцов матрицы: "))
        if row > 0 and col > 0:
            break
        print("Error: Строки и столбцы не могут иметь значение меньше 1!")
    except ValueError:
        print("Error: Принимаются только числа!")

# Заполнение матрицы
matrix = []
for i in range(row):
    line = []
    for j in range(col):
        while True:
            try:
                line.append(int(input(f"[{i+1}][{j+1}]: ")))
                break
            except ValueError:
                print("Принимаются только числа!")
    matrix.append(line)

# Суммы строк и столбцов
line_sum = [sum(line) for line in matrix]
col_sum = [sum(matrix[i][j] for i in range(row)) for j in range(col)]

# Вывод
print()
for i in range(row):
    for j in range(col):
        print(f"{matrix[i][j]:3}", end="")
    
    # Если это последняя строка, добавляем подпись "row sum"
    if i == row - 1:
        print(f" | {line_sum[i]}  | Сумма строк")
    else:
        print(f" | {line_sum[i]}")

print("-" * (4*col + 15))
for j in range(col):
    print(f"{col_sum[j]:3}", end="")
print(" | Сумма столбцов")