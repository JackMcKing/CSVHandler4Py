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
    ch = CSVHandler('./resource/testfile.csv', 'ID')
    ret = ch.read_table_head()
    print_ret('读取表头', ret)


def read_table_row_demo(row_num):
    ch = CSVHandler('./resource/testfile.csv', 'ID')
    ret = ch.read_table_row(row_num)
    print_ret('读取某一行', ret)


def read_table_column_demo(title):
    ch = CSVHandler('./resource/testfile.csv', 'ID')
    ret = ch.read_table_column(title)
    print_ret('读取某一列', ret)


def edit_table_head_demo(old_value, new_value):
    ch = CSVHandler('./resource/testfile.csv', 'ID')
    ch.edit_table_head(old_value, new_value)
    print_ret('修改表头', '返回类型void')


def edit_tbale_value_demo(row_num, column_num, new_value):
    ch = CSVHandler('./resource/testfile.csv', 'ID')
    ch.edit_table_value(row_num, column_num, new_value)
    print_ret('修改表值', '返回类型void')


def add_new_rows_demo(*lines):
    ch = CSVHandler('./resource/testfile.csv', 'ID')
    ch.add_new_rows(*lines)
    print_ret('增加新行', '返回类型void')


def dele_rows_demo(*row_num):
    ch = CSVHandler('./resource/testfile.csv', 'ID')
    ch.delete_rows(*row_num)
    print_ret('删除某行', '返回类型void')


def read_table_row_by_id_demo(id):
    ch = CSVHandler('./resource/testfile.csv', 'ID')
    ret = ch.read_table_row_by_id(id)
    print_ret('通过id读取某行', ret)
    

def read_table_column_by_title_demo(title):
    ch = CSVHandler('./resource/testfile.csv', 'ID')
    ret = ch.read_table_column_by_title(title)
    print_ret('通过title读取某一列', ret)
    
    
def read_table_value_demo(row_num, column_num):
    ch = CSVHandler('./resource/testfile.csv', 'ID')
    ret = ch.read_table_value(row_num, column_num)
    print_ret('通过坐标读取某一个值', ret)
    
    
def read_table_value_by_id_and_title_demo(id, title):
    ch = CSVHandler('./resource/testfile.csv', 'ID')
    ret = ch.read_table_value_by_id_and_title(id, title)
    print_ret('通过id和title读取某一个值', ret)
    
    
def edit_table_value_by_id_and_title_demo(id, title, new_value):
    ch = CSVHandler('./resource/testfile.csv', 'ID')
    ch.edit_table_value_by_id_and_title(id, title, new_value)
    print_ret('通过id和title读取某一个值', '返回类型void')


def add_new_head_demo(new_title):
    ch = CSVHandler('./resource/testfile.csv', 'ID')
    ch.add_new_head(new_title)
    print_ret('增加一个新的head', '返回类型void')


def delete_row_by_id_demo(*row_id):
    ch = CSVHandler('./resource/testfile.csv', 'ID')
    ch.delete_rows_by_id(*row_id)
    print_ret('通过id删除某一行', '返回类型void')


if __name__ == '__main__':
    init_csv()
    read_table_row_by_id_demo('1')  # 通过id读取某一行
    read_table_head_demo()  # 读取表头
    read_table_row_demo(1)  # 读取某一行
    read_table_column_demo(1)  # 读取某一列
    read_table_column_by_title_demo('TITLE1')  # 通过title读取某一列
    read_table_value_demo(3, 2)  # 通过坐标读取某一个值
    read_table_value_by_id_and_title_demo('3', 'TITLE2')  # 通过id和title读取某一个值
    edit_table_head_demo('TITLE2', 'NEW-TITLE2')  # 修改表头
    edit_tbale_value_demo(1, 1, 'new-1-1')  # 修改表值
    edit_table_value_by_id_and_title_demo('3', 'TITLE1', 'new-3-title1')  # 通过id和title修改一个值
    add_new_head_demo('new-title')
    add_new_rows_demo([['4', '4-1', '4-2'], ['5', '5-1', '5-2'], ['6', '6-1', '6-2']])  # 增加三行
    dele_rows_demo(2, 5)  # 删除好几行，参数可随便多少
    delete_row_by_id_demo('1', '3')  # 根据ID删除好几行
