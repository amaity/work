# -*- coding: cp1252 -*-
import csv

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
    
ss_name, divn, n = 0, 0, 0
data = [["Division", "Substation", "Consumer", "Cd", "Remarks"]]
with open("CD AS ON 31.1.2015.csv", 'r') as fa:
    reader = csv.reader(fa)
    for row in reader:
        row_list = filter(None, row)
        if row_list:
            if "CD AS ON" in row_list[0] and n<2:
                n += 1
            elif row_list[0] == "sl" or row_list[0] == "no":
                pass
            elif "GOMD" in row_list[0]:
                divn = "".join(row_list[0].split()[1:])
                divn = ''.join(divn.split('.'))
            elif is_number(row_list[0]):
                ss_name = row_list[1]
            elif n==2:
                break
            else:
                row_list.insert(0,divn)
                row_list.insert(1,ss_name)
                data.append(row_list)

with open("cdout.csv", "wb") as fb:
    writer = csv.writer(fb)
    writer.writerows(data)

data = []
with open("cdout.csv", "rb") as the_file:
    reader = csv.reader(the_file, delimiter=",")
    for row in reader:
        try:
            new_row = [row[0], row[1], row[2], row[3]]
	    #Basically ´write the rows to a list
            data.append(new_row)
        except IndexError as e:
            print e
            pass

print data

with open("modcd.csv", "w+") as to_file:
    writer = csv.writer(to_file,delimiter=',', lineterminator='\n')
    for new_row in data:
        writer.writerow(new_row)





