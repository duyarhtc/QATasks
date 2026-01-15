# SeleniumTest_K8s# Insider QA Automation Tests

---

## ⚙️ Installation

1. Python 3.13 veya üzeri yüklü olmalı.
2. Virtual environment oluştur:

```bash
python3 -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows

3. Gereksinimleri yükle:

```bash
pip install -r requirements.txt

🧪 Running Tests (firefox or chrome)

1.Run all tests
pytest tests/ --browser=firefox -vv -s

2.Run a single test file
pytest tests/test_qajob.py --browser=firefox -vv -s

3. HTML Report
pytest tests/ --browser=firefox -vv -s --html=report.html
After execution, open:

report.html

🧪 Test Scenarios
Scenario 1 – Filter QA Jobs

Navigate to QA careers page

Click See all QA jobs

Filter by:

Location → Istanbul, Turkey

Department → Quality Assurance

Verify job list is loaded

Scenario 2 – Job Card Validation

Verify all job cards:

Position contains Quality Assurance

Department contains Quality Assurance

Location contains Istanbul, Turkey

Scenario 3 – View Role Redirect

Click View Role button

Verify redirect to Lever application page

Sample Console Output
buraya ekle foto

👩‍💻 Author

Hatice Duyar Keskin
QA / Test Automation Engineer