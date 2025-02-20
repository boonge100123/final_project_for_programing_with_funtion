# final_project_for_programing_with_funtion
this is a python program that will track prices of products in amazon and then stor them in a csv file. you can then call a graph at any time to display the data. 

to run the app open the scrapper_app.py and run it. It should run through the setup prosess and then start the scraper. you will be given 3 buttons the first button named save url is paried with the box you can add an amazon link and click the button and it will save it to the user_data_request.csv file.
The second button is the start loop button this is the button that will look at the user_data_request.csv and then atempt to scrap the price from each url. if the url is not in the list it will atempt and then skip over it. this loop will then try and do this every 24 hours frome the time you started it.  there are also 2 funtions in there that are commented out that will have it run every 5 minnits and the other will run it every 1.5 minnits.
the third button is the stop loop button wich will break out of the loop.
the last button is how you can view the graph that tracks prices over time.

*important* before closeing the teminal it is important you close the loop. it shuldent break anything but you will have to break the loop before you can open the terminal again.

*important* i will include a fake data set in the user_data_request.csv to show that the data is working but you can add other products to the page by providing a url.

