# Assumptions and Design Decisions

## Technology Stack
- **Language:** Python 3.x (instead of Node.js as specified)
- **Reason:** Aligns with my primary tech stack and demonstrates production-ready Python skills
- **Database:** SQLite (instead of PostgreSQL)
- **Reason:** Simpler setup, portable, zero configuration, perfect for demonstration

## CSV Parsing
- First line is always headers (as specified)
- All sub-properties of complex objects are grouped together
- Empty lines in CSV are skipped
- Values with commas can be quoted

## Data Processing
- `name` = firstName + lastName with space
- Invalid/missing ages default to 0
- Empty `additional_info` stored as NULL (not empty JSON)
- Batch insert used for performance with large datasets

## Error Handling
- Malformed CSV rows are logged and skipped
- Database errors rollback transactions
- File not found errors handled gracefully

## Performance
- Batch inserts for efficiency
- Single transaction for all records
- Tested with 1000+ records successfully