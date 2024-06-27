# Soccer Player Database

This project is a graphical user interface (GUI) application for displaying soccer player statistics. It uses web scraping to gather data from Transfermarkt, stores the data in a MySQL database, and visualizes it using Tkinter. The application provides an interactive way to view and explore soccer player statistics such as player name, age, position, nation, team, and market value.

## How to load your CSV file into mySQL
After you webscraped the data and transferred into a CSV file, go to your terminal:
```
mysql -u -p --local_infile

LOAD DATA LOCAL INFILE 
"---path--/table.csv"
INTO table player_stats
COLUMNS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 LINES;
```
## Libraries
 - mySQL Connector
 - Beautiful Soup
 - Tkinter
 - Pandas Dataframe

## Database


<h3 align="center", text-style="bold">
<b>Example Database View</b><br/>
<img width="440" alt="Example Database View" src="https://github.com/Chen6528/Soccer-SQL-Database/assets/71508397/0379d45e-e370-409c-9319-02f336d3645c">
</h3>
<h3 align="center">
<br/><b>GUI Application</b><br/>
<img width="446" alt="GUI Application" src="https://github.com/Chen6528/Soccer-SQL-Database/assets/71508397/0d581cbc-6f2c-4009-8182-fe118a81d9ac">
</h3>
<h3 align="center">
<img width="597" alt="Example of Sorted Database (Decreasing Market Value)" src="https://github.com/Chen6528/Soccer-SQL-Database/assets/71508397/f47dc81c-65fd-4a61-8d17-edf8c43264c7">
<br/><i>Example from Decreasing Market Value</i>
</h3>
