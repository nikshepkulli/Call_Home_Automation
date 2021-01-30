# This script shows how to use the client in anonymous mode
# against jira.atlassian.com.
from jira import JIRA
import re

# prerequisite objects which you would be needing to use this API
jira = JIRA()


# issue = jira.issue("JRA-1330")


# By default, the client will connect to a Jira instance started from the Atlassian Plugin SDK
# (see https://developer.atlassian.com/display/DOCS/Installing+the+Atlassian+Plugin+SDK for details).
# Override this with the options parameter.
def connect_jira_server(URL):
    options = {"server": URL}
    jira = JIRA(options)


# Get an issue.
def get_issue(self, issue_no):
    self.issue = issue_no
    issue = jira.issue(self.issue)
    return issue


# Get all projects viewable by anonymous users.
def get_projects():
    projects = jira.projects()


# Find all comments made by Atlassians on this issue.
def find_comments():
    atl_comments = [
        comment
        for comment in get_issue().fields.comment.comments
        if re.search(r"@atlassian.com$", comment.author.emailAddress)
    ]


# Add a comment to the issue.
def add_comments(issue, comment):
    jira.add_comment(issue, comment)


# Change the issue's summary and description.
def update_issue(self, summary, description):
    self.summary = summary
    self.description = description
    get_issue().update(
        summary=self.summary, description=self.description
    )


# Send the issue away for good.
def delete_issue():
    get_issue().delete()


# Watchers
# you can the watchers
def get_watcher():
    watcher = jira.watchers(get_issue())
    return watcher


# Print the watchers count for yourself
def print_watchers_count():
    print("Issue has {} watcher(s)".format(get_watcher().watchCount))


# Print who's watching you
def print_watcher():
    for watcher in get_watcher().watchers:
        print(watcher)


# Print who's watching you
def print_watchers_email():
    for watcher in get_watcher().watchers:
        print(watcher.emailAddress)


# Add watcher
def add_watcher(issue, username):
    jira.add_watcher(issue, username)


# Remove watcher
def remove_watcher(issue, username):
    jira.remove_watcher(issue, username)


# Attachments
# upload file from `/some/path/attachment.txt`
def attach_file_using_path(issue, path):
    jira.add_attachment(issue=issue, attachment=path)


# read and upload a file (note binary mode for opening, it's important):
def read_upload_file(path, binary_mode, issue):
    with open(path, binary_mode) as f:
        jira.add_attachment(issue=issue, attachment=f)


# Attach file from memory (you can skip IO operations). In this case you MUST provide `filename`.
def file_from_memory(file_name, issue, data):
    from io import StringIO
    attachment = StringIO()
    attachment.write(data)
    jira.add_attachment(issue=issue, attachment=attachment, filename=file_name)


#  List all available attachment
def list_attachments(issue):
    for attachment in issue.fields.attachment:
        print("Name: '{filename}', size: {size}".format(
            filename=attachment.filename, size=attachment.size))
        # to read content use `get` method:
        print("Content: '{}'".format(attachment.get()))
