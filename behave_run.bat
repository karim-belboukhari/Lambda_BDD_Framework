@echo off
echo Running Behave Tests with Allure Report...
behave -f allure_behave.formatter:AllureFormatter -o reports/allure-results
allure generate reports/allure-results -o reports/allure-report --clean

