import tkinter as tk
import csv
from create_graph import create_graph
from scrape_raw_data import call_scraper
import threading
import time

class ScraperApp:
    def __init__(self, master):
        self.master = master
        self.is_running = False  # Track loop state
        self.loop_thread = None

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

        # Start Loop button
        self.start_loop_button = tk.Button(master, text="Start Loop", command=self.start_loop)
        self.start_loop_button.pack()

        # Stop Loop button
        self.stop_loop_button = tk.Button(master, text="Stop Loop", command=self.stop_loop)
        self.stop_loop_button.pack()

        # Open Graph button
        self.graph_button = tk.Button(master, text="Open Graph", command=self.open_graph)
        self.graph_button.pack()

    def save_url(self):
        url = self.url_entry.get()
        if url:  # Check if the URL is not empty
            filename = 'user_data_request.csv'  
            with open(filename, mode='a', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(['Amazon', url])  
            print(f"Saved URL: Amazon, {url}")  

    def start_loop(self):
        """Start the scraper loop."""
        if not self.is_running:
            self.is_running = True
            self.loop_thread = threading.Thread(target=self.run_scraper_loop, daemon=True)
            self.loop_thread.start()
            print("Loop started.")

    def stop_loop(self):
        """Stop the scraper loop."""
        self.is_running = False
        print("Loop stopped.")

    def run_scraper_loop(self):
        """Runs the scraping function in a loop every 24 hours."""
        while self.is_running:
            call_scraper()
            time.sleep(86400)  # Wait 24 hours before running again

    def open_graph(self):
        create_graph()

if __name__ == "__main__":
    root = tk.Tk()
    app = ScraperApp(root)
    root.mainloop()
