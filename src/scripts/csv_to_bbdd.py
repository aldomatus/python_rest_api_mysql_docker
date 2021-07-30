import csv
from src.app import Address

def import_data(file):
    with open(str(file)) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_counter = 0
        for row in csv_reader:
            if line_counter != 0:
                postal_code=row[0]
                colony=row[1]
                municipality=row[3],
                state=row[4]
                city=row[5]
                
                new_address= Address(postal_code, state, municipality, city, colony)
                db.session.add(new_address)
                db.session.commit()
            line_counter += 1
