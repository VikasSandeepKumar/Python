from tabulate import tabulate

table_data = [['Name', 'Age', 'Job'],
              ['Vikas', '32', 'DPO'],
              ['Dheeraj', '27', 'BPO']]

# for row in table_data:
#     for col in row:
#         print(col, end='')
#     print()

# print(tabulate(table_data, headers="firstrow", tablefmt="plain"))
# print(tabulate(table_data, headers="firstrow", tablefmt="psql"))
print(tabulate(table_data, headers="firstrow", tablefmt="fancy_grid"))