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

limitBase  = os.environ['CMSSW_BASE'] 
limitSetup = os.environ['CMSSW_BASE'] 
workDir    = os.getcwd()

print limitBase
print limitSetup
print workDir

dirList = os.listdir(workDir)
for fname in dirList:
  if not(os.path.isdir(fname)) : continue
  if str(fname).find("BOOSTED") > 0 and str(fname).find("VBF") < 0 : 
    boosted.append(fname)
  elif str(fname).find("VBF") > 0 and str(fname).find("BOOSTED") < 0:
    vbf.append(fname)

for b in boosted :
  os.chdir(workDir+'/'+b)
  os.system('python ~/.utils/plotter2012.py')
  os.system('python ~/.utils/smoother.py')  
  os.system('python ~/.utils/merger_2012.py')
  os.chdir(workDir+'/'+b+'/LimitInputs')
  os.system('python ~/.utils/mergeIntoOne.py')
  os.system('python ~/.utils/rebinner.py')
  #os.system('python ~/.utils/removeData.py')
  os.system('add_stat_shapes.py htt_tt.inputs-sm-8TeV.root htt_tt.inputs-sm-8TeV.root --filter "QCD" --prefix CMS_htt_tt_bb --threshold 0.01 > qcd_syst.txt')
  os.system('add_stat_shapes.py htt_tt.inputs-sm-8TeV.root htt_tt.inputs-sm-8TeV.root --filter "ZTT" --prefix CMS_htt_tt_bb --threshold 0.01 > ztt_syst.txt')
  #os.system('scale2SM.py -i htt_tt.inputs-sm-8TeV.root -s "ggH, qqH, VH" -e 8 -v 125 ')
  os.system('python ~/.utils/binBybin.py')
  os.system('cp htt_tt.inputs-sm-8TeV.root '+limitBase+'/src/HiggsAnalysis/HiggsToTauTau/setup/tt')
  
  #for mass in ['110','115','120','125','130','135','140','145'] :
  for mass in ['125'] :
    os.chdir(limitBase+'/src')
    os.system('setup-datacards.py --channels="tt" -p "8TeV" '+mass+' --sm-categories-tt="0"')
    os.system('setup-htt.py -o MY-LIMITS '+mass+' --channels="tt" -p "8TeV" -i auxiliaries/datacards/ --sm-categories-tt="0"')
    os.system("limit.py --expectedOnly --asymptotic --userOpt '-t-1 --minosAlgo stepping' MY-LIMITS/tt/"+mass+" >& MY-LIMITS/tt/"+mass+"/exp"+mass+".txt")
    os.system('mv MY-LIMITS/tt/'+mass+'/*txt ' +workDir+'/'+b+'/LimitInputs')
    os.system('mv MY-LIMITS/tt/'+mass+'/*root '+workDir+'/'+b+'/LimitInputs')
    os.system('rm '+limitBase+'/src/auxiliaries/datacards/sm/htt_tt/htt_tt*')
  
  os.chdir(workDir)





#add_bbb_errors.py tt:8TeV:00,01:QCD,ZTT --input-dir setup --output-dir setup_bbb --threshold 0.10
#add_stat_shapes.py htt_tt.inputs-sm-8TeV.root htt_tt.inputs-sm-8TeV.root --filter "QCD" --prefix CMS_htt_tt_bb --threshold 0.01 > qcd_syst.txt
#add_stat_shapes.py htt_tt.inputs-sm-8TeV.root htt_tt.inputs-sm-8TeV.root --filter "ZTT" --prefix CMS_htt_tt_bb --threshold 0.01 > ztt_syst.txt

