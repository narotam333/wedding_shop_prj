# wedding_shop

Solution:
I have used "Django" as a framework and "PostgreSQL" as a database to create this application wherein a couple can
manage their gift list based on product offerings from the wedding shop in form of product list. The same framework has
been used to create the report on gift list.

On the home page, user will have 3 buttons.

1. Product List - This will list all the products from the wedding shop. User will be able to perform below
                  actions on the list.

    a. Add a new product using POST button <br></br>
    b. Update an existing product using PUT button <br></br>
    c. Filter products based on different fields <br></br>
    d. Order products based on different fields <br></br>

2. Gift List - This will list all the gifts which will be added by a user. There will also be an option to purchase a
               product as per the stock availability and show the number of purchased products as well as available
               products. User will be able to perform below actions on the list.

    a. Add a new gift using POST button from the list of available products<br></br>
    b. Purchase an added product from the gift list based on "Available Quantity" using PUT button - This will automatically reduce the "availability quantity" as          per the "purchased quantity"<br></br>
    c. Change the number of purchased quantity (if required)<br></br>
    d. Delete a gift from the list (This is not working but code has been written for that)<br></br>
    d. Filter products based on different fields<br></br>
    e. Order products based on different fields<br></br>

3. Report - This will list all the gifts (purchased or not). User will be able to perform below actions on the list.

    a. Filter products based on different fields<br></br>
    b. Order products based on different fields<br></br>


Technical Stuff:
1. Code has been containerized so that application can be executed anywhere
2. Standard PostgreSQL image has been used for database
3. Django framework has been installed on standard python:3.7-slim.
4. Dump data is also been added on load

How to run application:

Pre-requisite:
Docker

Steps:
1. In the project root directory, execute : docker-compose up -d --build
2. To access application, use "http://localhost:8000/api"
3. To stop the application, execute : docker-compose down -v
4. To check logs, execute : docker-compose logs -f


Improvements (which could have been done with more time):
1. Display different report for purchased and not purchased gifts
2. Delete a gift from the list (would have diagnosed the issue)
3. Error handling
4. Display the lists in tabular format for better representation

