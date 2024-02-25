This can be done by making all aspects of a devops cycle work together to ensure a safe code.
steps:
static code analysis.
dependency scanning to find outdated deps
dynamic app security testing, since most microservices use api
scan for innate images through docker, container scanning tools to find if they run root or are outdated
runtime security to monitor apps and their cluster

since newers exploits comeout everyday, this process needs to be done everyday.

to do this, we can add these during:
## Development 
pre-commit/publish hooks to run tests to find any sensitive data left in the commit, then deny it.
## Git:
secret vaults to protect data
code scans to lint
## Test:
unit tests, mutation test and static code analysys
## Build:
dep scans to find outdated data
containerimage  scan to find if there are any vaulns
and image validation to ensure they are the correct image
## Deploy Stage:
validate image signiture and do integration testing
## Deploy Prod:
before promoting to production we do dynamic runtime security
runtime conflict check and ensure it's working
## Monitor
ensure logging works as intended.
## Security:
ensure the use of best standards such as SSL/TLS, using SELinux kernels and network policies.
finally, don't forget to audit.

never allow open ingress in Development environment.