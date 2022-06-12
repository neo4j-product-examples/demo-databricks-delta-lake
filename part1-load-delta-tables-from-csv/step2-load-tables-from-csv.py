# Databricks notebook source


# COMMAND ----------

# MAGIC %md
# MAGIC # Load HM CVS int Delta Tables

# COMMAND ----------

# MAGIC %md
# MAGIC ## Articles

# COMMAND ----------

df = spark.read.format("csv") \
  .option("inferSchema", "true") \
  .option("header", "true") \
  .load("/FileStore/hm-data/articles.csv")

table_name = "hmArticles"
df.write \
  .format("delta") \
  .saveAsTable(table_name)

display(spark.sql("SELECT * FROM " + table_name))

# COMMAND ----------

# MAGIC %md
# MAGIC ## Customers

# COMMAND ----------

df = spark.read.format("csv") \
  .option("inferSchema", "true") \
  .option("header", "true") \
  .load("/FileStore/hm-data/customers.csv")

table_name = "hmCustomers"
df.write \
  .format("delta") \
  .saveAsTable(table_name)

display(spark.sql("SELECT * FROM " + table_name))

# COMMAND ----------

# MAGIC %md
# MAGIC ## Transactions

# COMMAND ----------

# Use the cli to upload csv...too big for UI upload $databricks fs cp ~/Downloads/hm-data/transactions_train.csv dbfs:/FileStore/hm-data/transactions_train.csv
df = spark.read.format("csv") \
  .option("inferSchema", "true") \
  .option("header", "true") \
  .load("/FileStore/hm-data/transactions_train.csv")

table_name = "hmTransactions"
df.write \
  .format("delta") \
  .saveAsTable(table_name)

display(spark.sql("SELECT * FROM " + table_name))
