library(ggplot2)
library(car)
library(pls)

outliers <- c("Beijing","Tianjin","Shanghai")
response <- "g.Inflow"

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
    formula <- as.formula(paste(response," ~ ",paste(v,collapse="+")))
    lm <- lm(formula,data=all)
    print(summary(lm))
    print(vif(lm))
    plot(predict(lm),resid(lm))
    plot(data.frame(all[response],predict(lm)))
  }
  if(outliers==-1|setequal(outliers,FALSE)){
    v <- colnames(allo)
    v <- v[v %in% vs]
    formula <- as.formula(paste(response, " ~ ",paste(v,collapse="+")))
    lm <- lm(formula,data=allo)
    print(summary(lm))
    print(vif(lm))
    plot(predict(lm),resid(lm))
    plot(data.frame(allo[response],predict(lm)))
  }
}

exclude <- c("Region","p.Inflow","g.Inflow","Inflow","CHEI","Relative.GRP","Senior.Graduates","UG.Enrollment")
vars <- colnames(all)
vars <- vars[!(vars %in% exclude)]
run(vars)
