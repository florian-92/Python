student_tuples = [
        ('john', 'A', 15),
        ('jane', 'B', 12),
        ('dave', 'B', 10),
]
print(sorted(student_tuples, key=lambda student: student[2]))

inventaire = [
     ["pommes", 22],
    ["melons", 4],
     ["poires", 18],
     ["fraises", 76],
     ["prunes", 51],
]
print(sorted(inventaire, key=lambda inventaire: inventaire[1]))
