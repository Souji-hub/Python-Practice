import csv

with open('Python/CSV_files/NZ.csv') as cf:
     cf_read = csv.reader(cf, delimiter=',')
     line_count = 0
     col = 0
     for row in cf_read:
        if line_count<10:   
            print(f'{row[col]},{row[col+1]}')
            line_count+=1
            
                

