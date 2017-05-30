import xlrd, requests
book = xlrd.open_workbook("a.xls")
sh = book.sheet_by_index(0)

for rx in range(sh.nrows):
    if rx < 14:
        continue

    row = sh.row(rx)
    post_data = {
        'year': 2017,
        'month': 3,
        'region_code': str(row[1].value),
        'provider_code': str(row[2].value),
        'provider_name': str(row[3].value),
        'is_provider': False,
        'treatment_function_code': str(row[4].value),
        'treatment_function_name': str(row[5].value),
        'total_started': int(row[6].value)
    }
    #print(post_data)
    r = requests.post("http://localhost:5000/api/new-provider", json=post_data)
    #print(r.text)

sh = book.sheet_by_index(1)

for rx in range(sh.nrows):
    if rx < 14:
        continue

    row = sh.row(rx)
    post_data = {
        'year': 2017,
        'month': 3,
        'region_code': str(row[1].value),
        'provider_code': str(row[2].value),
        'provider_name': str(row[3].value),
        'is_provider': True,
        'treatment_function_code': str(row[4].value),
        'treatment_function_name': str(row[5].value),
        'total_started': int(row[6].value)
    }
    #print(post_data)
    r = requests.post("http://localhost:5000/api/new-provider", json=post_data)
    #print(r.text)


