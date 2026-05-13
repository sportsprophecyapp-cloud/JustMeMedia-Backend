import csv
import os
import sys
from database import add_lead, init_db

def load_prospects(csv_file_path):
    if not os.path.exists(csv_file_path):
        print(f"Error: File not found at {csv_file_path}")
        return

    print(f"Loading prospects from {csv_file_path}...")
    
    loaded_count = 0
    duplicate_count = 0
    skipped_count = 0

    with open(csv_file_path, mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        
        # Check for required headers (flexible naming)
        headers = [h.lower().strip() for h in reader.fieldnames]
        
        for row in reader:
            # Clean up keys to be lowercase/stripped
            clean_row = {k.lower().strip(): v for k, v in row.items()}
            
            company_name = clean_row.get('business_name') or clean_row.get('company_name') or clean_row.get('company')
            contact_email = clean_row.get('email')
            website = clean_row.get('website')
            contact_name = clean_row.get('contact_name') or clean_row.get('name', "")
            industry = clean_row.get('industry', "")
            city = clean_row.get('city', "")
            
            # Basic validation
            if not company_name or not contact_email or not website:
                print(f"Skipping row with missing data: {clean_row}")
                skipped_count += 1
                continue
            
            # Practice areas / focus - combining industry and city for now
            practice_areas = f"{industry} in {city}" if industry and city else industry or city
            
            # add_lead returns nothing, but it prints "Added lead" or "Lead already exists"
            # We can capture that or just rely on the database's UNIQUE constraint
            # For this script, we'll just call it and assume database handles duplicates
            add_lead(
                company_name=company_name,
                contact_name=contact_name,
                contact_email=contact_email,
                website=website,
                practice_areas=practice_areas
            )
            loaded_count += 1

    print("\n--- Load Summary ---")
    print(f"Total rows processed: {loaded_count + skipped_count}")
    print(f"Successful loads/attempts: {loaded_count}")
    print(f"Skipped due to missing data: {skipped_count}")
    print("Check the terminal output above for any 'Lead already exists' messages from the database.")

if __name__ == "__main__":
    init_db()
    if len(sys.argv) < 2:
        print("Usage: python prospect_loader.py <path_to_csv>")
    else:
        load_prospects(sys.argv[1])
