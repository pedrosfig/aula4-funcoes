import datetime as dt

def dias_vida(data):
    hoje = dt.date.today()
    dif = hoje - data
    return dif

eu = dt.date(day=26, month=12,year=1997)
print(dias_vida(eu))