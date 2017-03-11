import pprint


def read_csv(filename):
    f = open(filename, "r")
    string_list = f.read().splitlines()[1:]
    final_list = []
    for line in string_list:
        int_fields = []
        string_fields = line.split(",")
        [int_fields.append(int(i)) for i in string_fields]
        final_list.append(int_fields)
    return final_list


# pprint.pprint((read_csv("US_births_1994-2003_CDC_NCHS.csv"))[:10])
cdc_list = read_csv("US_births_1994-2003_CDC_NCHS.csv")
pprint.pprint(cdc_list[:10])


