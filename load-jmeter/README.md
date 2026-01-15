🔍 Load Test – Search Module (n11.com)
📌 Project Overview

This project focuses on load testing the search module triggered from the header and listing the search results.
The tests are implemented using Apache JMeter with 1 virtual user, as required.

Since n11.com blocks automated requests (Cloudflare protection), a mock server (Postman Echo) is also used to simulate search responses and validate test logic.

🎯 Test Objective

The main goals of this load test are:

Investigate the behavior of the search module

Validate search request structure

Verify search result listing response

Observe response times and error rates under minimal load (1 user)

🛠 Tools & Technologies

Apache JMeter

HTTP Header Manager

HTTP Request Sampler

Response Assertion

JSON Extractor

Listeners (View Results Tree, Summary Report)

Postman Echo (Mock Server)

🧰 Apache JMeter Installation & Execution Guide
📌 Prerequisites

Java JDK 8 or higher is required to run Apache JMeter.

Check Java Installation
java -version


If Java is not installed:

macOS: brew install openjdk

Windows: Download and install OpenJDK or Oracle JDK

🍎 macOS – JMeter Installation
Option 1: Install via ZIP (Recommended)

Download Apache JMeter from:

https://jmeter.apache.org/download_jmeter.cgi

Choose Binary (ZIP or TGZ)

Extract the archive:

unzip apache-jmeter-5.x.zip


Navigate to the JMeter bin directory:

cd apache-jmeter-5.x/bin

Run JMeter in GUI Mode
./jmeter.sh


If you receive a permission error:

chmod +x jmeter.sh
./jmeter.sh

Run JMeter in Non-GUI (CLI) Mode
./jmeter.sh -n -t search_load_test.jmx -l results.jtl


Command parameters:

Parameter	Description
-n	Run in non-GUI mode
-t	Test plan file (.jmx)
-l	Results file (.jtl)
🪟 Windows – JMeter Installation
Option 1: Install via ZIP

Download Apache JMeter:

https://jmeter.apache.org/download_jmeter.cgi

Select Binary ZIP

Extract the ZIP file (example):

C:\apache-jmeter-5.x\


Navigate to the bin folder:

C:\apache-jmeter-5.x\bin

Run JMeter in GUI Mode

Double-click jmeter.bat

or via Command Prompt:

jmeter.bat
