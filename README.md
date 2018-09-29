# Twitter_data_extraction

## Objective 

The main goal of the project is to collect the real time twitter data in Json format and  to analyze this big data using Apache Hadoop and Apache Spark. The twitter data we collected here is about Bitcoin. Then we extracted the hashtags and URL’s from the data and performed word count operation on the extracted hashtags and URL’s using Hadoop and Spark.
We have used Hadoop in order to perform the Map Reduce framework. Map Reduce exclusively works on key value pair. It works on large data sets.
We have used Spark here as it mainly works on Hadoop. It does faster computation than Hadoop and we can write applications in Java, Scala, Python and R language. Spark comes in rescue when we have to perform complex analytics on vast data.

## System Requirements

We need few languages and software that has to be installed in the system before collecting the data.

### Languages: 
Python, Scala.

### Software requirements: 
- Apache Hadoop (version 2.8.1)
- Apache Spark (version 2.3.1)
- Scala (version  2.12.6)
- 7z to unzip compressed twitter data output

### Folder Structure:
- src\output : Contains collected tweets data, extracted URLs and Hashtags from Hadoop,Spark.
- src\main\code: Contains the code used to extract tweets from twitter, logic to extract URLs and Hashtags
- src\log_files: Contains the log files collected from hadoop and spark
