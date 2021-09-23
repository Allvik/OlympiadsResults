import csv

answer = []
with open("olymp.csv", "r") as fin:
    results = csv.DictReader(fin, delimiter=';', quotechar='"')
    for cur in results:
        cur.pop('')
        if cur['Stage'] == '':
            cur['Stage'] = 'Заключительный'
        answer.append(cur)
with open("olymp.csv", "w") as fout:
    writer = csv.DictWriter(fout, fieldnames=["IDEKIS", "ID", "FullName", "ShortName", "OlympiadType", "Stage", "Class",
                                              "Subject", "Status", "Year", "global_id"], delimiter=';', quotechar='"')
    writer.writeheader()
    for cur in answer:
        writer.writerow(cur)
