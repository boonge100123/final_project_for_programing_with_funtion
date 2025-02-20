import tkinter as tk
import csv
from create_graph import create_graph
from scrape_raw_data import call_scraper
import threading
import time

#! this is the time that the loop will run for in the loop function this is in seconds
#! 86400 seconds is 24 hours
#! 300 seconds is 5 minutes
#! 90 seconds is 1.5 minutes .. and so on
LOOP_TIME = 86400  # 24 hours in seconds

#! this is the scraper app class
#! basicly this lets me run the scraper in a loop use buttons to start and stop the loop
#! and save the url to a csv file
class ScraperApp:
    #! this is the funtion that sets up the class 
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

    #! this function saves the url to a the user data request csv file that will be used to call the urls that need to be scraped
    def save_url(self):
        url = self.url_entry.get()
        if url:  # Check if the URL is not empty
            filename = 'user_data_request.csv'  
            with open(filename, mode='a', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(['Amazon', url])  
            print(f"Saved URL: Amazon, {url}")  

    #! this is the function that starts the loop when the button is pressed in the gui
    def start_loop(self):
        """Start the scraper loop."""
        if not self.is_running:
            self.is_running = True
            self.loop_thread = threading.Thread(target=self.run_scraper_loop, daemon=True)
            self.loop_thread.start()
            print("Loop started.")

    #! this is the function that stops the loop when the button is pressed in the gui
    def stop_loop(self):
        """Stop the scraper loop."""
        self.is_running = False
        print("Loop stopped.")

    #! this is the function that runs the scraper in a loop it is set for 24 hours but can be changed to any time by changing the loop time above
    def run_scraper_loop(self):
        while self.is_running:
            call_scraper()
            time.sleep(LOOP_TIME) 

    #! this is the function that opens the graph when the button is pressed in the gui
    def open_graph(self):
        create_graph()

if __name__ == "__main__":
    root = tk.Tk()
    app = ScraperApp(root)
    root.mainloop()
