import csv

class Customer:
    def __init__(self, name, date_of_birth, telephone_number, id_number, country_id, site_id):
        self.name = name
        self.date_of_birth = date_of_birth
        self.telephone_number = telephone_number
        self.id_number = id_number
        self.country_id = country_id
        self.site_id = site_id

    def __repr__(self):
        return f"Customer(name='{self.name}', date_of_birth='{self.date_of_birth}', telephone_number='{self.telephone_number}', id_number='{self.id_number}', country_id={self.country_id}, site_id={self.site_id})"

def parse_csv(file_path):
    customers = []
    errors = []
    try:
        with open(file_path, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for line, row in enumerate(reader, start=2):
                name = row['Name'].strip()
                date_of_birth = row['DoB'].strip()
                telephone_number = row['Phone'].strip()
                id_number = row.get('NationalID', '').strip()
                country_id = int(row['CountryID'])
                site_id = int(row['SiteCode'])

                if not name or not date_of_birth or not telephone_number:
                    errors.append({'error': 'Missing required fields', 'line': line})
                    continue

                if country_id not in [1, 2, 3] or site_id not in get_site_ids(country_id):
                    errors.append({'error': f'Site code {site_id} does not exist in the specified country.', 'line': line})
                    continue

                customer = Customer(name, date_of_birth, telephone_number, id_number, country_id, site_id)
                customers.append(customer)

    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None, None

    return customers, errors

def get_site_ids(country_id):
    site_ids = {
        1: [235, 657, 887],
        2: [772, 855],
        3: [465, 811, 980]
    }
    return site_ids.get(country_id, [])

# Example usage
file_path = 'input.csv'
customers, errors = parse_csv(file_path)

if customers is not None and errors is not None:
    print("Valid customer records:")
    for customer in customers:
        print(customer)

    print("\nErrors:")
    for error in errors:
        print(f"Line {error['line']}: {error['error']}")
