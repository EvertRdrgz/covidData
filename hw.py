import csv

data = "Mexico.csv"
fields = []
rows = []
pop = 127600000 #from google as of 2009
with open(data, 'r') as file:
    csvreader = csv.reader(file)

    fields = next(csvreader)

    for row in csvreader:
        rows.append(row)
data_points = csvreader.line_num-1

print("There are this many data points: %d"%data_points)
print('The field names are: ' + ', '.join(field for field in fields))


fully_vax = rows[data_points-1]
print("\nThe total number of fully vaxinated people in " + fully_vax[0] +" as of " + fully_vax[1] + " is: " + fully_vax[len(fully_vax)-1])
vax_pop = int(fully_vax[len(fully_vax)-1])
pervax = str((vax_pop/pop)*100)
print("This means that " + pervax + " of the population is protected from COVID-19")