# Load CSV Files to DBFS

1. Download `articles.csv`, `customers.csv`, and `transaction_train.csv` from Kaggle https://www.kaggle.com/competitions/h-and-m-personalized-fashion-recommendations/data
2. create directory `/FileStore/hm-data/` in the Databricks File System (DBFS) and upload csvs to that directory. 
   1. For `articles.csv` and `customers.csv` this can be done through either the UI upload feature or the cli
   2. For `transaction_train.csv` this must be done through the databricks cli due to file size.  i.e. `databricks fs cp transactions_train.csv dbfs:/FileStore/hm-data/transactions_train.csv`... it may take a while (like an hour)