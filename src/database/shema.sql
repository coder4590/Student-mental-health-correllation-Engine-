-- ============================================================
-- MINDGUARD DATABASE SCHEMA
-- Student Mental Health Prediction System
-- ============================================================

-- 1. RAW DATA TABLE (all 63 columns, untouched)
CREATE TABLE IF NOT EXISTS mental_health_raw (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    "Gender" TEXT,
    "Relationship Status" TEXT,
    "Age" REAL,
    "Academic Status" TEXT,
    "Do you work as well as Study?(পড়াশোনার পাশাপাশি চাকরি করেন?)" TEXT,
    "Residential Area (আবাসিক এলাকা)" TEXT,
    "Social Economic Status (আর্থ-সামাজিক অবস্থা)" TEXT,
    "Do you feel any financial pressure?(আপনি কি কোনো আর্থিক চাপ অনুভব করছেন?)" TEXT,
    "Does the participant have any debts?(অংশগ্রহণকারী কি কোন ঋণ আছে?)" TEXT,
    "Are you satisfied with your current living environment? (আপনি কি আপনার বর্তমান বসবাসের পরিবেশে সন্তুষ্ট?)" TEXT,
    "Have you recently lost someone close to you? (আপনি সম্প্রতি আপনার কাছের কাউকে হারিয়েছেন কি না )" TEXT,
    "You are actively engaging as a participant in physical exertion.(আপনি সক্রিয়ভাবে শারীরিক পরিশ্রমে অংশগ্রহণকারী হিসাবে জড়িত।)" TEXT,
    "Are you afflicted by any significant ailments?(আপনি কি কোনও গুরুতর অসুখে ভুগছেন?\")" TEXT,
    "Are you currently on any prescribed medication?(আপনি কি বর্তমানে কোনও ওষুধ সেবন করছেন?)" TEXT,
    "Are you accustomed to smoking?(আপনি কি ধূমপানে অভ্যস্ত?)" TEXT,
    "Do you consume alcoholic beverages?(আপনি কি অ্যালকোহলযুক্ত পানীয় গ্রহণ করেন?)" TEXT,
    "What is your average nightly sleep duration in hours?(আপনার রাতের ঘুমের গড় সময়কাল কত ঘন্টার মধ্যে?)" TEXT,
    "Average hours that the participant spends in social network (in a day)(অংশগ্রহণকারী সামাজিক নেটওয়ার্কে ব্যয় করে এমন গড় ঘন্টা (এক দিনে))" TEXT,
    "Do you have current workload or academic demands?(আপনার কি বর্তমান কাজের চাপ বা একাডেমিক চাহিদা রয়েছে?)" TEXT,
    "Depression Level (PHQ-9 items)" TEXT,
    -- BDI-II items (20 columns)
    -- CES-D items (20 columns)
    -- PHQ-9 items (9 columns)
    -- UCLA-8 items (8 columns)
    -- Remaining scale items omitted for brevity
);


-- 2. CLEAN TABLE (20 columns, no leakage, no NULLs, deduplicated)
CREATE TABLE IF NOT EXISTS students_clean (
    gender TEXT NOT NULL,
    relationship_status TEXT NOT NULL,
    age REAL NOT NULL,
    academic_status TEXT NOT NULL,
    work_and_study TEXT NOT NULL,
    residential_area TEXT NOT NULL,
    social_economic_status TEXT NOT NULL,
    financial_pressure TEXT NOT NULL,
    has_debt TEXT NOT NULL,
    living_environment_satisfaction TEXT NOT NULL,
    recent_loss TEXT NOT NULL,
    physical_activity TEXT NOT NULL,
    chronic_illness TEXT NOT NULL,
    medication TEXT NOT NULL,
    smoking TEXT NOT NULL,
    alcohol TEXT NOT NULL,
    sleep_duration_hours TEXT NOT NULL,
    social_media_hours_daily TEXT NOT NULL,
    academic_work_demands TEXT NOT NULL,
    depression_phq9 TEXT NOT NULL
);


-- 3. DEMOGRAPHICS TABLE (split for JOIN operations)
CREATE TABLE IF NOT EXISTS student_demographics (
    student_id INTEGER PRIMARY KEY,
    gender TEXT,
    age REAL,
    relationship_status TEXT,
    academic_status TEXT,
    work_and_study TEXT,
    residential_area TEXT,
    social_economic_status TEXT,
    financial_pressure TEXT,
    has_debt TEXT
);


-- 4. LIFESTYLE TABLE (split for JOIN operations)
CREATE TABLE IF NOT EXISTS student_lifestyle (
    student_id INTEGER PRIMARY KEY,
    living_environment_satisfaction TEXT,
    recent_loss TEXT,
    physical_activity TEXT,
    chronic_illness TEXT,
    medication TEXT,
    smoking TEXT,
    alcohol TEXT,
    sleep_duration_hours TEXT,
    social_media_hours_daily TEXT,
    academic_work_demands TEXT,
    depression_phq9 TEXT,
    FOREIGN KEY (student_id) REFERENCES student_demographics(student_id)
);


-- 5. VIEW: High-risk students (Severe + Moderate Severe with Financial Pressure)
CREATE VIEW IF NOT EXISTS high_risk_students AS
    SELECT 
        d.gender,
        d.age,
        d.academic_status,
        d.financial_pressure,
        l.sleep_duration_hours,
        l.social_media_hours_daily,
        l.depression_phq9
    FROM student_demographics d
    INNER JOIN student_lifestyle l ON d.student_id = l.student_id
    WHERE l.depression_phq9 IN ('Severe Depression', 'Moderate Severe Depression')
      AND d.financial_pressure = 'Yes';


-- 6. VIEW: Data ready for ML pipeline
CREATE VIEW IF NOT EXISTS ml_ready_data AS
    SELECT 
        d.gender, d.age, d.relationship_status, d.academic_status,
        d.work_and_study, d.residential_area, d.social_economic_status,
        d.financial_pressure, d.has_debt,
        l.living_environment_satisfaction, l.recent_loss,
        l.physical_activity, l.chronic_illness, l.medication,
        l.smoking, l.alcohol, l.sleep_duration_hours,
        l.social_media_hours_daily, l.academic_work_demands,
        l.depression_phq9
    FROM student_demographics d
    INNER JOIN student_lifestyle l ON d.student_id = l.student_id;