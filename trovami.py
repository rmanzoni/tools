import os
import sys
from operator import itemgetter

results = []

workDir  = os.getcwd()
workDir1 = workDir

for workDir, dirs, files in os.walk(workDir):
  for file in files:
    #if file == 'limit125.txt' :
    if file == 'expOnlyLimit125.txt' :
      fname = os.path.abspath(os.path.join(workDir,file))
      f = open(str(fname),'r')
      lines = f.readlines() 
      for l in lines :
        if '50.0%' in l :
          folder = fname.replace(workDir1,'')
          folder = folder.replace('LimitInputs','') 
          #folder = folder.replace('limit125.txt','')
          folder = folder.replace('expOnlyLimit125.txt','')
          folder = folder.replace('/','')          
          out = folder+' '+l
          
          result = out.split()
          results.append(result)

results = sorted(results,key=itemgetter(5))

for r in results :
  print r