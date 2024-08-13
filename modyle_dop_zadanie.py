grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
student1 = sorted(students)
average = sum(grades[0]) / len(grades[0])
average1 = sum(grades[1]) / len(grades[1])
average2 = sum(grades[2]) / len(grades[2])
average3 = sum(grades[3]) / len(grades[3])
average4 = sum(grades[4]) / len(grades[4])
my_dict = {student1[0]: average, student1[1]: average1, student1[2]: average2, student1[3]: average3, student1[4]: average4}
print(my_dict)







