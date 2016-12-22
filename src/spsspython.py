'''
Created on Dec 22, 2016

@author: weyu
'''


from pyspark.context import SparkContext
from pyspark.sql.context import SQLContext
import sys


ascontext=None
if len(sys.argv) > 1 and sys.argv[1] == "-test":
    sc = SparkContext('local')
    sqlContext = SQLContext(sc)
    pypath = "outsidecode.py"
    data = sqlContext.createDataFrame([
        ("Hi I heard about Spark".split(" "), ),
        ("I wish Java could use case classes".split(" "), ),
        ("Logistic regression models are neat".split(" "), )
    ], ["sentence"])
else:
    import spss.pyspark.runtime
    ascontext = spss.pyspark.runtime.getContext()
    sc = ascontext.getSparkContext()
    sqlContext = ascontext.getSparkSQLContext()
    data = ascontext.getSparkInputData()
    pypath = "%%file_python%%"

sys.argv = {
            'SparkContext': sc, 
            'SQLContext': sqlContext, 
            'inputDataframe': data, 
            'inputSchema': data.schema,
            'schemaOnly': ascontext != None and ascontext.isComputeDataModelOnly()}

execfile(pypath)

if ascontext != None:
    if ascontext.isComputeDataModelOnly():
        ascontext.setSparkOutputSchema(sys.argv['outputSchema'])
    else:
        ascontext.setSparkOutputData(sys.argv['outputDataframe'])
else:
    sys.argv['outputDataframe'].show()

