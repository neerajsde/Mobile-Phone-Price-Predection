# Greetings
def greeting(name):
    """Print a greeting message to the specified name."""
    print(f"Hello {name}, have a good day.")

# Sum of a list of numbers
def add(num):
    """Calculate and return the sum of a list of numbers."""
    s = 0
    for i in num:
        s += i
    return s

# Multiply a list of numbers
def multiply(num):
    """Calculate and return the product of a list of numbers."""
    m = 0
    for i in num:
        m += i
    return m

# Check for prime numbers in a list
def list_prime(num):
    """Find and return a list of prime numbers from the input list."""
    prime_numbers = []
    for i in num:
        if i >= 1:
            for k in range(2, i):
                if i % k == 0:
                    break
            else:
                prime_numbers.append(i)
    return prime_numbers

# Check if a number is prime
def prime(n):
    """Check if the given number is a prime number."""
    flag = False
    if n <= 1:
        flag = False
    elif n == 2:
        flag = True
    else:
        for i in range(2, n):
            if n % i == 0:
                flag = False
                break
            else:
                flag = True
    return flag

# Check for leap year
def leap(year):
    """Check if the given year is a leap year."""
    l = False
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                l = True
            else:
                l = False
        else:
            l = True
    else:
        l = False
    return l

# Check for Armstrong number
def armstrong(num):
    """Check if the given number is an Armstrong number."""
    x = len(str(num))
    z = 0
    for i in str(num):
        n = int(i) ** x
        z += n
    if num == z:
        return True
    else:
        return False

# Check if a number is palindrome
def palindrome(num):
    """Check if the given number is a palindrome."""
    x = str(num)
    z = x[::-1]
    if str(num) == z:
        return True
    else:
        return False

# Find ASCII value of a character
def ascii(s):
    """Get the ASCII value of a character."""
    return ord(s)

# Convert Celsius to Fahrenheit
def celsius(num):
    """Convert Celsius to Fahrenheit."""
    f = (num * 1.8) + 32
    return f

# Convert Fahrenheit to Celsius
def fahrenheit(num):
    """Convert Fahrenheit to Celsius."""
    c = (num - 32) / 1.8
    return c

# Find outliers in a list of data
def outlier(data):
    """Find and return a list of outliers from the input data."""
    import numpy as np
    data = sorted(data)
    q1, q3 = np.percentile(data, [25, 75])
    IQR = q3 - q1
    lower_fence = q1 - (1.5 * IQR)
    upper_fence = q3 + (1.5 * IQR)
    outliers = []
    for i in data:
        if lower_fence > i or upper_fence < i:
            outliers.append(i)
    return outliers

# Find the highest top 3 values in a list
def highest_three(num):
    """Find and return the highest top 3 values from the input list."""
    num.sort()
    x = num[-3:]
    z = x[::-1]
    return z

# Select a table from a database
def selectTable(**kwargs):
    """
    Connect to the specified database and return all records from the given table.

    Parameters:
        - database: The name of the database to connect to.
        - table: The name of the table to select from.

    Returns:
        A list of records fetched from the specified table.
    """
    import mysql.connector as ms
    mydb = ms.connect(host='localhost', user='root', password='Neeraj@123', database=kwargs['database'])
    mycur = mydb.cursor()
    sql = f"select * from {kwargs['table']}"
    mycur.execute(sql)
    x = mycur.fetchall()
    return x

# Timer function countdown
def countdown(time_sec):
    """Countdown from the specified time in seconds and print the remaining time."""
    import time
    while time_sec:
        mins, secs = divmod(time_sec, 60)
        tim = f"{mins:02}:{secs:02}"
        print(tim, end='\r')
        time.sleep(1)
        time_sec -= 1
    print("Time's Up")

# Sum of odd and even numbers in a list
def even_odd_sum(lst):
    """Calculate and print the sum of even and odd numbers in the input list."""
    even = 0
    odd = 0
    for i in lst:
        if i % 2 == 0:
            even += i
        else:
            odd += i
    print(f"Sum of even numbers is {even}.\nSum of odd numbers is {odd}.")

def file_to_database(file, **kwargs):
    """
    Read data from a CSV file and insert it into the specified database table.

    Parameters:
        - file: The path of the CSV file to read data from.
        - database: The name of the database to connect to.
        - table: The name of the table to insert data into.

    Returns:
        A string indicating the success status of the operation.
    """
    import pandas as pd
    import mysql.connector as ms
    df = pd.read_csv(file, encoding='unicode_escape')
    n = df.shape
    mydb = ms.connect(host='localhost', user='root', password='Neeraj@123', database=kwargs['database'])
    for i in range(n[0]):
        x = df.loc[i]
        mycur = mydb.cursor()
        c = kwargs['table']
        sql = f'insert into {c} values ({x[0]},"{x[1]}",{x[2]})'
        mycur.execute(sql)
        mydb.commit()
    return 'Submitted'

# Formatting DataFrame and printing in a tabular format
def formating_DataFrame(df, **kwargs):
    """
    Format the DataFrame and print it in a tabular format.

    Parameters:
        - df: The DataFrame to format and print.
        - title: The title to display above the table.

    Returns:
        None (Prints the formatted DataFrame).
    """
    columns = [i for i in df.columns]
    str_length = []
    for i in columns:
        check_len = [len(str(k)) for k in df[i]]
        check_len.insert(0, len(str(i)))
        str_length.append(max(check_len))

    # Print Table heading and Columns Name
    txt = ''
    for index, col in enumerate(columns):
        sc = ''
        for s in range(str_length[index] - len(col)):
            sc += ' '
        txt += f"| {col}{sc} "
    txt = txt + '|'
    heading = str(kwargs['title'])
    for line in range(round((len(txt)) / 2) - round(len(heading) / 2)):
        print(' ', end='')
    print(heading)
    print('+', end='')
    for line in range(len(txt) - 2):
        print('-', end='')
    print('+')
    print(txt)
    print('+', end='')
    for line in range(len(txt) - 2):
        print('-', end='')
    print('+')

    # Print data values
    dataset_shpe = df.shape
    for i in range(dataset_shpe[0]):
        row_data = df.iloc[i]
        txt_1 = ''
        for index, data in enumerate(row_data):
            sc = ''
            for s in range(str_length[index] - len(str(data))):
                c = ' '
                sc += c
            txt_1 += f"| {data}{sc} "
        txt_1 = txt_1 + '| '
        print(txt_1)
    print('+', end='')
    for line in range(len(txt) - 2):
        print('-', end='')
    print('+')

# Design String line
def design_text(text):
    """
    Format and print the given text in a decorative line.

    Parameters:
        - text: The text to display in the line.

    Returns:
        None (Prints the decorative line with the text).
    """
    x = f"| {text} |"
    print('+', end='')
    for i in range(len(x) - 2):
        print('-', end='')
    print('+')
    print(x)
    print('+', end='')
    for i in range(len(x) - 2):
        print('-', end='')
    print('+')
