import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
import pandas as pd
from pandasql import sqldf
from pandastable import Table
import glob

def read_csv() :
    csv = glob.glob("*.csv")
    csv = csv[0]
    db = pd.read_csv(csv, header=None,
                     names=["Type", "ID", "Birth_Time_ms", "Deathtime_Time_ms", "Time_lived", "Max_Health", "Updates", "Health_Ratio", "Energy", "Max_Energy", "Energy_Ratio", "Tiles_Travel",
                            "Attack_Power", "Organism_Attacked", "Animals_Kill", "Plants_Killed", "Number_Offspring", "R", "G", "B"])
    assert db is not None
    return db


def pysqldf(query):
    """Wrapper function for sqldf"""
    return sqldf(query, globals())

read_csv()
