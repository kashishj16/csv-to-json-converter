import os
from dotenv import load_dotenv
from app.config.database import Database
from app.services.csv_parser import CSVParser
from app.services.user_service import UserService
from app.utils.age_distribution import AgeDistribution

load_dotenv()

def main():
    """Main application entry point"""
    print("\n🚀 Starting CSV to JSON Converter API")
    print("="*50)
    
    # Get CSV file path from environment
    csv_file_path = os.getenv('CSV_FILE_PATH', './data/users.csv')
    print(f"📁 CSV File: {csv_file_path}\n")
    
    # Initialize database
    db = Database()
    
    if not db.connect():
        print("❌ Failed to connect to database. Exiting...")
        return
    
    if not db.create_table():
        print("❌ Failed to create table. Exiting...")
        db.close()
        return
    
    # Parse CSV file
    print("\n📖 Parsing CSV file...")
    records = CSVParser.parse_csv_file(csv_file_path)
    
    if not records:
        print("❌ No records found. Exiting...")
        db.close()
        return
    
    # Process records
    print("\n⚙️  Processing records...")
    processed_users = UserService.process_records(records)
    
    if not processed_users:
        print("❌ No valid records to insert. Exiting...")
        db.close()
        return
    
    # Insert into database
    print("\n💾 Inserting records into database...")
    if db.insert_users_batch(processed_users):
        print(f"✅ Successfully inserted {len(processed_users)} records")
    else:
        print("❌ Failed to insert records")
        db.close()
        return
    
    # Calculate age distribution
    print("\n📊 Calculating age distribution...")
    ages = db.get_all_ages()
    distribution = AgeDistribution.calculate_distribution(ages)
    AgeDistribution.print_report(distribution)
    
    # Close database connection
    db.close()
    
    print("✅ Process completed successfully!\n")

if __name__ == "__main__":
    main()