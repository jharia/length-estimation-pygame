import pymc
import myModel1 


S = pymc.MCMC(myModel1, db = 'pickle')
S.sample(iter = 10000, burn = 5000, thin = 2)
pymc.Matplot.plot(S)
