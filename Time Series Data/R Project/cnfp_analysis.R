install.packages('haven')
install.packages('dplyr')
library('haven')
library('dplyr')
data <- read_dta('ecfps2018person_202012.dta')
class(data)
dim(data)
head(data)
filter(data,ads1==1)
colnames(data)[0:500]
colnames(data)[501:1371]
datas <- subset(data,select = c(tb6_a18_p,provcd18,urban18,edu_last,birthw,birthp,school_last,a12hk))
head(data)
barplot(data)
table(data$tb6_a18_p)
datas
f <- filter(data,school_last!=-8)
expr[expr$school_last != -8, ]
f <- subset(f,select=c(tb6_a18_p,provcd18,urban18,edu_last,birthw,birthp,school_last,a12hk))
f
table(data$edu_last)
