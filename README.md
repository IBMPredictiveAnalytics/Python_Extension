# Python_Extension

This extension try provider a common node to execute python script.
![Screenshot](./Screenshot/stream.jpg)
![Screenshot1](./Screenshot/node.jpg)

---
Requirements
----
- IBM SPSS Modeler v18

More information here: [IBM Predictive Extensions](https://developer.ibm.com/predictiveanalytics/downloads/)

---
Installation instructions
----

### Install extension from Extension Hub
1. Open Extension Hub in Modeler Client by: "Extensions" -> "Extension Hub"
2. Select "Spark ML Feature TF-IDF"
3. Click "OK" to start auto installation

### Install extension manually
1. Open extension repository organization [Github IBM Predictive Analytics](https://github.com/IBMPredictiveAnalytics)
2. Search and open repository, download corresponding *.mpe file.
3. Start installation by: "Extensions" -> "Install Local Extension Bundle"
4. Select *.mpe file and install it.

---
Python Scripts Example
---
#### Use `sys.argv` to share variable
#### Get `inputDataframe` and `inputSchema` from `sys.argv`
#### Save `outputDataframe` and `outputSchema` to `sys.argv` after data transform

Example Code:

```
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
```

---
License
----

[Apache 2.0](http://www.apache.org/licenses/LICENSE-2.0.html)

----
Next Step
----
In next release, python model node will provider that able to produce a nugget node.

----
Contributors
----
 - Yu Wenpei [(mail)](yuwenp@cn.ibm.com)

