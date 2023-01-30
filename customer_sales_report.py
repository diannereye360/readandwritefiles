import csv

# open "sales" file to read; name to customer_sales
# call csv.reader to read customer_sales; name to sales_infile
# open "salesreport" csv file to write; name to sales_outfile
# call csv.writer for sales_outfile; name to sales_write

# create and write to sales_write header row
# skip header row sales_infile

# create customer_list and record_list

# create for loop to read sales_infile
# append record to record_list
# append customer name to customer_list only if unique

# create for loop for customer_list
# create accumulater for customer_total
# create for loop for record_list: if customer and record from list match, then sum subtotal, tax, and freight and add to customer_total
# write customer id from customer_list and customer_total to sales_write
# close open and created files

customer_sales = open("sales.csv", "r")

sales_infile = csv.reader(customer_sales, delimiter=",")
sales_outfile = open("salesreport.csv", "w", newline="")
sales_write = csv.writer(sales_outfile)

header = ["Customer", "Total"]
sales_write.writerow(header)

header = next(sales_infile)

customer_list = []
record_list = []

for record in sales_infile:
    record_list.append(record)
    if record[0] not in customer_list:
        customer_list.append(record[0])

for customer in customer_list:
    customer_total = 0.0
    for record in record_list:
        if record[0] == customer:
            record_total = float(record[3]) + float(record[4]) + float(record[5])
            customer_total += record_total
    line = customer, round(customer_total, 2)
    sales_write.writerow(line)

sales_outfile.close()
customer_sales.close()
