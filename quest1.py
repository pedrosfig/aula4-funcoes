import datetime as dt

def dias_vida(ano,mes,dia):
    hoje = dt.date.today()
    dia = dt.date(year=ano,month=mes,day=dia)
    dif = hoje - dia
    return dif


print(dias_vida(1997,12,26))