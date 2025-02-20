#python

import pytest
import csv

def test_scraper_app():
    data_file = 'scraped_data.csv'
    reader = csv.reader(open(data_file))
    next(reader)  # Skip the first line
    data = list(reader)
    product_info = set()
    seen_titles = {}
    for row in data:
        if len(row) > 3:
            title = ' '.join(row[2].split()[:3])
            price = row[3]
            seen_titles[title] = price  # Update the price if the title already exists
    for title, price in seen_titles.items():
        product_info.add((title, price))
    for info in product_info:
        

# pytest.main(["-v", "--tb=line", "-rN", __file__])
test_scraper_app()