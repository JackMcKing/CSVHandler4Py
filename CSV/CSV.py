import csv
from collections import defaultdict


class CSVHandler:

    def __init__(self, file_path):
        self.file_path = file_path

    def read_table(self):
        with open(self.file_path, 'r') as csv_file:
            creader = csv.reader(csv_file)
            lines = [l for l in creader]
            return lines

    def read_table_head(self):
        with open(self.file_path, 'r') as csv_file:
            header = next(csv_file)
            header = header.replace('\n', '')
            header_list = header.split(",")
            return header_list

    def read_table_row(self, row_num):
        with open(self.file_path, 'r') as csv_file:
            creader = csv.reader(csv_file)
            try:
                for i, row in enumerate(creader):
                    if i == row_num:
                        return row
            except Exception:
                raise Exception('No Such Row In This File!')

    def read_table_column(self, column_name):
        columns = defaultdict(list)
        with open(self.file_path, 'r') as csv_file:
            creader = csv.DictReader(csv_file)
            try:
                for row in creader:
                    for (k, v) in row.items():  # go over each column name and value
                        if k == column_name:
                            columns[k].append(v)
            except Exception:
                    raise Exception('No Such Column In This File!')

        return columns[column_name]

    def edit_table_value(self, row_num, column_num, new_value):
        file_content = None
        with open(self.file_path, 'r') as f:
            creader = csv.reader(f)
            lines = [l for l in creader]
            lines[row_num][column_num] = new_value
            file_content = lines
        with open(self.file_path, 'w', newline='') as csv_file:
            cwriter = csv.writer(csv_file)
            cwriter.writerows(file_content)

    # 没找到更好的方法，只能先读在内存里，再修改相应值，然后再写回文件
    def edit_table_head(self, old_head, new_head):
        column_num = None
        head_list = self.read_table_head()
        try:
            for i, item in enumerate(head_list):
                if item == old_head:
                    column_num = i
        except Exception:
            raise Exception('No Such Value In This Head!')
        self.edit_table_value(0, column_num, new_head)

    # 一行是一个list， *kw可以一下传好几行
    def add_new_rows(self, *new_lines):
        with open(self.file_path, 'a', newline='') as csv_file:
            cwriter = csv.writer(csv_file)
            for line in new_lines:
                cwriter.writerows(line)

    def delete_rows(self, *row_nums):
        table_list = self.read_table()
        for row_num in row_nums:
            try:
                table_list.pop(row_num)
            except Exception:
                raise Exception('No Such Row In This File!')
        with open(self.file_path, 'w', newline='') as csv_file:
            cwriter = csv.writer(csv_file)
            cwriter.writerows(table_list)
