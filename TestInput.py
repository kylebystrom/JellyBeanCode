#!/home/Install/anaconda/bin/python

#import EstNumJellyBeans as jelly
import EstNumJellyBeans as jelly

# Get a jelly bean estimator
estimator = jelly.NumJellyEstimator()

# Set the fraction of land being used for sugar, the world population,
# and the fraction of the population that loves pink.
land_frac = 0.1
ppl = 7e9
pink_frac = 0.18

#Several values have not been set
est = estimator.compute_Njelly_est_2()

#Test assertion statements
test_vals = [0.0,1.0,2.3,-0.3,0,1,15e9,1e12,-300000,"jellybean!"]
for val in test_vals:
	try:
		estimator.set_world_pop(val)
		print(str(val) + " is a valid input for the world population.")
	except AssertionError:
		print(str(val) + " is not a valid input for the number of people in the world, which must be a whole, nonnegative number below 100 billion.")
	print
	try:
		estimator.set_frac_ppl_loving_pink(val)
		print(str(val) + " is a valid input for the fraction of people who love pink.")
	except AssertionError:
		print(str(val) + " is not a valid input for the fraction of people who love pink, which must be a float between 0 and 1, inclusive.")
	print("\n")

#Set the values to arbitrary acceptable values
estimator.set_land_frac_for_sugar(land_frac)
estimator.set_world_pop(ppl)
estimator.set_frac_ppl_loving_pink(pink_frac)

print("No more warning statments should be printed.")
est = estimator.compute_Njelly_est_2()

print "\nIt is estimated that when\n", land_frac*100, "percent\nof the land is"+\
      " used for sugar and\n", pink_frac*100, "percent of", int(ppl), \
      "people\nLOVE pink, then there are\n", est, "\nJelly Beans in the world."
