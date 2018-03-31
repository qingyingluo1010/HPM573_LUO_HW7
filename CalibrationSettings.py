import scipy.stats as stat


SIM_POP_SIZE = 1000       # population size of simulated cohorts
TIME_STEPS = 1000        # length of simulation
ALPHA = 0.05             # significance level for calculating confidence intervals
NUM_SIM_COHORTS = 500   # number of simulated cohorts used to calculate prediction intervals

# details of a clinical study estimating the mean survival time
OBS_N = 573        # number of patients involved in the study
OBS_Surv = 400       # number of patients survived at the end of 5 year period
OBS_MEAN = stat.binom.mean(573, 0.5, loc=0)   # estimated mean survival time
OBS_ALPHA = 0.05   # significance level
# the standard deviation of the mean survival time reported in the clinical study
# assumes that the reported confidence interval in this study is a t-confidence interval
OBS_STDEV =stat.binom.std(n=573, p=0.5, loc=0)

# how to sample the posterior distribution of mortality probability
# minimum, maximum and the number of samples for the mortality probablity
POST_L, POST_U, POST_N = 0.05, 0.25, 1000


#P6
OBS_N2 = 1146        # number of patients involved in the study
OBS_Surv2 = 800       # number of patients survived at the end of 5 year period
OBS_MEAN2 = stat.binom.mean(1146, 0.5, loc=0)   # estimated mean survival time
OBS_ALPHA2 = 0.05   # significance level
# the standard deviation of the mean survival time reported in the clinical study
# assumes that the reported confidence interval in this study is a t-confidence interval
OBS_STDEV2 =stat.binom.std(n=1146, p=0.5, loc=0)
