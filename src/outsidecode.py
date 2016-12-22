'''
Created on Dec 22, 2016

@author: weyu
'''
from pyspark.sql.functions import lit
from pyspark.sql.types import StructType, StructField, DoubleType
import sys


data = sys.argv['inputDataframe']
schema = sys.argv['inputSchema']

if sys.argv['schemaOnly']:
    sys.argv['outputSchema'] = StructType(data.schema.fields + 
                    [StructField("newConstant", DoubleType(), False) ])
else:
    sys.argv['outputDataframe'] = data.withColumn('new', lit(1.0))