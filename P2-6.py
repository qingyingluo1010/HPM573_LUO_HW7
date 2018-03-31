
#P2: Likelihood Assumption
print("Problem2: It follows the binomial distribution model, the parameter is q (the probability of 5-year survival")


#P3: Likelihood Calculation

import scipy.stats as stat


from scipy.stats import binom

print("Problem3: The likelihood that a clinical study reports 400 of 573 participants survived at the end of the 5-year study period if 50% of the patients in our simulated cohort survived beyond 5 years is",stat.binom.pmf(k=400,n=573,p=0.5))


#P4: Calibration
import CalibrationClasses as Cls
import CalibrationSettings as CalibSets


# create a calibration object
calibration = Cls.Calibration()

# sample the posterior of the mortality probability
calibration.sample_posterior()

# Estimate of mortality probability and the posterior interval
print('Problem4: Estimate of annual mortality probability ({:.{prec}%} credible interval):'.format(1-CalibSets.ALPHA, prec=0),
      calibration.get_mortality_estimate_credible_interval(CalibSets.ALPHA, 4))


#P5: Projection

# initialize a calibrated model
calibrated_model = Cls.CalibratedModel('CalibrationResults.csv')
# simulate the calibrated model
calibrated_model.simulate(CalibSets.NUM_SIM_COHORTS, CalibSets.SIM_POP_SIZE, CalibSets.TIME_STEPS)

# report mean and projection interval
print('Problem5: Mean survival time and {:.{prec}%} projection interval:'.format(1 - CalibSets.ALPHA, prec=0),
      calibrated_model.get_mean_survival_5years_proj_interval(CalibSets.ALPHA, deci=4))


#P6: Projection

#Calibration


import CalibrationClasses2 as Cls2
import CalibrationSettings as CalibSets


# create a calibration object
calibration = Cls2.Calibration()

# sample the posterior of the mortality probability
calibration.sample_posterior()

# Estimate of mortality probability and the posterior interval
print('Problem6: Estimate of annual mortality probability ({:.{prec}%} credible interval):'.format(1-CalibSets.ALPHA, prec=0),
      calibration.get_mortality_estimate_credible_interval(CalibSets.ALPHA, 4))


#Projection

# initialize a calibrated model
calibrated_model = Cls2.CalibratedModel('CalibrationResults.csv')
# simulate the calibrated model
calibrated_model.simulate(CalibSets.NUM_SIM_COHORTS, CalibSets.SIM_POP_SIZE, CalibSets.TIME_STEPS)

# report mean and projection interval
print('Problem6: Mean survival time and {:.{prec}%} projection interval:'.format(1 - CalibSets.ALPHA, prec=0),
      calibrated_model.get_mean_survival_5years_proj_interval(CalibSets.ALPHA, deci=4))
print('Problem6: The changes I observed are as following：'
      'the incredible intervals became smaller, and the estimated annual mortality probability is not changed； '
      'the projection interval of the mean survival time is a little bit larger and the projection interval became smaller')













