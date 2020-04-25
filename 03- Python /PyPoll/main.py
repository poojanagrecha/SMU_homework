import csv
import os

csvpath = os.path.join ("SMU stuff/smu-dal-data-pt-03-2020-u-c/02-Homework/03-Python/Solutions/PyPoll/Resources/election_data.csv")

totalvotes = 0
votes = []
candidateCount = []
uniqueCandidates = []
percent = []



with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    print(csvreader)

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    for row in csvreader: 
        print(". ", end=""),
        totalvotes += 1 
        if row[2] not in uniqueCandidates:
            uniqueCandidates.append(row[2])

        votes.append(row[2])

    for candidate in uniqueCandidates:
        candidateCount.append(votes.count(candidate))
        percent.append(round(votes.count(candidate)/totalvotes*100,3))

    winner = uniqueCandidates[candidateCount.index(max(candidateCount))]

    print("Election Results")
    print(f'Total Votes: {totalvotes}')
    for i in range(len(uniqueCandidates)):
        print(f'{uniqueCandidates[i]}: {percent[i]}% {candidateCount[i]}')
    print(f'Winner: {winner}')

poll_results = os.path.join("PyPollResults.txt")
with open(poll_results, "w") as txtfile:
        txtfile.write('Election Results')
        txtfile.write('\n------------------------------------')
        txtfile.write(f'\nTotal Votes: {totalvotes}')
        txtfile.write('\n------------------------------------')
        for i in range (len(uniqueCandidates)):
            txtfile.write(f'\n{uniqueCandidates[i]}: {percent[i]}% {candidateCount[i]}')
        txtfile.write('\n------------------------------------')
        txtfile.write(f'\nWinner: {winner}')
        txtfile.write('\n------------------------------------')

