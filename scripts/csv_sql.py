
import csv

def import_data(file):
    with open(str(file)) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_counter = 0
        for row in csv_reader:
            if line_counter != 0:
                c = Circle(
                    name=row[0],
                    slug_name=row[1],
                    is_public=(False if int(row[2]) == 0 else True),
                    verified=(False if int(row[3]) == 0 else True),
                    members_limit=int(row[4])
                )
                c.save()
            line_counter += 1

import_data('circles.csv')