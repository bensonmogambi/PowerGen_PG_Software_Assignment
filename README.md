# PowerGen_PG_Software_Assignment

# CSV Parser
This program parses a CSV file containing customer records and returns a Customer record or an error for each row.

# Features
- Reads a CSV file as input.
- The CSV file's customer records are parsed.
- Validates each customer record's fields.
- Returns valid customer records and errors for any invalid records.

# Usage
1. Clone the repository:

git clone
https://github.com/bensonmogambi/PowerGen_PG_Software_Assignment.git

2. Navigate to the project directory:

  cd csv-parser

3. Place the input CSV file in the project directory.

4. Run the program:
  python main.py

5. The program will parse the CSV file and display the valid customer records and any errors encountered during parsing.

# File Format

The input CSV file should have the following format:

Name,DoB,Phone,NationalID,CountryID,SiteCode
Benson Mogambi,1990-01-01,+123456789,987654321,1,235
Treva Okumu,1985-05-10,+987654321,,2,772

~ Each row corresponds to a customer record.

~ Commas are used to separate the fields.

~ The fields should be in the specified order: Name, DoB, Phone, NationalID, CountryID, SiteCode.

~ The NationalID field is optional.

~ The CountryID field should be an integer representing the country (1: Kenya, 2: Sierra Leone, 3: Nigeria).

~ The SiteCode field should be an integer representing the site ID for the corresponding country.


# Output

The program will display the following output:

1. Valid customer records: A list of valid customer records, including their fields.
2. Errors: Any errors encountered during parsing, including the line number and error message.

Example output:

Valid customer records:
Customer(name='John Doe', date_of_birth='1990-01-01', telephone_number='+123456789', id_number='987654321', country_id=1, site_id=235)

Errors:
Line 3: Site code 772 does not exist in the specified country.


