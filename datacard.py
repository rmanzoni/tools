import os
from sys  import argv     as av
from copy import deepcopy as dc
from ROOT import TFile, gDirectory

if len(av) < 2 or av[1] == 'diTauJet':
  os.system('python $CMSSW_BASE/src/CMGTools/H2TauTau/python/proto/plot_H2TauTauDataMC_diTau.py /afs/cern.ch/user/m/manzoni/public/diTau_Feb8_nom  $CMSSW_BASE/src/CMGTools/H2TauTau/Colin/test_diTau_2012c_nom_gold_cfg.py  -S nom' )
  os.system('python $CMSSW_BASE/src/CMGTools/H2TauTau/python/proto/plot_H2TauTauDataMC_diTau.py /afs/cern.ch/user/m/manzoni/public/diTau_Feb8_down $CMSSW_BASE/src/CMGTools/H2TauTau/Colin/test_diTau_2012c_down_gold_cfg.py -S down')
  os.system('python $CMSSW_BASE/src/CMGTools/H2TauTau/python/proto/plot_H2TauTauDataMC_diTau.py /afs/cern.ch/user/m/manzoni/public/diTau_Feb8_up   $CMSSW_BASE/src/CMGTools/H2TauTau/Colin/test_diTau_2012c_up_gold_cfg.py   -S up'  )

elif av[1] == 'diTau1p' :
  os.system('python $CMSSW_BASE/src/CMGTools/H2TauTau/python/proto/plot_H2TauTauDataMC_diTau.py /afs/cern.ch/work/m/manzoni/public/diTau1pFeb8/diTau_Feb8_1p_nom  $CMSSW_BASE/src/CMGTools/H2TauTau/Colin/test_diTau_2012c_gold_cfg.py -S nom' )
  os.system('python $CMSSW_BASE/src/CMGTools/H2TauTau/python/proto/plot_H2TauTauDataMC_diTau.py /afs/cern.ch/work/m/manzoni/public/diTau1pFeb8/diTau_Feb8_1p_up   $CMSSW_BASE/src/CMGTools/H2TauTau/Colin/test_diTau_2012c_gold_cfg.py -S up'  )
  os.system('python $CMSSW_BASE/src/CMGTools/H2TauTau/python/proto/plot_H2TauTauDataMC_diTau.py /afs/cern.ch/work/m/manzoni/public/diTau1pFeb8/diTau_Feb8_1p_down $CMSSW_BASE/src/CMGTools/H2TauTau/Colin/test_diTau_2012c_gold_cfg.py -S down')

else : pass 

folders = []

dirList = os.listdir(os.getcwd())
for fname in dirList:
  if os.path.isdir(fname) :
    if 'CMS_2012_' not in fname : continue
    fname = fname.replace('_nom' ,'')
    fname = fname.replace('_down','')
    fname = fname.replace('_up'  ,'')
    folders.append(fname)

folders = set(folders)

hists = {'boost':[], 'vbf':[]}

for fol in folders :
  print fol
  if 'BOOSTED' in fol : cat = 'boost'
  if 'VBF'     in fol : cat = 'vbf'
  
  f1 = TFile(fol+'_nom/'+fol+'_nom_tauTau_'+cat+'_svfitMass.root','read')
  dir = 'tauTau_'+cat
  f1.cd(dir)
  dirList = gDirectory.GetListOfKeys()
  for k1 in dirList: 
    h1 = k1.ReadObj()
    hh = dc(h1)
    if 'ZTT' in hh.GetName() or 'QCD' in hh.GetName() :
      for bin in range(hh.GetNbinsX()+1) :
        if hh.GetBinError(bin) == 0 :
          hh.SetBinError(bin, 1./10.) 
    hists[cat].append(hh)
  f1.Close()  
  
  f2 = TFile(fol+'_up/'+fol+'_up_tauTau_'+cat+'_svfitMass.root','read') 
  dir = 'tauTau_'+cat
  f2.cd(dir)
  dirList = gDirectory.GetListOfKeys()
  for k2 in dirList: 
    h2 = k2.ReadObj()
    if 'ZTT' in h2.GetName() or 'qqH' in h2.GetName() or 'ggH' in h2.GetName() or 'VH' in h2.GetName() :
      hh = dc(h2)
      hh.SetName(hh.GetName()+'_CMS_scale_t_tautau_8TeVUp')
      hists[cat].append(hh)
  f2.Close()  

  f3 = TFile(fol+'_down/'+fol+'_down_tauTau_'+cat+'_svfitMass.root','read')
  dir = 'tauTau_'+cat
  f3.cd(dir)
  dirList = gDirectory.GetListOfKeys()
  for k3 in dirList: 
    h3 = k3.ReadObj()
    if 'ZTT' in h3.GetName() or 'qqH' in h3.GetName() or 'ggH' in h3.GetName() or 'VH' in h3.GetName() :
      hh = dc(h3)
      hh.SetName(hh.GetName()+'_CMS_scale_t_tautau_8TeVDown')
      hists[cat].append(hh)
  f3.Close()  


tot = TFile('htt_tt.inputs-sm-8TeV.root','recreate')
for d in hists.keys():
  tot.mkdir('tauTau_'+d)
  tot.cd('tauTau_'+d)
  for h in hists[d] :
    h.Write()
  tot.cd('..')  
tot.Close()  


