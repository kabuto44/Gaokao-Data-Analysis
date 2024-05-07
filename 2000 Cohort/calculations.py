import numpy as np
import operations as ops
import pandas as pd


# calculate CHEDI
pop = ops.indicator_to_series("Population")
total_pop = pop.sum()
rel_pop = pop/total_pop
ug = ops.indicator_to_series("Undergraduate Institutions")
total_ug = ug.sum()
rel_ug = ug / total_ug
chedi = rel_ug / rel_pop
ops.save_series(chedi,path="CHEDI")


#Calculate p inflow and g inflow
grad = ops.indicator_to_series("Senior Graduates")
enroll = ops.indicator_to_series("UG Enrollment")
inflow = enroll - grad
ops.save_series(inflow,path="Inflow")
pop = ops.indicator_to_series("Population")
p_inflow = inflow/pop
ops.save_series(p_inflow,path="p Inflow")
g_inflow = inflow/grad
ops.save_series(g_inflow,path="g Inflow")


#calculate grp per capita
grp = ops.indicator_to_series("GRP")
pop = ops.indicator_to_series("Population")
grp_capita = grp/pop
ops.save_series(grp_capita,path="GRP per Capita")


#calculate urban percentage
ur = ops.indicator_to_series("Urban")
pop = ops.indicator_to_series("Population")
ur_ratio = ur/pop
ops.save_series(ur_ratio, path = "Urban Ratio")