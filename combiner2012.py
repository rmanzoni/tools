import os
import sys

baseDir = os.getcwd()
limitDir  = "/afs/cern.ch/work/m/manzoni/diTauLimit/CMGTools/CMSSW_5_2_3_patch2/src/CMGTools/H2TauTau/limits2/"
tauTauDir = "/afs/cern.ch/work/m/manzoni/diTauLimit/CMGTools/CMSSW_5_2_3_patch2/src/CMGTools/H2TauTau/limits2/tauTau/"

boosted = []
vbf = []
combined = []

dirList = os.listdir(os.getcwd())
for fname in dirList:
  if not(os.path.isdir(fname)) : continue
  if str(fname).find("BOOSTED") > 0 : 
    boosted.append(fname)
  elif str(fname).find("VBF") > 0  :
    vbf.append(fname)

for b in boosted :
  for v in vbf :
    print 'BOOSTED folder: \t', b
    print 'VBF folder: \t', v
    os.system("cp "+baseDir+"/"+str(b)+"/LimitInputs/tauTau_2012_SM1_mH*.root "+tauTauDir)
    os.system("cp "+baseDir+"/"+str(v)+"/LimitInputs/tauTau_2012_SM2_mH*.root "+tauTauDir)
    os.chdir(limitDir)
    os.system("root -l -b createDataCards_diTau_2012.C")
    os.system("bash combineCards_diTau.sh")
    os.system("bash computeLimits_diTau.sh")
    os.system("source plotLimitsScript.csh")
    newCombinedDir = baseDir+"/COMBINED_"+str(b)+"_"+str(v)
    os.system("mkdir "+newCombinedDir)
    os.system("mv "+tauTauDir+"/* "+newCombinedDir)
    os.chdir(baseDir)

