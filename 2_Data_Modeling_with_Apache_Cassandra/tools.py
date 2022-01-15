import csv
# Map containing column-name to data-type mapping used for inserting to cassandra
dataMap = {
    'itemInSession': int,
    'sessionId': int,
    'length': float,
    'userId': int,
}

def getData(line, columns, index):
    """
    Get data from csv rows, extract the information
    :param List[str] line: Csv rows that has the list of strings
    :param Tuple[str] columns: Columns to be used
    :param Dict[str, int] index: Index to be used for the dictionary
    :return Tuple that contained extracted rows
    :rtype Tuple[Any]
    """
    
    row_data = []
    for i in columns:
        # Extract value from row using the index
        value = f"{line[index[i]]}"
        
        # Use the map to add the values
        row_data.append(dataMap.get(i, str)(value))
    return tuple(row_data)

def insertInto (session, filename, table_name, column_names):
    """
    This funtion is created to insert data into database table from the csv
    :param cassandra-session session: Current database session
    :param str filename: data from csv
    :param str table_name: table name to be edited
    :param Tuple[str] column_names: columns from csv
    :return nothing
    :rtype None
    """
    
    columnLoc = "%s, "*len(column_names)
    columnLocCorrect = f"({columnLoc[:-2]})"
    columns_in_query = "(" + ', '.join(column_names) + ")"
    with open(filename, encoding = 'utf8') as f:
        csvreader = csv.reader(f)
        header_row = next(csvreader)
        index = {name:index for index,name in enumerate(header_row)}
        for line in csvreader:
                query = f"INSERT INTO {table_name} "
                query = query + f"{columns_in_query} VALUES {columnLocCorrect}"
                data_values = getData(line, column_names, index)
                session.execute(query, data_values)
    print(f"Data inserting into {table_name} completed.")
