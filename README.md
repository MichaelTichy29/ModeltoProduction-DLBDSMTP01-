# Konzept
This is my Project for the course Model to Production. The flow is as follows: 
Based on the data we present in Testdaten the file Model.py generates a simple prediction model for an error of an supervised system. 

In sensor_stream an endless stream of data with normal states and errors is produced. The api has to run and the model exported from the run of the file Model.py is necassary. Then the client can run and gets all the time measures of the factory and presents an answer if the system is ok or an error is detected.
