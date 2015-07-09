import pandas as pd  
# import numpy as np
import statsmodels.api as sm
# import matplotlib.pyplot as plt 


loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')

# Export to CSV: 
#loansData.to_csv('loansData_clean.csv', header=True, index=False)


# Clean Interest Rate: 
cleanInterestRate = loansData['Interest.Rate'].map(lambda x: round(float(x.rstrip('%')) / 100, 4))
loansData['Interest.Rate'] = cleanInterestRate


 
# Clean Loan Length:
cleanLoanLength = loansData['Loan.Length'].map(lambda x: int(x.rstrip(' months')))
loansData['Loan.Length'] = cleanLoanLength

# Clean FICO Range
cleanFicoRange = loansData['FICO.Range'].map(lambda x: x.split('-'))
cleanFicoRange = cleanFicoRange.map(lambda x: [int(num) for num in x])
loansData['FICO.Range'] = cleanFicoRange

# Create a New Column called FICO.Score: 
fico_score = loansData['FICO.Range'].map(lambda x: x.pop(0)) #How calc midpoint? 
loansData['FICO.Score'] = fico_score


twelve_column = loansData['Interest.Rate'].map(lambda x: 1 if x<0.1200 else 0)
# print twelve_column
# print len(twelve_column)

loansData['IR_TF'] = twelve_column
print loansData['IR_TF'].head()

#print loansData.head(1)

# IT WORKED! http://stackoverflow.com/questions/14029245/python-putting-an-if-elif-else-statement-on-one-line
# http://stackoverflow.com/questions/1585322/is-there-a-way-to-perform-if-in-pythons-lambda
# 81174    0.0890   81174    1
# 99592    0.1212	99592    0
# 80059    0.2198	80059    0
# 15825    0.0999	15825    1
# 33182    0.1171	33182    1
# Name: Interest.Rate, dtype: float64



# Statsmodels needs an intercept column in your dataframe, so add a column with a constant intercept of 1.0.
constant_intercept = loansData['Interest.Rate'].map(lambda x: 1.0 if x >= 1  else 1.0)
loansData['Constant.Intercept'] = constant_intercept



print loansData.head(10)




# Does it literally mean a list? 
# Create a list of the column names of our independent variables, including the intercept, and call it ind_vars
ind_vars = [loansData['FICO.Score'], loansData['Amount.Funded.By.Investors']]













