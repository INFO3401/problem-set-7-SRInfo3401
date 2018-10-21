#Steven Rothaus Problem Set 7 Friday Answers
setwd ("/Users/Steven/Desktop/University Of Colorado BOulder/INFO 3401/problem-set-7-SRInfo3401")
#setwd("INFO 3401")
getwd()
titanic_data <- read.csv(file='titanic.csv', head=TRUE, sep=",")

titanic_data

summary(titanic_data)

#6. Store the contents of the titanic.csv data in a variable in R. Then print the variable. Finally, print a summary table of that variable.

#reference the different values in each column
titanic_data$Name
#get the full set of column names
names(titanic_data)
#create a table summarizing the count of values for each possible column setting
table(titanic_data$Sex)

#7. Print out the names of the columns in the titanic.csv file. Then, print out the values for the first two columns in the dataset. Finally, create a table that outlines the distribution of genders in the dataset.

#Print out the names of the columns in the titanic.csv file.
names(titanic_data)

#Print out the values for the first two columns in the dataset
table(titanic_data$PassengerId)
table(titanic_data$Survived)
#or is this what you were looking for
table(titanic_data$PassengerId), titanic_data$Survived)

#Create a table that outlines the distribution of genders in the dataset.
table(titanic_data$Sex)

#construct the same table and look at the proportion of people in that table
gender_table <- table(titanic_data$Sex) 
gender_prop <- prop.table(gender_table)

survived_table <- table(titanic_data$Survived) 
survived_prop <- prop.table(gender_table)

#combined with the "Survived" column data to determine what proportion of survivors fell into each gender.
table(titanic_data$Sex,  titanic_data$Survived)
#table(gender_prop$Sex, survived_prop$Survived)

#allows us to look at the percentages a function of either the rows (1) or columns (2)
prop.table(table(titanic_data$Sex,  titanic_data$Survived), 1or2)

#8. Compute the proportion of men and women who survived. Then, compute the probability that if someone was a women, they would survive the crash and the probability that if someone was a man, they would survive the crash. 
#Compute the proportion of men and women who survived.
prop.table(table(titanic_data$Sex,  titanic_data$Survived))
#Compute the probability that if someone was a women, they would survive the crash.
prop.table(table(titanic_data$Sex,  titanic_data$Survived),1)
#Compute the probability that if someone was a man, they would survive the crash.
prop.table(table(titanic_data$Sex,  titanic_data$Survived), 2)
#We can define a new column in R that is computed from the available data. One way to do this is to create a new variable that contains only zeros: 
<variable name>$<column name><-0
