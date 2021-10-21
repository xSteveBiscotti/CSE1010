mpg = float(input())
gpd = float(input())

tm = (20 / mpg)
tmc = (tm * gpd)
sfm = (75 / mpg)
sfmc = (sfm * gpd)
fhm = (500 / mpg)
fhmc = (fhm * gpd)

print('{:.2f} {:.2f} {:.2f}'.format(tmc, sfm, fhmc))

