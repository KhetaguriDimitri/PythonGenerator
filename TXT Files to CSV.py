import csv,os
to_add=1
fieldnames=['Name','Phone 1 - Value']
for each in os.listdir():
    c=1
    if each.endswith(".txt"):
        with open("{}".format(each)) as fp:
            with open('{}.csv'.format(each.replace(".txt","")), 'w', newline='') as csvfile:
                
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                while(a:=fp.readline()):
                        writer.writerow({'Name': to_add, 'Phone 1 - Value': a})
                        
                        to_add+=1   
                
    
#del *.txt
#Convert CSV Format
