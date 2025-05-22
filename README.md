# OrangeHrmPOM

# Login OrangeHrm automation

## 🔗 Application URL

https://opensource-demo.orangehrmlive.com/web/index.php/auth/login



## 📌 Project Overview

This automation project is designed to validate key Login flows on the application using the Page Object Model (POM) approach. 
The automation covers logging into the system successfully.


## 🎯 Scope of Automation

The following user flows are automated:

### 1. 🔐 Login Page

Automates user login using valid credentials.
Verifies successful login by checking redirection or dashboard element visibility.



Automates login process.
Validates login credentials


## 🧱 Project Structure (POM)

📁 OrangeHrmPOM/
├── 📁 pages/                  # Page Object Classes
│   ├── login_page.py
│   
│   ── locator_page.py
├── 📁 tests/                  # Test Cases
│   └── test_suite.py
├── 📁 utils/                  # Utilities (e.g., config, data)
│   └── test_data.py
├── config.py               # Pytest fixtures and setup
├── requirements.txt          # Dependencies
└── README.md                 # Project Documentation


## 🧪 Technologies & Tools

 Language: Python
 Framework: PyTest
 Automation Tool: Selenium WebDriver
 Design Pattern: Page Object Model (POM)
 Other Tools: WebDriver Manager, ChromeDriver



## ▶️ How to Run the Tests

1. Clone the Repository**

git clone https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
cd opensource-demo.orangeHrmPOM

2. Installed Dependencies


pip install -r requirements.txt
requiremnets.txt file
pytest

3. Run the Tests

pytest 
pytest --html=report.html --self-contained-html

## ✅ Test Data Example

python
login_credentials = {
    Username : Admin
    Password : admin123
}

