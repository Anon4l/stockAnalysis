import csv
def writeFile(fileName,data):
    csvhead = ['news','sentiment','sentimentSum']
    with open(fileName+'.csv','w') as csvfile:
        result_csv = csv.DictWriter(csvfile, fieldnames=csvhead)
        result_csv.writeheader()
        sentimentSum = 0
        for i in data:
            sentiment = i['sentiment'][0]
            if(sentiment['label'] == 'positive'):
                sentimentSum += sentiment['score']
            if(sentiment['label'] == 'negative'):
                sentimentSum -= sentiment['score']*3
            if(sentiment['label'] == 'neutral'):
                sentimentSum += 0

            result_csv.writerow(
                                {
                                 "news":i['news'],
                                 "sentiment":i['sentiment'][0],
                                 "sentimentSum":sentimentSum
                                }
                               )
        csvfile.close()
