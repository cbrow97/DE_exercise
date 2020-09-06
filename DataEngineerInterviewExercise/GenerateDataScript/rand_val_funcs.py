import pandas as pd
from collections import namedtuple
import numpy as np
import random
import names
import string
import pycountry
import datetime

def generate_random_date(start_date=datetime.date(2017, 1, 1), end_date=datetime.date.today(), date_format=None):
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)

    if date_format:
        return (start_date + datetime.timedelta(days=random_number_of_days)).strftime(date_format)
    else:
        return start_date + datetime.timedelta(days=random_number_of_days)