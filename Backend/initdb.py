import sqlite3

# Open a connection to the SQLite database file
conn = sqlite3.connect('birthdays.db')

# Create a new table to store the data
conn.execute('''
CREATE TABLE IF NOT EXISTS birthdays (
    name TEXT,
    day TEXT,
    month TEXT,
    yeargroup TEXT,
    images TEXT
)
''')

# Open the text file and read the data line by line
with open('data.txt', 'r') as f:
    for line in f:
        # Split the line into name, day, and month
        # Find the position of the first integer in the text
        index = next((i for i, c in enumerate(line) if c.isdigit()), None)

        if index is not None:
            # Split the text into two parts at the position of the first integer
            name = line[:index]
            name = name.strip()
            name_d = name.replace("\t","-")
            png = ".png"
            name_d = name_d.lower()
            image = "https://raw.githubusercontent.com/vitalik-hakim/TABLES404/main/imgs/{}{}".format(name_d,png)
            month_day = line[index:]
            month_day = month_day.split('\t')
            print(month_day)
        # name, month_day = line.split('\t')
        day, month = month_day[0].split('-')
        year_group = month_day[1]
        
        # Insert the data into the table
        conn.execute('INSERT INTO birthdays VALUES (?, ?, ?, ? ,? )', (name, day, month,year_group.strip(),image))

# Commit the changes and close the connection
conn.commit()
conn.close()
