library(car)
response <- "g.Inflow"
all <- read.csv("Dataframes/All Data.csv")
outliers = c("Beijing","Tianjin","Shanghai")
allo <- all[!(all$Region %in% outliers),]
outs <- all[all$Region %in% outliers,]
exclude = c("Region","g.Inflow","p.Inflow","CHEI","Relative.GRP","Inflow","Senior.Graduates","UG.Enrollment","Testtakers","GRP")
vars <- colnames(all)
vars <- vars[!(vars %in% exclude)]




rownames(all) <- all$Region
rownames(allo) <- allo$Region
rownames(outs) <- outs$Region
all$Region <- NULL
allo$Region <- NULL
outs$Region <- NULL

corr <- function(var, data,graph=FALSE){
  lm_var <- lm(as.formula(paste(response," ~ ",var)), data = data)
  if(graph){
    plot(predict(lm_var),resid(lm_var),main=var)
  }
  return(summary(lm_var)$r.squared)
}

corrw = c()
for (v in vars){
  corrw <- c(corrw,corr(v,all))
}

corro = c()
for (v in vars){
  corro <- c(corro,corr(v,allo))
}

corrout = c()
for (v in vars){
  corrout <- c(corrout,corr(v,outs))
}


single_correlations_with <- data.frame(Indicator = vars,R2.With.Outliers = corrw)
single_correlations_without <- data.frame(Indicator = vars,R2.Without.Outliers = corro)
single_correlations_with[order(single_correlations_with$R2.With.Outliers,decreasing=TRUE),]
single_correlations_without[order(single_correlations_without$R2.Without.Outliers,decreasing=TRUE),]