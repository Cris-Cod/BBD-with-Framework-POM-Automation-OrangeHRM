Execute especific Feature:   

behave features\scenariobg.feature  


Execute all features:

behave ./features   


Install allure en cmd:

npm install -g allure-commandline

Run the allure report in terminal:

behave -f allure_behave.formatter:AllureFormatter -o reports/ features

Generate report allure in cmd:

allure serve "C:\{}\{}\PycharmProjects\BBD_POM_Automation_OrangeHRM\reports"

allure open