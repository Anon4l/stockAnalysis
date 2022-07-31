from distutils.log import debug
import scraper
import ai
import fileWriter
import fileReader

stocks = fileReader.read_file('stocks.json')
for stock in stocks:
    input = stock['Name'] + ' Stocks'
    news = scraper.get_news(input);
    result = ai.get_sentiment(news)
    fileWriter.writeFile(input.replace(' ','_'),result)



debug