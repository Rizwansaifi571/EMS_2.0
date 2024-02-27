import tkinter as tk
from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import os
from datetime import datetime
from final import *
import pandas as pd


def update_time(time_label):
    # Get the current time, format it, and update the label
    current_time = datetime.now().strftime("%d-%m-%Y \n %H:%M:%S")
    time_label.config(text=current_time)
    # Schedule the `update_time` function to be called after 1000ms
    time_label.after(1000, lambda: update_time(time_label))


opened_files = []
opened_columns = [] 
def open_file(file_type, display_area):
    global opened_columns
    # Define a dictionary to map file types to their extensions
    file_extensions = {
        "Excel": "xlsx",
        "CSV": "csv",
        "Word": "docx",
        "TXT": "txt",
        "MySQL": "sql",  # Assuming you're opening SQL files for MySQL
        "JSON": "json",
        "Others": "*"  # Use '*' for all file types; adjust as necessary for "Others"
    }
    file_extension = file_extensions.get(file_type, "*")
    file_path = filedialog.askopenfilename(title=f"Select {file_type} File", filetypes=[(f"{file_type} files", f"*.{file_extension}")])
    if file_path:
        filename = os.path.splitext(os.path.basename(file_path))[0]  # Get filename without extension
        display_file_name(filename, display_area)
    
        if file_type in ["Excel", "CSV"]:
            # Read the file using pandas
            if file_type == "Excel":
                df = pd.read_excel(file_path)
            else:  # CSV
                df = pd.read_csv(file_path)
            # Extract column names
            columns = df.columns.tolist()
            # Now call data_cleaning and pass the columns
            opened_columns = columns
            
def display_file_name(filename, display_area):
    # Function to display the filename in the specified area
    global opened_files
    opened_files.append(filename)  # Add filename to the list of opened files
    
    for i, name in enumerate(opened_files):
        tk.Label(display_area, text=name, bg='#ffffff', font=('Arial', 12, 'bold')).grid(row=i, column=0, sticky='w', padx=10, pady=5)

def show_secondary_page():
    window = tk.Tk()
    window.title("Dashboard")
    window.state("zoomed")
    window.title('EMS - A Business Intelligence tool')
    window.configure(bg="#eff5f6")
    image_icon = PhotoImage(file="files/images/logo.png")
    window.iconphoto(False,image_icon)
    
    # Menu Bar
    menubar = Menu(window)
    window.config(menu=menubar)
    
    # File Menu
    file_menu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="File", menu=file_menu)
    file_menu.add_command(label="Open", command=lambda: messagebox.showinfo("Open", "Open clicked!"))
    file_menu.add_command(label="New", command=lambda: messagebox.showinfo("Open", "Open clicked!"))
    file_menu.add_command(label="print", command=lambda: messagebox.showinfo("Open", "Open clicked!"))
    file_menu.add_command(label="Save", command=lambda: messagebox.showinfo("Save", "Save clicked!"))
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=window.quit)
    
    # Help Menu
    help_menu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Help", menu=help_menu)
    help_menu.add_command(label="About", command=lambda: messagebox.showinfo("About", "Your App Version 1.0"))
    
    header = Frame(window, bg="#616596", width=1366, height=60)
    header.place(x=200, y=0)
        
    logout_text = Button(header, text="Logout",border = 0, font="arial 12 bold", bg="#616596", fg="white", cursor="hand2")
    logout_text.place(x=1090,y=15)
        
    #sidebar
    sidebar = Frame(window, bg="#ffffff")
    sidebar.place(x=0,y=0,width=200,height=700)
    
    time_label = Label(window, font=('Arial', 12, 'normal'), fg='black', bg='#ffffff')
    time_label.place(x=40, y=25)
    update_time(time_label)

# Replace PhotoImage with ImageTk.PhotoImage
    original_img = Image.open('files/images/avatar.png')
    resized_img = original_img.resize((150, 150), Image.Resampling.LANCZOS) 
    img = ImageTk.PhotoImage(resized_img)
    sidebar.img = img
    # Create a label to display the image and place it on the sidebar
    avatar_label = Label(sidebar, image=img, bg='#ffffff')
    avatar_label.place(x=20, y=80)
    
    username_label = Label(sidebar, text=f"Hello", font="arial 12 bold", bg="#ffffff")
    username_label.place(x=50,y=240)
    
    #body
    heading = Label(window, text = "User Dashboard", font="arial 20 bold", fg="#616596")
    heading.place(x=700, y=70)
    
    #frames
    bodyframe1 = Frame(window, bg='#ffffff')
    bodyframe1.place(x=240, y= 110, width=710, height=320)
    
    sub_frame = Frame(window, bg="#616596")
    sub_frame.place(x=1030,y=110, width=310, height=320)
    Label(sub_frame, text=f"{opened_columns}", font="arial 20 bold", bg="#616596", fg="white").place(x=65, y=30)
    
    file_types = ["Excel", "CSV", "Word", "TXT", "MySQL", "JSON", "Others"]
    
    for i, file_type in enumerate(file_types):
        Button(sidebar, text=file_type, command=lambda ft=file_type, bf=bodyframe1: open_file(ft, bf),
               border=0, font="arial 10 bold", bg="black", fg="white").place(x=20, y=300 + (i * 50), width=160, height=30)
    
    bodyframe2 = Frame(window, bg='#616596')
    bodyframe2.place(x=240, y= 455, width=310, height=220)
    
    heading_data_analysis = Label(bodyframe2, text = "Data Analysis", font="arial 20 bold", bg='#616596', fg="white")
    heading_data_analysis.place(x=65, y=30)
    
    pil_image = Image.open("files/images/analysis.png")
    analysis_image = ImageTk.PhotoImage(pil_image)
    Button(bodyframe2, image=analysis_image, command=EmployeeManagementSystem.data_cleaning, border=0, bg="#616596",width=200, height=100).place(x=53, y=90)
    
    bodyframe3 = Frame(window, bg='#414656')
    bodyframe3.place(x=640, y= 455, width=310, height=220)
    
    heading_data_visualization = Label(bodyframe3, text = "Data Visualization", font="arial 20 bold", bg='#414656', fg="white")
    heading_data_visualization.place(x=35, y=30)
    
    pil_image2 = Image.open("files/images/visualization.png")
    visualization_image = ImageTk.PhotoImage(pil_image2)
    Button(bodyframe3, image=visualization_image, border=0, bg="#616596",width=200, height=100).place(x=53, y=90)
    
    bodyframe4 = Frame(window, bg='#616596')
    bodyframe4.place(x=1030, y= 455, width=310, height=220)
    
    heading_Machine_learning_algorithms = Label(bodyframe4, text = "Machine learning", font="arial 20 bold", bg='#616596', fg="white")
    heading_Machine_learning_algorithms.place(x=40, y=30)
    
    pil_image3 = Image.open("files/images/machine_learning.png")
    machine_learning_image = ImageTk.PhotoImage(pil_image3)
    Button(bodyframe4, image=machine_learning_image, border=0, bg="#616596",width=200, height=100).place(x=53, y=90)
    
    window.mainloop()
    
show_secondary_page()