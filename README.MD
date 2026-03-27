# Heart Disease Data Pipeline 

An automated data engineering pipeline designed to ingest, validate, and load heart disease clinical records into a MySQL database. 

This project processes raw CSV data, enforces strict data quality rules, and separates valid records from erroneous ones, ensuring only clean data reaches the production tables.

## Features

* **Automated Data Ingestion:** Reads clinical records directly from a local `heart.csv` file.
* **Rigorous Data Validation:** Checks each row against specific clinical criteria (e.g., age limits, valid ECG readings, valid blood pressure ranges).
* **Error Handling & Segregation:** Valid records are routed to a primary database table, while rejected records are logged into a dedicated error table along with the specific reasons for failure.
* **Secure Database Connection:** Uses environment variables to protect database credentials.

## Tech Stack

* **Language:** Python 3.x
* **Database:** MySQL
* **Libraries:** `mysql-connector-python`, `python-dotenv`, built-in `csv` and `os` modules.

## Pipeline Architecture

1. **Extract:** The script reads raw data from `heart.csv`.
2. **Transform (Validate):** A custom validation function checks 12 different clinical features. If a row fails any check (e.g., negative cholesterol, invalid string format), the specific error is appended to an error list.
3. **Load:** * Clean data is bulk-inserted into the `patients` MySQL table.
   * Invalid data, along with its error message, is inserted into the `patients_errors` MySQL table for auditing.

## Setup and Installation

**1. Clone the repository:**
```bash
git clone [https://github.com/yourusername/your-repo-name.git](https://github.com/yourusername/your-repo-name.git)
cd your-repo-name