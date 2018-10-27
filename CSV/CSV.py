import csv
import sys
from collections import defaultdict


class CSVHandler:

    uniq_key = ''

    def __init__(self, file_path, key):
        self.file_path = file_path
        self.id_row_map = {}

        if key == '':
            try:
                sys.exit(0)
            except:
                raise Exception('没有唯一key为识别')
        else:
            global uniq_key
            uniq_key = key
        self.title_column_map = {}
        self.__mapping_title_and_column_number()  # 同上，但是read_table_row_by_id，read_value_by_id_and_title等一些方法会失效
        self.__mapping_id_and_row_number()  # 不需要这个功能的话把这个注释掉

    def __mapping_title_and_column_number(self):
        head_list = self.read_table_head()
        for i, head in enumerate(head_list):
            self.title_column_map.__setitem__(head, i)

    def __mapping_id_and_row_number(self):
        with open(self.file_path, 'r') as csv_file:
            creader = csv.reader(csv_file)
            for i, row in enumerate(creader):
                global uniq_key
                key_column = self.title_column_map.get(uniq_key)
                self.id_row_map.__setitem__(row[key_column], i)

    def __refresh__mappings(self):
        self.__mapping_id_and_row_number()
        self.__mapping_title_and_column_number()

    def read_table_row_by_id(self, id):
        row_num = self.id_row_map.get(id)
        ret = self.read_table_row(row_num)
        return ret

    # 这个方法写的真是太垃圾了，但是我赶着打游戏，就这样吧，凑合能用
    def read_table_column(self, column_num):
        columns = defaultdict(list)
        with open(self.file_path, 'r') as csv_file:
            creader = csv.DictReader(csv_file)
            try:
                for row in creader:
                    for (k, v) in row.items():  # go over each column name and value
                        if self.title_column_map.get(k) == column_num:
                            columns[k].append(v)
                            k_static = k
            except Exception:
                raise Exception('No Such Column In This File!')

        return columns[k_static]

    def read_table_value_by_id_and_title(self, id, title):
        row_num = self.id_row_map.get(id)
        column_num = self.title_column_map.get(title)
        ret = self.read_table_value(row_num, column_num)
        return ret

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

    # 按理说是调用上面那个read_table_column方法的，但我写完才想起来，就这样吧
    def read_table_column_by_title(self, title):
        columns = defaultdict(list)
        with open(self.file_path, 'r') as csv_file:
            creader = csv.DictReader(csv_file)
            try:
                for row in creader:
                    for (k, v) in row.items():  # go over each column name and value
                        if k == title:
                            columns[k].append(v)
            except Exception:
                raise Exception('No Such Column In This File!')

        return columns[title]

    def read_table_value(self, row_num, column_num):
        row = self.read_table_row(row_num)
        return row[column_num]

    def edit_table_value(self, row_num, column_num, new_value):
        with open(self.file_path, 'r') as f:
            creader = csv.reader(f)
            lines = [l for l in creader]
            lines[row_num][column_num] = new_value
            file_content = lines
        with open(self.file_path, 'w', newline='') as csv_file:
            cwriter = csv.writer(csv_file)
            cwriter.writerows(file_content)

    def edit_table_value_by_id_and_title(self, id, title, new_value):
        row_num = self.id_row_map.get(id)
        column_num = self.title_column_map.get(title)
        self.edit_table_value(row_num, column_num, new_value)

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

    # 一行是一个list， *new_lines可以一下传好几行
    def add_new_rows(self, *new_lines):
        with open(self.file_path, 'a', newline='') as csv_file:
            cwriter = csv.writer(csv_file)
            for line in new_lines:
                cwriter.writerows(line)

    def add_new_head(self, new_title):
        with open(self.file_path, 'r') as f:
            creader = csv.reader(f)
            lines = [l for l in creader]
            lines[0].append(new_title)
        with open(self.file_path, 'w', newline='') as csv_file:
            cwriter = csv.writer(csv_file)
            cwriter.writerows(lines)

    def delete_rows(self, *row_nums):
        table_list = self.read_table()
        for i, row_num in enumerate(row_nums):
            try:
                table_list.pop(int(row_num) - i)
            except Exception:
                raise Exception('No Such Row In This File!')
        with open(self.file_path, 'w', newline='') as csv_file:
            cwriter = csv.writer(csv_file)
            cwriter.writerows(table_list)
        self.__refresh__mappings()

    def delete_rows_by_id(self, *ids):
        for id in ids:
            row_num = self.id_row_map.get(id)
            self.delete_rows(row_num)
        self.__refresh__mappings()
