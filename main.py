from BalanceSheets import *
from StatementsCashFlow import *
from Utilities import *


def printBalanceSheets():
    for i in range(len(balanceSheets)):
        if balanceSheets[i][1] == 'Cash and cash equivalents':
            print('\nCurrent Assets\n')
        elif balanceSheets[i][1] == 'Long-term marketable securities':
            print('\nNon-current Assets\n')
        elif balanceSheets[i][1] == 'Accounts payable':
            print('\nCurrent liabilities\n')
        elif balanceSheets[i][1] == 'Deferred revenue, non-current':
            print('\nNon-current liabilities\n')
        elif balanceSheets[i][1] == 'Common stock and additional paid-in capital, $0.00001 par value:\n12,600,000 shares authorized;\n5,126,201 and 5, 336,166 shares issued and outstanding, respectively':
            print('\nShareholders’ equity:')
        printList(balanceSheets[i][1], balanceSheets[i][0])


def printCashFlowStatements():
    printPeriod("CONSOLIDATED STATEMENTS OF CASH FLOWS", 2020)
    for i in range(len(cashFlow)):
        if cashFlow[i][1] == 'Net income':
            print('\nOperating activities:\n')
        elif cashFlow[i][1] == 'Accounts receivable, net':
            print('\nChanges in operating assets and liabilities:\n')
        elif cashFlow[i][1] == 'Purchases of marketable securities':
            print('\nInvesting activities:\n')
        elif cashFlow[i][1] == 'Proceeds from issuance of common stock':
            print('\nFinancing activities:\n')
        elif cashFlow[i][1] == 'Cash paid for income taxes, net':
            print('\nSupplemental cash flow disclosure:')
        printList(cashFlow[i][1], cashFlow[i][0])


def main():
#    printBalanceSheets()
    printCashFlowStatements()


if __name__ == '__main__':
    main()
