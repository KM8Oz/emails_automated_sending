# Email Sender Script

This is a Python script that sends an email from a Gmail account to a specified recipient email address every specified interval in minutes.

## Prerequisites

- Python 3.x
- A Gmail account with [Less secure app access](https://myaccount.google.com/security)

## Installation

1. Clone or download the source code from this repository.
2. Install the required Python packages listed in `requirements.txt` using pip: `pip install -r requirements.txt`.

## Usage

1. Create a `email.conf` file in the project directory and set the following environment variables:
   - `SENDER_EMAIL`: The email address of the Gmail account you want to send emails from.
   - `SENDER_PASSWORD`: The password or app password of the Gmail account.
   - `EMAIL_SUBJECT`: Send an email
   - `EMAIL_MESSAGE`: This is a test email sent from Python.
   - `EMAIL_SERVER`: smtp.gmail.com
   - `EMAIL_PORT`: 587
2. Open a command prompt or terminal and navigate to the project directory.
3. Run the command `python main.py RECIPIENT_EMAIL TIME_INTERVAL` to start the script.
