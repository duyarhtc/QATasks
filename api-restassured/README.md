🐾 Petstore API Test Automation Project

This project demonstrates API Test Automation using the Swagger Petstore API, covering CRUD operations with positive and negative test scenarios.
The framework is built with Java + Rest Assured + TestNG + Allure Report, following clean code and reusable test architecture principles.

📌 Tech Stack & Tools
Tool	            Purpose
Java 17	            Programming language
Rest Assured	    API test automation
TestNG	            Test framework (test execution, priority, dependencies)
Maven	            Dependency & build management
Allure Report	    Test reporting and visualization
Swagger Petstore	Public API under test

🧪 Test Execution
▶️ Run all tests via Maven
mvn clean test
sSample Output :


▶️ Run via TestNG Suite
mvn test -DsuiteXmlFile=testng.xml


📊 Allure Reporting
📌 Allure Integration

Test lifecycle events are captured via Allure TestNG Listener

Reports include:

Passed / Failed tests

Request & Response details

Test descriptions & hierarchy

▶️ Generate Report
allure serve target/allure-results
Sample Output:


👩‍💻 Author

Hatice Duyar Keskin
QA / Test Automation Engineer