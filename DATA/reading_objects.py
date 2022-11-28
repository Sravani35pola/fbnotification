import xlrd
from LIBRARY.config import Config


class ReadExcel():

    def read_test_data(self, sheetname):
        wb = xlrd.open_workbook(Config.DATA_PATH)
        ws = wb.sheet_by_name(sheetname)
        columns = ws.ncols
        rows = ws.get_rows()  #generator object
        header = next(rows)
        data = []

        for row in rows:
            values = ()
            for j in range(columns):
                values += (row[j].value,)
            data.append(values)
        return data

    def read_locator(self, sheetname):
        wb = xlrd.open_workbook(Config.LOCATOR_PATH)
        ws = wb.sheet_by_name(sheetname)
        #rows = ws.get_rows()
        rows=ws.nrows
        #header = next(rows)
        # dict_1
        d={}
        for i in range(1,rows):
            rows=ws.row_values(i)
            d[rows[0]]=(rows[1],rows[2])
        return d
#print(read_locators())


