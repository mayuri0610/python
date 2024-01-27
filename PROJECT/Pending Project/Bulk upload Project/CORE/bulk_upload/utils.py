import csv
from .models import Person

def bulk_create_persons_from_csv(csv_file):
    persons_to_create = []
    csv_reader = csv.DictReader(csv_file)

    for row in csv_reader:
        person = Person(
            first_name=row['first_name'],
            last_name=row['last_name'],
            email=row['email'],
            gender=row['gender'],
            ip_address=row['ip_address'],
            address=row['address']
            # Add other fields as needed
        )
        persons_to_create.append(person)

    Person.objects.bulk_create(persons_to_create)
