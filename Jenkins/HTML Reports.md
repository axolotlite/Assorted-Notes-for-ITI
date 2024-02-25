we can enable them through:
- To enable the HTML reports login into the Jenkins server and go to the required job.
- Click on Pipeline Syntax
- Under Sample Step select publishHTML: Publish HTML reports
- Under HTML directory to archive enter owasp-zap-report
- Enter zap_report.html in Index page
- Enter OWASP ZAP HTML Reports under Index page title
	(Optional) and Report title
- Click on Publishing options and click on Keep past HTML reports and Always link to last build
- Finally click on Generate Pipeline Script
- Copy the generated script and add under pipeline post actions