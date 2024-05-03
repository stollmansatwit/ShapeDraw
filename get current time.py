import datetime
from dateutil.relativedelta import relativedelta


now = datetime.datetime.now()
date_formated = now.strftime("%m/%d/%Y")
print(date_formated)