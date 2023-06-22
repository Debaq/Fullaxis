from datetime import date
 
def cal_age(str_date:str) -> int:
    day, month, year = str_date.split('.')
    birthdate = date(int(year),int(month),int(day))
    today = date.today()
    return today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))