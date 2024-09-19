import tkinter as tk
from tkinter import messagebox


# Contact Book class to manage contact details
class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone, email, address):
        self.contacts[name] = {'phone': phone, 'email': email, 'address': address}

    def get_contacts(self):
        return self.contacts

    def search_contact(self, name):
        return self.contacts.get(name)

    def update_contact(self, name, phone, email, address):
        if name in self.contacts:
            self.contacts[name] = {'phone': phone, 'email': email, 'address': address}
            return True
        return False

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            return True
        return False


# GUI Application class for the Contact Book
class ContactBookApp:
    def __init__(self, root):
        self.book = ContactBook()
        self.root = root
        self.root.title("Contact Book")

        # Add Contact Fields
        self.name_label = tk.Label(root, text="Name")
        self.name_label.grid(row=0, column=0)
        self.name_entry = tk.Entry(root)
        self.name_entry.grid(row=0, column=1)

        self.phone_label = tk.Label(root, text="Phone")
        self.phone_label.grid(row=1, column=0)
        self.phone_entry = tk.Entry(root)
        self.phone_entry.grid(row=1, column=1)

        self.email_label = tk.Label(root, text="Email")
        self.email_label.grid(row=2, column=0)
        self.email_entry = tk.Entry(root)
        self.email_entry.grid(row=2, column=1)

        self.address_label = tk.Label(root, text="Address")
        self.address_label.grid(row=3, column=0)
        self.address_entry = tk.Entry(root)
        self.address_entry.grid(row=3, column=1)

        # Buttons
        self.add_button = tk.Button(root, text="Add Contact", command=self.add_contact)
        self.add_button.grid(row=4, column=0, pady=10)

        self.view_button = tk.Button(root, text="View Contacts", command=self.view_contacts)
        self.view_button.grid(row=4, column=1)

        self.search_button = tk.Button(root, text="Search Contact", command=self.search_contact)
        self.search_button.grid(row=5, column=0)

        self.update_button = tk.Button(root, text="Update Contact", command=self.update_contact)
        self.update_button.grid(row=5, column=1)

        self.delete_button = tk.Button(root, text="Delete Contact", command=self.delete_contact)
        self.delete_button.grid(row=6, column=0, pady=10)

        self.result_text = tk.Text(root, height=10, width=50)
        self.result_text.grid(row=7, columnspan=2, pady=10)

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()

        if name and phone and email and address:
            self.book.add_contact(name, phone, email, address)
            self.result_text.insert(tk.END, f"Contact {name} added successfully.\n")
        else:
            messagebox.showwarning("Input Error", "Please fill in all fields.")

    def view_contacts(self):
        self.result_text.delete(1.0, tk.END)
        contacts = self.book.get_contacts()
        if contacts:
            for name, details in contacts.items():
                self.result_text.insert(tk.END, f"Name: {name}, Phone: {details['phone']}, Email: {details['email']}, Address: {details['address']}\n")
        else:
            self.result_text.insert(tk.END, "No contacts available.\n")

    def search_contact(self):
        name = self.name_entry.get()
        contact = self.book.search_contact(name)
        self.result_text.delete(1.0, tk.END)
        if contact:
            self.result_text.insert(tk.END, f"Name: {name}, Phone: {contact['phone']}, Email: {contact['email']}, Address: {contact['address']}\n")
        else:
            self.result_text.insert(tk.END, "Contact not found.\n")

    def update_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()

        if self.book.update_contact(name, phone, email, address):
            self.result_text.insert(tk.END, f"Contact {name} updated successfully.\n")
        else:
            self.result_text.insert(tk.END, "Contact not found.\n")

    def delete_contact(self):
        name = self.name_entry.get()
        if self.book.delete_contact(name):
            self.result_text.insert(tk.END, f"Contact {name} deleted successfully.\n")
        else:
            self.result_text.insert(tk.END, "Contact not found.\n")


if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBookApp(root)
    root.mainloop()