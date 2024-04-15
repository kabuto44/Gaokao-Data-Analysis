PROVINCES = ['Beijing', 'Tianjin', 'Hebei', 'Shanxi', 'Inner Mongolia', 'Liaoning', 'Jilin', 'Heilongjiang', 'Shanghai', 'Jiangsu', 'Zhejiang', 'Anhui', 'Fujian', 'Jiangxi', 'Shandong', 'Henan', 'Hubei', 'Hunan', 'Guangdong', 'Guangxi', 'Hainan', 'Chongqing', 'Sichuan', 'Guizhou', 'Yunnan', 'Tibet', 'Shaanxi', 'Gansu', 'Qinghai', 'Ningxia', 'Xinjiang']
PROV_DICT = {}
for i in range(len(PROVINCES)):
    PROV_DICT[PROVINCES[i]]=i

NORTH_CHINA = ['Beijing', 'Tianjin', 'Hebei', 'Shanxi', 'Inner Mongolia']
NORTHEAST = ['Liaoning', 'Jilin', 'Heilongjiang']
EAST_CHINA = ['Shanghai', 'Jiangsu', 'Zhejiang', 'Anhui', 'Fujian', 'Jiangxi', 'Shandong']
CENTRAL_CHINA = ['Henan', 'Hubei', 'Hunan', 'Guangdong', 'Guangxi', 'Hainan']
SOUTHWEST = ['Chongqing', 'Sichuan', 'Guizhou', 'Yunnan', 'Tibet']
NORTHWEST = ['Shaanxi', 'Gansu', 'Qinghai', 'Ningxia', 'Xinjiang']
NORTH_CHINA_MINUS_CITIES = ['Hebei', 'Shanxi', 'Inner Mongolia']
EAST_CHINA_MINUS_CITIES = ['Jiangsu', 'Zhejiang', 'Anhui', 'Fujian', 'Jiangxi', 'Shandong']
LASTYEAR = 2022
FIRSTYEAR = 2004