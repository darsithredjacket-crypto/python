import random
from datetime import datetime, timedelta
start_date=datetime(2020,1,1)
end_date=datetime(2026,12,31)
time_difference=end_date-start_date
random_seconds=random.randint(0,int(time_difference.total_seconds()))
random_datetime=start_date+timedelta(seconds=random_seconds)
print("random date and time", random_datetime)