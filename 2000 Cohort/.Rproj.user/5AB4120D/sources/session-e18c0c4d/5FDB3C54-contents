library(ggplot2)
all <- read.csv("Dataframes/All Data.csv")
ggplot(all,aes(y=(Scaled.Inflow-min(Scaled.Inflow))^2,x=CHEQI))+geom_point()
outliers = c("Beijing","Tianjin","Shanghai")
allo <- all[!(all$Region %in% outliers),]
ggplot(allo,aes(y=(Scaled.Inflow-min(Scaled.Inflow))^2,x=CHEQI))+geom_point()

qqPlot(all$Scaled.Inflow)
qqPlot(allo$Scaled.Inflow)