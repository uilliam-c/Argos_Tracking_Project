#-------------------------------------------------------------
# ArgosSelectionTool.py
#
# Description: Reads in an Argos tracking data file and allows
#   the user to identify the tracked sitings found within a 
#   specified bounding box.
#
# Author: Liam Connolly (liam.connolly@duke.edu)
# Date:   Fall 2026
#--------------------------------------------------------------

# Create the geographic selection box
the_box = {
    'x_min' : 34.00,
    'y_min' : -76.00,
    'x_max' : 34.50,
    'y_max' : -75.00
}

# Create a variable pointing to the data file
file_name = 'data/raw/MoveBank/Satellite tracking of black-capped petrels 2019-argos.csv'

# Open the file
f = open(file_name, 'r')
# Read and skip the header
lineString = f.readline()
# Read the first actual data line
lineString = f.readline()
# Iterate through lines
while lineString != "":

    # Use the split command to parse the items in lineString into a list object
    line_data = lineString.split(',')

    # Assign variables to specific items in the list
    event_id = line_data[0]
    timestamp = line_data[2]
    lc = line_data[14]
    # Skip unreliable records
    if lc not in ["1", "2", "3"]:
        lineString = f.readline()
        continue
    lat = float(line_data[4])
    lon = float(line_data[3])
    tag_id = line_data[-3]

    # Evaluate latitude and longitude conditions
    lat_condition = the_box['y_min'] < lat < the_box['y_max']
    lon_condition = the_box['x_min'] < lon < the_box['x_max']

    # Report the status of the points
    if lat_condition & lon_condition:
        print(f'Record {event_id}: {tag_id} was IN the box at {timestamp}')
    else:
        print(f'Record {event_id}: {tag_id} was NOT IN the box at {timestamp}')

    # Move to the next line
    lineString = f.readline()
    
# Close the file
f.close()