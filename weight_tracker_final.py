import tkinter as tk
from tkinter import messagebox
import pickle

class WeightTracker:
    def __init__(self):
        self.cache_file = 'weight_cache.pkl'
        self.load_cache()

    def load_cache(self):
        try:
            with open(self.cache_file, 'rb') as file:
                self.weight_data = pickle.load(file)
        except FileNotFoundError:
            self.weight_data = {}  # Hash table to store weight entries

    def save_cache(self):
        with open(self.cache_file, 'wb') as file:
            pickle.dump(self.weight_data, file)

    def add_weight_entry(self, date, weight):
        self.weight_data[date] = weight
        self.save_cache()

    def get_weight_entry(self, date):
        return self.weight_data.get(date, None)

    def remove_weight_entry(self, date):
        if date in self.weight_data:
            del self.weight_data[date]
            self.save_cache()
            return True
        return False

    def get_all_entries(self):
        return self.weight_data

class WeightTrackerGUI:
    def __init__(self, weight_tracker):
        self.weight_tracker = weight_tracker

        self.root = tk.Tk()
        self.root.title("Weight Tracker")

        self.date_label = tk.Label(self.root, text="Date (dd/mm/yyyy):")
        self.date_label.pack()
        self.date_entry = tk.Entry(self.root)
        self.date_entry.pack()

        self.weight_label = tk.Label(self.root, text="Weight (kg):")
        self.weight_label.pack()
        self.weight_entry = tk.Entry(self.root)
        self.weight_entry.pack()

        self.add_button = tk.Button(self.root, text="Add Entry", command=self.add_entry)
        self.add_button.pack()

        self.get_button = tk.Button(self.root, text="Get Entry", command=self.get_entry)
        self.get_button.pack()

        self.remove_button = tk.Button(self.root, text="Remove Entry", command=self.remove_entry)
        self.remove_button.pack()

        self.view_all_button = tk.Button(self.root, text="View All Entries", command=self.view_all_entries)
        self.view_all_button.pack()

        self.entries_label = tk.Label(self.root, text="")
        self.entries_label.pack()

    def add_entry(self):
        date = self.date_entry.get()
        weight = self.weight_entry.get()

        if date and weight:
            self.weight_tracker.add_weight_entry(date, weight)
            messagebox.showinfo("Success", "Weight entry added!")
            self.clear_entries()
        else:
            messagebox.showerror("Error", "Please enter both date and weight.")

    def get_entry(self):
        date = self.date_entry.get()
        if date:
            weight = self.weight_tracker.get_weight_entry(date)
            if weight:
                messagebox.showinfo("Weight Entry", f"Date: {date}\nWeight: {weight} kg")
            else:
                messagebox.showwarning("Not Found", "Weight entry not found.")
            self.clear_entries()
        else:
            messagebox.showerror("Error", "Please enter a date.")

    def remove_entry(self):
        date = self.date_entry.get()
        if date:
            if self.weight_tracker.remove_weight_entry(date):
                messagebox.showinfo("Success", "Weight entry removed!")
                self.clear_entries()
            else:
                messagebox.showwarning("Not Found", "Weight entry not found.")
        else:
            messagebox.showerror("Error", "Please enter a date.")

    def view_all_entries(self):
        all_entries = self.weight_tracker.get_all_entries()
        if all_entries:
            entries_text = "All Entries:\n"
            for date, weight in all_entries.items():
                entries_text += f"Date: {date} | Weight: {weight} kg\n"
            self.entries_label.config(text=entries_text)
        else:
            self.entries_label.config(text="No entries found.")

    def clear_entries(self):
        self.date_entry.delete(0, tk.END)
        self.weight_entry.delete(0, tk.END)

    def run(self):
        self.root.mainloop()

# Usage example
weight_tracker = WeightTracker()
gui = WeightTrackerGUI(weight_tracker)
gui.run()
