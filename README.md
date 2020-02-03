# Pizza order website (Work in progress)

This is (potentially) a solution for the third problem from CS50 course conducted at Harvard University. The course is accessible through edX platform: https://www.edx.org/

## Description

The goal is to develop own version of following website: http://www.pinocchiospizza.net/menu.html with additional ability allowing users to place orders composed of dishes listed in menu.

## Running

The program requires Django installed to run.

The file `extract data.ipynb` extracts data from orignal website and inserts it into database. Should be run once after initiating database.

The database file `db.sqlite3` has already extracted menu data from the orignal site and also contains already created superuser (username: `beznick`, password: `abc123`).

### Progress so far

02.02.2020:
- database structure in file `orders/models.py` is complete
- program for data extracting from original website and inserting it into database is complete
- creating dishes and orders works properly and is possible so far only from admin site (route `/admin')

### To do

- login/logout for users
- `/menu` route with menu items listed, all with `add to cart` buttons
- `/menu/add/<dish_name>` route allowing users to customise dishes and add them to cart
- `/your_cart` route with all dishes created by logged user, with total amount of $ to bill and with a textfield allowing the user to leave an additional message for restauration's owners
