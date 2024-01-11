import tkinter as tk
from tkinter import filedialog

class EmployeeManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("EMS - A Business Intelligence Tool")
        self.root.geometry("800x400")

        # Header Frame
        self.header_frame = tk.Frame(root, bg="#3498db", height=50, bd=1, relief=tk.SOLID)
        self.header_frame.pack(fill=tk.X)

        header_label = tk.Label(self.header_frame, text="EMS - A Business Intelligence Tool", font=("Helvetica", 16), bg="#3498db", fg="white")
        header_label.pack(pady=10)

        # Main Part Frame
        self.main_frame = tk.Frame(root, bg="#ecf0f1", height=250, bd=1, relief=tk.SOLID)
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Skyblue Left Frame
        self.menu_frame = tk.Frame(self.main_frame, bg="#3498db", width=150, bd=1, relief=tk.SOLID)
        self.menu_frame.pack(fill=tk.Y, side=tk.LEFT)

        # Heading for File Upload
        file_heading = tk.Label(self.menu_frame, text="Upload File", font=("Helvetica", 12), bg="#3498db", fg="white")
        file_heading.pack(pady=10)

        # Buttons for Different File Types
        file_types = ["CSV", "Text", "Excel", "Word"]
        for file_type in file_types:
            button = tk.Button(self.menu_frame, text=f"Open {file_type}", command=lambda ft=file_type: self.open_file(ft),
                               bg="#2980b9", fg="white", width=15, bd=1, relief=tk.RAISED)
            button.pack(pady=5)

        # Buttons for Business Intelligence Tool Features
        bi_tool_features = ["Dashboard", "Charts", "Reports", "Data Analysis"]
        for feature in bi_tool_features:
            feature_button = tk.Button(self.menu_frame, text=feature, command=lambda f=feature: self.perform_bi_action(f),
                                       bg="#2980b9", fg="white", width=15, bd=1, relief=tk.RAISED)
            feature_button.pack(pady=5)

        # Your menu content goes here

        # Main Content Frame (2/3 of Main Part Frame)
        self.content_frame = tk.Frame(self.main_frame, bg="#ecf0f1", bd=1, relief=tk.SOLID)
        self.content_frame.pack(fill=tk.BOTH, expand=True)

        # Frame for Sample Files
        sample_files_frame = tk.Frame(self.content_frame, bg="#bdc3c7", bd=1, relief=tk.SOLID)
        sample_files_frame.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)

        # Button to Add Sample Tableau File
        tableau_button = tk.Button(sample_files_frame, text="Add Tableau Sample", command=self.add_tableau_sample,
                                   bg="#7f8c8d", fg="white", width=20, bd=1, relief=tk.RAISED)
        tableau_button.grid(row=0, column=0, padx=10, pady=10)

        # Button to Add Sample Power BI File
        power_bi_button = tk.Button(sample_files_frame, text="Add Power BI Sample", command=self.add_power_bi_sample,
                                     bg="#7f8c8d", fg="white", width=20, bd=1, relief=tk.RAISED)
        power_bi_button.grid(row=0, column=1, padx=10, pady=10)

        # Your main content goes here

        # Footer Frame
        self.footer_frame = tk.Frame(root, bg="#2c3e50", height=50, bd=1, relief=tk.SOLID)
        self.footer_frame.pack(fill=tk.X, side=tk.BOTTOM)

        footer_label = tk.Label(self.footer_frame, text="© 2024 EMS - A Business Intelligence Tool", font=("Helvetica", 10), bg="#2c3e50", fg="white")
        footer_label.pack(pady=10)

    def open_file(self, file_type):
        file_extension = file_type.lower()
        file_path = filedialog.askopenfilename(title=f"Select {file_type} File", filetypes=[(f"{file_type} files", f"*.{file_extension}")])
        if file_path:
            print(f"Opening {file_type} file: {file_path}")

    def perform_bi_action(self, action):
        # Add code to perform Business Intelligence action
        print(f"Performing Business Intelligence action: {action}")

    def add_tableau_sample(self):
        # Add code to simulate adding a Tableau sample file
        print("Adding Tableau Sample File")

    def add_power_bi_sample(self):
        # Add code to simulate adding a Power BI sample file
        print("Adding Power BI Sample File")

if __name__ == "__main__":
    root = tk.Tk()
    app = EmployeeManagementSystem(root)
    root.mainloop()


