# Upload Files To S3

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

## Installation

**Prerequisites**:

- Python 3.12 or higher installed on your system.
- Pip package manager installed.

**Clone the Repository**:
   Clone this repository to your local machine:

   ```bash
   git clone git@github.com:dev-bruno-arruda/upload_to_s3.git
   ```

**Create and Activate a Virtual Environment**:
Navigate to the project directory and create a virtual environment using the following command:

```bash
cd your_repository
python -m venv venv
```

**Activate the virtual environment**:
Windows:

```bash
.\venv\Scripts\activate
```

**Install Required Packages**:
Install the required Python packages using pip:

```bash
pip install -r requirements.txt
```

**Configure Environment Variables**:
Create a .env file in the project directory and add the following environment variables:

```text
SOURCE_DIRECTORY="C:\\inetpub\\logs\\LogFiles\\W3SVC1\\"
S3_BUCKET_NAME=your_bucket_name
AWS_ACCESS_KEY_ID=your_access_key_id
AWS_SECRET_ACCESS_KEY=your_secret_access_key
SCHEDULE_TIME=23:30
```

Replace your_bucket_name, your_access_key_id, and your_secret_access_key with your actual Amazon S3 bucket name, access key ID, and secret access key respectively. Adjust the SOURCE_DIRECTORY and SCHEDULE_TIME variables as needed.

**Run the Script**:
Execute the scheduler.py script to start the automated upload process:

```bash
py scheduler.py
```

## Files Overview

- main.py: This script contains the main logic for uploading files to Amazon S3. It loads environment variables from the .env file, retrieves file paths, uploads files to the specified S3 bucket, and deletes uploaded files from the local directory.
- scheduler.py: This script schedules the execution of the main.py script to run daily at a specified time. It retrieves the scheduled time from the .env file, configures the scheduler, and triggers the upload process accordingly.
- .env: This file stores environment variables such as the source directory path, S3 bucket name, AWS access key ID, AWS secret access key, and schedule time. These variables are used by the main.py and scheduler.py scripts.
- services/upload_to_s3.py: This module provides a service class UploadToS3 with a static method upload. It handles the process of uploading files to Amazon S3, including renaming files with the IP address and uploading them to the specified directory.
- infrastructure/s3_connector.py: This module defines the S3 class, which serves as an interface for interacting with an S3 bucket. It provides methods for uploading files, listing files, deleting files, creating directories, and deleting files within a directory.
- infrastructure/Boto3S3Connector.py: This module extends the S3 class with a specific implementation using the Boto3 library. It overrides methods for uploading files, listing files, and deleting files to leverage Boto3 functionality.
