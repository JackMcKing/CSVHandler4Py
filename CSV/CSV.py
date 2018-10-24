import csv

class CSVHandler:


    def __init__(self, file_path):
        self.file_path = file_path

    def read_table_head(self):
        with open(self.file_path, 'r') as csv_file:
            reader = csv.reader(csv_file)
            for line in reader:
                print(line)
