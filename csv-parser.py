import csv
import re
from datetime import datetime

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
            try:
                reader = csv.DictReader(csvfile)
                for line, row in enumerate(reader, start=2):
                    name = row['Name'].strip()
                    date_of_birth = row['DoB'].strip()
                    telephone_number = row['Phone'].strip()
                    id_number = row.get('NationalID', '').strip()
                    country_id = row.get('CountryID', '').strip()
                    site_id = row.get('SiteCode', '').strip()

                    # Check if the row is empty or contains only whitespace
                    if not any(row.values()):
                        errors.append({'error': 'Empty row', 'line': line})
                        continue

                    # Validate name
                    if not name:
                        errors.append({'error': 'Missing name', 'line': line})
                        continue

                    # Validate date of birth
                    if not is_valid_date(date_of_birth):
                        errors.append({'error': 'Invalid date of birth', 'line': line})
                        continue

                    # Validate telephone number
                    if not is_valid_telephone_number(telephone_number):
                        errors.append({'error': 'Invalid telephone number', 'line': line})
                        continue

                    # Validate ID number (optional)
                    if id_number and not is_valid_id_number(id_number):
                        errors.append({'error': 'Invalid ID number', 'line': line})
                        continue

                    # Validate country ID
                    if not country_id or not country_id.isdigit() or int(country_id) not in [1, 2, 3]:
                        errors.append({'error': 'Invalid country ID', 'line': line})
                        continue
                    country_id = int(country_id)

                    # Validate site ID
                    if not site_id or not site_id.isdigit() or int(site_id) not in get_site_ids(country_id):
                        errors.append({'error': 'Invalid site code', 'line': line})
                        continue
                    site_id = int(site_id)

                    customer = Customer(name, date_of_birth, telephone_number, id_number, country_id, site_id)

                    # Check for duplicate customer records
                    if customer in customers:
                        errors.append({'error': 'Duplicate customer record', 'line': line})
                        continue

                    customers.append(customer)

            except csv.Error as e:
                errors.append({'error': 'CSV parsing error', 'line': line, 'exception': str(e)})

    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None, None

    return customers, errors

def is_valid_date(date):
    # Check if the date is in ISO 8601 format (YYYY-MM-DD)
    pattern = r'^\d{4}-\d{2}-\d{2}$'
    if not re.match(pattern, date):
        return False

    # Additional check for valid date components
    try:
        datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        return False

    return True

def is_valid_telephone_number(telephone_number):
    # Check if the telephone number contains only digits and has the expected length
    pattern = r'^\d{12}$'
    return bool(re.match(pattern, telephone_number))

def is_valid_id_number(id_number):
    return True

def get_site_ids(country_id):
    site_ids = {
        1: [235, 657, 887],
        2: [772, 855],
        3: [465, 811, 980]
    }
    return site_ids.get(country_id, [])

# usage
file_path = 'input.csv'
customers, errors = parse_csv(file_path)

if customers is not None and errors is not None:
    print("Valid customer records:")
    for customer in customers:
        print(customer)

    print("\nErrors:")
    for error in errors:
        line = error.get('line', 'unknown')
        error_msg = error.get('error', 'Unknown error')
        exception_msg = error.get('exception', '')
        print(f"Line {line}: {error_msg} - {exception_msg}")
