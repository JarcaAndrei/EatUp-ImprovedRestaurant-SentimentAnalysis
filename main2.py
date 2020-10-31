from tkinter import Button, Tk, HORIZONTAL
from tkinter.ttk import Progressbar
import tkinter
import tkinter as tk
from tkinter import ttk  
from tkinter import *
import tkinter.messagebox
import random
import string

def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str
a=get_random_string(8)
conn=sqlite3.connect('orders.db')
c=conn.cursor()

c.execute("""UPDATE orders SET 
            cdkey=:cdkey

            WHERE oid= :oid""",
            {
                'cdkey': a,
                'oid': 0
            })

