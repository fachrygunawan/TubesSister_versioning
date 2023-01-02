# INI CALCULATOR JELEK OLD VERSION
import xmlrpc.client
import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        # Create the display for the calculator
        self.display = tk.Entry(master, font=("Helvetica", 20))
        self.display.grid(row=0, column=0, columnspan=4, pady=10)

        # Create the buttons for the calculator
        self.create_buttons()

        # Create a button for checking the version
        self.check_version_button = tk.Button(master, text="Check Version", command=self.check_version)
        self.check_version_button.grid(row=6, column=0, columnspan=2, pady=10)

        # Create a button for updating the version
        self.update_version_button = tk.Button(master, text="Update Version", command=self.update_version)
        self.update_version_button.grid(row=6, column=2, columnspan=2, pady=10)

        # Connect to the xmlrpc server
        self.client = xmlrpc.client.ServerProxy("http://localhost:8000")

    def create_buttons(self):
        # Create the buttons for the calculator
        self.button1 = tk.Button(self.master, text="1", command=lambda: self.append_to_display("1"))
        self.button1.grid(row=5, column=0, padx=10, pady=10)
        self.button2 = tk.Button(self.master, text="2", command=lambda: self.append_to_display("2"))
        self.button2.grid(row=5, column=1, padx=10, pady=10)
        self.button3 = tk.Button(self.master, text="3", command=lambda: self.append_to_display("3"))
        self.button3.grid(row=5, column=2, padx=10, pady=10)
        self.button4 = tk.Button(self.master, text="4", command=lambda: self.append_to_display("4"))
        self.button4.grid(row=4, column=0, padx=10, pady=10)
        self.button5 = tk.Button(self.master, text="5", command=lambda: self.append_to_display("5"))
        self.button5.grid(row=4, column=1, padx=10, pady=10)
        self.button6 = tk.Button(self.master, text="6", command=lambda: self.append_to_display("6"))
        self.button6.grid(row=4, column=2, padx=10, pady=10)
    def append_to_display(self, text):
        # Append the text to the display
        self.display.insert(tk.END, text)

    def check_version(self):
        # Check the version of the calculator
        client_version = "2.0"
        result = self.client.check_version(client_version)
        self.display.delete(0, tk.END)
        self.display.insert(0, result)

    def update_version(self):
        # Ask the user if they want to update the version
        update = tk.messagebox.askyesno("Update Version", "A new version is available. Would you like to update?")
        if update:
            client_version = self.client.update_version(client_version)
            tk.messagebox.showinfo("Update Successful", f"Update successful to: {client_version}")
        else:
            tk.messagebox.showinfo("Update Declined", "Version update declined")

root = tk.Tk()
app = Calculator(root)
root.mainloop()