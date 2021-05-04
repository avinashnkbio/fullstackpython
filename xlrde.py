import xlwt
from datetime import datetime

style0 = xlwt.easyxf('font: name Times New Roman, color-index red, bold on',
    num_format_str='#,##0.00')
style1 = xlwt.easyxf(num_format_str='D-MMM-YY')

wb = xlwt.Workbook()
ws = wb.add_sheet('A Test Sheet')
style = xlwt.XFStyle()
style.alignment.wrap = 1

   
    

ws.write(0, 0, 1234.56, style0)
ws.write(1, 0, datetime.now(), style1)
ws.write(2, 0, 1)
ws.write(2, 1, 1)
ws.write(2, 2, xlwt.Formula("A3+B3"))
ws.write(2, 7, 100)
ws.write(3, 10,'Full stack python\n',style)

ws.write(5, 0, 'Name',style)
ws.write(5, 1, 'Email',style)

ws.write(7, 0, 'Avinash Nandakumar')
ws.write(7, 1, 'avinash.nkbio@gmail.com')

ws.write(8, 0, 'Anjana Sasi')
ws.write(8, 1, 'anjanasasi@gmail.com')

ws.write(9, 0, 'Anju Sasi')
ws.write(9, 1, 'anjuak3456@gmail.com')

ws.write(10, 0, 'Rincy Reji')
ws.write(10, 1, 'rincyanna10@gmail.com')

ws.write(11, 0, 'Nithin joseph')
ws.write(11, 1, 'Nithinjo2599@gmail.com')


wb.save('example.xls')