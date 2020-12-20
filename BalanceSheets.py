"""

The class contains information about the balances sheets of Apple for period between 2016 and 2020 years.

"""
from Utilities import *

"""Current assets"""
#   Years                              2020    2019    2018    2017    2016
cashAndCashEquivalents =            [ 38016,  48844,  25913,  20289,  20484]
shortTermMarketableSecurities =     [ 52927,  51713,  40388,  53892,  46671]
accountsReceivableLessAllowances =  [ 16120,  22926,  23186,  17874,  15754]
Inventories =                       [  4061,   4106,   3956,   4855,   2132]
VendorNonTradeReceivables =         [ 21325,  22878,  25809,  17799,  13545]
OtherCurrentAssets =                [ 11264,  12352,  12087,  13936,   8283]
# cashAndCashEquivalents + shortTermMarketableSecurities + accountsReceivableLessAllowances + Inventories +
# + VendorNonTradeReceivables + OtherCurrentAssets = totalCurrentAssets
totalCurrentAssets =                [0 for a in range(PERIOD)]

"""Non-current assets"""
longTermMarketableSecurities =      [100887, 105341, 170799, 194714, 170430]
propertyPlantAndEquipmentNet =      [ 36766,  37378,  41304,  33783,  27010]
goodwill =                          [     0,      0,      0,   5717,   5414]
acquiredIntangibleAssetsNet =       [     0,      0,      0,   2298,   3206]
otherNonCurrentAssets =             [ 42522,  32978,  22283,  10162,   8757]
# longTermMarketableSecurities + propertyPlantAndEquipmentNet + goodwill +
# + acquiredIntangibleAssetsNet + otherNonCurrentAssets
totalNonCurrentAssets =             [0 for b in range(PERIOD)]

# Total assets
# totalCurrentAssets + totalNonCurrentAssets
totalAssets =                       [0 for c in range(PERIOD)]

"""Current liabilities"""
accountsPayable =                   [ 42296,  46236,  55888,  49049,  37294]
otherCurrentLiabilities =           [ 42684,  37720,  32687,      0,      0]
accruedExpanses =                   [     0,      0,      0,  25744,  22027]
deferredRevenueCurrent =            [  6643,   5522,   7543,   7548,   8080]
commercialPaper =                   [  4996,   5980,  11964,  11977,   8105]
currentPortionLongTermDebt =        [  8773,  10260,   8784,   6496,   3500]
# accountsPayable + accruedExpanses + deferredRevenueCurrent +
# + commercialPaper + currentPortionLongTermDebt
totalCurrentLiabilities =           [0 for d in range(PERIOD)]

"""Non-current liabilities"""
deferredRevenueNonCurrent =         [     0,      0,   2979,   2836,   2930]
longTermDebt =                      [ 98667,  91807,  93735,  97207,  75427]
otherNonCurrentLiabilities =        [ 54490,  50503,  45180,  40415,  36074]
# deferredRevenueNonCurrent + longTermDebt + otherNonCurrentLiabilities
totalNonCurrentLiabilities =        [0 for e in range(PERIOD)]
# totalCurrentLiabilities + totalNonCurrentLiabilities
totalLiabilities =                  [0 for f in range(PERIOD)]

"""Shareholders equity"""
# Common stock and additional paid-in capital, $0.00001 par value: 12,600,000 shares authorized;
# 5,126,201 and 5,336,166 shares issued and outstanding, respectively
commonStockAndAdditionalPaidInCapitalSharesAuthorizedSharesIssuedAndOutstanding = \
                                    [ 50779,  45174,  40201,  35867,  31251]
retainedEarnings =                  [ 14966,  45898,  70400,  98330,  96364]
accumulatedOtherComprehensiveIncomeLoss = \
                                    [  -406,   -584,  -3454,   -150,    634]
# commonStockAndAdditionalPaidInCapitalSharesAuthorizedSharesIssuedAndOutstanding + retainedEarnings +
# + accumulatedOtherComprehensiveIncomeLoss
totalShareholdersEquity =           [0 for g in range(PERIOD)]
# totalShareholdersEquity + totalLiabilities
totalLiabilitiesAndShareholdersEquity = \
                                    [0 for h in range(PERIOD)]

"""I create insufficient reports"""
for state in range(PERIOD):
    # Assets
    totalCurrentAssets[state] = \
        cashAndCashEquivalents[state] + \
        shortTermMarketableSecurities[state] + \
        accountsReceivableLessAllowances[state] + \
        Inventories[state] + \
        VendorNonTradeReceivables[state] + \
        OtherCurrentAssets[state]
    totalNonCurrentAssets[state] = \
        longTermMarketableSecurities[state] + \
        propertyPlantAndEquipmentNet[state] + \
        goodwill[state] + \
        acquiredIntangibleAssetsNet[state] + \
        otherNonCurrentAssets[state]
    totalAssets[state] = \
        totalCurrentAssets[state] + \
        totalNonCurrentAssets[state]
    # Liabilities
    totalCurrentLiabilities[state] = \
        accountsPayable[state] + \
        otherCurrentLiabilities[state] + \
        accruedExpanses[state] + \
        deferredRevenueCurrent[state] + \
        commercialPaper[state] + \
        currentPortionLongTermDebt[state]
    totalNonCurrentLiabilities[state] = \
        deferredRevenueNonCurrent[state] + \
        longTermDebt[state] + \
        otherNonCurrentLiabilities[state]
    totalLiabilities[state] = \
        totalCurrentLiabilities[state] + \
        totalNonCurrentLiabilities[state]
    # Shareholders equity
    totalShareholdersEquity[state] = \
        commonStockAndAdditionalPaidInCapitalSharesAuthorizedSharesIssuedAndOutstanding[state] + \
        retainedEarnings[state] + \
        accumulatedOtherComprehensiveIncomeLoss[state]
    totalLiabilitiesAndShareholdersEquity[state] = \
        totalShareholdersEquity[state] + \
        totalLiabilities[state]

"""I initialize a list, which contains all reports of this balance"""
balanceSheets = [
    [cashAndCashEquivalents, 'Cash and cash equivalents'],
    [shortTermMarketableSecurities, 'Short-term marketable securities'],
    [accountsReceivableLessAllowances, 'Accounts receivable, less allowances of $58 and $53, respectively'],
    [Inventories, 'Inventories'],
    [VendorNonTradeReceivables, 'Vendor non-trade receivables'],
    [OtherCurrentAssets, 'Other current assets'],
    [totalCurrentAssets, 'Total current assets'],
    [longTermMarketableSecurities, 'Long-term marketable securities'],
    [propertyPlantAndEquipmentNet, 'Property, plant and equipment, net'],
    [goodwill, 'Goodwill'],
    [acquiredIntangibleAssetsNet, 'Acquired intangible assets, net'],
    [otherNonCurrentAssets, 'Other non-current assets'],
    [totalNonCurrentAssets, 'Total non-current assets'],
    [totalAssets, 'Total assets'],
    [accountsPayable, 'Accounts payable'],
    [otherCurrentLiabilities, 'Other current liabilities'],
    [accruedExpanses, 'Accrued expenses'],
    [deferredRevenueCurrent, 'Deferred revenue'],
    [commercialPaper, 'Commercial paper'],
    [currentPortionLongTermDebt, 'Current portion of long-term debt'],
    [totalCurrentLiabilities, 'Total current liabilities'],
    [deferredRevenueNonCurrent, 'Deferred revenue, non-current'],
    [longTermDebt, 'Long-term debt'],
    [otherNonCurrentLiabilities, 'Other non-current liabilities'],
    [totalLiabilities, 'Total liabilities'],
    [commonStockAndAdditionalPaidInCapitalSharesAuthorizedSharesIssuedAndOutstanding,
     'Common stock and additional paid-in capital, $0.00001 par value:\n12,600,000 shares authorized;\n5,126,201 and 5, 336,166 shares issued and outstanding, respectively'],
    [retainedEarnings, 'Retained earnings'],
    [accumulatedOtherComprehensiveIncomeLoss, 'Accumulated other comprehensive income/(loss)'],
    [totalShareholdersEquity, 'Total shareholders\' equity'],
    [totalLiabilitiesAndShareholdersEquity, 'Total liabilities and shareholders’ equity']
]