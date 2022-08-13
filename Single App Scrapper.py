# -*- coding: utf-8 -*-
"""
Created on Sun Dec 19 22:21:40 2021

"""
#Example

"""
binaryearth.coordsystool
com.VillageRun.AdventureGame
"""


import pandas as pd
from google_play_scraper import Sort, reviews_all
from tkinter import *

window=Tk()
window.title('Scrapper')
window.geometry("500x300")
window.configure(bg='purple')

def function():
    url = txtfld_api.get()
    result = reviews_all(
        url,
        sort=Sort.MOST_RELEVANT, 
    )
    print(result)
    df = pd.DataFrame(result) 
    df.to_csv('Scraped App.csv')
    
    messagebox.showinfo("Completed", "scraped")

lbl=Label(window, text="Play Store Scrapper", fg='white', bg='purple', font=("Calibiri", 12))
lbl.place(x=250, y=30, anchor='s')
lbl_id=Label(window, text="Enter App ID", fg='white',bg='purple', width=10)
lbl_id.place(x=80, y=50)
txtfld_api=Entry(window, text="ID",fg='black',bg='white', bd=5, width=45)
txtfld_api.place(x=170, y=50)
btn_aud=Button(window, text="Scrape", fg='white',bg='black' , bd=2, width=15, command=function)
btn_aud.place(x=170, y=100)
window.mainloop()