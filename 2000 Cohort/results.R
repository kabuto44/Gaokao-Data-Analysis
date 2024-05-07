library(lmtest)
library(ggplot2)
library(car)
library(pls)

# set up dataframes
all <- read.csv("Dataframes/All Data.csv",check.names=FALSE)
outliers <- c("Beijing","Tianjin","Shanghai")
allo <- all[!(all$Region %in% outliers),]
rownames(all) <- all$Region
rownames(allo) <- allo$Region
all$Region <- NULL
allo$Region <- NULL

#plot g inflow, p inflow
{
  boxplot(all$`p Inflow`,horizontal=TRUE,main = substitute(paste(italic("p"),"-Inflow by Province")),xlab = substitute(paste(italic("p"),"-Inflow")))
  text(all$`p Inflow`[all$`Short Name` %in% c("SH","BJ","TJ")],1.1,labels=all$`Short Name`[all$`Short Name` %in% c("SH","BJ","TJ")])
}
{
  boxplot(all$`g Inflow`,horizontal=TRUE,main = substitute(paste(italic("g"),"-Inflow by Province")),xlab = substitute(paste(italic("g"),"-Inflow")))
  text(all$`g Inflow`[all$`Short Name` %in% c("SH","BJ")],1.1,labels=all$`Short Name`[all$`Short Name` %in% c("SH","BJ")])
  text(all$`g Inflow`[all$`Short Name` %in% c("TJ")],1.15,labels = "TJ")
}

#run nested regressions with outliers
model_1 = lm(`g Inflow` ~ `Urban Ratio` + `Population`,data=all)
model_2 = lm(`g Inflow` ~ `Urban Ratio` + `Population`
             + `CHEDI`+ `CHEQI`
             ,data=all)
model_3 = lm(`g Inflow` ~ `Urban Ratio` + `Population`
             + `CHEDI` + `CHEQI`
             + `GRP per Capita` + `Unemployment`+ `Wages` + `Foreign Enterprises`
             ,data=all)

summary(model_1)
summary(model_2)
summary(model_3)

#run pairwise likelihood ratio testing for models with outliers
l_2 <- c(lrtest(model_1,model_2)[,"Pr(>Chisq)"][2],"NA")
l_3 <- c(lrtest(model_1,model_3)[,"Pr(>Chisq)"][2],lrtest(model_2,model_3)[,"Pr(>Chisq)"][2])
likelihoods <- data.frame(l_2,l_3)
colnames(likelihoods) <- c("Model 2","Model 3")
rownames(likelihoods) <- c("Model 1","Model 2")
likelihoods



#run nested regressions without outliers
model_1 = lm(`g Inflow` ~ `Urban Ratio` + `Population`,data=allo)
model_2 = lm(`g Inflow` ~ `Urban Ratio` + `Population`
             + `CHEDI`+ `CHEQI`
             ,data=allo)
model_3 = lm(`g Inflow` ~ `Urban Ratio` + `Population`
             + `CHEDI` + `CHEQI`
             + `GRP per Capita` + `Unemployment`+ `Wages` + `Foreign Enterprises`
             ,data=allo)

summary(model_1)
summary(model_2)
summary(model_3)

#run pairwise likelihood ratio testing for models with outliers
l_2 <- c(lrtest(model_1,model_2)[,"Pr(>Chisq)"][2],"NA")
l_3 <- c(lrtest(model_1,model_3)[,"Pr(>Chisq)"][2],lrtest(model_2,model_3)[,"Pr(>Chisq)"][2])
likelihoods <- data.frame(l_2,l_3)
colnames(likelihoods) <- c("Model 2","Model 3")
rownames(likelihoods) <- c("Model 1","Model 2")
likelihoods


#check for individual correlations for each model variable, with out liers
corr <- function(var, data,graph=FALSE){
  lm_var <- lm(as.formula(paste("`g Inflow` ~ `",var,"`",sep="")), data = data)
  if(graph){
    plot(predict(lm_var),resid(lm_var),main=var)
  }
  return(summary(lm_var)$r.squared)
}

corrw = c()
vars = c("Urban Ratio", "Population", "CHEDI", "CHEQI",
               "GRP per Capita" , "Unemployment", "Wages",
               "Foreign Enterprises")
for (v in vars){
  corrw <- c(corrw,corr(v,all))
}

correlations <- data.frame(Indicator = vars,R2 = corrw)
correlations[order(correlations$R2,decreasing=TRUE),]

corro = c()
for (v in vars){
  corro <- c(corro,corr(v,allo))
}
correlations <- data.frame(Indicator = vars,R2 = corro)
correlations[order(correlations$R2,decreasing=TRUE),]

#run pairwise tests using p inflow as response
model_1 = lm(`p Inflow` ~ `Urban Ratio` + `Population`,data=all)
model_2 = lm(`p Inflow` ~ `Urban Ratio` + `Population`
             + `CHEDI`+ `CHEQI`
             ,data=all)
model_3 = lm(`p Inflow` ~ `Urban Ratio` + `Population`
             + `CHEDI` + `CHEQI`
             + `GRP per Capita` + `Unemployment`+ `Wages` + `Foreign Enterprises`
             ,data=all)
l_2 <- c(lrtest(model_1,model_2)[,"Pr(>Chisq)"][2],"NA")
l_3 <- c(lrtest(model_1,model_3)[,"Pr(>Chisq)"][2],lrtest(model_2,model_3)[,"Pr(>Chisq)"][2])
likelihoods <- data.frame(l_2,l_3)
colnames(likelihoods) <- c("Model 2","Model 3")
rownames(likelihoods) <- c("Model 1","Model 2")
likelihoods

model_1 = lm(`p Inflow` ~ `Urban Ratio` + `Population`,data=allo)
model_2 = lm(`p Inflow` ~ `Urban Ratio` + `Population`
             + `CHEDI`+ `CHEQI`
             ,data=allo)
model_3 = lm(`p Inflow` ~ `Urban Ratio` + `Population`
             + `CHEDI` + `CHEQI`
             + `GRP per Capita` + `Unemployment`+ `Wages` + `Foreign Enterprises`
             ,data=allo)
l_2 <- c(lrtest(model_1,model_2)[,"Pr(>Chisq)"][2],"NA")
l_3 <- c(lrtest(model_1,model_3)[,"Pr(>Chisq)"][2],lrtest(model_2,model_3)[,"Pr(>Chisq)"][2])
likelihoods <- data.frame(l_2,l_3)
colnames(likelihoods) <- c("Model 2","Model 3")
rownames(likelihoods) <- c("Model 1","Model 2")
likelihoods