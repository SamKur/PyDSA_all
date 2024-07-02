# Import SparkSession from pyspark.sql
# from pyspark.sql import SparkSession
# Create my_spark
# spark = SparkSession.builder.getOrCreate()
# sc = SparkSession.sparkContext()


data = [{"name": "John", "age": 30, "department": "Sales"},
        {"name": "Jane", "age": 25, "department": "Marketing"},
        {"name": "Alice", "age": 40, "department": "Engineering"}]

# Create DataFrame from dictionary list
# df = spark.createDataFrame(data)
# print(sc)

# Print the DataFrame (infers column names)
# df.show()

print(data)