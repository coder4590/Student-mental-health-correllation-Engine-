import sqlite3
import pandas as pd
import numpy as np

DB_NAME = "/home/farhan/Desktop/All Programming Folders and Files/4rth semester project/data/processed/mindguard_full.db"


def clean_data():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    print("=" * 60)
    print("DATA CLEANING — STUDENT MENTAL HEALTH")
    print("=" * 60)

    print("\n[1] MISSING VALUES CHECK & REMOVAL")
    cursor.execute("SELECT COUNT(*) FROM mental_health_raw")
    total_before = cursor.fetchone()[0]
    print(f"  Rows before cleaning: {total_before}")

    cursor.execute("PRAGMA table_info(mental_health_raw)")
    null_rows_deleted = 0
    for col in cursor.fetchall():
        col_name = col[1]
        safe_name = col_name.replace('"', '""')
        cursor.execute(f'SELECT COUNT(*) FROM mental_health_raw WHERE "{safe_name}" IS NULL')
        nulls = cursor.fetchone()[0]
        if nulls > 0:
            print(f"  Deleting {nulls} rows with NULL in: {col_name[:60]}...")
            cursor.execute(f'DELETE FROM mental_health_raw WHERE "{safe_name}" IS NULL')
            null_rows_deleted += nulls

    cursor.execute("SELECT COUNT(*) FROM mental_health_raw")
    total_after_nulls = cursor.fetchone()[0]
    print(f"  Rows after removing NULLs: {total_after_nulls}")

    print("\n[2] DUPLICATE CHECK & REMOVAL")
    cursor.execute("PRAGMA table_info(mental_health_raw)")
    all_cols = [f'"{col[1].replace(chr(34), chr(34)+chr(34))}"' for col in cursor.fetchall() if col[1] != 'id']
    all_cols_str = ", ".join(all_cols)

    cursor.execute(f"""
        SELECT {all_cols_str}, COUNT(*) as cnt
        FROM mental_health_raw
        GROUP BY {all_cols_str}
        HAVING cnt > 1
    """)
    dup_groups = cursor.fetchall()
    print(f"  Duplicate groups found: {len(dup_groups)}")

    if dup_groups:
        cursor.execute("""
            DELETE FROM mental_health_raw
            WHERE rowid NOT IN (
                SELECT MIN(rowid)
                FROM mental_health_raw
                GROUP BY """ + all_cols_str + """
            )
        """)
        deleted_dupes = total_after_nulls - cursor.execute("SELECT COUNT(*) FROM mental_health_raw").fetchone()[0]
        print(f"  Duplicate rows removed: {deleted_dupes}")

    cursor.execute("SELECT COUNT(*) FROM mental_health_raw")
    total_after_dupes = cursor.fetchone()[0]
    print(f"  Rows after removing duplicates: {total_after_dupes}")

    print("\n[3] DATA QUALITY CHECKS")
    print("\n  3a. Removing 'Invalid Score' and 'None' from target")
    cursor.execute("""
        DELETE FROM mental_health_raw 
        WHERE "Depression Level (PHQ-9 items)" = 'Invalid Score'
           OR "Depression Level (PHQ-9 items)" = 'None'
           OR "Depression Level (PHQ-9 items)" IS NULL
    """)
    cursor.execute("SELECT COUNT(*) FROM mental_health_raw")
    print(f"  Rows after target cleaning: {cursor.fetchone()[0]}")

    print("\n  3b. Trimming whitespace from text columns")
    text_cols = [
        'Relationship Status',
        'Academic Status',
        'Social Economic Status (আর্থ-সামাজিক অবস্থা)',
    ]
    for col in text_cols:
        safe_col = col.replace('"', '""')
        cursor.execute(f'UPDATE mental_health_raw SET "{safe_col}" = TRIM("{safe_col}")')
    print(f"  Trimmed whitespace from: {len(text_cols)} columns")

    print("\n  3c. Fixing typos in categorical columns")
    cursor.execute("""
        UPDATE mental_health_raw 
        SET "Social Economic Status (আর্থ-সামাজিক অবস্থা)" = CASE 
            WHEN "Social Economic Status (আর্থ-সামাজিক অবস্থা)" = 'Lowe-Middle' THEN 'Lower-Middle'
            WHEN "Social Economic Status (আর্থ-সামাজিক অবস্থা)" = 'Uper-Middle' THEN 'Upper-Middle'
            WHEN "Social Economic Status (আর্থ-সামাজিক অবস্থা)" = 'lower' THEN 'Lower'
            ELSE "Social Economic Status (আর্থ-সামাজিক অবস্থা)"
        END
    """)
    print(f"  Fixed typos in: social_economic_status")

    cursor.execute("""
        UPDATE mental_health_raw 
        SET "What is your average nightly sleep duration in hours?(আপনার রাতের ঘুমের গড় সময়কাল কত ঘন্টার মধ্যে?)" = CASE
            WHEN "What is your average nightly sleep duration in hours?(আপনার রাতের ঘুমের গড় সময়কাল কত ঘন্টার মধ্যে?)" = 'low 5 Hours' THEN 'Below 5 Hours'
            ELSE "What is your average nightly sleep duration in hours?(আপনার রাতের ঘুমের গড় সময়কাল কত ঘন্টার মধ্যে?)"
        END
    """)
    print(f"  Fixed typos in: sleep_duration_hours")

    cursor.execute('SELECT DISTINCT "Social Economic Status (আর্থ-সামাজিক অবস্থা)" FROM mental_health_raw')
    ses_values = [r[0] for r in cursor.fetchall()]
    print(f"  SES values after fix: {ses_values}")

    cursor.execute('SELECT DISTINCT "What is your average nightly sleep duration in hours?(আপনার রাতের ঘুমের গড় সময়কাল কত ঘন্টার মধ্যে?)" FROM mental_health_raw')
    sleep_values = [r[0] for r in cursor.fetchall()]
    print(f"  Sleep values after fix: {sleep_values}")

    print("\n[4] OUTLIER CHECK — AGE")
    cursor.execute('SELECT AVG("Age") FROM mental_health_raw WHERE "Age" IS NOT NULL')
    mean_age = cursor.fetchone()[0]
    print(f"  Mean age: {mean_age:.1f}")

    cursor.execute('SELECT "Age", COUNT(*) FROM mental_health_raw WHERE "Age" IS NOT NULL GROUP BY "Age" ORDER BY "Age"')
    age_dist = cursor.fetchall()
    print(f"  Age distribution:")
    for age, cnt in age_dist:
        flag = " ← OUTLIER" if abs(age - mean_age) > 4 else ""
        print(f"    Age {age}: {cnt} students{flag}")

    cursor.execute("""
        SELECT COUNT(*) FROM mental_health_raw 
        WHERE "Age" < ? OR "Age" > ?
    """, (mean_age - 4, mean_age + 4))
    outlier_count = cursor.fetchone()[0]
    print(f"  Students outside ±4 years of mean: {outlier_count}")
    print(f"  Action: KEPT (real data, not errors). Document in report.")

    print("\n[5] SELECTING REQUIRED 20 COLUMNS")
    cursor.execute("DROP TABLE IF EXISTS students_clean")

    cursor.execute("""
        CREATE TABLE students_clean AS
        SELECT 
            "Gender" AS gender,
            "Relationship Status" AS relationship_status,
            "Age" AS age,
            "Academic Status" AS academic_status,
            "Do you work as well as Study?(পড়াশোনার পাশাপাশি চাকরি করেন?)" AS work_and_study,
            "Residential Area (আবাসিক এলাকা)" AS residential_area,
            "Social Economic Status (আর্থ-সামাজিক অবস্থা)" AS social_economic_status,
            "Do you feel any financial pressure?(আপনি কি কোনো আর্থিক চাপ অনুভব করছেন?)" AS financial_pressure,
            "Does the participant have any debts?(অংশগ্রহণকারী কি কোন ঋণ আছে?)" AS has_debt,
            "Are you satisfied with your current living environment? (আপনি কি আপনার বর্তমান বসবাসের পরিবেশে সন্তুষ্ট?)" AS living_environment_satisfaction,
            "Have you recently lost someone close to you? (আপনি সম্প্রতি আপনার কাছের কাউকে হারিয়েছেন কি না )" AS recent_loss,
            "You are actively engaging as a participant in physical exertion.(আপনি সক্রিয়ভাবে শারীরিক পরিশ্রমে অংশগ্রহণকারী হিসাবে জড়িত।)" AS physical_activity,
            'Are you afflicted by any significant ailments?(আপনি কি কোনও গুরুতর অসুখে ভুগছেন?")' AS chronic_illness,
            "Are you currently on any prescribed medication?(আপনি কি বর্তমানে কোনও ওষুধ সেবন করছেন?)" AS medication,
            "Are you accustomed to smoking?(আপনি কি ধূমপানে অভ্যস্ত?)" AS smoking,
            "Do you consume alcoholic beverages?(আপনি কি অ্যালকোহলযুক্ত পানীয় গ্রহণ করেন?)" AS alcohol,
            "What is your average nightly sleep duration in hours?(আপনার রাতের ঘুমের গড় সময়কাল কত ঘন্টার মধ্যে?)" AS sleep_duration_hours,
            "Average hours that the participant spends in social network (in a day)(অংশগ্রহণকারী সামাজিক নেটওয়ার্কে ব্যয় করে এমন গড় ঘন্টা (এক দিনে))" AS social_media_hours_daily,
            "Do you have current workload or academic demands?(আপনার কি বর্তমান কাজের চাপ বা একাডেমিক চাহিদা রয়েছে?)" AS academic_work_demands,
            "Depression Level (PHQ-9 items)" AS depression_phq9
        FROM mental_health_raw
    """)

    cursor.execute("SELECT COUNT(*) FROM students_clean")
    final_rows = cursor.fetchone()[0]
    cursor.execute("PRAGMA table_info(students_clean)")
    final_cols = len(cursor.fetchall())
    print(f"  Rows in 'students_clean': {final_rows}")
    print(f"  Columns in 'students_clean': {final_cols}")

    print("\n  REMOVED FEATURES EXPLANATION:")
    print('  "We removed 43 features from the original 63 columns.')
    print('   These removed features are individual scale items from BDI-II (20 items),')
    print('   CES-D (20 items), PHQ-9 (9 items), and UCLA-8 (8 items).')
    print('   These items are the components that SUM UP to create the depression and')
    print('   loneliness scores. Including them as features while predicting the total')
    print('   score would cause direct data leakage — the model would learn that')
    print('   feeling melancholic + feeling hopeless = depression, which is tautology,')
    print('   not prediction. Only pre-diagnostic, screening-level features are kept."')

    df_clean = pd.read_sql_query("SELECT * FROM students_clean", conn)

    conn.commit()
    conn.close()

    print(f"\n{'=' * 60}")
    print("DATA CLEANING COMPLETE")
    print(f"{'=' * 60}")
    print(f"  Final table: students_clean")
    print(f"  Final rows: {final_rows}")
    print(f"  Final columns: {final_cols}")
    print(f"  Database: {DB_NAME}")

    return df_clean



clean_data()