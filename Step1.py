import os #Allows interaction with the operating system  
import csv #Allows read and write files
import pandas as pd

stations = ["ML0004", "ML0021", "ML0029"] #List containing the stations
counter = 0 #Set to 0 to number the rows in the output file

#Opens in write mode, as this will create an empty version of the file
#With ensures file to be closed after execution even with error
with open("project_data.csv", "w", newline="") as f: 
    pass #Does nothing to the file while open

#This section loops through various csv data files and imports relevant data
for i in range(2014,2020): #2014 to 2019
    for j in range(1,5): #Q1 to Q4
        fileName = f"{i}-Q{j}-Central.csv"

#Checks whether the file exists before opening file
        if os.path.exists(fileName):
            with open(fileName, "r", newline="") as f: #Opens csv file in read mode
                reader = csv.reader(f) #Creates a csv reader to read the file
                header = next(reader) #Reads the first row as the header

#Iterates through each row in the CSV file
                for row in reader: 
#Checks if row is not empty and if second column is containted in the station
                    if row and row[1] in stations:
#Change the first column to represent the year+quarter format
                        row[0] = f"{i}Q{j}" 
#Creates a new row by adding a counter
                        out_row = [counter] + row
                        counter += 1 #Increments the counter for the next row
#Opens the output file in append mode to modify the row to store the file object
                        with open("project_data.csv", "a", newline="") as output_file:
                            #Variable writer stores the csv writer object 
                            writer = csv.writer(output_file)
                            #Writes the modified row to the output csv file 
                            writer.writerow(out_row)
 
#Defining the column names
col_names = ["Quarter", "Station", "Date", "Weather", "Time", "Day", "Drop1", "Direction", "Drop2", "Mode", "Count"]
#Reads the csv file into the dataframe with the correct column names
df = pd.read_csv("project_data.csv", names=col_names)
#Drop unnecessary columns
df = df.drop(columns=["Drop1", "Drop2"])
#Creates the Full_Time column by concatenating "Date" and "Time"
df["Full_time"] = df["Date"] + " " + df["Time"]
#Save the cleaned version of the dataframe to an excel file "CycleData.xlsx"
df.to_excel("CycleData.xlsx", sheet_name="Sheet1", index=False)
          
                    
                
                
            

