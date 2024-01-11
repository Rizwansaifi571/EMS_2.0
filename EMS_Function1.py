import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from PIL import Image, ImageTk
import pandas as pd
import openpyxl
from docx import Document

class EmployeeManagementSystem:
    def __init__(self, root):
        self.root = root
        self.theme = "light"  # Default theme

        # Header Frame
        self.header_frame = tk.Frame(root, bg="#273746", height=70, bd=1, relief=tk.SOLID)
        self.header_frame.pack(fill=tk.X)

        header_label = tk.Label(self.header_frame, text="EMS - A Business Intelligence Tool", font=("Arial", 20, "bold"), bg="#273746", fg="white")
        header_label.pack(pady=15)

        # Main Part Frame
        self.main_frame = tk.Frame(root, bg="#ecf0f1", height=250, bd=1, relief=tk.SOLID)
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Skyblue Left Frame
        self.menu_frame = tk.Frame(self.main_frame, bg="darkgrey", width=150, bd=1, relief=tk.SOLID)
        self.menu_frame.pack(fill=tk.Y, side=tk.LEFT)

        # Heading for File Upload
        file_heading = tk.Label(self.menu_frame, text="Upload File", font=("Arial", 14, "bold"), bg="darkgrey", fg="white")
        file_heading.pack(pady=10)

        # Buttons for Different File Types
        file_types = ["CSV", "Text", "Excel", "Word"]
        for file_type in file_types:
            button = tk.Button(self.menu_frame, text=f"Open {file_type}", command=lambda ft=file_type: self.open_file(ft),
                               bg="#273746", fg="#ecf0f1", width=15, bd=1, relief=tk.RAISED)
            button.pack(pady=5)

        # Main Content Frame (2/3 of Main Part Frame)
        self.content_frame = ttk.Frame(self.main_frame, style="Light.TFrame")
        self.content_frame.pack(fill=tk.BOTH, expand=True)

        # Treeview widget for tabular and non-tabular display
        self.treeview_frame = ttk.Frame(self.content_frame, style="Light.TFrame")
        self.treeview_frame.pack(expand=True, fill=tk.BOTH)

        self.treeview_style = ttk.Style()
        self.treeview_style.configure("Treeview", font=("Arial", 10), background="#ecf0f1", fieldbackground="#ecf0f1", foreground="#17202a")  # Set font and background color for Treeview widget

        # Configure styles for Light and Dark themes
        self.treeview_style.configure("Light.TFrame", background="#ecf0f1")
        self.treeview_style.configure("Dark.TFrame", background="#2c3e50")

        self.treeview = ttk.Treeview(self.treeview_frame, show="headings", style="Treeview")
        self.treeview["columns"] = tuple()  # The columns will be dynamically set based on the CSV file
        self.treeview.pack(expand=True, fill=tk.BOTH)

        # Add vertical scrollbar
        y_scrollbar = ttk.Scrollbar(self.treeview_frame, orient="vertical", command=self.treeview.yview)
        y_scrollbar.pack(side="right", fill="y")
        self.treeview.configure(yscrollcommand=y_scrollbar.set)

        # Add horizontal scrollbar
        x_scrollbar = ttk.Scrollbar(self.treeview_frame, orient="horizontal", command=self.treeview.xview)
        x_scrollbar.pack(side="bottom", fill="x")
        self.treeview.configure(xscrollcommand=x_scrollbar.set)

        # Footer Frame
        self.footer_frame = tk.Frame(root, bg="#273746", height=30, bd=1, relief=tk.SOLID)
        self.footer_frame.pack(fill=tk.X, side=tk.BOTTOM)

        footer_label = tk.Label(self.footer_frame, text="© 2024 EMS - A Business Intelligence Tool", font=("Arial", 8), bg="#273746", fg="white")
        footer_label.pack(pady=5)

        # Toggle Theme Button with Image
        toggle_image_light = Image.open("files/images/light.png")  # Replace with your light theme icon
        toggle_image_dark = Image.open("files/images/dark.png")  # Replace with your dark theme icon
        light_icon_resized = toggle_image_light.resize((20, 20))  # Resize the image
        dark_icon_resized = toggle_image_dark.resize((20, 20))  # Resize the image
        self.light_icon = ImageTk.PhotoImage(light_icon_resized)
        self.dark_icon = ImageTk.PhotoImage(dark_icon_resized)

        self.toggle_theme_button = tk.Button(self.menu_frame, image=self.light_icon, command=self.toggle_theme, bd=0)
        self.toggle_theme_button.pack(side=tk.BOTTOM, padx=10, pady=5, anchor='w')

        # Call set_theme after all frames are initialized
        self.set_theme()

    def toggle_theme(self):
        self.theme = "dark" if self.theme == "light" else "light"
        self.set_theme()

    def set_theme(self):
        if self.theme == "light":
            self.root.configure(bg="#17202a")  # Set background color
            self.header_frame.configure(bg="#273746")
            self.menu_frame.configure(bg="darkgrey")
            self.main_frame.configure(bg="#ecf0f1")
            self.content_frame.configure(style="Light.TFrame")
            self.treeview_frame.configure(style="Light.TFrame")
            self.footer_frame.configure(bg="#273746")
            self.toggle_theme_button.configure(image=self.light_icon)
        else:
            self.root.configure(bg="black")  # Set background color
            self.header_frame.configure(bg="#001f3f")
            self.menu_frame.configure(bg="#1a1a1a")
            self.main_frame.configure(bg="#2c3e50")
            self.content_frame.configure(style="Dark.TFrame")
            self.treeview_frame.configure(style="Dark.TFrame")
            self.footer_frame.configure(bg="#001f3f")
            self.toggle_theme_button.configure(image=self.dark_icon)

    def open_file(self, file_type):
        file_extension = file_type.lower()
        file_path = filedialog.askopenfilename(title=f"Select {file_type} File", filetypes=[(f"{file_type} files", f"*.{file_extension}")])
        if file_path:
            print(f"Opening {file_type} file: {file_path}")
            try:
                self.display_data(file_path, file_type)
            except Exception as e:
                messagebox.showerror("Error", f"Error reading {file_type} file: {e}")

    def display_data(self, file_path, file_type):
        if file_type.lower() == 'csv':
            df = pd.read_csv(file_path)
            self.display_in_treeview(df)
        elif file_type.lower() == 'text':
            with open(file_path, 'r') as file:
                text_data = file.read()
            self.display_in_treeview(pd.DataFrame({"Text Data": [text_data]}))
        elif file_type.lower() == 'excel':
            workbook = openpyxl.load_workbook(file_path)
            sheet = workbook.active
            data = []
            for row in sheet.iter_rows(min_row=1, values_only=True):
                data.append(row)
            workbook.close()
            df = pd.DataFrame(data, columns=sheet[1])
            self.display_in_treeview(df)
        elif file_type.lower() == 'word':
            document = Document(file_path)
            text_data = ""
            for paragraph in document.paragraphs:
                text_data += paragraph.text + "\n"
            self.display_in_treeview(pd.DataFrame({"Text Data": [text_data]}))

    def display_in_treeview(self, df):
        # Clear existing columns and data
        for col in self.treeview["columns"]:
            self.treeview.heading(col, text="")
            self.treeview.column(col, width=0)

        # Set columns based on DataFrame columns
        self.treeview["columns"] = tuple(df.columns)

        # Insert column headings
        for col in df.columns:
            self.treeview.heading(col, text=col)
            self.treeview.column(col, width=100)  # Adjust the width as needed

        # Insert data
        for index, row in df.iterrows():
            self.treeview.insert("", index, values=tuple(row))

if __name__ == "__main__":
    root = tk.Tk()
    app = EmployeeManagementSystem(root)
    root.mainloop()
