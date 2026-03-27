import csv
import os
import db_connection
import logging

logging.basicConfig(
     filename='pipeline.log',
     level=logging.INFO,
     format='%(asctime)s — %(levelname)s — %(message)s'
)

base_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(base_dir, 'heart.csv')

CHEST_PAIN_TYPE = {'ATA', 'NAP', 'ASY', 'TA'}
VALID_GENDER = {'M', 'F'}
VALID_RESTING_ECG = {'Normal', 'ST', 'LVH'}
VALID_ST_SLOPE = {'Up', 'Flat', 'Down'}

def validate_heart_disease_row(row):
  errors = []
  
  age_str = row['Age']
  if not age_str.isdigit():
      errors.append('Age is not a valid number')
  else:
    age = int(age_str)
    if not (1 <= age <= 120):
      errors.append('Invalid age range') 
  
  if row['Sex'].strip() not in VALID_GENDER:
     errors.append('Gender not found')
  
  if row['ChestPainType'].strip() not in CHEST_PAIN_TYPE:
     errors.append('Invalid Chest Pain Type')

  if not row['RestingBP'].strip().isdigit() or  int(row['RestingBP']) <= 0:
    errors.append('Resting Blood Pressure is invalid')

  if not row['Cholesterol'].strip().isdigit() or  int(row['Cholesterol']) <= 0:
     errors.append('Cholesterol is invalid')

  if row['FastingBS'].strip() not in {'0', '1'}:
     errors.append('Invalid Fasting Blood Sugar')

  if not row['MaxHR'].strip().isdigit() or not (40 <= int(row['MaxHR']) <= 250):
    errors.append('Heart Rate is invalid')
  
  if row['HeartDisease'].strip() not in {'0', '1'}:
     errors.append('Invalid value')
  
  if row['RestingECG'].strip() not in VALID_RESTING_ECG:
    errors.append('Invalid Resting ECG value')

  if row['ExerciseAngina'].strip() not in {'Y', 'N'}:
    errors.append('Invalid Exercise Angina value')

  try:
    oldpeak = float(row['Oldpeak'])
    if oldpeak < -10 or oldpeak > 10:
        errors.append('Oldpeak value out of range')
  except ValueError:
    errors.append('Oldpeak is not a valid number')

  if row['ST_Slope'].strip() not in VALID_ST_SLOPE:
    errors.append('Invalid ST Slope value')
  
  return errors


valid_rows = []
error_rows = []

with open(file_path, encoding='utf-8') as f:
  csv_reader = csv.DictReader(f)
  for row in csv_reader:
      errors = validate_heart_disease_row(row)
      if errors:
        error_rows.append({'row': row, 'reasons': errors})
      else:
        valid_rows.append(row)


db_connection.load_valid_rows(valid_rows)
db_connection.load_error_rows(error_rows)


print()
logging.info(f'Pipeline started')
#logging.info(f'Total rows read  {len(valid_rows) + len(error_rows)}')
logging.info(f'Loaded {len(valid_rows)} rows')
logging.warning(f'Rejected {len(error_rows)} rows')