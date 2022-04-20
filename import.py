import csv
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine('postgres://wsxxnzhydsbosx:9d5e915237ad9d8434a42e0edfec4ae04825e8fda5fb5b80077015651780edd7@ec2-54-75-246-118.eu-west-1.compute.amazonaws.com:5432/d1c0fg0tsnnrsk')
db = scoped_session(sessionmaker(bind=engine))

def backline():
    print('\r', end='')

def main():
    filename = input('File Name: ')
    #filename = "books.csv"
    count = 0
    print("Counting rows...", end='')
    with open(filename, 'r') as file:
        for line in file:
            count += 1
    f = open(filename)
    reader = csv.reader(f)
    i = 0
    print(f" {count}")
    for provincia in reader:
        backline()
        i += 1
        for asd in provincia:
            asd = asd.replace('{', '')
            asd = asd.replace('}', '')
            db.execute("INSERT INTO province (provincia) VALUES (:provincia)",
                    {"provincia": asd})
        print(f"Importando comune {i} di {count}", end='')


    db.commit()
    print("\nDone!")
if __name__ == "__main__":
    main()
