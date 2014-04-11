from ROOT import TFile, TH1F, gDirectory
import os
import math
import sys

pairs   = []
boosted = []
vbf     = []

workDir = os.getcwd()
dirList = os.listdir(os.getcwd())
for fname in dirList:
  if not(os.path.isdir(fname)) : continue
  if str(fname).find("BOOSTED") > 0 : 
    boosted.append(fname)
  elif str(fname).find("VBF") > 0  :
    vbf.append(fname)

for b in boosted :
  for v in vbf :
    if b.replace('_BOOSTED','') == v.replace('_VBF','') :
      pairs.append([b,v])
      boosted.remove(b)
      vbf.remove(v)
      
if len(boosted) > 0 :
  for b in boosted :
    pairs.append([b,''])
    
if len(vbf) > 0 :
  for v in vbf :
    pairs.append(['',v])

for pair in pairs :
  if pair[0] != '' :
    os.system('mkdir '+ (pair[0]).replace('_BOOSTED',''))
    myDir = (pair[0]).replace('_BOOSTED','')
  elif pair[1] != '' :
    os.system('mkdir '+ (pair[1]).replace('_VBF',''))
    myDir = (pair[1]).replace('_VBF','')
  
  os.system('mv '+myDir+'_* '+myDir)
  os.system('cd '+myDir)
  #os.chdir(workDir+'/'+myDir)
  for i in [0,1] :
    os.system('cd '+pair[i])
    #os.system('python ~manzoni/.utils/plotter2012.py')
    if i == 1 : 
      print 'VBFVBFVBFVBFVBFVBFVBF'
      os.system('python ~manzoni/.utils/smoother.py')
    os.system('python ~manzoni/.utils/merger_2012.py')
    #os.system('cd ..')
  
os.system('cd ..')









#os.system('python ~manzoni/.utils/plotter2012.py')
#os.system('python ~manzoni/.utils/smoother.py')
#os.system('python ~manzoni/.utils/merger_2012.py')
#os.system('python ~manzoni/.utils/mergeIntoOne.py')
#os.system('python ~manzoni/.utils/removeData.py')
#os.system('python ~manzoni/.utils/shaper2.py')



