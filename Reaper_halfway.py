__author__ = 'Robert Blaauboer'
#A script that takes a marker file from Reaper
#then it creates a new marker file where the markers are
#halfway between the old ones


#import marker file as .txt file



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
