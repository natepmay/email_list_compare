import csv

test1Filepath = "mailchimp.csv"
test1EmailColumn = 0
test2Filepath = "profiles.csv"
test2EmailColumn = 0

def makeList(fileIn, column):
    with open(fileIn, newline='', mode='r', encoding='utf-8-sig') as test:
        testEmails = []
        reader = csv.reader(test)
        index = 0
        for row in reader:
            if index > 0:
                testEmails.append(row[column])
            index += 1
        return testEmails

test1Emails = makeList(test1Filepath, test1EmailColumn)
test2Emails = makeList(test2Filepath, test2EmailColumn)

print("Unique to " + test1Filepath)
for email in test1Emails:
    if email not in test2Emails:
        print(email)

print("")
print("Unique to " + test2Filepath)
for email in test2Emails:
    if email not in test1Emails:
        print(email)