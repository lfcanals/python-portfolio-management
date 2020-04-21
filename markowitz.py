import csv
import sys
import numpy
import statistics
import random



#
# Calculate standard deviation, and average return  for given portfolio
# 
# weights: vector of N elements, sum(weights)=1 with the portfolio composition.
# prices: matrix 2-dimensions. prices[i][j] = price of asset i in moment j
#         dimension of prices is NxM
#
# return: mean,stdev
#
def avgAndStd(weights, prices):
    dailyPortfolioPrices = []
    dailyPortfolioReturns = []
    initialPortfolioPrice = 0
    for dayPrices in prices:
        portfolioPrice = numpy.dot(dayPrices, weights)
        if initialPortfolioPrice == 0: 
            initialPortfolioPrice = portfolioPrice
        else:
            dailyPortfolioReturns.append(\
                (portfolioPrice-initialPortfolioPrice) / initialPortfolioPrice)
        dailyPortfolioPrices.append(portfolioPrice)


    mean = statistics.mean(dailyPortfolioReturns)        
    stdev = statistics.stdev(dailyPortfolioReturns, mean)

    return mean, stdev



#
# Utility function to generaterandom weigths that sum 1
#
# param: size of vector
# return: vector of weights of sie given param and that sums 1
def randomWeights(size):
    s = 0
    weights = []
    for i in range(0,size):
        r = random.random()
        s = s + r
        weights.append(r)

    weights = numpy.divide(weights, s)
    return weights

####################################################### THE SCRIPT


inputFileNames = []
for x in sys.argv[1:]:
    inputFileNames.append(x)

# Assumption: all files have equal hnumber of rows, and in same date.
# Format of CSVs is :  date; close-price
#
prices = []
for x in inputFileNames:
    with open(x) as pricesCSV:
        reader = csv.reader(pricesCSV, delimiter=";")
        activePrices = []
        for row in reader:
            activePrices.append(float(row[1]))

    prices.append(activePrices)

prices = numpy.transpose(prices)


for idx in range(0,1000):
    weights = randomWeights(len(inputFileNames))
    mean, stdev = avgAndStd(weights, prices)
    print(str(stdev) + "," + str(mean))

