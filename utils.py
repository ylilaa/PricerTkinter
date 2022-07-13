from tkinter import *
from tkinter import messagebox
from xml.dom.minidom import TypeInfo

import pandas as pd
import numpy as np
from termcolor import colored

from config import *


def donothing():
    messagebox.showinfo(title="walo", message=" w ta 9lwa walo")

def get_fund_by_name(fund):
    config = AppConfig()
    original_df = pd.read_excel(config.db_name)
    df = original_df[original_df['CODE_FONDS'] == fund]
    print(colored('Fund retrieved from database Successfully','green'))
    return df

def get_funds_array():
    config = AppConfig()
    original_df = pd.read_excel(config.db_name).astype(str)
    array = original_df['CODE_FONDS'].unique()
    print(colored('List of Funds retrieved from database Successfully','green'))
    return array





