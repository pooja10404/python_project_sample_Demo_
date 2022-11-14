import csv

with open('Python.csv', 'w') as csvfile:
    fieldnames = ['first_name', 'last_name', 'Rank']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'Rank': 'B', 'first_name': 'Parker', 'last_name': 'Brian'})
    writer.writerow({'Rank': 'A', 'first_name': 'Smith', 'last_name': 'Rodriguez'})
    writer.writerow({'Rank': 'B', 'first_name': 'Jane', 'last_name': 'Oscar'})
    writer.writerow({'Rank': 'B', 'first_name': 'Jane', 'last_name': 'Loive'})

print("Writing complete")

# opening the CSV file
with open('Python.csv', mode='r') as file:
    # reading the CSV file
    csvFile = csv.reader(file)

    # displaying the contents of the CSV file
    for lines in csvFile:
        print(lines)
