import os
import sqlite3
import json
from dotenv import load_dotenv

load_dotenv()

class Database:
    def __init__(self):
        self.connection = None
        self.cursor = None
        self.db_path = os.getenv('DB_PATH', './database.db')
    
    def connect(self):
        """Establish database connection"""
        try:
            self.connection = sqlite3.connect(self.db_path)
            self.cursor = self.connection.cursor()
            print(f"✅ Database connected successfully: {self.db_path}")
            return True
        except Exception as e:
            print(f"❌ Database connection failed: {e}")
            return False
    
    def create_table(self):
        """Create users table if it doesn't exist"""
        try:
            create_table_query = """
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                age INTEGER NOT NULL,
                address TEXT,
                additional_info TEXT
            );
            """
            self.cursor.execute(create_table_query)
            self.connection.commit()
            print("✅ Table 'users' is ready")
            return True
        except Exception as e:
            print(f"❌ Table creation failed: {e}")
            return False
    
    def insert_user(self, name, age, address, additional_info):
        """Insert a single user record"""
        try:
            insert_query = """
            INSERT INTO users (name, age, address, additional_info)
            VALUES (?, ?, ?, ?)
            """
            self.cursor.execute(insert_query, (
                name,
                age,
                json.dumps(address) if address else None,
                json.dumps(additional_info) if additional_info else None
            ))
            return True
        except Exception as e:
            print(f"❌ Insert failed: {e}")
            return False
    
    def insert_users_batch(self, users):
        """Insert multiple users in a batch"""
        try:
            insert_query = """
            INSERT INTO users (name, age, address, additional_info)
            VALUES (?, ?, ?, ?)
            """
            data = [
                (
                    user['name'],
                    user['age'],
                    json.dumps(user['address']) if user.get('address') else None,
                    json.dumps(user['additional_info']) if user.get('additional_info') else None
                )
                for user in users
            ]
            self.cursor.executemany(insert_query, data)
            self.connection.commit()
            print(f"✅ Inserted {len(users)} users successfully")
            return True
        except Exception as e:
            self.connection.rollback()
            print(f"❌ Batch insert failed: {e}")
            return False
    
    def get_all_ages(self):
        """Fetch all ages from the database"""
        try:
            self.cursor.execute("SELECT age FROM users")
            ages = [row[0] for row in self.cursor.fetchall()]
            return ages
        except Exception as e:
            print(f"❌ Failed to fetch ages: {e}")
            return []
    
    def get_all_users(self):
        """Fetch all users from database"""
        try:
            self.cursor.execute("SELECT * FROM users")
            columns = [description[0] for description in self.cursor.description]
            users = []
            for row in self.cursor.fetchall():
                user = dict(zip(columns, row))
                # Parse JSON fields
                if user.get('address'):
                    user['address'] = json.loads(user['address'])
                if user.get('additional_info'):
                    user['additional_info'] = json.loads(user['additional_info'])
                users.append(user)
            return users
        except Exception as e:
            print(f"❌ Failed to fetch users: {e}")
            return []
    
    def clear_table(self):
        """Clear all data from users table"""
        try:
            self.cursor.execute("DELETE FROM users")
            self.connection.commit()
            print("✅ Table cleared successfully")
            return True
        except Exception as e:
            print(f"❌ Failed to clear table: {e}")
            return False
    
    def close(self):
        """Close database connection"""
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
        print("✅ Database connection closed")