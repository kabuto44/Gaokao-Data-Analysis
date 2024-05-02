library(car)
all <- read.csv("Dataframes/All Data.csv")
outliers = c("Beijing","Tianjin","Shanghai")
allo <- all[!(all$Region %in% outliers),]
outs <- all[all$Region %in% outliers,]
exclude = c("Region","Scaled.Inflow","CHEI","Relative.GRP","Inflow","Senior.Graduates","UG.Enrollment","Undergraduate.Institutions","Testtakers","GRP")
vars <- colnames(all)
vars <- vars[!(vars %in% exclude)]
formula <- as.formula(paste("(Scaled.Inflow-min(Scaled.Inflow)) ~ ",paste(vars,collapse="+")))




rownames(all) <- all$Region
rownames(allo) <- allo$Region
rownames(outs) <- outs$Region
all$Region <- NULL
allo$Region <- NULL
outs$Region <- NULL


lm_all <- lm(formula,data=all)
summary(lm_all)
vif(lm_all)

lm_allo <- lm(formula,data = allo)
summary(lm_allo)
vif(lm_allo)

corr <- function(var, data,graph=FALSE){
  lm_var <- lm(as.formula(paste("Scaled.Inflow ~ ",var)), data = data)
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
  corro <- c(corro,corr(v,allo,graph=TRUE))
}

corrout = c()
for (v in vars){
  corrout <- c(corrout,corr(v,outs))
}


single_correlations_with <- data.frame(Indicator = vars,R2.With.Outliers = corrw)
single_correlations_without <- data.frame(Indicator = vars,R2.Without.Outliers = corro)
single_correlations_with[order(single_correlations_with$R2.With.Outliers,decreasing=TRUE),]
single_correlations_without[order(single_correlations_without$R2.Without.Outliers,decreasing=TRUE),]


# outliers <- data.frame(Indicator = vars, R2 = corrout)
# outliers
# 
# corr_mat <- cor(all)
# corr_mat
# corr_mato <- cor(allo)
# corr_mato