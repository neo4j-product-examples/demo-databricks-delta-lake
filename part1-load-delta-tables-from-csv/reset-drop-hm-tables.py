# Databricks notebook source
# MAGIC %md
# MAGIC # Drop Delta Lake Tables

# COMMAND ----------

display(spark.sql("DROP TABLE hmArticles"))

# COMMAND ----------

display(spark.sql("DROP TABLE hmCustomers"))

# COMMAND ----------

display(spark.sql("DROP TABLE hmTransactions"))
