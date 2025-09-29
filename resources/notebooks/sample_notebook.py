# Databricks notebook source
# MAGIC %md
# MAGIC ## Sample Notebook
# MAGIC This notebook demonstrates basic data operations in Databricks.

# COMMAND ----------

# MAGIC %python
# Create a sample DataFrame
import pandas as pd
import pyspark.sql.functions as F

data = [("Alice", 34), ("Bob", 45), ("Cathy", 29)]
df = spark.createDataFrame(data, ["Name", "Age"])
df.show()

# COMMAND ----------

# MAGIC %sql
-- Create a temporary view and query it
CREATE OR REPLACE TEMP VIEW people AS
SELECT * FROM VALUES
  ('Alice', 34),
  ('Bob', 45),
  ('Cathy', 29)
AS data(name, age);

SELECT * FROM people WHERE age > 30;
