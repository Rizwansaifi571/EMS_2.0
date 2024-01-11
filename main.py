



# import tkinter as tk
# from tkinter import ttk, filedialog
# import openpyxl
# import pandas as pd

# def load_data(file_path):
#     global treeview  # Declare treeview as a global variable
#     try:
#         if file_path.endswith('.csv'):
#             df = pd.read_csv(file_path)
#             # Handle case insensitivity for column names
#             df.columns = df.columns.str.upper()
#             display_data(df)
#         elif file_path.endswith(('.xlsx', '.xlsm', '.xltx', '.xltm')):
#             workbook = openpyxl.load_workbook(file_path)
#             sheet = workbook.active
#             list_values = list(sheet.values)
#             for col_name in list_values[0]:
#                 treeview.heading(col_name, text=col_name)

#             for value_tuple in list_values[1:]:
#                 treeview.insert('', tk.END, values=value_tuple)
#         else:
#             result_label.config(text="Unsupported file format")
#     except pd.errors.ParserError as e:
#         if "Invalid column index" in str(e):
#             result_label.config(text="Invalid column index in the file. Check column names and case sensitivity.")
#         else:
#             result_label.config(text=f"Error reading file: {str(e)}")
#     except Exception as e:
#         result_label.config(text=f"Error: {str(e)}")


# def insert_row():
#     name = name_entry.get()
#     age = int(age_spinbox.get())
#     subscription_status = status_combobox.get()
#     employment_status = "Employed" if a.get() else "Unemployed"

#     print(name, age, subscription_status, employment_status)

#     # Insert row into Excel sheet
#     path = filedialog.askopenfilename(title="Select file", filetypes=[("Excel files", "*.xlsx;*.xlsm;*.xltx;*.xltm"), ("CSV files", "*.csv")])
#     if path:
#         try:
#             if path.endswith('.csv'):
#                 df = pd.read_csv(path)
#                 df.loc[len(df.index)] = [name, age, subscription_status, employment_status]
#                 df.to_csv(path, index=False)
#                 display_data(df)
#             elif path.endswith(('.xlsx', '.xlsm', '.xltx', '.xltm')):
#                 workbook = openpyxl.load_workbook(path)
#                 sheet = workbook.active
#                 row_values = [name, age, subscription_status, employment_status]
#                 sheet.append(row_values)
#                 workbook.save(path)
#                 load_data(path)  # Reload the data after inserting row
#             else:
#                 result_label.config(text="Unsupported file format")
#         except Exception as e:
#             result_label.config(text=f"Error inserting row: {str(e)}")

#     # Clear the values
#     name_entry.delete(0, "end")
#     name_entry.insert(0, "Name")
#     age_spinbox.delete(0, "end")
#     age_spinbox.insert(0, "Age")
#     status_combobox.set(combo_list[0])
#     a.set(False)  # Unselect the checkbutton

# def display_data(data_frame):
#     # Clear previous data in treeview
#     for item in treeview.get_children():
#         treeview.delete(item)

#     # Display headers
#     headers = data_frame.columns
#     for header in headers:
#         treeview.heading(header, text=header)

#     # Display data
#     for row in data_frame.itertuples(index=False):
#         treeview.insert('', tk.END, values=row)

# # Tkinter setup
# root = tk.Tk()
# root.title("Data Viewer")

# style = ttk.Style(root)
# root.tk_setPalette(background='#2e2e2e', foreground='#ffffff')  # Dark mode

# combo_list = ["Subscribed", "Not Subscribed", "Other"]

# frame = ttk.Frame(root)
# frame.pack()

# # Define widgets_frame here
# widgets_frame = ttk.LabelFrame(frame, text="Insert Row")
# widgets_frame.grid(row=0, column=0, padx=20, pady=10)

# name_entry = ttk.Entry(widgets_frame)
# age_spinbox = ttk.Spinbox(widgets_frame, from_=18, to=100)
# status_combobox = ttk.Combobox(widgets_frame, values=combo_list)
# a = tk.BooleanVar()

# # ... (rest of the code)

# # Create a treeview to display data
# # Create a frame for the treeview
# treeFrame = ttk.Frame(root)
# treeFrame.pack(pady=10)

# # Create a treeview with the yscrollcommand set to the scrollbar's set method
# treeview = ttk.Treeview(treeFrame, show="headings")
# treeview.pack(side="left", fill="both", expand=True)

# # Create a vertical scrollbar associated with the treeview
# treeScroll = ttk.Scrollbar(treeFrame, command=treeview.yview)
# treeScroll.pack(side="right", fill="y")

# # Configure the treeview to use the scrollbar
# treeview.configure(yscrollcommand=treeScroll.set)

# # Create a label for displaying error messages
# result_label = ttk.Label(root, text="")
# result_label.pack(pady=5)

# # Create a button to open Excel or CSV file
# open_button = ttk.Button(root, text="Open File", command=lambda: load_data(filedialog.askopenfilename(title="Select file", filetypes=[("Excel files", "*.xlsx;*.xlsm;*.xltx;*.xltm"), ("CSV files", "*.csv")])))
# open_button.pack(pady=10)

# # Create widgets for inserting rows
# # ... (your existing code for widgets)

# # Create a button to insert a row
# insert_button = ttk.Button(root, text="Insert Row", command=insert_row)
# insert_button.pack(pady=10)

# root.mainloop()
