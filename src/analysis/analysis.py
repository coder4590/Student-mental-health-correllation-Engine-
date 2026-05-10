import sqlite3
import pandas as pd
import numpy as np

DB_NAME = "mindguard_full.db"

def analysis_data():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    print("=" * 60)
    print("FULL DATA ANALYSIS — STUDENT MENTAL HEALTH")
    print("=" * 60)

    print("\n[1] DATABASE OVERVIEW")
    cursor.execute("SELECT COUNT(*) FROM mental_health_raw")
    total_rows = cursor.fetchone()[0]
    cursor.execute("PRAGMA table_info(mental_health_raw)")
    total_cols = len(cursor.fetchall())
    print(f"  Total rows: {total_rows}")
    print(f"  Total columns: {total_cols}")

    print("\n[2] TARGET VARIABLE — DEPRESSION LEVEL DISTRIBUTION")
    cursor.execute("""
        SELECT "Depression Level (PHQ-9 items)", 
            COUNT(*) as count,
            ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM mental_health_raw), 2) as percentage
        FROM mental_health_raw 
        GROUP BY "Depression Level (PHQ-9 items)"
        ORDER BY count DESC
    """)
    print(f"  {'Target Value':<30} {'Count':<8} {'Percentage'}")
    print(f"  {'-'*30} {'-'*8} {'-'*10}")
    for row in cursor.fetchall():
        print(f"  {str(row[0]):<30} {row[1]:<8} {row[2]}%")

    print("\n[3] MISSING VALUES — ALL COLUMNS WITH NULLS")
    cursor.execute("PRAGMA table_info(mental_health_raw)")
    null_report = []
    for col in cursor.fetchall():
        col_name = col[1]
        safe_name = col_name.replace('"', '""')
        cursor.execute(f'SELECT COUNT(*) FROM mental_health_raw WHERE "{safe_name}" IS NULL')
        nulls = cursor.fetchone()[0]
        if nulls > 0:
            null_report.append((col_name, nulls, round(nulls*100/total_rows, 2)))

    if null_report:
        print(f"  {'Column':<50} {'NULLs':<8} {'% Missing'}")
        print(f"  {'-'*50} {'-'*8} {'-'*10}")
        for col_name, nulls, pct in null_report:
            print(f"  {col_name[:50]:<50} {nulls:<8} {pct}%")
    else:
        print("  No missing values found")

    print("\n[4] DUPLICATE ANALYSIS")
    cursor.execute("""
        SELECT "Gender", "Age", "Academic Status", "Depression Level (PHQ-9 items)", 
            COUNT(*) as copies
        FROM mental_health_raw
        WHERE "Gender" IS NOT NULL 
        AND "Age" IS NOT NULL 
        AND "Academic Status" IS NOT NULL
        GROUP BY "Gender", "Age", "Academic Status", "Depression Level (PHQ-9 items)"
        HAVING copies > 1
        ORDER BY copies DESC
    """)
    dupes = cursor.fetchall()
    print(f"  Total duplicate groups: {len(dupes)}")
    if dupes:
        print(f"\n  {'Gender':<10} {'Age':<6} {'Academic':<12} {'Depression':<30} {'Copies'}")
        print(f"  {'-'*10} {'-'*6} {'-'*12} {'-'*30} {'-'*6}")
        for row in dupes[:15]:
            print(f"  {row[0]:<10} {row[1]:<6} {row[2]:<12} {row[3]:<30} {row[4]}")

    print("\n[5] DEMOGRAPHIC BREAKDOWN")
    print("\n  5a. Gender Distribution")
    cursor.execute("""
        SELECT "Gender", COUNT(*) as count,
            ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM mental_health_raw WHERE "Gender" IS NOT NULL), 2) as pct
        FROM mental_health_raw 
        WHERE "Gender" IS NOT NULL
        GROUP BY "Gender"
    """)
    for row in cursor.fetchall():
        print(f"  {row[0]:<10} {row[1]:<6} ({row[2]}%)")

    print("\n  5b. Age Group Distribution")
    cursor.execute("""
        SELECT 
            CASE 
                WHEN "Age" BETWEEN 18 AND 20 THEN '18-20'
                WHEN "Age" BETWEEN 21 AND 23 THEN '21-23'
                WHEN "Age" BETWEEN 24 AND 26 THEN '24-26'
                WHEN "Age" >= 27 THEN '27+'
                ELSE 'Unknown'
            END as age_group,
            COUNT(*) as count,
            ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM mental_health_raw WHERE "Age" IS NOT NULL), 2) as pct
        FROM mental_health_raw
        WHERE "Age" IS NOT NULL
        GROUP BY age_group
        ORDER BY age_group
    """)
    for row in cursor.fetchall():
        print(f"  {row[0]:<10} {row[1]:<6} ({row[2]}%)")

    print("\n  5c. Academic Status Distribution")
    cursor.execute("""
        SELECT TRIM("Academic Status") as academic_status, COUNT(*) as count,
            ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM mental_health_raw WHERE "Academic Status" IS NOT NULL), 2) as pct
        FROM mental_health_raw
        WHERE "Academic Status" IS NOT NULL
        GROUP BY TRIM("Academic Status")
        ORDER BY count DESC
    """)
    for row in cursor.fetchall():
        print(f"  {row[0]:<15} {row[1]:<6} ({row[2]}%)")

    print("\n  5d. Relationship Status Distribution")
    cursor.execute("""
        SELECT TRIM("Relationship Status") as rel_status, COUNT(*) as count
        FROM mental_health_raw
        WHERE "Relationship Status" IS NOT NULL
        GROUP BY TRIM("Relationship Status")
        ORDER BY count DESC
    """)
    for row in cursor.fetchall():
        print(f"  {row[0]:<20} {row[1]}")

    print("\n[6] LIFESTYLE FACTORS ANALYSIS")

    print("\n  6a. Sleep Duration vs Depression")
    cursor.execute("""
        SELECT "What is your average nightly sleep duration in hours?(আপনার রাতের ঘুমের গড় সময়কাল কত ঘন্টার মধ্যে?)" as sleep,
            "Depression Level (PHQ-9 items)" as depression,
            COUNT(*) as count
        FROM mental_health_raw
        WHERE sleep IS NOT NULL AND depression IS NOT NULL 
        AND depression != 'Invalid Score'
        GROUP BY sleep, depression
        ORDER BY sleep, depression
    """)
    current_sleep = None
    for row in cursor.fetchall():
        if row[0] != current_sleep:
            print(f"\n  Sleep: {row[0]}")
            current_sleep = row[0]
        print(f"    {row[1]:<30} {row[2]}")

    print("\n  6b. Social Media Usage vs Depression")
    cursor.execute("""
        SELECT "Average hours that the participant spends in social network (in a day)(অংশগ্রহণকারী সামাজিক নেটওয়ার্কে ব্যয় করে এমন গড় ঘন্টা (এক দিনে))" as social,
            "Depression Level (PHQ-9 items)" as depression,
            COUNT(*) as count
        FROM mental_health_raw
        WHERE social IS NOT NULL AND depression IS NOT NULL 
        AND depression != 'Invalid Score'
        GROUP BY social, depression
        ORDER BY social, depression
    """)
    current_social = None
    for row in cursor.fetchall():
        if row[0] != current_social:
            print(f"\n  Social Media: {row[0]}")
            current_social = row[0]
        print(f"    {row[1]:<30} {row[2]}")

    print("\n  6c. Physical Activity vs Depression")
    cursor.execute("""
        SELECT "You are actively engaging as a participant in physical exertion.(আপনি সক্রিয়ভাবে শারীরিক পরিশ্রমে অংশগ্রহণকারী হিসাবে জড়িত।)" as activity,
            "Depression Level (PHQ-9 items)" as depression,
            COUNT(*) as count
        FROM mental_health_raw
        WHERE activity IS NOT NULL AND depression IS NOT NULL 
        AND depression != 'Invalid Score'
        GROUP BY activity, depression
        ORDER BY activity, depression
    """)
    for row in cursor.fetchall():
        print(f"  {row[0]:<10} | {row[1]:<30} | {row[2]}")

    print("\n[7] FINANCIAL & SOCIOECONOMIC ANALYSIS")

    print("\n  7a. Financial Pressure vs Depression")
    cursor.execute("""
        SELECT "Do you feel any financial pressure?(আপনি কি কোনো আর্থিক চাপ অনুভব করছেন?)" as finance,
            "Depression Level (PHQ-9 items)" as depression,
            COUNT(*) as count,
            ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER(PARTITION BY "Do you feel any financial pressure?(আপনি কি কোনো আর্থিক চাপ অনুভব করছেন?)"), 2) as pct
        FROM mental_health_raw
        WHERE finance IS NOT NULL AND depression IS NOT NULL 
        AND depression != 'Invalid Score'
        GROUP BY finance, depression
        ORDER BY finance, count DESC
    """)
    current_fin = None
    for row in cursor.fetchall():
        if row[0] != current_fin:
            print(f"\n  Financial Pressure = {row[0]}")
            current_fin = row[0]
        print(f"    {row[1]:<30} {row[2]:<5} ({row[3]}%)")

    print("\n  7b. Social Economic Status vs Depression")
    cursor.execute("""
        SELECT "Social Economic Status (আর্থ-সামাজিক অবস্থা)" as ses,
            "Depression Level (PHQ-9 items)" as depression,
            COUNT(*) as count
        FROM mental_health_raw
        WHERE ses IS NOT NULL AND depression IS NOT NULL 
        AND depression != 'Invalid Score'
        GROUP BY ses, depression
        ORDER BY ses, depression
    """)
    current_ses = None
    for row in cursor.fetchall():
        if row[0] != current_ses:
            print(f"\n  SES: {row[0]}")
            current_ses = row[0]
        print(f"    {row[1]:<30} {row[2]}")

    print("\n[8] HEALTH FACTORS ANALYSIS")

    print("\n  8a. Chronic Illness vs Depression")
    cursor.execute("""
        SELECT "Are you afflicted by any significant ailments?(আপনি কি কোনও গুরুতর অসুখে ভুগছেন?"")" as illness,
            "Depression Level (PHQ-9 items)" as depression,
            COUNT(*) as count
        FROM mental_health_raw
        WHERE illness IS NOT NULL AND depression IS NOT NULL 
        AND depression != 'Invalid Score'
        GROUP BY illness, depression
        ORDER BY illness, depression
    """)
    for row in cursor.fetchall():
        print(f"  {row[0]:<10} | {row[1]:<30} | {row[2]}")

    print("\n  8b. Medication vs Depression")
    cursor.execute("""
        SELECT "Are you currently on any prescribed medication?(আপনি কি বর্তমানে কোনও ওষুধ সেবন করছেন?)" as med,
            "Depression Level (PHQ-9 items)" as depression,
            COUNT(*) as count
        FROM mental_health_raw
        WHERE med IS NOT NULL AND depression IS NOT NULL 
        AND depression != 'Invalid Score'
        GROUP BY med, depression
        ORDER BY med, depression
    """)
    for row in cursor.fetchall():
        print(f"  {row[0]:<10} | {row[1]:<30} | {row[2]}")

    print("\n[9] CROSS-TABULATION — Gender × Academic Status × Depression")
    cursor.execute("""
        SELECT "Gender", TRIM("Academic Status") as acad, 
            "Depression Level (PHQ-9 items)" as dep,
            COUNT(*) as count
        FROM mental_health_raw
        WHERE "Gender" IS NOT NULL AND "Academic Status" IS NOT NULL 
        AND "Depression Level (PHQ-9 items)" IS NOT NULL
        AND "Depression Level (PHQ-9 items)" != 'Invalid Score'
        GROUP BY "Gender", acad, dep
        ORDER BY "Gender", acad, count DESC
    """)
    print(f"  {'Gender':<10} {'Academic':<12} {'Depression':<30} {'Count'}")
    print(f"  {'-'*10} {'-'*12} {'-'*30} {'-'*6}")
    for row in cursor.fetchall():
        print(f"  {row[0]:<10} {row[1]:<12} {row[2]:<30} {row[3]}")

    print("\n[10] SUMMARY STATISTICS — AGE")
    cursor.execute("""
        SELECT 
            COUNT(*) as total,
            ROUND(AVG("Age"), 2) as mean,
            MIN("Age") as min,
            MAX("Age") as max
        FROM mental_health_raw
        WHERE "Age" IS NOT NULL
    """)
    row = cursor.fetchone()
    print(f"  Count: {row[0]}")
    print(f"  Mean: {row[1]}")
    print(f"  Min: {row[2]}")
    print(f"  Max: {row[3]}")

    cursor.execute("""
        SELECT "Age" FROM mental_health_raw 
        WHERE "Age" IS NOT NULL 
        GROUP BY "Age" 
        ORDER BY COUNT(*) DESC 
        LIMIT 1
    """)
    mode = cursor.fetchone()
    print(f"  Mode: {mode[0]}")

    print("\n[11] RISK FACTOR SUMMARY")
    print(f"  {'Risk Factor':<35} {'Depressed':<12} {'Not Depressed':<15} {'Risk Ratio'}")
    print(f"  {'-'*35} {'-'*12} {'-'*15} {'-'*10}")

    risk_checks = [
        ("Financial Pressure = Yes", 
         '"Do you feel any financial pressure?(আপনি কি কোনো আর্থিক চাপ অনুভব করছেন?)" = \'Yes\''),
        ("Physical Activity = No",
         '"You are actively engaging as a participant in physical exertion.(আপনি সক্রিয়ভাবে শারীরিক পরিশ্রমে অংশগ্রহণকারী হিসাবে জড়িত।)" = \'No\''),
        ("Sleep < 6 Hours",
         '"What is your average nightly sleep duration in hours?(আপনার রাতের ঘুমের গড় সময়কাল কত ঘন্টার মধ্যে?)" IN (\'Below 5 Hours\', \'5 Hours\')'),
        ("Social Media > 8 hrs/day",
         '"Average hours that the participant spends in social network (in a day)(অংশগ্রহণকারী সামাজিক নেটওয়ার্কে ব্যয় করে এমন গড় ঘন্টা (এক দিনে))" IN (\'8–10 hours a day\', \'More than 10 hours a day\')'),
    ]

    for label, condition in risk_checks:
        cursor.execute(f"""
            SELECT 
                SUM(CASE WHEN "Depression Level (PHQ-9 items)" IN ('Severe Depression', 'Moderate Severe Depression') THEN 1 ELSE 0 END) as depressed,
                SUM(CASE WHEN "Depression Level (PHQ-9 items)" IN ('Minimal Depression', 'Mild Depression', 'Moderate Depression') THEN 1 ELSE 0 END) as not_depressed
            FROM mental_health_raw
            WHERE {condition}
            AND "Depression Level (PHQ-9 items)" IS NOT NULL
            AND "Depression Level (PHQ-9 items)" != 'Invalid Score'
        """)
        dep, not_dep = cursor.fetchone()
        ratio = round(dep / max(not_dep, 1), 2)
        print(f"  {label:<35} {dep:<12} {not_dep:<15} {ratio}")

    conn.close()

    print(f"\n{'=' * 60}")
    print("FULL DATA ANALYSIS COMPLETE")
    print(f"{'=' * 60}")


def clean_data():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    print("=" * 60)
    print("DATA CLEANING — STUDENT MENTAL HEALTH")
    print("=" * 60)

    # ============================================================
    # 1. CHECK AND REMOVE MISSING VALUES
    # ============================================================
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

    # ============================================================
    # 2. CHECK AND REMOVE DUPLICATE ROWS
    # ============================================================
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

    # ============================================================
    # 3. DATA QUALITY CHECKS
    # ============================================================
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

    # Verify fixes
    cursor.execute('SELECT DISTINCT "Social Economic Status (আর্থ-সামাজিক অবস্থা)" FROM mental_health_raw')
    ses_values = [r[0] for r in cursor.fetchall()]
    print(f"  SES values after fix: {ses_values}")

    cursor.execute('SELECT DISTINCT "What is your average nightly sleep duration in hours?(আপনার রাতের ঘুমের গড় সময়কাল কত ঘন্টার মধ্যে?)" FROM mental_health_raw')
    sleep_values = [r[0] for r in cursor.fetchall()]
    print(f"  Sleep values after fix: {sleep_values}")

    # ============================================================
    # 4. OUTLIER CHECK
    # ============================================================
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

    # ============================================================
    # 5. SELECT ONLY REQUIRED 20 COLUMNS + CREATE CLEAN TABLE
    # ============================================================
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

    conn.commit()
    conn.close()

    print(f"\n{'=' * 60}")
    print("DATA CLEANING COMPLETE")
    print(f"{'=' * 60}")
    print(f"  Final table: students_clean")
    print(f"  Final rows: {final_rows}")
    print(f"  Final columns: {final_cols}")
    print(f"  Database: {DB_NAME}")



if __name__ == "__main__":
    analysis_data()
    clean_data()