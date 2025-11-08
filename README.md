# QA Automation Framework

A Python Selenium-based automation framework for login testing with the Page Object Model, data-driven tests, cross-browser support, screenshots on failure, and HTML reporting.

---

## 🧰 Technologies Used
- Python
- Selenium
- Pytest
- pytest-html
- JSON (for test data)
- Optional: webdriver-manager for automatic browser driver management

---

## 🔹 Project Structure

QA_Automation_Portfolio/
├─ Pages/
│ ├─ Base.py
│ └─ loginpage.py
├─ Data/
│ └─ testdata.json
├─ tests/
│ └─ test_login.py
├─ conftest.py
├─ screenshots/ # screenshots on failure
├─ reports/ # HTML reports
├─ requirements.txt
└─ README.md


---

## ⚡ Features
- Page Object Model (BasePage + LoginPage)
- Data-driven tests using JSON
- Positive and negative login scenarios
- Cross-browser support via `--browser` (Chrome, Firefox, Edge)
- Screenshots automatically saved on test failure
- HTML test report generation with pytest-html

---

## 🚀 How to Run

1. Clone the repository:

```bash
git clone https://github.com/<your-username>/qa-automation-framework.git
cd qa-automation-framework
```

2. Install dependencies:
pip install -r requirements.txt

3. Run tests with HTML report (default Chrome browser):
pytest -v --browser chrome --html=reports/report.html --self-contained-html

4. Run tests in other browsers:
pytest -v --browser firefox --html=reports/report.html --self-contained-html


📝 Test Data

Test data is stored in Data/testdata.json in this format:
{
    "test1": { "username": "student", "password": "Password123" },
    "test2": { "username": "wronguser", "password": "Password123" },
    "test3": { "username": "student", "password": "wrongpass" }
}


🖼 Screenshots & Reports

Failed tests automatically generate screenshots in the screenshots/ folder.
HTML reports are generated in the reports/ folder.


💡 Notes

Make sure Chrome/Firefox/Edge browsers are installed.
