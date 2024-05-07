all <- read.csv("Dataframes/All Data.csv")
outliers <- c("Beijing","Tianjin","Shanghai")
all <- all[!(all$Region %in% outliers),]
exclude <- c("Region","Scaled.Inflow","CHEI","Relative.GRP","Inflow","Senior.Graduates","UG.Enrollment","Undergraduate.Institutions","Population")
vars <- colnames(all)
vars <- vars[!(vars %in% exclude)]
formula <- as.formula(paste("Scaled.Inflow ~ ",paste(vars,collapse="+")))

pos <- all[all$Scaled.Inflow>0,]

# pos$Scaled.Inflow <- log(pos$Scaled.Inflow)
# for (v in vars){
#   pos[v] <- log(pos[v])
# }

rownames(pos) <- pos$Region
pos$Region <- NULL

lm_pos <- lm(formula,data=pos)
summary(lm_pos)
plot(pos$Scaled.Inflow,resid(lm_pos))

neg <- all[all$Scaled.Inflow <0,]

# neg$Scaled.Inflow <- -neg$Scaled.Inflow
# neg$Scaled.Inflow <- log(neg$Scaled.Inflow)
# for (v in vars){
#   neg[v] <- log(neg[v])
# }

rownames(neg) <- neg$Region
neg$Region <- NULL

lm_neg <- lm(formula, data = neg)
summary(lm_neg)
plot(neg$Scaled.Inflow,resid(lm_neg))
