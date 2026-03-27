CREATE DATABASE IF NOT EXISTS heart_disease_db;
USE heart_disease_db;

CREATE table patients (
	id 				  INT auto_increment PRIMARY KEY,
	age 			  INT NOT NULL,
	sex 			  ENUM('M','F') NOT NULL,
	chest_pain_type   ENUM('ATA', 'NAP', 'ASY', 'TA') NOT NULL,
	resting_bp 		  INT NOT NULL,
    cholesterol       INT NOT NULL,
    fasting_bs        TINYINT(1) NOT NULL,
    resting_ecg       ENUM('Normal', 'ST', 'LVH') NOT NULL,
    max_hr            INT NOT NULL,
    exercise_angina   ENUM('Y', 'N') NOT NULL,
    oldpeak           DECIMAL(4,1) NOT NULL,
    st_slope          ENUM('Up', 'Flat', 'Down') NOT NULL,
    heart_disease     TINYINT(1) NOT NULL,
    loaded_at         TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE patients_errors (
    id            INT AUTO_INCREMENT PRIMARY KEY,
    raw_data      TEXT NOT NULL,
    error_reason  VARCHAR(255) NOT NULL,
    rejected_at   TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


