import mysql.connector as msc
import numpy as np
import pandas as pd

def create_database(dbname):
    '''
    Create a new database in MySQL.

    Parameters:
    dbname (str): The name of the database to be created.

    Returns:
    str: A success message indicating the database creation status.
    '''
    try:
        mydb = msc.connect(host='localhost', user='root', password='Neeraj@123')
        mycur = mydb.cursor()

        # Check if the database exists
        mycur.execute(f"SELECT SCHEMA_NAME FROM INFORMATION_SCHEMA.SCHEMATA WHERE SCHEMA_NAME = '{dbname}'")
        existing_db = mycur.fetchone()

        if existing_db:
            # If the database exists, drop it
            mycur.execute(f"DROP DATABASE {dbname}")
            print(f"Database '{dbname}' dropped successfully.")

        # Create the database
        mycur.execute(f"CREATE DATABASE {dbname}")
        
        return f"Database '{dbname}' created successfully."
    
    except Exception as e:
        return f"Error: {str(e)}"

def drop_database(database_name):
    """
    Drop a MySQL database.

    Parameters:
        database_name (str): The name of the database to drop.

    Returns:
        str: A message indicating the status of the database drop process.
    """
    try:
        mydb = msc.connect(host='localhost', user='root', password='Neeraj@123')
        cur = mydb.cursor()

        cur.execute(f'DROP DATABASE {database_name}')
        mydb.commit()
        
        cur.close()
        mydb.close()

        return f"Database '{database_name}' dropped successfully."
    except Exception as e:
        return f"Error: {str(e)}"

def create_table(columns, table, database):
    '''
    Create a new table in the specified database with given columns and constraints.

    Parameters:
    columns (str): A string containing the columns name, data types, and constraints.
    table (str): The name of the table to be created.
    database (str): The name of the database in which to create the table.

    Returns:
    str: A success message indicating the table creation status.
    '''
    try:
        mydb = msc.connect(host='localhost', user='root', password='Neeraj@123', database=database)
        mycur = mydb.cursor()
        sql = f"create table {table} ({columns})"
        mycur.execute(sql)
        
        return f"Table '{table}' created successfully."
    except Exception as e:
        return f"Error: {str(e)}"

def insert_data(table, database):
    '''
    Insert data into the specified table in the database.

    Parameters:
    table (str): The name of the table where data will be inserted.
    database (str): The name of the database containing the table.

    Returns:
    str: A message indicating the number of rows inserted.
    '''
    try:
        mydb = msc.connect(host='localhost', user='root', password='Neeraj@123', database=database)
        mycur = mydb.cursor()
        mycur.execute(f"desc {table}")
        columns_info = mycur.fetchall()
        row = int(input('How many rows do you want to insert: '))
        for n in range(row):
            lst = []
            for info in columns_info:
                col_name = info[0]
                if str(info[1]).find('int') >= 0:
                    val = int(input(f"Enter {col_name}: "))
                else:
                    val = input(f"Enter {col_name}: ")
                lst.append(val)
            lst = tuple(lst)
            sql = f"insert into {table} values {lst}"
            mycur = mydb.cursor()
            mycur.execute(sql)
            mydb.commit()
            print('row inserted')
        
        return f"Inserted data into '{table}' successfully."
    except Exception as e:
        return f"Error: {str(e)}"

def select_table(table, database):
    '''
    Select and display all columns and rows from the specified table in the database.

    Parameters:
    table (str): The name of the table to be selected.
    database (str): The name of the database containing the table.

    Returns:
    None
    '''
    try:
        mydb = msc.connect(host='localhost', user='root', password='Neeraj@123', database=database)
        mycur = mydb.cursor()
        mycur.execute(f"DESC {table}")
        col = mycur.fetchall()
        columns = [info[0] for info in col]
        mycur.execute(f"SELECT * FROM {table}")
        show = mycur.fetchall()
        arr = np.array(show)
        length = []
        for n, col_name in enumerate(columns):
            x = [row[n] for row in arr]
            x.append(col_name)
            check_len = max([len(str(item)) for item in x])
            length.append(check_len)
        txt = ''
        for index, col_name in enumerate(columns):
            sc = ''
            for s in range(length[index] - len(col_name)):
                c = ' '
                sc += c
            t = f"| {col_name}{sc} "
            txt += t
        txt = txt + '|'
        print('+', end='')
        for p in range(len(txt) - 2):
            print('-', end='')
        print('+')
        print(txt)
        print('+', end='')
        for p in range(len(txt) - 2):
            print('-', end='')
        print('+')
        for data in show:
            txt_1 = ''
            for index, item in enumerate(data):
                sc = ''
                for s in range(length[index] - len(str(item))):
                    c = ' '
                    sc += c
                t = f"| {item}{sc} "
                txt_1 += t
            txt_1 = txt_1 + '| '
            print(txt_1)
        print('+', end='')
        for p in range(len(txt) - 2):
            print('-', end='')
        print('+')
        
    except Exception as e:
        return f"Error: {str(e)}"

    
def dataframe_to_database(df, password='Neeraj@123', **kwargs):
    """
    Inserts data from a DataFrame into a MySQL database table.

    Parameters:
        df (pandas.DataFrame): The DataFrame containing the data to be inserted.
        password (str): The password to connect to the MySQL database. Default is 'Neeraj@123'.
        **kwargs: Additional keyword arguments.
            table_name (str): The name of the table in the database where data will be inserted.
            database (str): The name of the database where the table exists.

    Returns:
        str: A message indicating the status of the data insertion process.
    """
    try:
        int_col = [i for i in df.columns if 'int' in str(df[i].dtype)]
        float_var = [i for i in df.columns if 'float' in str(df[i].dtype)]
        str_var = [i for i in df.columns if 'object' in str(df[i].dtype)]
        columns_list = int_col + float_var + str_var
        change_var_name = [name.replace(" ", "") for name in str_var]
        str_length = [max(len(str(i)) for i in df[columns].unique()) for columns in str_var]

        query = f"CREATE TABLE {kwargs['table_name']} ("

        if int_col:
            query += ', '.join([f"{col} INT" for col in int_col])

        if float_var:
            if int_col:
                query += ', '
            query += ', '.join([f"{col} FLOAT" for col in float_var])

        if str_var:
            if int_col or float_var:
                query += ', '
            query += ', '.join([f"{col_name} VARCHAR({length})" for col_name, length in zip(change_var_name, str_length)])

        
        query += ")"

        # Connect to the database
        mydb = msc.connect(host='localhost', user='root', password=password, database=kwargs['database'])
        mycur = mydb.cursor()

        # Create the table
        mycur.execute(query)

        # Insert data
        insert_query = f"INSERT INTO {kwargs['table_name']} VALUES ("
        mycur = mydb.cursor()

        for row in range(df.shape[0]):
            row_data = df.iloc[row]

            # Create the values part of the INSERT query using parameterized queries
            values = []
            for col in columns_list:
                value = row_data[col]
                if col in int_col:
                    values.append(int(value))
                elif col in float_var:
                    values.append(float(value))
                elif col in str_var:
                    values.append(str(value))

            # Prepare the parameterized query
            placeholders = ", ".join(["%s"] * len(values))
            insert_query_row = insert_query + placeholders + ")"

            # Execute the INSERT query for the current row
            mycur.execute(insert_query_row, tuple(values))
            mydb.commit()

        # Commit the changes and close the connection
        mydb.close()

        return 'Data inserted successfully.'
    except Exception as e:
        return f'Error: {str(e)}'