import sqlite3
from datetime import date




## Method to get the specific day's birthdays a dict ##

def get_birthdays_by_month(day: str, month: str) -> list:
    # Convert the month prefix to a month number

    print(day,month)
    # Connect to the database
    conn = sqlite3.connect('birthdays.db')
    
    # Construct the SQL query
    query = """
        SELECT name, day, month, yeargroup, images
        FROM birthdays
        WHERE day = ? AND month = ?
    """
    
    # Get the current year
    current_year = date.today().year
    
    # Execute the query and fetch the results
    cursor = conn.execute(query, (day, month))
    rows = cursor.fetchall()
    
    # Close the database connection
    conn.close()
    
    # Return the matching rows as a list of dictionaries
    birthdays_dict = {
        'count': len(rows),
        'birthdays': [dict(name=row[0], day=row[1], month=row[2], yeargroup=row[3], image=row[4], year=current_year) for row in rows]
    }
    
    # Return the dictionary
    return birthdays_dict




def GetTodayBirthdays():
        
    # Get the current day and month prefix
    current_day = 9

    # current_day = date.today().day
    current_month_prefix = date.today().strftime('%b')

    # Get the birthdays for the current day and month
    birthdays = get_birthdays_by_month(current_day, current_month_prefix)

    return birthdays

# print(GetTodayBirthdays())




### Method to delete a year group eg.dp2 and promote yeargroup ###


def delete_dp2s():
    # Connect to the database
    conn = sqlite3.connect('birthdays.db')
    
    # Construct the SQL query
    query = "DELETE FROM birthdays WHERE yeargroup = 'DP2'"
    
    # Execute the query
    conn.execute(query)
    
    # Commit the changes and close the database connection
    conn.commit()
    conn.close()

# 

##### Update the yeargroup after the dp2 have been deleted ###
def update_yeargroup():
    # Connect to the database
    conn = sqlite3.connect('birthdays.db')
    
    # Construct the SQL queries to update the yeargroup values
    myp4_query = "UPDATE birthdays SET yeargroup = 'MYP5' WHERE yeargroup = 'MYP4'"
    myp5_query = "UPDATE birthdays SET yeargroup = 'DP1' WHERE yeargroup = 'MYP5'"
    dp1_query = "UPDATE birthdays SET yeargroup = 'DP2' WHERE yeargroup = 'DP1'"
    
    # Execute the queries
    conn.execute(dp1_query)
    conn.execute(myp5_query)
    conn.execute(myp4_query)
    
    # Commit the changes and close the database connection
    conn.commit()
    conn.close()

def PromoteYear():
    delete_dp2s()
    update_yeargroup()


## Return all students ##

def getAllBirthdays():
    conn = sqlite3.connect('birthdays.db')
    cursor = conn.cursor()

    cursor.execute("SELECT rowid, * FROM birthdays")
    rows = cursor.fetchall()

    result = []
    for row in rows:
        dict_row = {
            'id': row[0],
            'name': row[1],
            'day': row[2],
            'month': row[3],
            'yeargroup': row[4],
            'image': row[5]
        }
        result.append(dict_row)

    conn.close()
    return result


    return result
# print(get_birthdays())


#### Add a new student data ####

def Add_student(name, day, month, yeargroup,image):
    conn = sqlite3.connect('birthdays.db')  # replace with your database filename
    cursor = conn.cursor()

    # Use placeholders to prevent SQL injection attacks
    cursor.execute("INSERT INTO birthdays (name, day, month, yeargroup, images) VALUES (?, ?, ?, ?, ?)", (name, day, month, yeargroup,image))

    conn.commit()
    conn.close()

    return 'okay'

# add_student('John Doe', '10', 'Mar', 'MYP4')

## Delete student ###

def Delete_student(name, day, month, yeargroup):
    conn = sqlite3.connect('birthdays.db')  # replace with your database filename
    cursor = conn.cursor()

    # Use placeholders to prevent SQL injection attacks
    cursor.execute("DELETE FROM birthdays WHERE name = ? AND day = ? AND month = ? AND yeargroup = ?", (name, day, month, yeargroup))

    conn.commit()
    conn.close()

    return 'Successfully Deleted'

# Delete_student('Vitalik Hakim','11','Mar','MYP5')


## Update Student


def updateBirthday(name, day, month, yeargroup, id):
    conn = sqlite3.connect('birthdays.db')
    cursor = conn.cursor()
    print(id)
    cursor.execute("UPDATE birthdays SET name=?, day=?, month=?, yeargroup=? WHERE rowid=?", (name, day, month, yeargroup, id))

    conn.commit()
    conn.close()

    return 'Successfully Updated'