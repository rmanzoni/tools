from ROOT import TFile, TH1F, gDirectory
import os
import math
import sys
import inspect

def lineno():
  '''Returns the current line number in our program.'''
  return inspect.currentframe().f_back.f_lineno

pairs   = []
boosted = []
vbf     = []

limitBase  = '/afs/cern.ch/work/m/manzoni/diTauLimit2012/CMSSW_4_4_4/src'
limitSetup = '/afs/cern.ch/work/m/manzoni/diTauLimit2012/CMSSW_4_4_4/src'
workDir    = os.getcwd()

dirList = os.listdir(workDir)
for fname in dirList:
  if not(os.path.isdir(fname)) : continue
  if str(fname).find("BOOSTED") > 0 and str(fname).find("VBF") < 0 : 
    boosted.append(fname)
  elif str(fname).find("VBF") > 0 and str(fname).find("BOOSTED") < 0:
    vbf.append(fname)

for v in vbf :
  os.chdir(workDir+'/'+v)
  os.system('python ~/.utils/plotter2012.py') 
  os.system('python ~/.utils/smoother.py')  
  os.system('python ~/.utils/merger_2012.py')
  os.chdir(workDir+'/'+v+'/LimitInputs')
  os.system('python ~/.utils/mergeIntoOne.py')
  os.system('python ~/.utils/rebinner.py')
  #os.system('python ~/.utils/removeData.py')
  os.system('add_stat_shapes.py htt_tt.inputs-sm-8TeV.root htt_tt.inputs-sm-8TeV.root --filter "QCD" --prefix CMS_htt_tt_1 --threshold -100 > qcd_syst.txt')
  os.system('add_stat_shapes.py htt_tt.inputs-sm-8TeV.root htt_tt.inputs-sm-8TeV.root --filter "ZTT" --prefix CMS_htt_tt_1 --threshold -100 > ztt_syst.txt')
  #os.system('scale2SM.py -i htt_tt.inputs-sm-8TeV.root -s "ggH, qqH, VH" -e 8 -v 125')
  os.system('python ~/.utils/binBybin.py')
  os.system('cp htt_tt.inputs-sm-8TeV.root '+limitBase+'/HiggsAnalysis/HiggsToTauTau/setup/tt')
  os.chdir(limitBase)
  #os.system('setup-datacards.py --channels="tt" -p "8TeV" 125 --sm-categories-tt="1"')
  #os.system('setup-htt.py -o MY-LIMITS 125 --channels="tt" -p "8TeV" -i auxiliaries/datacards/ --sm-categories-tt="1"')
  #os.system("limit.py --expectedOnly --asymptotic --userOpt '-t-1 --minosAlgo stepping' MY-LIMITS/tt/125 >& MY-LIMITS/tt/125/exp.txt")
  #os.system('mv MY-LIMITS/tt/125/*txt '+workDir+'/'+v+'/LimitInputs')
  #os.system('mv MY-LIMITS/tt/125/*root '+workDir+'/'+v+'/LimitInputs')
  #os.system('rm /afs/cern.ch/work/m/manzoni/diTauLimit2012/CMSSW_4_4_4/src/auxiliaries/datacards/sm/htt_tt/htt_tt*')

  #for mass in ['110','115','120','125','130','135','140','145'] :
  for mass in ['125'] :
    os.chdir(limitBase)
    os.system('setup-datacards.py --channels="tt" -p "8TeV" '+mass+' --sm-categories-tt="1"')
    os.system('setup-htt.py -o MY-LIMITS '+mass+' --channels="tt" -p "8TeV" -i auxiliaries/datacards/ --sm-categories-tt="1"')
    os.system("limit.py --expectedOnly --asymptotic --userOpt '-t-1 --minosAlgo stepping' MY-LIMITS/tt/"+mass+" >& MY-LIMITS/tt/"+mass+"/exp"+mass+".txt")
    os.system('mv MY-LIMITS/tt/'+mass+'/*txt ' +workDir+'/'+v+'/LimitInputs')
    os.system('mv MY-LIMITS/tt/'+mass+'/*root '+workDir+'/'+v+'/LimitInputs')
    os.system('rm /afs/cern.ch/work/m/manzoni/diTauLimit2012/CMSSW_4_4_4/src/auxiliaries/datacards/sm/htt_tt/htt_tt*')

  os.chdir(workDir)
