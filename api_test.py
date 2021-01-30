from jira import JIRA
options = {'server': 'https://jira3.cerner.com/'}
jira = JIRA(options, basic_auth=('nk077651', ''))
issue = jira.issue('OLYDEV-15062')
allfields = jira.fields()
nameMap = {field['name']:field['id'] for field in allfields}
getvalue = getattr(issue.fields, nameMap["Please Answer"])
print(getvalue)
