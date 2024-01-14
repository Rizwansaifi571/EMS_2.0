import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from tkinter.simpledialog import askstring
from PIL import Image, ImageTk
import pandas as pd
import openpyxl
from docx import Document
from scipy.stats import mode as scipy_mode

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

        # Bottom Frame
        self.bottom_frame = tk.Frame(self.main_frame, bg="#ecf0f1", bd=1, relief=tk.SOLID)
        self.bottom_frame.pack(fill=tk.X)

        # Buttons for Data Operations
        data_operations = ["DATA CLEANING", "DATA INFORMATION", "DATA VISUALIZATION", "STATISTIC OF DATA"]
        for operation in data_operations:
            operation_button = tk.Button(self.bottom_frame, text=operation, command=lambda op=operation: self.perform_operation(op),
                                         bg="#273746", fg="#ecf0f1", width=17, bd=1, relief=tk.RAISED)
            operation_button.pack(side=tk.LEFT, padx=10, pady=5)

        # Download Button
        download_button = tk.Button(self.bottom_frame, text="Download Data", command=self.download_data, bg="#273746", fg="#ecf0f1", width=15, bd=1, relief=tk.RAISED)
        download_button.pack(side=tk.RIGHT, padx=10, pady=5)

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
        self.treeview_style.configure("Treeview", font=("Arial", 10), background="#ecf0f1", fieldbackground="#ecf0f1", foreground="#17202a")

        # Configure styles for Light and Dark themes
        self.treeview_style.configure("Light.TFrame", background="#ecf0f1")
        self.treeview_style.configure("Dark.TFrame", background="#2c3e50")

        self.treeview = ttk.Treeview(self.treeview_frame, show="headings", style="Treeview")
        self.treeview["columns"] = tuple()
        self.treeview.pack(expand=True, fill=tk.BOTH)

        y_scrollbar = ttk.Scrollbar(self.treeview_frame, orient="vertical", command=self.treeview.yview)
        y_scrollbar.pack(side="right", fill="y")
        self.treeview.configure(yscrollcommand=y_scrollbar.set)

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
        light_icon_resized = toggle_image_light.resize((20, 20))
        dark_icon_resized = toggle_image_dark.resize((20, 20))
        self.light_icon = ImageTk.PhotoImage(light_icon_resized)
        self.dark_icon = ImageTk.PhotoImage(dark_icon_resized)

        self.toggle_theme_button = tk.Button(self.menu_frame, image=self.light_icon, command=self.toggle_theme, bd=0)
        self.toggle_theme_button.pack(side=tk.BOTTOM, padx=10, pady=5, anchor='w')

        self.set_theme()

    def toggle_theme(self):
        self.theme = "dark" if self.theme == "light" else "light"
        self.set_theme()

    def set_theme(self):
        if self.theme == "light":
            self.root.configure(bg="#17202a")
            self.header_frame.configure(bg="#273746")
            self.menu_frame.configure(bg="darkgrey")
            self.main_frame.configure(bg="#ecf0f1")
            self.content_frame.configure(style="Light.TFrame")
            self.treeview_frame.configure(style="Light.TFrame")
            self.footer_frame.configure(bg="#273746")
            self.toggle_theme_button.configure(image=self.light_icon)
        else:
            self.root.configure(bg="black")
            self.header_frame.configure(bg="#001f3f")
            self.menu_frame.configure(bg="#1a1a1a")
            self.main_frame.configure(bg="#2c3e50")
            self.content_frame.configure(style="Dark.TFrame")
            self.treeview_frame.configure(style="Dark.TFrame")
            self.footer_frame.configure(bg="#001f3f")
            self.toggle_theme_button.configure(image=self.dark_icon)

    def download_data(self):
        if self.current_data is not None and isinstance(self.current_data, pd.DataFrame):
            file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])

            if file_path:
                try:
                    self.current_data.to_csv(file_path, index=False)
                    messagebox.showinfo("Download Successful", f"Data has been successfully downloaded to:\n{file_path}")
                except Exception as e:
                    messagebox.showerror("Error", f"Error while saving data: {e}")
        else:
            messagebox.showwarning("No Data", "Please open a file first to load data.")


    def perform_operation(self, operation):
        if operation == "DATA CLEANING":
            self.data_cleaning()
        elif operation == "DATA INFORMATION":
            self.data_information()
        elif operation == "DATA VISUALIZATION":
            self.data_visualization()
        elif operation == "STATISTIC OF DATA":
            self.statistic_of_data()

    def data_cleaning(self):
        cleaning_window = tk.Toplevel(self.root)
        cleaning_window.title("Data Cleaning - Dealing with Empty Cells")
        cleaning_window.configure(bg="#ecf0f1")  # Background color for the cleaning window

        # Header Frame of data_cleaning
        self.header_frame2 = tk.Frame(cleaning_window, bg="#273746", height=70, bd=1, relief=tk.SOLID)
        self.header_frame2.pack(fill=tk.X)

        header_label = tk.Label(self.header_frame2, text="DATA_CLEANING", font=("Arial", 20, "bold"), bg="#273746", fg="white")
        header_label.pack(pady=15)

        # Main Part Frame of data_cleaning
        self.main_frame2 = tk.Frame(cleaning_window, bg="#ecf0f1", height=250, bd=1, relief=tk.SOLID)
        self.main_frame2.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Skyblue Left Frame of data_cleaning
        self.menu_frame2 = tk.Frame(self.main_frame2, bg="darkgrey", width=150, bd=1, relief=tk.SOLID)
        self.menu_frame2.pack(fill=tk.Y, side=tk.LEFT)

        remove_empty_cells_button = tk.Button(self.menu_frame2, text="Removing Rows of Empty Cells ", command=self.remove_empty_cells, bg="grey", fg="white")
        remove_empty_cells_button.pack(pady=10)

        replace_empty_values_button = tk.Button(self.menu_frame2, text="Replace Empty Values", command=self.replace_empty_values, bg="grey", fg="white")
        replace_empty_values_button.pack(pady=10)

        replace_using_mean_button = tk.Button(self.menu_frame2, text="Replacing Empty Cells Using Mean", command=self.replace_using_mean, bg="grey", fg="white")
        replace_using_mean_button.pack(pady=10)

        replace_using_median_button = tk.Button(self.menu_frame2, text="Replacing Empty Cells Using Median", command=self.replace_using_median, bg="grey", fg="white")
        replace_using_median_button.pack(pady=10)

        replace_using_mode_button = tk.Button(self.menu_frame2, text="Replacing Empty Cells Using Mode", command=self.replace_using_mode, bg="grey", fg="white")
        replace_using_mode_button.pack(pady=10)

    def remove_empty_cells(self):
        if self.current_data is not None and isinstance(self.current_data, pd.DataFrame):
            # Ask the user for the column name
            column_name = askstring("Column Name", "Enter the column name:")

            if column_name is not None:
                try:
                    # Remove rows with empty cells or cells containing any value
                    self.current_data = self.current_data.dropna(subset=[column_name], how='any')
                
                    self.display_in_treeview(self.current_data)
                    messagebox.showinfo("Remove Cells", f"All rows with empty cells in column '{column_name}' removed successfully.")
                except KeyError:
                    messagebox.showwarning("Column Not Found", f"Column '{column_name}' not found.")
            else:
                messagebox.showwarning("Invalid Input", "Please enter a valid column name.")
        else:
            messagebox.showwarning("No Data", "Please open a file first to load data.")



    def replace_empty_values(self):
        if self.current_data is not None and isinstance(self.current_data, pd.DataFrame):
            # Ask the user for the column name
            column_name = askstring("Column Name", "Enter the column name:")

            if column_name is not None:
                try:
                    # Ask the user for the row number (if any)
                    row_number_input = askstring("Row Number", "Enter the row number (leave blank to replace all):")
                
                    if row_number_input:
                        row_number = int(row_number_input) - 1  # Adjust for zero-based indexing
                        if row_number < 0 or row_number >= len(self.current_data):
                            raise ValueError("Invalid row number.")
                    else:
                        row_number = None

                    # Ask the user for the value to replace NaN
                    replacement_value = askstring("Replacement Value", "Enter the value to replace NaN:")

                    if row_number is not None:
                        # Replace NaN in a specific row
                        self.current_data.at[row_number, column_name] = replacement_value
                        messagebox.showinfo("Replace Value", f"Value in row {row_number + 1}, column '{column_name}' replaced successfully.")
                    else:
                        # Replace all NaN values in the specified column
                        self.current_data[column_name].fillna(replacement_value, inplace=True)
                        messagebox.showinfo("Replace Value", f"All NaN values in column '{column_name}' replaced successfully.")

                    # Refresh the Treeview
                    self.display_in_treeview(self.current_data)

                except ValueError as e:
                    messagebox.showwarning("Invalid Input", str(e))
            else:
                messagebox.showwarning("Invalid Input", "Please enter a valid column name.")
        else:
            messagebox.showwarning("No Data", "Please open a file first to load data.")


    def replace_using_mean(self):
        if self.current_data is not None and isinstance(self.current_data, pd.DataFrame):
            # Ask the user for the column name
            column_name = askstring("Column Name", "Enter the column name:")

            if column_name is not None:
                try:
                    # Ask the user for the row number (if any)
                    row_number_input = askstring("Row Number", "Enter the row number (leave blank to replace all):")

                    if row_number_input:
                        row_number = int(row_number_input) - 1  # Adjust for zero-based indexing
                        if row_number < 0 or row_number >= len(self.current_data):
                            raise ValueError("Invalid row number.")
                    else:
                        row_number = None

                    # Calculate the mean of the specified column
                    column_mean = self.current_data[column_name].mean()

                    if row_number is not None:
                        # Replace NaN in a specific row with the mean
                        self.current_data.at[row_number, column_name] = column_mean
                        messagebox.showinfo("Replace Value", f"Value in row {row_number + 1}, column '{column_name}' replaced with the mean: {column_mean}")
                    else:
                        # Replace all NaN values in the specified column with the mean
                        self.current_data[column_name].fillna(column_mean, inplace=True)
                        messagebox.showinfo("Replace Value", f"All NaN values in column '{column_name}' replaced with the mean: {column_mean}")
                    
                    # Refresh the Treeview
                    self.display_in_treeview(self.current_data)

                except ValueError as e:
                    messagebox.showwarning("Invalid Input", str(e))
            else:
                messagebox.showwarning("Invalid Input", "Please enter a valid column name.")
        else:
            messagebox.showwarning("No Data", "Please open a file first to load data.")
    
    def replace_using_median(self):
        if self.current_data is not None and isinstance(self.current_data, pd.DataFrame):
            # Ask the user for the column name
            column_name = askstring("Column Name", "Enter the column name:")

            if column_name is not None:
                try:
                    # Convert the column to numeric type
                    self.current_data[column_name] = pd.to_numeric(self.current_data[column_name], errors='coerce')

                    # Ask the user for the row number (if any)
                    row_number_input = askstring("Row Number", "Enter the row number (leave blank to replace all):")

                    if row_number_input:
                        row_number = int(row_number_input) - 1  # Adjust for zero-based indexing
                        if row_number < 0 or row_number >= len(self.current_data):
                            raise ValueError("Invalid row number.")
                    else:
                        row_number = None

                    # Calculate the median of the specified column
                    column_median = self.current_data[column_name].median()

                    if row_number is not None:
                        # Replace NaN in a specific row with the median
                        self.current_data.at[row_number, column_name] = column_median
                        messagebox.showinfo("Replace Value", f"Value in row {row_number + 1}, column '{column_name}' replaced with the median: {column_median}")
                    else:
                        # Replace all NaN values in the specified column with the median
                        self.current_data[column_name].fillna(column_median, inplace=True)
                        messagebox.showinfo("Replace Value", f"All NaN values in column '{column_name}' replaced with the median: {column_median}")

                    # Refresh the Treeview
                    self.display_in_treeview(self.current_data)

                except ValueError as e:
                    messagebox.showwarning("Invalid Input", str(e))
            else:
                messagebox.showwarning("Invalid Input", "Please enter a valid column name.")
        else:
            messagebox.showwarning("No Data", "Please open a file first to load data.")


    def replace_using_mode(self):
        if self.current_data is not None and isinstance(self.current_data, pd.DataFrame):
            # Ask the user for the column name
            column_name = askstring("Column Name", "Enter the column name:")

            if column_name is not None:
                try:
                    # Convert the column to numeric type
                    self.current_data[column_name] = pd.to_numeric(self.current_data[column_name], errors='coerce')

                    # Ask the user for the row number (if any)
                    row_number_input = askstring("Row Number", "Enter the row number (leave blank to replace all):")

                    if row_number_input:
                        row_number = int(row_number_input) - 1  # Adjust for zero-based indexing
                        if row_number < 0 or row_number >= len(self.current_data):
                            raise ValueError("Invalid row number.")
                    else:
                        row_number = None

                    # Calculate the mode of the specified column
                    column_mode = float(scipy_mode(self.current_data[column_name].dropna()).mode)

                    if row_number is not None:
                        # Replace NaN in a specific row with the mode
                        self.current_data.at[row_number, column_name] = column_mode
                        messagebox.showinfo("Replace Value", f"Value in row {row_number + 1}, column '{column_name}' replaced with the mode: {column_mode}")
                    else:
                        # Replace all NaN values in the specified column with the mode
                        self.current_data[column_name].fillna(column_mode, inplace=True)
                        messagebox.showinfo("Replace Value", f"All NaN values in column '{column_name}' replaced with the mode: {column_mode}")

                    # Refresh the Treeview
                    self.display_in_treeview(self.current_data)

                except ValueError as e:
                    messagebox.showwarning("Invalid Input", str(e))
            else:
                messagebox.showwarning("Invalid Input", "Please enter a valid column name.")
        else:
            messagebox.showwarning("No Data", "Please open a file first to load data.")

    def data_information(self):
        messagebox.showinfo("Data Information", "Displaying Data Information")

    def data_visualization(self):
        messagebox.showinfo("Data Visualization", "Creating Data Visualization")

    def statistic_of_data(self):
        messagebox.showinfo("Statistic of Data", "Calculating Statistics")

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
            self.current_data = pd.read_csv(file_path)
        elif file_type.lower() == 'text':
            with open(file_path, 'r') as file:
                text_data = file.read()
            self.current_data = pd.DataFrame({"Text Data": [text_data]})
        elif file_type.lower() == 'excel':
            workbook = openpyxl.load_workbook(file_path)
            sheet = workbook.active
            data = []
            for row in sheet.iter_rows(min_row=1, values_only=True):
                data.append(row)
            workbook.close()
            self.current_data = pd.DataFrame(data, columns=sheet[1])
        elif file_type.lower() == 'word':
            document = Document(file_path)
            text_data = ""
            for paragraph in document.paragraphs:
                text_data += paragraph.text + "\n"
            self.current_data = pd.DataFrame({"Text Data": [text_data]})

        self.display_in_treeview(self.current_data)

    def display_in_treeview(self, df):
        # Clear existing data
        for item in self.treeview.get_children():
            self.treeview.delete(item)

        for col in self.treeview["columns"]:
            self.treeview.heading(col, text="")
            self.treeview.column(col, width=0)

        self.treeview["columns"] = tuple(['Row No.'] + list(df.columns))

        for col in self.treeview["columns"]:
            self.treeview.heading(col, text=col)
            self.treeview.column(col, width=100)

        for index, row in df.iterrows():
            self.treeview.insert("", index, values=tuple([index + 1] + list(row)))


if __name__ == "__main__":
    root = tk.Tk()
    app = EmployeeManagementSystem(root)
    root.mainloop()
