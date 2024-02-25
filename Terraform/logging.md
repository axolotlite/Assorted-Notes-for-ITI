#terraform/environment
there are 5 logging levels in terraform:
- INFO 
- WARNING 
- ERROR
- debug
- trace: which is most verbose

we can specify the logging level by using:
`TF_LOG=LEVEL`
we can specify the logging file using an evironment variable:
`TF_LOG_PATH=file_name`
