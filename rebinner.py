import os
import ROOT
import array
import copy
from ROOT import gROOT, gStyle, TFile, gDirectory

import inspect

def lineno():
    '''Returns the current line number in our program.'''
    return inspect.currentframe().f_back.f_lineno

gROOT.SetBatch(True)

binningB = array.array('d')
for bin in (0,10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200,225,250,275,300,325,350):
   binningB.append(bin)

binningV = array.array('d')
for bin in (0,20,40,60,80,100,120,140,160,180,200,250,300,350):
   binningV.append(bin)

binningVH = array.array('d')
for bin in (0,15,30,45,60,75,90,105,120,135,150,165,180,195,210,250,300,350):
   binningVH.append(bin)

grandeFile = TFile.Open('htt_tt.inputs-sm-8TeV.root','read')

histosB = []
histosV = []

for directory, binning, hists in [ ['tauTau_boost',binningB,histosB],['tauTau_vbf',binningV,histosV] ] :
  print directory
  print binning
  gDirectory.cd(directory)
  dirList = gDirectory.GetListOfKeys()
  for k1 in dirList :
    histo = copy.deepcopy(k1.ReadObj())
    if histo.GetNbinsX() > 0:
      histo = histo.Rebin(len(binning)-1,histo.GetName(),binning)
      histo2 = copy.deepcopy(histo)
      for bin in range(histo2.GetNbinsX()+1) :
        if 'QCD' in histo2.GetName() or 'ZTT' in histo2.GetName() and not 'tau' in histo2.GetName():
          if histo2.GetBinContent(bin)<0.001:
            histo2.SetBinContent(bin,0.001)
            histo2.SetBinError(bin,1.)
      hists.append(histo2)
  gDirectory.cd('..')

grandeFile.Close()


fileFinale = TFile.Open('htt_tt.inputs-sm-8TeV-rebinned.root','recreate')
gDirectory.mkdir('tauTau_boost')
gDirectory.cd('tauTau_boost')
for h in histosB :
  h.Write()
gDirectory.cd('..')
gDirectory.mkdir('tauTau_vbf')
gDirectory.cd('tauTau_vbf')
for h in histosV :
  h.Write()

fileFinale.Close()

os.system('cp htt_tt.inputs-sm-8TeV.root htt_tt.inputs-sm-8TeV-notRebinned.root')
os.system('cp htt_tt.inputs-sm-8TeV-rebinned.root htt_tt.inputs-sm-8TeV.root')

