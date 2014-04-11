import os
import sys

baseDir = os.getcwd()
limitDir  = "/afs/cern.ch/work/m/manzoni/diTauLimit/CMGTools/CMSSW_5_2_3_patch2/src/CMGTools/H2TauTau/limits2/"
tauTauDir = "/afs/cern.ch/work/m/manzoni/diTauLimit/CMGTools/CMSSW_5_2_3_patch2/src/CMGTools/H2TauTau/limits2/tauTau/"

boosted = []
vbf = []

dirList = os.listdir(os.getcwd())
for fname in dirList:
  if not(os.path.isdir(fname)) : continue
  if str(fname).find("BOOSTED") > 0 : 
    boosted.append(fname)
  elif str(fname).find("VBF") > 0  :
    vbf.append(fname)

print 'BOOSTED'
for b1 in boosted :
  print b1
print 'VBF'
for v1 in vbf :
  print v1

for b in boosted :
  print 'BOOSTED folder: \t', b
  os.chdir(baseDir+"/"+str(b))
  os.system("python ~/.utils/plotter2012.py")
  os.system("python ~/.utils/merger_2012.py")
  os.system("rm LimitInputs/tauTau_2012_SM2_mH*.root")
  os.system("cp LimitInputs/tauTau_2012_SM1_mH*.root "+tauTauDir)
  os.chdir(limitDir)
  os.system("root -l -b createDataCards_diTau_2012.C")
  os.system("bash computeLimits_diTau.sh")
  #os.system("root -l -b plotLimits_SM1_diTau.C")
  os.system("mv "+tauTauDir+"/* "+baseDir+"/"+str(b)+"/LimitInputs")
  os.chdir(baseDir)

for v in vbf :
  print 'VBF folder: \t', v
  os.chdir(baseDir+"/"+str(v))
  os.system("python ~/.utils/plotter2012.py")
  os.system("python ~/.utils/merger_2012.py")
  os.system("rm LimitInputs/tauTau_2012_SM1_mH*.root")
  os.system("cp LimitInputs/tauTau_2012_SM2_mH*.root "+tauTauDir)
  os.chdir(limitDir)
  os.system("root -l -b createDataCards_diTau_2012.C")
  os.system("bash computeLimits_diTau.sh")
  #os.system("root -l -b plotLimits_SM2_diTau.C")
  os.system("mv "+tauTauDir+"/* "+baseDir+"/"+str(v)+"/LimitInputs")
  os.chdir(baseDir)
