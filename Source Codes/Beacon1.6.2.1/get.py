import sys
import pytz
import datetime, calendar
from Messages_Declear import *

class get:
    def __init__(self,*arg, **kwarg) -> None:
        get.main(*arg, **kwarg)
    def main(software: str, args: str) -> None:
        globals()[software](args)

def time(timezone: str | None = None):
    tmz = pytz.timezone(timezone)
    curretTime = datetime.datetime.now(tmz)
    print("Current Time at: ", tmz, "is: ", curretTime)

def cal(month, year):
    cal = calendar.month(int(year), int(month))
    print(cal)

def gtcal_info():
    print("gtcal: get a calendar for a desired month in a year")
    print("Command Syntax: gtcal [month] [year]")
    print("[month]: month, have to be a int")

def get_info():
    print("get: get values or run softwares supported by this command")
    print("Command Syntax: get [software name]")