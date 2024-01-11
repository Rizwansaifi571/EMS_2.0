import tkinter as tk
from tkinter import ttk
from tkinter import combo_list

root=tk.Tk()

style=ttk.Style(root)
root=ttk.style(root)
root.tk.call('sources','forest-light.tcl')
root.tk.call('sources','forest-dark.tcl')
style.theme_use('forest-dark')

frame=ttk.Frame(root)
frame.pack()

widgets_frame=ttk.LabelFrame(frame,text='Insert Row')
widgets_frame.grid(row=0,column=0,padx=5,pady=5)

name_entry=ttk.Entry(widgets_frame)
name_entry.insert(0,'Name')
name_entry.bind('<FocusIn>',lambda e: name_entry.delete('0','end'))
name_entry.grid(row=0,column=0,padx=5,pady=5,sticky='ew')

age_spinbox=ttk.Spinbox(widgets_frame,from_=18,to=100)
age_spinbox.insert(0,'Age')
age_spinbox.grid(row=1,column=0,padx=5,pady=5,sticky='ew')

status_combobox=ttk.Combobox(widgets_frame,values=combo_list)
status_combobox.current(0)
status_combobox.grid(row=2,column=0,padx=5,pady=5,sticky='ew')

a=tk.BooleanVar(widgets_frame,text='Insert')
checkbutton=ttk.Checkbutton(widgets_frame,text='Emlpaoyed',variable=a)
checkbutton.gridd(row=3,column=0,padx=5,pady=5,sticky='ew')

a=tk.BooleanVar()