grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
#a=[1, 2, 3, 5]
#print(sum(a)/len(a))
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
#grades_middle = sum(grades[0]/len[0]), sum(grades[1]/len[1]), sum(grades[2]/len[2]), sum(grades[3]/len[3]), sum(grades[4]/len[4])]
grades_middle = sum(grades[0])/len(grades[0]), sum(grades[1])/len(grades[1]),\
                sum(grades[2])/len(grades[2]), sum(grades[3])/len(grades[3]),\
                sum(grades[4])/len(grades[4])
#print(grades_middle)
students_sort = sorted(students)
#print(students_sort)
dictionary = dict(zip(students_sort, grades_middle))
print(dictionary)