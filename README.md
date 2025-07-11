# API Automation Framework

This is a lightweight, modular API automation framework built using **Python**, **Pytest**, and **Requests**. It is designed for quick integration, easy configuration, and extensibility.

---

## Folder Structure

api-framework/
├── api/ # Contains API endpoint methods
│ └── users_api.py
├── tests/ # All API test cases
│ └── test_users.py
├── utils/ # Configuration, reusable utilities
│ └── config.py
├── pytest.ini # Pytest configuration
├── requirements.txt # Project dependencies
├── .gitignore # Files/folders to ignore in Git
└── README.md # Project info and execution guide

---

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/Shi-kh/api-framework.git
cd api-framework

# Create
python -m venv venv

# Activate on Windows
venv\Scripts\activate

# Activate on Mac/Linux
source venv/bin/activate

#install depedencies
pip install -r requirements.txt

#run all the tests
pytest -v

#run tests from specific file
pytest tests/test_users.py -v

#generate HTML report
pytest --html=report.html
