from CSV.CSV import CSVHandler

if __name__ == '__main__':
    ch = CSVHandler('./resource/testfile.csv')
    ret = ch.read_table_head()
    print(ret)
