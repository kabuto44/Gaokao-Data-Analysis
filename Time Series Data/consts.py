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
PROVINCES_MINUS_CITIES = ['Hebei', 'Shanxi', 'Inner Mongolia', 'Liaoning', 'Jilin', 'Heilongjiang', 'Jiangsu', 'Zhejiang', 'Anhui', 'Fujian', 'Jiangxi', 'Shandong', 'Henan', 'Hubei', 'Hunan', 'Guangdong', 'Guangxi', 'Hainan', 'Chongqing', 'Sichuan', 'Guizhou', 'Yunnan', 'Tibet', 'Shaanxi', 'Gansu', 'Qinghai', 'Ningxia', 'Xinjiang']
CATEGORIES = [PROVINCES,NORTH_CHINA,NORTH_CHINA_MINUS_CITIES,NORTHEAST,EAST_CHINA,EAST_CHINA_MINUS_CITIES,CENTRAL_CHINA,SOUTHWEST,NORTHWEST, PROVINCES_MINUS_CITIES]
CATEGORY_NAMES = ["All Provinces","North China", "North China (Excluding Beijing, Tianjin)", "Northeast China", "East China", "East China (Excluding Shanghai)", "Central China", "Southwest China","Northwest China", "All Provinces (Excluding Beijing, Tianjin, and Shanghai)"]
SHORT_CATEGORIES = ["all","nc","nc-","ne","e","e-","c","sw","nw","all-"]
LASTYEAR = 2022
FIRSTYEAR = 2000