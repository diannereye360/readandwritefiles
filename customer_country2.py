import csv

infile = open("customers.csv", "r")
csvfile = csv.reader(infile)
# if delimiter other than comma add argument, ie. delimiter='/'

outfile = open("customer_country2.csv", "w")

outfile.write("Full Name,Country\n")

next(csvfile)
for record in csvfile:
    # full_name = record[1] + " " + record[2]
    outfile.write(record[1] + " " + record[2] + "," + record[4] + "\n")

outfile.close()
