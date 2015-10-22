__author__ = 'Robert Blaauboer'

import re

#A script that takes a marker file from Reaper
#then it creates a new marker file where the markers are
#halfway between the old ones

#data example
#1 46.19841269841201 "Hammersmith " 0 -1.00000000000000 0
#2 151.29471655328800 "Barons Court " 0 -1.00000000000000 0
#3 346.55131519273567 "Earl's Court " 0 -1.00000000000000 0



def markers_halfway(in_data):
    markers_tmp = " ".join(in_data)
    print(markers_tmp)




    return markers_tmp


#read through entire file and create list with ID, Time, Description




#Replace marker times with marker times at halfway point
#example:   1 200 "Cannon Street"   #first marker stays at same place
#           2 300 "Hammersmith"
#           3 500 "Embankment"
#           4 800 "Waterloo"        #last marker does change but a new
                                    #marker is created at it's place
                                    #called "Last station"
# new file
#           1 200 "Cannon Street"
#           2 250 "Hammersmith"
#           3 400 "Embankment"
#           4 650 "Waterloo"
#           5 800 "Last station"



#Output list as new file

#import marker file as .txt file
f = open("markers.txt")
for line in f:
    in_data = line.split()
    print("###############ORIGINAL DATA##################")
    print(in_data)
    print("##############################################")
    print()
#change time of markers
    out_data = markers_halfway(in_data)
    print("################PROCESSED#####################")
    print(out_data)
    print("##############################################")