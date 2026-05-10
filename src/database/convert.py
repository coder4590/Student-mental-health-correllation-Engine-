import sqlite3
import pandas as pd
import os

CSV_FILE = "data.csv"
DB_NAME = "mindguard_full.db"

print(f"Reading {CSV_FILE}...")
df = pd.read_csv(CSV_FILE)
print(f"CSV rows: {len(df)}")
print(f"CSV columns: {len(df.columns)}")

if os.path.exists(DB_NAME):
    os.remove(DB_NAME)

conn = sqlite3.connect(DB_NAME)

# DUMP ALL 63 COLUMNS — NO REMOVAL, NO RENAMING, NO CLEANING
df.to_sql('mental_health_raw', conn, if_exists='replace', index=True, index_label='id')

# VERIFY
cursor = conn.cursor()
cursor.execute("SELECT COUNT(*) FROM mental_health_raw")
db_rows = cursor.fetchone()[0]

cursor.execute("PRAGMA table_info(mental_health_raw)")
db_cols = len(cursor.fetchall())

print(f"\nDatabase: {DB_NAME}")
print(f"Table: mental_health_raw")
print(f"Rows: {db_rows}")
print(f"Columns: {db_cols}")

if db_rows == len(df) and db_cols == len(df.columns) + 1:  # +1 for id
    print("✅ All 63 columns imported successfully")
else:
    print("❌ Mismatch — check the import")

conn.close()