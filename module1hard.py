import statistics

grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

new_grades = []
for i in grades:
    new_grades.append(statistics.mean(i))

result = {}
for i in range(len(students)):
    result[sorted(students)[i]] = new_grades[i]

print(result)
