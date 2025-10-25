class UserService:
    """Service to process user records"""
    
    @staticmethod
    def process_record(record):
        """Process a single record and extract required fields"""
        try:
            # Extract mandatory fields
            first_name = record.get('name', {}).get('firstName', '')
            last_name = record.get('name', {}).get('lastName', '')
            full_name = f"{first_name} {last_name}".strip()
            
            age_str = str(record.get('age', '0'))
            age = int(age_str) if age_str.isdigit() else 0
            
            # Extract address (all properties under 'address')
            address = record.get('address', None)
            
            # Extract additional info (everything except name, age, address)
            additional_info = {}
            for key, value in record.items():
                if key not in ['name', 'age', 'address']:
                    additional_info[key] = value
            
            # Return None for additional_info if empty
            if not additional_info:
                additional_info = None
            
            return {
                'name': full_name,
                'age': age,
                'address': address,
                'additional_info': additional_info
            }
        
        except Exception as e:
            print(f"❌ Record processing failed: {e}")
            return None
    
    @staticmethod
    def process_records(records):
        """Process multiple records"""
        processed = []
        for record in records:
            processed_record = UserService.process_record(record)
            if processed_record:
                processed.append(processed_record)
        
        print(f"✅ Processed {len(processed)} records")
        return processed