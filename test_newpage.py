import requests
import json
import jsonpath
from xlrd import open_workbook

def test_newpagedata():
    data = {'season': 2017, 'total': 20}
    # data1= {'season': 2016, 'total': 21}
    url1='http://ergast.com/api/f1/2017/circuits.json'
    resp = requests.get(url1, params=data)
    print(f'RESP: {resp}')
    print(resp.text)
    assert('Status code: {}'.format(resp.status_code))=='Status code: 200'
    reponsetotal=('Payload:\n{}'.format(resp.text))
    for i,v  in enumerate(reponsetotal):
        if i=='total':
            assert v==20
        else:
            assert 1==2
    print(resp.elapsed.total_seconds())

def test_dynamicdata():
    book = open_workbook('Automation_Result')
    for sheet in book.sheets():
        for rowidx in range(sheet.nrows):
            row = sheet.row(rowidx)
            for colidx, cell in enumerate(row):
                if cell.value == "particularString":
                    print(sheet.name)
                    i=( colidx)
                    j=( rowidx)

    data={i:j}
    readval=sheet.cell_value(i, j)
    url1 = 'http://ergast.com/api/f1/'+readval+'/circuits.json'
    resp = requests.get(url1, params=data)
    assert ('Status code: {}'.format(resp.status_code)) == 'Status code: 200'
    reponsetotal = ('Payload:\n{}'.format(resp.text))
    for i, v in enumerate(reponsetotal):
        if i == 'total':
            assert v == 20
        else:
            assert 1 == 2



