Web Application Firewall (WAF) Project
This project is a learning-focused Web Application Firewall (WAF) built in Python with Flask, designed to protect web applications from various cyber threats. The project is modularly structured and includes protections against SQL Injection, XSS, and CSRF attacks.

Project Goal
The main objective of this project is to provide a practical understanding of how a WAF works, the types of attacks it defends against, and the methods used for protection.

Key Components
WAF Core (waf.py): The primary WAF module that inspects request traffic and applies the security rules.

Rules (rules/): A directory containing specific rules for different attack types.

sql_injection.py: For detecting SQL Injection attacks.

xss.py: For detecting XSS attacks.

csrf.py: For preventing CSRF attacks (by checking for a missing token).

rate_limiting.py: For mitigating DoS attacks by limiting the rate of requests.

Utilities (utils/): A directory for additional helper functions.

logger.py: For logging security events and warnings.

config.py: For loading WAF configurations from a file.

Tests (test_*.py): Unit tests to ensure the WAF rules and core logic function correctly.

How to Run
Prerequisites
To run this project, you need to have Python 3 and Pip installed.

Installing Dependencies
Bash

pip install Flask
pip install -r requirements.txt # If requirements.txt is not available, you can just install Flask.
Execution
Set up the project directory structure.

Next, create a file named waf_config.json and add the following code to it:

JSON

{
    "rate_limiting": {
        "TIME_FRAME": 60,
        "REQUEST_LIMIT": 100
    },
    "rules_enabled": {
        "sql_injection": true,
        "xss": true,
        "csrf": true,
        "rate_limiting": true
    }
}
To run the WAF analyzer (e.g., WAF_analyzer.py), use the following command in your terminal:

Bash

python waf_analyzer.py
This code will provide a warning on both the console and in the log file when it detects an attack.

Example Attacks
You can simulate the following attacks to test your WAF's capabilities:

SQL Injection: username=admin' OR '1'='1

XSS: comment=<script>alert('XSS')</script>

CSRF: Send a POST request without the X-CSRF-Token header.

Rate Limiting: Send more than 100 requests from a single IP address in a short period.

License
This project is distributed under the MIT License.
