import csv

# open "customers" file to read; name to customer_infile
# call csv.reader to read "customers" file

# open "customer_country" csv file to write; name to customer_outfile
# call csv.writer for customer_outfile

# create for loop to read customer_infile
# write records name, country to customer_outfile
# close open and created files

customers = open("customers.csv", "r")

customer_infile = csv.reader(customers, delimiter=",")
customer_outfile = open("customer_country.csv", "w", newline="")
name_country_write = csv.writer(customer_outfile)

header = ["Name", "Country"]
name_country_write.writerow(header)

header_line = next(customer_infile)

for record in customer_infile:
    name = record[1] + " " + record[2]
    name_country = name, record[4]
    name_country_write.writerow(name_country)

customer_outfile.close()
customers.close()
