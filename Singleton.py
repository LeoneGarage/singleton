# Databricks notebook source
import threading
import time
import pandas as pd
from pyspark.sql.functions import col, pandas_udf, udf
from pyspark.sql.types import StringType
from functools import lru_cache
import os
import sys
import time
from mods.singleton_provider import SingletonProvider
from mods.singleton import Singleton

# COMMAND ----------

broadcast_provider = sc.broadcast(SingletonProvider(Singleton))

def run_row(text: str) -> str:
  res = broadcast_provider.value.getInstance().getValue()
  return res

def run_series(s: pd.Series) -> pd.Series:
  return s.apply(run_row)

series = pandas_udf(run_series, returnType=StringType())

# COMMAND ----------

df = spark.createDataFrame([(x, x*2) for x in range(0, 10000)]).toDF('a', 'b').repartition(128)

# COMMAND ----------

df = df.withColumn('c', series(col('a')))

# COMMAND ----------

display(df.select(col('c')).distinct())
