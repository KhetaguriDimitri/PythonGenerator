import csv
import sys
def convert(somefile,name):
    with open( somefile, 'r' ) as source:
        reader = csv.reader( source ) #reader now holds the whole data like ['lastname', 'firstname', 'phonenumber', 'mail']
        allvcf = open(name, 'w') 
        i = 0
        for row in reader:
            allvcf.write( 'BEGIN:VCARD' + "\n")
            allvcf.write( 'VERSION:2.1' + "\n")
            allvcf.write( 'N:' + row[1] + "; \n")
            allvcf.write( 'FN:' + "Bootcamp \n") #remember that lastname first
            allvcf.write( 'ORG:' + 'Bootcamp' + "\n")
            allvcf.write( 'TEL;CELL:' + row[2] + "\n")
            allvcf.write( "EMAIL:\n")
            allvcf.write( 'END:VCARD' + "\n")
            allvcf.write( "\n")

            i += 1#counts

        allvcf.close()
        print (str(i) + " vcf cards generated")

def main():
    for i in range (1,3):
        st = str(i)+".csv"
        stri = str(555)+str(i)
        print(st)
        stri = stri + ".vcf"
        convert(st,stri)

if __name__ == '__main__':
    main()
