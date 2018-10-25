from CSV import CSVHandler


# 这个方法是演示用的，平时不要这么写
def init_csv():
    lines = [['ID', 'TITLE1', 'TITLE2'], ['1', '1-1', '1-2'], ['2', '2-1', '2-2'], ['3', '3-1', '3-2']]
    import csv  # 演示用，平时不要这样import
    with open('./resource/testfile.csv', 'w', newline='') as f:
        cwriter = csv.writer(f, quotechar=',')
        for line in lines:
            cwriter.writerow(line)


# 这个也是演示用的
def print_ret(demo_name, ret):
    print('==============================')
    print(demo_name, ': ')
    print(ret)
    print('==============================\n')


def read_table_head_demo():
    ch = CSVHandler('./resource/testfile.csv')
    ret = ch.read_table_head()
    print_ret('读取表头', ret)


def read_table_row_demo(row_num):
    ch = CSVHandler('./resource/testfile.csv')
    ret = ch.read_table_row(row_num)
    print_ret('读取某一行', ret)


def read_table_column_demo(column_name):
    ch = CSVHandler('./resource/testfile.csv')
    ret = ch.read_table_column(column_name)
    print_ret('读取某一列', ret)


def edit_table_head_demo(old_value, new_value):
    ch = CSVHandler('./resource/testfile.csv')
    ch.edit_table_head(old_value, new_value)
    print_ret('修改表头', '返回类型void')


def edit_tbale_value_demo(row_num, column_num, new_value):
    ch = CSVHandler('./resource/testfile.csv')
    ch.edit_table_value(row_num, column_num, new_value)
    print_ret('修改表值', '返回类型void')


def add_new_rows_demo(*lines):
    ch = CSVHandler('./resource/testfile.csv')
    ch.add_new_rows(*lines)
    print_ret('增加新行', '返回类型void')


def dele_rows_demo(*row_num):
    ch = CSVHandler('./resource/testfile.csv')
    ch.delete_rows(*row_num)
    print_ret('删除某行', '返回类型void')


if __name__ == '__main__':
    init_csv()
    read_table_head_demo()  # 读取表头
    read_table_row_demo(1)  # 读取某一行
    read_table_column_demo('TITLE1')  # 读取某一列
    edit_table_head_demo('TITLE2', 'TITLE2')  # 修改表头
    edit_tbale_value_demo(1, 1, 'new-1-1')  # 修改表值
    add_new_rows_demo([['a', 'a-1', 'a-2'], ['b', 'b-1', 'b-2'], ['c', 'c-1', 'c-2']])
    dele_rows_demo(2, 5)  # 删除好几行，参数可随便多少
