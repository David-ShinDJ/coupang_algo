import csv

class CSVReader:
    def __init__(self, filename):
        self.filename = filename

    def data(self):
        with open(self.filename, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            return list(reader)


csv_reader = CSVReader('product_sample.csv')
print(csv_reader.data)