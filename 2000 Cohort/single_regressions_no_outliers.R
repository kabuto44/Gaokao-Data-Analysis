all <- read.csv("Dataframes/All Data.csv")
outliers = c("Beijing","Tianjin","Shanghai")
all <- all[!(all$Region %in% outliers),]
lm_all <- lm(Scaled.Inflow ~ ., data = all)
summary(lm_all)

vars <- colnames(all)
vars <- vars[!(vars=="Region")]
vars <- vars[!(vars=="Scaled.Inflow")]
formula <- as.formula(paste("Scaled.Inflow ~ ",paste(vars,collapse="+")))
lm_all <- lm(formula,data=all)
summary(lm_all)

corr <- function(var, data){
  lm_var <- lm(as.formula(paste("Scaled.Inflow ~ ",var)), data = data)
  return(summary(lm_var)$r.squared)
}

correlations = c()
for (v in vars){
  correlations <- c(correlations,corr(v,all))
}

single_correlations <- data.frame(vars = vars,corrs = correlations)
single_correlations