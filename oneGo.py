import os
import datetime

now = datetime.datetime.now()

plotDir = 'src/CMGTools/H2TauTau/python/proto'
anaDir  = 'src/CMGTools/H2TauTau/Colin'
myDir   = '$CMSSW_BASE/src/CMGTools/H2TauTau/RiccardoWD_PostAppoval/'
myDaily = '12Sept_4/' 
folders = []


os.system('cd '+myDir+myDaily)

print 'Now in', os.getcwd()
workDir = os.getcwd()
 
if os.path.isfile(os.getcwd()+'/list_of_WP.txt') :
  os.system('mv list_of_WP.txt list_of_WP.txt.backup')

os.system('python $CMSSW_BASE/'+plotDir+'/plot_H2TauTauDataMC_diTau.py $SAMPLES_IsoCand $CMSSW_BASE/'+anaDir+'/test_diTau_2012_cfg.py')

for line in open(os.getcwd()+'/list_of_WP.txt','r').readlines() :
  if 'BOOSTED' in line and 'forRW' in line:
    folders.append(line)

folders = list(set(folders))

for fol in folders :
  os.chdir(workDir+'/'+fol.replace('\n',''))
  os.system('python ~/.utils/reweighter_v2.py')
  os.chdir(workDir.replace('\n',''))

os.chdir(workDir.replace('\n',''))
os.system('python $CMSSW_BASE/'+plotDir+'/plot_H2TauTauDataMC_diTau.py $SAMPLES_IsoCand $CMSSW_BASE/'+anaDir+'/test_diTau_2012_cfg.py -W '+myDir+myDaily)





