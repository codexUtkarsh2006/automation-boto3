Automation Scripts (Local Backup & AWS S3 Upload)

This repository contains Python scripts to automate backup creation and upload backups to AWS S3.

📂 Project Structure
automation/
│── backups/                  # Stores local backup files
│── backup.py                 # Script to create local backups
│── s3_backup.py              # Script to upload backups to AWS S3

⚙️ Requirements

Python 3.7+

AWS Account with S3 access

AWS CLI configured (aws configure) with your Access Key and Secret Key

Python libraries:

pip install boto3

💾 Script 1: backup.py

This script creates a compressed .tar.gz backup of a given folder.

How it works:

Takes the source folder.

Compresses it into .tar.gz.

Saves it inside the backups/ folder with today’s date.

Example:
python backup.py


✅ Output file:

backups/backup_YYYY-MM-DD.tar.gz

☁️ Script 2: s3_backup.py

This script uploads your generated backup file to an AWS S3 bucket.

Features:

List all S3 buckets.

Create a new bucket (if not already present).

Upload backup files to your bucket.

Example:
python s3_backup.py


✅ Uploads your backup to:

s3://<your-bucket-name>/my-backup.tar.gz

🔐 AWS Setup

Before running s3_backup.py, make sure AWS credentials are configured:

aws configure


You’ll be asked for:

AWS Access Key ID

AWS Secret Access Key

Default Region (example: eu-north-1)

🚀 Future Improvements

Automate scheduling with cron (Linux) or Task Scheduler (Windows).

Add logging and error handling.

Encrypt backups before upload.

📌 Author
Utkarsh Thakur 

Developed while learning DevOps & AWS automation 🚀