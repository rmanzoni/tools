#!/usr/bin/python

'''
For each template in a given datacard,
collapses all bins into one only.
Effectively transforms a shape analysis into a
counting experiment.

Datacard structure must me

datacard.root
    |
    |__ category 1
    |      |
    |      |__ template 1
    |      |
    |      |__ template 2
    |      |
    |      |__ ...
    |__ category 2
    |      |
    |      |__ template 1
    |      |
    |      |__ template 2
    |      |
    |      |__ ...
    |__ ...

'''

import ROOT
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('INPUT_DATACARD', help = 'input datacard to be collapsed')
args = parser.parse_args()

file_in  = ROOT.TFile.Open(args.INPUT_DATACARD,'r')
file_out = ROOT.TFile.Open(args.INPUT_DATACARD.replace('.root','-onebin.root'),'recreate')

file_in.cd()
dirList = ROOT.gDirectory.GetListOfKeys()

# not doable in python < 2.7
# histos_in = {key.GetName():[] for key in dirList}

histos_in = {}
for key in dirList:
  histos_in[key.GetName()] = []

for k, v in histos_in.items():
  file_in.cd(k)
  dirList = ROOT.gDirectory.GetListOfKeys()
  for key in dirList:
    histo = ROOT.gDirectory.FindObjectAny(key.GetName())
    histo.Rebin(histo.GetNbinsX())
    v.append(histo)
  file_in.cd()

for k, v in histos_in.items():
  file_out.cd()
  file_out.mkdir(k)
  file_out.cd(k)
  for histo in v:
    histo.Write()

file_in.Close()
file_out.Close()
