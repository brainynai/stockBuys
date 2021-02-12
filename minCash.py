import pandas as pd
import yfinance as yf

def minCash(deposit, xgroPrice, vgroPrice):
    #Just buy vgro
    numV = int(deposit//vgroPrice)
    bestRemainder = deposit - vgroPrice * numV
    result = (numV, 0, bestRemainder)
    print(result)
    for numX in range(1, int(deposit // xgroPrice) + 1):
        leftover = deposit - numX * xgroPrice
        numV = int(leftover // vgroPrice)
        leftover -= numV * vgroPrice
        if leftover < bestRemainder:
            bestRemainder = leftover
            result = (numV, numX, bestRemainder)
            print(result)

    print(f'\nBuy {result[0]} vgro at {vgroPrice} and {result[1]} xgro at {xgroPrice} for a min remainder of {result[2]}')

    return result


def checkPrice(tickerStr):
    etfTick = yf.Ticker(tickerStr)
    etfDF = etfTick.history(period='1d', interval='1m')
    closeHistory = etfDF['Close']
    lastPrice = float(closeHistory[-1])

    print(f'The last price of {tickerStr} was {lastPrice}.')

    return round(lastPrice,2)

deposit = float(input('Investment amount: '))
minCash(deposit, checkPrice('XGRO.TO'), checkPrice('VGRO.TO'))
input('Enter to close...')
