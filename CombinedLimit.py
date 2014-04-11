from ROOT import TFile, TH1F, gDirectory
import os
import math
import sys
import inspect
from sys import argv

script, boosted, vbf = argv


print boosted
print vbf

limitBase  = '/afs/cern.ch/work/m/manzoni/diTauLimit2012/CMSSW_4_4_4/src'
limitSetup = '/afs/cern.ch/work/m/manzoni/diTauLimit2012/CMSSW_4_4_4/src'
workDir    = os.getcwd()

booCat = boosted
vbfCat = vbf

if 'BOOSTED' not in boosted :
  print 'wrong boosted folder'
  sys.exit(0)
  
if 'VBF' not in vbf :
  print 'wrong vbf folder'
  sys.exit(0)
  
newCombDir = booCat+'_'+vbfCat



os.system('mkdir '+newCombDir)
os.system('cp '+booCat+'/LimitInputs/tauTau_2012_SM1_mH*.root '+newCombDir)
os.system('cp '+vbfCat+'/LimitInputs/tauTau_2012_SM2_mH*.root '+newCombDir)
os.chdir(workDir+'/'+newCombDir)
os.system('python ~/.utils/mergeIntoOne.py')
#os.system('python ~/.utils/removeData.py')
os.system('add_stat_shapes.py htt_tt.inputs-sm-8TeV.root htt_tt.inputs-sm-8TeV.root --filter "QCD" --prefix CMS_htt_tt_bb --threshold -100 > qcd_syst.txt')
os.system('add_stat_shapes.py htt_tt.inputs-sm-8TeV.root htt_tt.inputs-sm-8TeV.root --filter "ZTT" --prefix CMS_htt_tt_bb --threshold -100 > ztt_syst.txt')
os.system('python ~/.utils/binBybin.py')

os.system('cp htt_tt.inputs-sm-8TeV.root '+limitBase+'/HiggsAnalysis/HiggsToTauTau/setup/tt')

for mass in ['110','115','120','125','130','135','140','145'] :
#for mass in ['125'] :
  os.chdir(limitBase)
  os.system('setup-datacards.py --channels="tt" -p "8TeV" '+mass+' --sm-categories-tt="0 1"')
  os.system('setup-htt.py -o MY-LIMITS '+mass+' --channels="tt" -p "8TeV" -i auxiliaries/datacards/ --sm-categories-tt="0 1"')
  os.system("limit.py --expectedOnly --asymptotic --userOpt '-t-1 --minosAlgo stepping' MY-LIMITS/tt/"+mass+" >& MY-LIMITS/tt/"+mass+"/exp"+mass+".txt")
  os.system('mv MY-LIMITS/tt/'+mass+'/*txt '+workDir+'/'+newCombDir)
  os.system('mv MY-LIMITS/tt/'+mass+'/*root '+workDir+'/'+newCombDir)
