#!/usr/bin/env python

# for homework:
# identify what type of data each value is, and cast it
# to the appropriate type, then print the new, properly-typed
# list to the screen.
# I.e. ['0.04741', '0.00', '11.930', '0', '0.5730', '6.0300', '80.80', '2.5050', '1', '273.0', '21.00', '396.90', '7.88', '11.90']
# becomes: [0.04741, 0.0, 11.93, 0, 0.573, '6.03, 80.8, 2.505, 1, 273.0, 21.0, 396.90, 7.88, 11.90]

import os

myfilename = 'housing.data.txt;'
newvalues = []
listfinal = []
feature = []
n = -1

with open(myfilename, 'r') as file_handle:
    for line in file_handle.readlines():
        line_clean = line.replace('   ', ' ').replace('  ', ' ')
        line_clean = line_clean.strip()
        values = line_clean.split(' ')
        #print(values)
        #print(len(values))
        for value in values:

            # Verifies if value is an Integer or Float, adds to new list
            try:
                val = int(value)
                newvalues += [int(value)]
            except ValueError:
                newvalues += [float(value)]

    # Indetify how many rows and columns I have
    rows = int(len(newvalues)/len(values))
    cols = int(len(values))

    # Creates rows for my final list 2D array
    for i in range(rows):
        listfinal.append([])

    # Creates columns for final list 2D array
    # Uses n counter variable to identify the data location in newvalues list
    # Adds that value from newvalues to finale list
    # Final list is now a proper array with columns and rows
    for i in range(rows):
        for j in range(cols):
            n = n + 1
            listfinal[i].append(j)
            listfinal[i][j] = newvalues[n]

    # For each column in the Final list
    # Adding it to it's own respective feature
    # In the array of feature each row is equivalent to the column in listfinal
    # Prints each feature set
    for j in range(cols):
        feature.append([])
        print('Feature', j+1, ':')
        for i in range(rows):
            feature[j].append(i)
            feature[j][i] = listfinal[i][j]
            print(feature[j][i], end = ' ')
        print()

    print('finished!')
