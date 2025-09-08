# Reading Data from a Spreadsheet:
# the spreadsheet about census tracts -: which is a geographic area defined for the purpose of census;
# we will write a code to calculate the countrie's population by hand.
# in seconds
# what your program do:
# Read the data from the excel spreadsheet
# counts the number of census tracts in each country
# counts the whole population of each country
# prints the results
# so
# open and read cells of excell with openpyxl
# calculate the tract and population data and store it in a data structure
# write the data structure to a text file with .py ext using pprint module
#
# Read cansus tract data:
import openpyxl

wb = openpyxl.load_workbook("censuspopdata.xlsx")
she = wb["Population by Census Tract"]
countyData = {}
for row in range(2, she.max_row + 1):
    state = she["B" + str(row)].value
    county = she["C" + str(row)].value
    pop = she["D" + str(row)].value
    print(state+" " + county+" "+ str(pop))
    countyData.setdefault(state,{})


#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
