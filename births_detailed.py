import pprint


def read_csv(filename):
    """open a csv file and break lines, etc. return a list of lists"""
    f = open(filename, "r")
    string_list = f.read().splitlines()[1:]
    final_list = []
    for line in string_list:
        int_fields = []
        string_fields = line.split(",")
        [int_fields.append(int(i)) for i in string_fields]
        final_list.append(int_fields)
    return final_list


def months_births(lol):
    """takes input list of lists"""
    births_per_month = {}
    for l in lol:
        (month, births) = (l[1],l[4])
        if month in births_per_month:
            births_per_month[month] = births_per_month[month] + births
        else:
            births_per_month[month] = births
    return births_per_month


def dow_births(lol):
    """take a list of lists (lol) and calculate births per day of the week (dow)"""
    dow_births = {}
    for l in lol:
        (dow, births) = (l[3],l[4])
        if dow in dow_births:
            dow_births[dow] = dow_births[dow] + births
        else:
            dow_births[dow] = births
    return dow_births


def calc_counts(lol, column):
    """better function generalizing the ones above.
    Takes input a list of lists and the column we want to calculate the totals for"""
    dict_births = {}
    for l in lol:
        (one, births) = (l[column], l[4])
        if one in dict_births:
            dict_births[one] = dict_births[one] + births
        else:
            dict_births[one] = births
    return dict_births


def calc_minmax(dikt):
    """return min and max value for the input dictionary dikt"""
    dmin = min(dikt.values())
    dmax = max(dikt.values())
    return (dmin, dmax)
    


#
# pprint.pprint((read_csv("US_births_1994-2003_CDC_NCHS.csv"))[:10])
cdc_list = read_csv("US_births_1994-2003_CDC_NCHS.csv")
# pprint.pprint(cdc_list[:10])
#
print("\nmonths")
cdc_month_births = months_births(cdc_list)
pprint.pprint(cdc_month_births)
#
print("\ndays")
cdc_day_births = dow_births(cdc_list)
pprint.pprint(cdc_day_births)
# do year with the generalized function
cdc_year_births = calc_counts(cdc_list, 0)
print("cdc_year_births")
pprint.pprint(cdc_year_births)
#
cdc_month_births = calc_counts(cdc_list, 1)
print("cdc_month_births")
pprint.pprint(cdc_month_births)
#
cdc_dom_births = calc_counts(cdc_list, 2)
print("cdc_dom_births")
pprint.pprint(cdc_dom_births)
#
cdc_dow_births = calc_counts(cdc_list, 3)
print("cdc_dow_births")
pprint.pprint(cdc_dow_births)
#
print("min, max for cdc_year_births")
print(calc_minmax(cdc_year_births))


