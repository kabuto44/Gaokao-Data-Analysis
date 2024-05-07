library(lmtest)
outliers <- c("Beijing","Tianjin","Shanghai")
response <- "p.Inflow"

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
    formula <- as.formula(paste(response, " ~ ",paste(v,collapse="+")))
    lm <- lm(formula,data=all)
    print(summary(lm))
    # print(vif(lm))
    plot(predict(lm),resid(lm))
    # plot(all$g.Inflow,predict(lm))
  }
  if(outliers==-1|setequal(outliers,FALSE)){
    v <- colnames(allo)
    v <- v[v %in% vs]
    formula <- as.formula(paste(response, " ~ ",paste(v,collapse="+")))
    lm <- lm(formula,data=allo)
    print(summary(lm))
    # print(vif(lm))
    plot(predict(lm),resid(lm))
    # plot(allo$g.Inflow,predict(lm))
  }
}
get_lm <- function(vs,outliers=FALSE){
  if(outliers){
    v <- colnames(all)
    v <- v[v %in% vs]
    formula <- as.formula(paste(response, " ~ ",paste(v,collapse="+")))
    lm <- lm(formula,data=all)
    return(lm)
  } else {
    v <- colnames(allo)
    v <- v[v %in% vs]
    formula <- as.formula(paste(response, " ~ ",paste(v,collapse="+")))
    lm <- lm(formula,data=allo)
    return(lm)
  }
}

model_1 = c("Urban.Ratio","Population")
model_2 = c(model_1,"Undergraduate.Institutions","CHEDI","CHEQI")
model_3 = c(model_2,"GRP.per.Capita","Disposable.Income","Unemployment","Wages")
model_4 = c(model_3,"Foreign.Enterprises","Imports.Exports","Tourism.Earnings")

run(model_1)
run(model_2)
run(model_3)
run(model_4)
lrtest(get_lm(model_1),get_lm(model_2))
lrtest(get_lm(model_2),get_lm(model_3))
lrtest(get_lm(model_3),get_lm(model_4))
lrtest(get_lm(model_2),get_lm(model_4))
