# Insider QA Automation Tests

This project contains automated UI tests for the Insider Careers – Quality Assurance job listings page.  
Tests are implemented using **Selenium + Pytest** following the **Page Object Model (POM)** approach.

## 🔧 Tech Stack

- Python 3.13
- Selenium 4
- Pytest
- Pytest-HTML
- Firefox / Chrome


## ⚙️ Installation

### 1. Create virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```
```bash
python3 -m venv venv
```
```bash
source venv/bin/activate  # Mac/Linux
```
```bash
venv\Scripts\activate     # Windows
```

### 2.Install dependencies

```bash
pip install -r requirements.txt
```
## 🧪 Test Scenarios
Scenario 1
– Filter QA Jobs
- Navigate to QA careers page
- Click See all QA jobs

Filter by:
- Location → Istanbul, Turkey
- Department → Quality Assurance
- Verify job list is loaded

Scenario 2 
– Job Card Validation
- Verify all job cards:
- Position contains Quality Assurance
- Department contains Quality Assurance
- Location contains Istanbul, Turkey

Scenario 3 
– View Role Redirect
- Click View Role button
- Verify redirect to Lever application page

## 🧪 Running Tests  (Firefox or Chrome)

1) Run all tests
 ```bash
pytest tests/ --browser=firefox -vv -s
```
2) Run a single test file
   
```bash
pytest tests/test_qajob.py --browser=firefox -vv -s
```

3) HTML Report
```bash
pytest tests/ --browser=firefox -vv -s --html=report.html
```
After execution, open:
```bash
report.html
```


Sample Console Output:

<img width="567" height="343" alt="Screenshot 2026-01-16 at 00 56 59" src="https://github.com/user-attachments/assets/68089bcf-1415-4872-b336-68f062fac49a" />

👩‍💻 Author

Hatice Duyar Keskin
QA / Test Automation Engineer
