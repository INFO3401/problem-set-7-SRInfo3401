####################################################
# Wednesday Questions #2-5
####################################################
#Was stuck trying to solve with parsers used pandas, thought process/code is below.

#2.What does A equal in the expression X ∈ A?

#There are 9 different random variable outcomes possible for A, these are shown in the Questions column.
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
%matplotlib inline

CDC_data = pd.read_csv('CDC_Obesity_Data.csv')
print(CDC_data['Question'].unique())

#3.What does B equal in the expression B = ∀ Y , ∑ yi?

#B = For all random variables for Y, what is the the sum of all the existing data_value outputs.
print(CDC_data["Data_Value"].sum())

#4.The kind of data distribution you have determines the kinds of analyses you can conduct on a variable. Plot the distribution of Y for X = "Percentage of adults aged 18 years and older who have obesity."
X = CDC_data[CDC_data['Question'] == 'Percent of adults aged 18 years and older who have obesity']

X_0 = X.fillna(0)

Y = X_0['Data_Value']
sns.distplot(Y)
print("CDC Data Distribution")

#??What distribution does this data follow?? (ANSWER)
#Based on the output of the plot it is pretty clear this data follows a noraml distribution. I can confirm this by visually comparing the semi semertrical hump pattern shown by the median value climbing then droping.

#5. Plot the same distribution Y as a function of T with T on the x-axis and Y on the y-axis. 

CDC_data.plot(title="CDC Obesity Rate Distribution in the US", kind='hist', x=['YearStart'], y=['Data_Value'], color ='r')
print("CDC Data Distribution")

CDC_data.plot(title="CDC Obesity Rate Distribution in the US", kind='box', x=['YearStart'], y=['Data_Value'])
print("CDC Data Box Plot")

#??What distribution does this data follow?? (ANSWER)
#Based on the output of the plot it is pretty clear this data follows a extreme value distribution. I see this because of the gradual rise to the median then the drastic value drop after. This was not part of the subset you mention for critical analysis in the video lecture but I believe it fits best. 

#??What does this distribution tell us about obesity rates in the US?? (ANSWER)
#This distribution and median is a clear visual indication which tells us that about 30% of adults who are the age of 18 or older are clasified as obesse indivudials. It is very worrying that this constant increase may eventually drive the median up to around half of the US population.