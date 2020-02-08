# Pizza order website (Work in progress)

This is (potentially) a solution for the third problem from CS50 course conducted at Harvard University. The course is accessible through edX platform: https://www.edx.org/

## Description

The goal is to develop own version of following website: http://www.pinocchiospizza.net/menu.html with additional ability allowing users to place orders composed of dishes listed in menu.

## Running

The program requires Django installed to run. Type `python3 manage.py runserver` and copy output link from terminal to go to the basic route.

The file `extract data.ipynb` extracts data from orignal website and inserts it into database. Should be run once after initiating database.

The database file `db.sqlite3` has already extracted menu data from the orignal site and also contains already created superuser (username: `admin`, password: `abc123`).

### Progress so far

02.02.2020:
- database structure in file `orders/models.py` is complete
- program for data extracting from original website and inserting it into database is complete
- creating dishes and orders works properly and is possible so far only from admin site (route `/admin`):
1) First you have to create a new empty `order` (at least one)
2) Then you can create various `dishes` and assign them to a choosed `order`. The order consists of dishes which the user is going to see in their cart.
3) Note: a `dish` differs from a `menu item` is such way, that in case of creating a pizza kind `dish` you can assign **various** `toppings` to it, where `menu item` pizza only defines **number** of `toppings`.

03.02.2020
- you can view price menu with links to corresponding pizza's info

08.02.2020
- exchanged the notebook that <ins>extracts data from web and inserts into database</ins> to a notebook <ins>that extracts data to .csv file</ins>, which will be futher processed using django's ORM outside of the app with file `import csv.py` (WIP so far)

### To do

- login/logout for users
- <strike>`/menu` route with menu items listed</strike>**done**, all with `add to cart` buttons
- `/menu/add/<dish_name>` route allowing users to customise dishes and add them to cart
- `/your_cart` route with all dishes created by logged user, with total amount of $ to bill and with a textfield allowing the user to leave an additional message for restauration's owner
