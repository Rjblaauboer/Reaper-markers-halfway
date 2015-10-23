__author__ = 'Robert Blaauboer'

import re

#A script that takes a marker file from Reaper
#then it creates a new marker file where the markers are
#halfway between the old ones
#list needs to be ordered acccording to time

#data example
#1 46.19841269841201 "Hammersmith " 0 -1.00000000000000 0
#2 151.29471655328800 "Barons Court " 0 -1.00000000000000 0
#3 346.55131519273567 "Earl's Court " 0 -1.00000000000000 0



def markers_halfway(in_data, time_previous):   # takes one line of text and the marker time of the previous line
                                # if time is NULL it is assumed that this is the first marker
    markers_tmp = in_data


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

    re_1 = re.compile("((?<=[\s])\d*\.\d*(?=[\s]))", re.I)
    time_current = re.search(re_1, markers_tmp)
    if time_current and time_previous == 'NULL':
        print("first marker")
        time_new = time_current.group(0)
    elif time_current:
        print("previous time")
        time_new = (float(time_previous) + float(time_current.group(0))) / 2
        print("time current: " + time_current.group(0))
    else:
        return (markers_tmp, time_previous)

    markers_tmp = re.sub(re_1, str(time_new), markers_tmp)

    return (markers_tmp, time_current.group(0))








#Output list as new file

#import marker file as .txt file
#f = open("markers.txt")
#n = open("markers_halfway.txt", 'w')
time_previous = "NULL"
with open("markers.txt") as f, open("markers-halfway.txt","w") as n:
   line = f.readline()
   while line != "":
       in_data = line
       out_data, time_previous = markers_halfway(in_data, time_previous)
       n.write("%s" % out_data)
       line = f.readline()
   