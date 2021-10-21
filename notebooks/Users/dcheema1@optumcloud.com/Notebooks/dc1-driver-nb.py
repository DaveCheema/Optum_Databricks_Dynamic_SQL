# Databricks notebook source
# MAGIC %md Let's begin...

# COMMAND ----------

print('Starting job...')

# COMMAND ----------

# MAGIC %md Read SQL script file.

# COMMAND ----------

file_path = '/dbfs/FileStore/scripts/employee_reader.sql';

def run_file(path):
    return open(path).read();

sql_script = run_file(file_path);

# COMMAND ----------

# MAGIC %md Create parameters to be passed.

# COMMAND ----------

dbutils.widgets.text(
  name='sql_script',
  defaultValue=sql_script,
  label='sql_script'
);

# COMMAND ----------

# MAGIC %md A test script that shows how various ways parameters can be passed.

# COMMAND ----------

# MAGIC %run ../support_files/dc1-dbscript-processor

# COMMAND ----------

# MAGIC %md Run common task.

# COMMAND ----------

# MAGIC %run /Shared/dc1-common-code

# COMMAND ----------

print('Ending job...')

# COMMAND ----------

# MAGIC %md THE END.