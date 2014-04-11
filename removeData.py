import os
import ROOT
from ROOT import gROOT, gStyle, TFile, gDirectory
import inspect

def lineno():
    '''Returns the current line number in our program.'''
    print inspect.currentframe().f_back.f_lineno
    
gROOT.SetBatch(True)

grandeFile = TFile.Open('htt_tt.inputs-sm-8TeV.root','recreate')
grandeFile.mkdir("tauTau_boost")
grandeFile.mkdir("tauTau_vbf")


myFile = TFile.Open('htt_tt.inputs-sm-8TeV.root','read')
#myFile = TFile.Open('tauTau.root','read')
gDirectory.cd()

listOfDir = gDirectory.GetListOfKeys()

for fol1 in listOfDir :
  folObj = fol1.ReadObj()
  folder = folObj.GetName()

#for folder in ['tauTau_boost','tauTau_vbf'] :
#for folder in ['tauTau_boost'] :
#for folder in ['tauTau_vbf'] :
  #lineno()

  myFile.cd(folder)

  dirList = gDirectory.GetListOfKeys()
  if len(dirList) == 0 : continue
  
  found = False
  
  for h1 in dirList :
    histo = h1.ReadObj()
    #print 'nome: ', str(histo.GetName())   
    if ( str(histo.GetName()).find('ZTT') >= 0 and str(histo.GetName()).find('scale') < 0 ):
      print 'mi prendo questo:\t', histo.GetName()
      dataDummy = histo.Clone()
      #dataDummy.Clear()
      found = True
  
  added=[]
  for h2 in dirList :
    histo = h2.ReadObj()
    if ( str(histo.GetName()).find('ZTT')      < 0 and\
         str(histo.GetName()).find('data_obs') < 0 and\
         str(histo.GetName()).find('CMS')      < 0 and\
         str(histo.GetName()).find('ggH')      < 0 and\
         str(histo.GetName()).find('VH')       < 0 and\
         str(histo.GetName()).find('qqH')      < 0    \
         ) and not histo.GetName() in added:
      print 'sto sommando:\t', histo.GetName(), 'in:\t', folder
      added+=[histo.GetName()]
      dataDummy.Add(histo)

  dataDummy.SetName('data_obs')
  for bin in range(dataDummy.GetNbinsX()*3):
    binIntero = dataDummy.GetBinContent(bin)
    dataDummy.SetBinContent(bin,int(binIntero))
  

  for h3 in dirList :
    histo = h3.ReadObj()
    if str(histo.GetName()).find('data_obs') < 0 :
      grandeFile.cd(folder)
      histo.Write()
      print "data histo written"
  
  grandeFile.cd(folder)
  dataDummy.Scale(1)
  print 'integral', dataDummy.Integral()
  dataDummy.Write()
    
  myFile.cd('..')
  grandeFile.cd('..')
  
#grandeFile.Close()  
  
