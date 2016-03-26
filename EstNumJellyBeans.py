#!/c/Python34/python

import sys

## This class estimates the number of jelly beans in the world using input data
# determined to be correlated to this result.
# The number of jelly beans in the world is correlated to the fraction
# of land used for sugar, the world population, and the fraction of 
# people who like the color pink.
class NumJellyEstimator:

    ## Instantiating the class initializes some variables.
    def __init__(self):

        ## Fraction of land used for growing sugar
        self.fracLand4Sugar = 0.0
        ## World population
        self.worldPop = 0
        ## Scaling constant used in estimate
        self.scalingConst = 1e-1
        ## Fraction of people who love the color pink.
        self.fracPplLovingPink = 0.0


    ## Set the fraction of land used for sugar.
    # \param frac fraction of land used for sugar (float between 0 and 1)
    def set_land_frac_for_sugar(self, frac):

        # Make sure we've got a float.
        assert type(frac) is float, \
            "Error: fraction of land set must be a float."

        # Check that the value is between zero and one.
        if ((frac <= 0.0) or (frac >= 1.0)):
            print "\nError: Fraction of land used for sugar must be between"\
                  +" 0.0 and 1.0.\n"
            sys.exit()

        # Store the fraction.
        self.fracLand4Sugar = frac


    ## Set the world population
    # \param people integer number of people on earth
    def set_world_pop(self, people):

        # Store the fraction.
        assert type(people) == int or ((type(people) == long or type(people) == float) and people%1==0) and people >= 0, \
            "The number of people in the world must be whole and nonnegative."
        # These test statements are needed because Python uses the long type for large whole numbers and 
        # float for scientific notation, so these entries must be allowed for.
        assert people <= 1e11, "The world cannot sustain " + str(people) + "people."
        
        self.worldPop = people


    ## Set the fraction of people who love the color pink.
    def set_frac_ppl_loving_pink(self, frac):

        # Store the fraction.
        assert type(frac) == float and 0.0 <= frac and 1.0 >= frac, "The fraction of people who love pink must be a decimal between 0 and 1"

        self.fracPplLovingPink = frac


    ## Return the scaling constant so the user can check it if they want.
    def get_scaling_const(self):

        return self.scalingConst


    ## Estimate the number of jelly beans in the world.
    # This is based on a previous understanding of the estimate that did not
    # take the color pink into account. Still supported for legacy reasons.
    def compute_Njelly_est_nopink(self):

        n = self.fracLand4Sugar * self.worldPop * self.scalingConst
        # If this value is zero, it means that some value didn't get set.
        if (n == 0.0):
            print "\nError: fraction of land for sugar and world population"\
                  +"must be set before computing estimate.\n"
        return int(n)


    ## Estimate the number of jelly beans in the world using the new pink data.
    def compute_Njelly_est(self):

        n = self.fracLand4Sugar * self.worldPop * self.scalingConst / \
            (1.0 - self.fracPplLovingPink)
        # If this value is zero, it means that some value didn't get set.
        if (n == 0.0):
            print "\nError: fraction of land for sugar, world population, and"\
                  +"fraction of people loving pink must be set before "\
                  +"computing estimate.\n"

        # NE24: What other checks might be useful? What is a better way to do this?

        # It would be best to test each variable separately so more in depth feedback
        # can be given on errors. One could argue that exceptions or assertions should
        # be used, but simply warning the user of errors allows the user to test
        # extreme conditions of model if they so choose (e.g. everyone likes pink).
        # I would rewrite the code to individually test each condition and print warnings
        # if any proportion is 0 or if the faction of people liking pink or the fraction
        # of land used for sugar production are 1.

        return int(n)

    def compute_Njelly_est_2(self):

        n = self.fracLand4Sugar * self.worldPop * self.scalingConst / \
            (1.0 - self.fracPplLovingPink)
        # If this value is zero, it means that some value didn't get set.
        if self.fracLand4Sugar == 0:
            print("WARNING: No land is used for sugar. You may not have set the fraction of land used for sugar.")
        if self.worldPop == 0:
            print("WARNING: The population of the world is 0. You may not have set the world population.")
        if self.fracPplLovingPink == 0:
            print("WARNING: No one likes pink. You may not have set the fraction of people who like pink.")
        if self.fracLand4Sugar == 1:
            print("WARNING: The entire world is used for sugar production. You might have made a mistake in setting \
                the fraction of land used for sugar production.")
        if self.fracPplLovingPink == 1:
            print("WARNING: Everyone likes pink. You might have made a mistake in setting the faction of people who like pink.")

        return int(n)


