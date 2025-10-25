class CSVParser:
    """Custom CSV parser without using external libraries"""
    
    @staticmethod
    def parse_csv_line(line):
        """Parse a single CSV line handling quoted values"""
        values = []
        current_value = ''
        in_quotes = False
        
        for char in line:
            if char == '"':
                in_quotes = not in_quotes
            elif char == ',' and not in_quotes:
                values.append(current_value.strip())
                current_value = ''
            else:
                current_value += char
        
        # Add the last value
        values.append(current_value.strip())
        return values
    
    @staticmethod
    def build_nested_object(key, value):
        """Build nested object from dot-separated key"""
        keys = key.split('.')
        
        # Build from innermost to outermost
        result = value
        for k in reversed(keys):
            result = {k: result}
        
        return result
    
    @staticmethod
    def merge_nested_objects(obj1, obj2):
        """Deep merge two nested objects"""
        for key, value in obj2.items():
            if key in obj1:
                if isinstance(obj1[key], dict) and isinstance(value, dict):
                    CSVParser.merge_nested_objects(obj1[key], value)
                else:
                    obj1[key] = value
            else:
                obj1[key] = value
        return obj1
    
    @staticmethod
    def parse_csv_file(file_path):
        """Parse entire CSV file and return list of objects"""
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                lines = file.readlines()
            
            if not lines:
                print("❌ CSV file is empty")
                return []
            
            # Parse header (first line)
            headers = CSVParser.parse_csv_line(lines[0])
            headers = [h.strip() for h in headers]
            
            print(f"📋 Found {len(headers)} columns: {headers}")
            
            # Parse data rows
            records = []
            for i, line in enumerate(lines[1:], start=2):
                line = line.strip()
                if not line:
                    continue
                
                values = CSVParser.parse_csv_line(line)
                
                if len(values) != len(headers):
                    print(f"⚠️  Row {i}: Column count mismatch (expected {len(headers)}, got {len(values)})")
                    continue
                
                # Build nested object
                record = {}
                for header, value in zip(headers, values):
                    nested_obj = CSVParser.build_nested_object(header, value)
                    record = CSVParser.merge_nested_objects(record, nested_obj)
                
                records.append(record)
            
            print(f"✅ Parsed {len(records)} records from CSV")
            return records
        
        except FileNotFoundError:
            print(f"❌ File not found: {file_path}")
            return []
        except Exception as e:
            print(f"❌ CSV parsing failed: {e}")
            return []