import os
import mysql.connector
from dotenv import load_dotenv
load_dotenv()

def get_connection():
    return mysql.connector.connect(
        host=os.getenv('DB_HOST'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_NAME')
    )

def load_valid_rows(valid_rows):
    conn = get_connection()
    cursor = conn.cursor()

    query = """
        INSERT INTO patients 
        (age, sex, chest_pain_type, resting_bp, cholesterol,
         fasting_bs, resting_ecg, max_hr, exercise_angina,
         oldpeak, st_slope, heart_disease)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

    for row in valid_rows:
        cursor.execute(query, (
            int(row['Age']),
            row['Sex'].strip(),
            row['ChestPainType'].strip(),
            int(row['RestingBP']),
            int(row['Cholesterol']),
            int(row['FastingBS']),
            row['RestingECG'].strip(),
            int(row['MaxHR']),
            row['ExerciseAngina'].strip(),
            float(row['Oldpeak']),
            row['ST_Slope'].strip(),
            int(row['HeartDisease'])
        ))

    conn.commit()
    cursor.close()
    conn.close()
    print(f' {len(valid_rows)} rows loaded into patients table')


def load_error_rows(error_rows):
    conn = get_connection()
    cursor = conn.cursor()

    query = """
        INSERT INTO patients_errors (raw_data, error_reason)
        VALUES (%s, %s)
    """

    for e in error_rows:
        raw = str(e['row'])
        reasons = ', '.join(e['reasons'])
        cursor.execute(query, (raw, reasons))

    conn.commit()
    cursor.close()
    conn.close()
    print(f' {len(error_rows)} rejected rows logged into patients_errors table')