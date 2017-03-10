
# open file and read text
f = open("US_births_1994-2003_CDC_NCHS.csv", "r")
text = f.read()
#print(text)

# split lines and extract week and births
lines = text.splitlines()
# print(lines)
fields = [(line.split(",")[3:5]) for line in lines[1:]]
print(fields[1:3])

# create a dictionary of day_of_week to births
dikt = {}
lines = text.splitlines()
# print(lines)
fields = [(line.split(",")[3:5]) for line in lines[1:]]
# print(fields)
for l1 in fields:
    day_of_week = l1[0]
    births = l1[1]
    if day_of_week in dikt:
        dikt[day_of_week] += births
    else:
        dikt[day_of_week] = births
print(dikt)
