Demo: https://team7demo.herokuapp.com/

Student managment web application using Flask and Mongodb for the ITMO WAD 2021 Spring project developed by team 7:
(Supervised by A.P. Menshikov Alexander Alekseevich)
1-Hossam Montasser
2-Armida Caushaj
3-Appiah Prince
4-Hashim Hawwaz

Note for usage:
copy paste the CSV file in the text area of the dashboard after log in and please note that the app is configured to convert CSV files with the semicolon delimiter only, also please note that there must be only one semicolon between each value or else the value will not be processed and it will apear as an empty field, there is an example file in the rep so you can test the application with it

Steps to deploy (windows 10, VScode):
1- delete the venv folder
2- run: "py -3 -m venv venv"
3- run: ".\venv\Scripts\activate"
4- run: "pip install -r requirements.txt"
5- press on the app.py and run the project from the run button on the left of VS code and chose flask or run: python app.py

Brief technical description (all code is commented for more detaild explanation):

The responsive app starts with an animated registeration using svg and bootstrap, authentication with mongodb.
in the dashboard there is a text area that you paste the content of a csv file and it will be converted into a python list of dictionaries and rendered to an html table.
each row in the table is clickable (using javascript to enable the link becasue html doesn't allow links inside tables by defaults) and the link points to a private web page to display the data of the student's row that were clicked.
When the clicked row data is forwarded to the private page, it is transfered as a string because "url_for" doesn't reansfer dictionaries, so in the info page the string is converted back to a dictionary so it can be iterated and rendered as a dynamic html table.

Prospects:

the follwoing list are doable features for the future, that will be added to the app to be more efficent.

1- build a url shotner to store each student private link in mongodb as a pointer to the long url that is created in the first place
2- build a dynamic mongodb model to implement the csv data in the database dynamically without any restriction
3- implement CRUD operations so the user can edit and store multiple CSV files and assign them to each group of students
4- build a middleware so the web application can communicate the data to the ITMO student accounts to display the course progress, details and marks privately.
