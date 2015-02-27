from StatUncGetter import StatUncGetter
from itertools import product

myGet = StatUncGetter()

collection = product( ['mt','et','tt'], 
                      ['inclusive', 'btag', 'nobtag', 'btag_low', 'btag_high', 'nobtag_low', 'nobtag_medium', 'nobtag_high'],
                      ['ZTT','W'] )

for i in collection :
  integral = myGet.getContributionUnc(i[0],i[1],i[2])[0]
  error    = myGet.getContributionUnc(i[0],i[1],i[2])[1]
  
  if error/integral < 0.05 :
    continue
    
  print '\n', i[0],i[1],i[2]
  print 'integral %.2f +/- %.2f' % (integral, error) 
  print 'relative error %.2f%s' % ( 100*error/integral, '%' )

