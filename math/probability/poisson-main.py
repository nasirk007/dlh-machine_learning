#!/usr/bin/env python3

import numpy as np
Poisson = __import__('poisson').Poisson

np.random.seed(0)
data = np.random.poisson(5., 100).tolist()

# task.0
p1 = Poisson(data)
print('Lambtha:', p1.lambtha)
# Ans. Lambtha: 4.84

p2 = Poisson(lambtha=5)
print('Lambtha:', p2.lambtha)
# Ans. Lambtha: 5.0

#task.1
p1 = Poisson(data)
print('P(9):', p1.pmf(9))
# P(9): 0.03175849616802446

p2 = Poisson(lambtha=5)
print('P(9):', p2.pmf(9))
# P(9): 0.036265577412911795

#task.2
p1 = Poisson(data)
print('F(9):', p1.cdf(9))
# Ans. F(9): 0.6160650724382195

p2 = Poisson(lambtha=5)
print('F(9):', p2.cdf(9))
# Ans. F(9): 0.6160609376299134

# this will print default arguments value, which is None and 1
P = Poisson()
print(P)

# this will result in error there is condition defined, 
# if data avaialble compute lambtha overwise use lambdha as 1
# in code file, data is not defined and below check will give name error
# need to define data in code file, so run np.random(lamdha, 100), 
# so improt np library inside code file
p1 = Poisson(data, lambtha=5)
print('P(9):', p1.pmf(9))