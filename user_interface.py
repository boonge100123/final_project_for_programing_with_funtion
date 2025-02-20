import tkinter as tk
import csv
from loop_and_graphing import create_graph

class ScraperApp:
    def __init__(self, master):
        self.master = master
        
        # Set window size (width x height)
        master.geometry("600x400")  # Adjust the dimensions as needed

        # URL input
        self.url_label = tk.Label(master, text="Enter Amazon URL:")
        self.url_label.pack()
        
        self.url_entry = tk.Entry(master)
        self.url_entry.pack()
        
        # Save URL button
        self.save_button = tk.Button(master, text="Save URL", command=self.save_url)
        self.save_button.pack()

        # Start button
        self.start_button = tk.Button(master, text="Start Loop", command=self.start_loop)
        self.start_button.pack()

        # Stop button
        self.stop_button = tk.Button(master, text="Stop Loop", command=self.stop_loop)
        self.stop_button.pack()

        # Open Graph button
        self.graph_button = tk.Button(master, text="Open Graph", command=self.open_graph)
        self.graph_button.pack()

    def save_url(self):
        url = self.url_entry.get()
        if url:  # Check if the URL is not empty
            filename = 'user_data_request.csv'  # Updated CSV filename here
            with open(filename, mode='a', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(['Amazon', url])  # Write "Amazon" and the URL to the CSV file
            print(f"Saved URL: Amazon, {url}")  # Optional: Print confirmation

    def start_loop(self):
        # Placeholder for start loop logic
        print("Start loop function called. Add your logic here.")

    def stop_loop(self):
        # Placeholder for stop loop logic
        print("Stop loop function called. Add your logic here.")

    def open_graph(self):
        create_graph()

if __name__ == "__main__":
    root = tk.Tk()
    app = ScraperApp(root)
    root.mainloop()
