# main.py  Python Challenge - PyBoss    Author: Inna Baloyan

# For creating file paths across operation system
import os

# For reading CSV file
import csv

# For date conversion
from datetime import datetime as dt

###employee_data_file = "employee_data1.csv"
employee_data_file = "employee_data2.csv"
###output_employee_data_CSV = "output_employee_data1.csv"
output_employee_data_CSV = "output_employee_data2.csv"

# Path to collect data from the Resources folder
employee_data_CSV = os.path.join('Resources', employee_data_file)

###print(employee_data_CSV)  ### comment out later

# Lists to store Employee data
Emp_ID = []
First_Name = []
Last_Name = []
DOB = []
SSN = []
State = []

# Python Dictionary for State abbreviations
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
    }

# Read in the employee_data_CSV file without header, i.e the first line
with open(employee_data_CSV, 'r') as employee_data:

      my_reader = csv.reader(employee_data, delimiter=',')
      Emp_Header = next(my_reader)

      # Read in the employee data file 
      # Emp ID, Name, DOB, SSN, State
      # row{0], row[1], row[2], row[3], row[4]     
     
      # Loop through all 
      for row in my_reader:    

            FOUND_STATE = False
            # Get all data in employee data row
            EMP_ID = row[0]
            Emp_ID.append(EMP_ID)

            NAME = row[1]
            FIRST_NAME, LAST_NAME = NAME.split(" ")
            First_Name.append(FIRST_NAME)
            Last_Name.append(LAST_NAME)

            OLD_DOB = row[2]
            datetimeobject = dt.strptime(OLD_DOB,'%Y-%m-%d')
            NEW_DOB = datetimeobject.strftime('%m/%d/%Y')
            DOB.append(str(NEW_DOB))

            OLD_SSN = row[3]
            LAST4_SSN = OLD_SSN[7:11]
            NEW_SSN = "***-**-" + LAST4_SSN
            SSN.append(NEW_SSN)

            OLD_STATE = row[4]
            for key, value in us_state_abbrev.items():
                if ( key == OLD_STATE ):
                    NEW_STATE = value
                    FOUND_STATE = True
                    break
            if ( FOUND_STATE != True ):
                    print ( OLD_STATE + " is wrong state, need to be corrected for person with SSN# " + OLD_SSN) 
                    NEW_STATE = "  "   
            State.append(NEW_STATE)

# Zip lists together
new_employee_layout = zip(Emp_ID, First_Name, Last_Name, DOB, SSN, State)

#  Open the output file
with open(output_employee_data_CSV, "w", newline="") as datafile:
    New_Employee_File = csv.writer(datafile)

    # Write the header row
    New_Employee_File.writerow(["Emp ID", "First Name", "Last Name", "DOB", "SSN", "State"])

    # Write in zipped rows
    New_Employee_File.writerows(new_employee_layout)

# ##### The End ###################################################### 