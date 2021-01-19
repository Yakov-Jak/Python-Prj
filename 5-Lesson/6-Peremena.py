les_hrs_dict = {}

with open('6-Raspis.txt', 'r') as rasp:
    for el in rasp.readlines():
        str_data = list(el.split())
        les_hrs = 0

        for wrs in str_data:
            a = int(wrs) if wrs.isdigit() else 0
            les_hrs = les_hrs + a
        les_hrs_dict[str_data[0]] = les_hrs
print(les_hrs_dict)
