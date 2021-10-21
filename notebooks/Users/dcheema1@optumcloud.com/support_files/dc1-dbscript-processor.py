# Databricks notebook source
# MAGIC %md Read in the parameter(s) that were passed by the caller.

# COMMAND ----------

sql_script = dbutils.widgets.get("sql_script");

# COMMAND ----------

# MAGIC %md Install ODBC driver.

# COMMAND ----------

# MAGIC %sh
# MAGIC curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
# MAGIC curl https://packages.microsoft.com/config/ubuntu/16.04/prod.list > /etc/apt/sources.list.d/mssql-release.list
# MAGIC sudo apt-get update
# MAGIC sudo ACCEPT_EULA=Y apt-get -q -y install msodbcsql17

# COMMAND ----------

# MAGIC %md Install pyodbc.

# COMMAND ----------

!pip install pyodbc

import pyodbc

import pandas as pd

# COMMAND ----------

# MAGIC %md Create a database connection (and cursor).

# COMMAND ----------

# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port
server = 'tcp:dc1-sql-server.database.windows.net' 
database = 'dc1-sql-db1' 
username = 'dc-admin' 
password = 'Toaster2010!' 
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()

# COMMAND ----------

# MAGIC %md Excecute SQL command using cursor.

# COMMAND ----------

cursor.execute('SELECT * FROM employees')
for i in cursor:
    print(i)

# COMMAND ----------

# MAGIC %md Execute SQL command that was passed in via parameters and store results in a DataFrame.

# COMMAND ----------

df = pd.read_sql_query(sql_script, cnxn)

print(df)
print(type(df))