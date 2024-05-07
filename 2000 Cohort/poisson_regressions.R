mean(all$Scaled.Inflow)
var(all$Scaled.Inflow)
poisson <- glm(Scaled.Inflow ~.,data=all,family=poisson(link="log"))
adj <- all$Scaled.Inflow+var(all$Scaled.Inflow)-mean(all$Scaled.Inflow)
poisson <- glm(adj~(.-Scaled.Inflow),data=all,family=poisson(link="log"))
  