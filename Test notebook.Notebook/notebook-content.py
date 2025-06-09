# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "170ea32d-6ea5-4dd6-981b-2babba0c6a18",
# META       "default_lakehouse_name": "Test_LH",
# META       "default_lakehouse_workspace_id": "46428b8e-33cf-4812-a262-ff0f257a6317",
# META       "known_lakehouses": [
# META         {
# META           "id": "170ea32d-6ea5-4dd6-981b-2babba0c6a18"
# META         }
# META       ]
# META     }
# META   }
# META }

# CELL ********************

# Welcome to your new notebook
# Type here in the cell editor to add code!

df = spark.sql("SELECT * FROM Test_LH.publicholidays LIMIT 1000")
display(df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************



import pandas
df = spark.read.parquet("abfss://46428b8e-33cf-4812-a262-ff0f257a6317@onelake.dfs.fabric.microsoft.com/170ea32d-6ea5-4dd6-981b-2babba0c6a18/Files/sample_datasets/public_holidays.parquet")
df_pandas = df.toPandas()
df_pandas.to_parquet("output_download.parquet", index=False)

import IPython
IPython.display.FileLink("output_download.parquet")

# df = spark.read.parquet("abfss://46428b8e-33cf-4812-a262-ff0f257a6317@onelake.dfs.fabric.microsoft.com/170ea32d-6ea5-4dd6-981b-2babba0c6a18/Files/sample_datasets/public_holidays.parquet")
# # df now is a Spark DataFrame containing parquet data from "abfss://46428b8e-33cf-4812-a262-ff0f257a6317@onelake.dfs.fabric.microsoft.com/170ea32d-6ea5-4dd6-981b-2babba0c6a18/Files/sample_datasets/public_holidays.parquet".
# display(df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# import pandas as pd

# # Read Parquet file directly to Spark DataFrame
# df_spark = spark.read.parquet("abfss://46428b8e-33cf-4812-a262-ff0f257a6317@onelake.dfs.fabric.microsoft.com/170ea32d-6ea5-4dd6-981b-2babba0c6a18/Files/sample_datasets/public_holidays.parquet")

# # Convert to Pandas (only use if small file)
# df_pd = df_spark.toPandas()

# # Save as CSV locally in the notebook environment
# df_pd.to_csv("converted_output.csv", index=False)

# Read Parquet file
df_spark = spark.read.parquet("abfss://46428b8e-33cf-4812-a262-ff0f257a6317@onelake.dfs.fabric.microsoft.com/170ea32d-6ea5-4dd6-981b-2babba0c6a18/Files/sample_datasets/public_holidays.parquet")

# Save as CSV in the same folder path
df_spark.write.mode("overwrite").option("header", True).csv("Files/sample_datasets/public_holidays_csv")


# # Show download link
# import IPython
# IPython.display.FileLink("converted_output.csv")


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# Read the Parquet file
df_spark = spark.read.parquet("Files/sample_datasets/public_holidays.parquet")

# Write as CSV in the same folder, under a new subfolder
df_spark.write.mode("overwrite").option("header", True).csv("Files/sample_datasets/public_holidays_csv")


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
