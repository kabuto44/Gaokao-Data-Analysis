library(ggplot2)
library(car)
outliers = c("Beijing","Tianjin","Shanghai")

all <- read.csv("Dataframes/All Data.csv")
allo <- all[!(all$Region %in% outliers),]
rownames(all) <- all$Region
rownames(allo) <- allo$Region
all$Region <- NULL
allo$Region <- NULL

run <- function(vs,outliers=-1){
  if(outliers==-1|setequal(outliers,TRUE)){
    v <- colnames(all)
    v <- v[v %in% vs]
    formula <- as.formula(paste("Scaled.Inflow ~ ",paste(v,collapse="+")))
    lm <- lm(formula,data=all)
    print(summary(lm))
    plot(predict(lm),resid(lm))
    plot(all$Scaled.Inflow,predict(lm))
  }
  if(outliers==-1|setequal(outliers,FALSE)){
    v <- colnames(allo)
    v <- v[v %in% vs]
    formula <- as.formula(paste("Scaled.Inflow ~ ",paste(v,collapse="+")))
    lm <- lm(formula,data=allo)
    print(summary(lm))
    plot(predict(lm),resid(lm))
    plot(allo$Scaled.Inflow,predict(lm))
  }
}

exclude <- c("Scaled.Inflow","CHEI","Relative.GRP","Inflow","Senior.Graduates","UG.Enrollment","Population","Undergraduate.Institutions")
vars <- colnames(all)
vars <- vars[!(vars %in% exclude)]
run(vars)

run("GRP.per.Capita",outliers=FALSE)
run("CHEQI",outliers=FALSE)
run(c("GRP.per.Capita","CHEDI","CHEQI"),outliers=FALSE)