import pandas as pd  
import statsmodels.api as sm

# Load in the Loans: 
loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')

# Clean Interest Rate: 
loansData['Interest.Rate'] = loansData['Interest.Rate'].map(lambda x: round(float(x.rstrip('%')) / 100, 4))

# Clean Loan Length:
loansData['Loan.Length'] = loansData['Loan.Length'].map(lambda x: int(x.rstrip(' months')))

# Clean FICO Range
cleanFicoRange = loansData['FICO.Range'].map(lambda x: x.split('-'))
cleanFicoRange = cleanFicoRange.map(lambda x: [int(num) for num in x]) #Review List Comp
loansData['FICO.Range'] = cleanFicoRange

# Create a New Column called FICO.Score: 
loansData['FICO.Score'] = loansData['FICO.Range'].map(lambda x: x.pop(0)) #How calc midpoint? 

# Create Column to group loans Above and Below 12% interest rate:
loansData['IR_TF'] = loansData['Interest.Rate'].map(lambda x: 1 if x<0.1200 else 0)
#print loansData.head(10)


# Statsmodels needs an intercept column in your dataframe, so add a column with a constant intercept of 1.0.
# constant_intercept = loansData['Interest.Rate'].map(lambda x: 1.0 if x >= 1  else 1.0)
# loansData['Constant.Intercept'] = constant_intercept

loansData['Constant.Intercept'] = 1  
#print loansData['Constant.Intercept'].head(10) - Entire column set to 1

# Create a list of the column names of our independent variables, including the intercept, and call it ind_vars
ind_vars = [loansData['FICO.Score'], loansData['Amount.Funded.By.Investors'], loansData['Constant.Intercept']]

# print loansData[0:0] Are all the Headers: 
# Empty DataFrame
# Columns: 
	# [Amount.Requested, Amount.Funded.By.Investors, Interest.Rate, 
	# Loan.Length, Loan.Purpose, Debt.To.Income.Ratio, State, Home.Ownership, 
	# Monthly.Income, FICO.Range, Open.CREDIT.Lines, Revolving.CREDIT.Balance, 
	# Inquiries.in.the.Last.6.Months, Employment.Length, FICO.Score, IR_TF, Constant.Intercept]
# Index: []

column_names = loansData[0:0]
data_rows = loansData[1::]
df = pd.DataFrame(data_rows, columns=column_names)





# # Define the logistic Regression model: 
logit = sm.Logit(df['IR_TF'], df[ind_vars])
#logit = sm.Logit(loansData['IR_TF'], )

# # Fit the model: 
result = logit.fit()

# # 3 - Get the fitted coefficients from the result: 
coeff = result.params
print coeff # Gives the coefficient of each independent (predictor) variable
















