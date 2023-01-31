import csv

with open('NZ.csv') as cf:
    cf_read = csv.reader(cf, delimiter=',')
    line_count = 0
    for row in cf_read:
        if line_count ==5:
            break
        
        elif line_count == 0:
               print(f'{row[0]},{row[1]},{row[2]},{row[3]}')
               line_count+=1
        else:
        
            print(f'{row[:5]}')
            line_count+=1


with open('NZ.csv') as cf:
    cf_read = csv.DictReader(cf)
    line_count = 0
    for row in cf_read:
        if line_count ==5:
            break
        if line_count == 0:
            print(f'Column Names are{",".join(row)}')
            line_count+=1
        else:
            print(f'\t{row["Year"]} works in the {row["Industry_code_NZSIOC"]} industry with variable code {row["Variable_category"]}')
            line_count+=1
    print(f"Processed {line_count} lines")


    with open('NZ.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        count = 0
        for row in reader:
            count+=1
            if count==5:
                break
            print(row['Year'],row['Variable_code'])

    