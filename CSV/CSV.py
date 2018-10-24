import csv


class CSVHandler:

    def __init__(self, file_path):
        self.file_path = file_path

    def read_table_head(self):
        with open(self.file_path, 'rb') as csv_file:
            header = next(csv_file)
            header = header.decode()
            header = header.replace('\r', '')
            header = header.replace('\n', '')
            header_list = header.split(",")
            return header_list
