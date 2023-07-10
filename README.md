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

# For Personal Use.

Code handles the following errors:
Empty or whitespace rows: It detects and logs an "Empty row" error for any rows in the CSV file that are empty or contain only whitespace.

Missing name: It logs a "Missing name" error if the Name field in a row is empty.

Invalid date of birth: It logs an "Invalid date of birth" error if the DoB field does not match the expected ISO 8601 date format (YYYY-MM-DD) or if the date is not a valid date (e.g., invalid month or day).

Invalid telephone number: It logs an "Invalid telephone number" error if the Phone field does not match the expected format of 12 digits.

Invalid ID number: If the NationalID field is provided, the code can log an "Invalid ID number" error if the is_valid_id_number function returns False (although the function is currently a placeholder and assumes all ID numbers are valid).

Invalid country ID: It logs an "Invalid country ID" error if the CountryID field is missing, not a digit, or not one of the specified values (1, 2, or 3).

Invalid site code: It logs an "Invalid site code" error if the SiteCode field is missing, not a digit, or not a valid site code for the corresponding country.

Duplicate customer record: It detects and logs a "Duplicate customer record" error if a customer with the same combination of name and date of birth already exists.

File not found: It handles the FileNotFoundError exception and prints an appropriate error message if the input file is missing or cannot be found.

Additionally, the code includes generic error handling for csv.Error during parsing. If any error occurs while parsing the CSV file, it logs a "CSV parsing error" with the line number and the exception message.

These error handling mechanisms help improve the robustness of the code by gracefully handling various invalid input scenarios and preventing crashes or unexpected behavior.
