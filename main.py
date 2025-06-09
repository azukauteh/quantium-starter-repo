import csv
import os

DATA_DIRECTORY = "./data"
OUTPUT_FILE_PATH = "./data/formatted_sales_data.csv"

""" Open the output file"""
with open(OUTPUT_FILE_PATH, "w", newline="") as output_file:
    
    """ Write CSV header"""
    writer = csv.writer(output_file)

    writer.writerow(["sales", "date", "region"])

    """ Loop through files"""
    for file_name in os.listdir(DATA_DIRECTORY):
        if file_name.endswith(".csv"):
            file_path = os.path.join(DATA_DIRECTORY, file_name)

            with open(file_path, "r") as input_file:
                reader = csv.reader(input_file)

                """ Skip header row"""
                next(reader)

                for row in reader:
                    if len(row) < 5:
                        continue  # Skip malformed rows

                    product = row[0]
                    raw_price = row[1]
                    quantity = row[2]
                    transaction_date = row[3]
                    region = row[4]

                    if product.lower() == "pink morsel":
                        try:
                            price = float(raw_price.replace("$", ""))
                            sales = price * int(quantity)
                            writer.writerow([sales, transaction_date, region])
                        except ValueError:
                            continue  # Skip rows with bad number formatting

print("✅ Output saved to data/formatted_sales_data.csv")
