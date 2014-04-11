from ROOT import TFile, TH1F, gDirectory, TCanvas
import os

WJets  = TFile.Open('/afs/cern.ch/work/m/manzoni/public/DiTau2012June5_5_1fb_nominal/WJets/H2TauTauTreeProducerTauTau/H2TauTauTreeProducerTauTau_tree.root'                      ,'read')
gDirectory.cd()
treeWJets = gDirectory.FindObjectAny('H2TauTauTreeProducerTauTau')
nVertWJets = TH1F( 'nVert_WJets', 'nVert_WJets', 50, 0, 50 )
treeWJets.Project( 'nVert_WJets', 'nVert', '')
nVertWJets.Scale(1/nVertWJets.Integral())

W3Jets = TFile.Open('/afs/cern.ch/work/m/manzoni/public/DiTau2012June5_5_1fb_nominal/W3Jets/H2TauTauTreeProducerTauTau/H2TauTauTreeProducerTauTau_tree.root'                     ,'read')
gDirectory.cd()
treeW3Jets = gDirectory.FindObjectAny('H2TauTauTreeProducerTauTau')
nVertW3Jets = TH1F( 'nVert_W3Jets', 'nVert_W3Jets', 50, 0, 50 )
treeW3Jets.Project( 'nVert_W3Jets', 'nVert', '')
nVertW3Jets.Scale(1/nVertW3Jets.Integral())

DataA  = TFile.Open('/afs/cern.ch/work/m/manzoni/public/DiTau2012June5_5_1fb_nominal/data_Run2012B_PromptReco_v1/H2TauTauTreeProducerTauTau/H2TauTauTreeProducerTauTau_tree.root','read')
gDirectory.cd()
treeDataA = gDirectory.FindObjectAny('H2TauTauTreeProducerTauTau')
nVertDataA = TH1F( 'nVert_DataA', 'nVert_DataA', 50, 0, 50 )
treeDataA.Project( 'nVert_DataA', 'nVert', '')
nVertDataA.Scale(1/nVertDataA.Integral())

DataB  = TFile.Open('/afs/cern.ch/work/m/manzoni/public/DiTau2012June5_5_1fb_nominal/data_Run2012B_PromptReco_v1/H2TauTauTreeProducerTauTau/H2TauTauTreeProducerTauTau_tree.root','read')
gDirectory.cd()
treeDataB = gDirectory.FindObjectAny('H2TauTauTreeProducerTauTau')
nVertDataB = TH1F( 'nVert_DataB', 'nVert_DataB', 50, 0, 50 )
treeDataB.Project( 'nVert_DataB', 'nVert', '')
nVertDataB.Scale(1/nVertDataB.Integral())

print nVertDataB.GetName()
nVertDataB.Add(nVertDataA)
data = nVertDataB.Clone()
data.Scale(1/data.Integral())

weightWJets = data.Clone()
weightWJets.Divide(data,nVertWJets,1,1)

weightW3Jets = data.Clone()
weightW3Jets.Divide(data,nVertW3Jets,1,1)

print '###################################'
print '###   WJets'
print '###################################'
for bin in range(weightWJets.GetNbinsX()) :
  print 'w[', bin, ']\t=',weightWJets.GetBinContent(bin),';'

print '###################################'
print '###   W3Jets'
print '###################################'
for bin in range(weightW3Jets.GetNbinsX()) :
  print 'w[', bin, ']\t=',weightW3Jets.GetBinContent(bin),';'



'''
histos = []

dict = {DataA:'DataA',DataB:'DataB',WJets:'WJets',W3Jets:'W3Jets'}
for sample in [DataA,DataB,WJets,W3Jets] :
  print dict[sample]
  tree = gDirectory.FindObjectAny('H2TauTauTreeProducerTauTau')
  nVert = TH1F( 'nVert_'+dict[sample], 'nVert_'+dict[sample], 50, 0, 50 )
  tree.Project( 'nVert_'+dict[sample], 'nVert', '')
  nVert.Scale(1/nVert.Integral())
  histos.append(nVert)
  c = TCanvas()
  nVert.Draw()
  c.SaveAs(nVert.GetName()+'.png')
  del tree

for h in histos :
  if h.GetName() == 'nVert_DataA' :
    data = h.Clone()
  if h.GetName() == 'nVert_DataB' :
    data.Add(h)
  if h.GetName() == 'nVert_WJets' :
    WJets = h.Clone()
  if h.GetName() == 'nVert_W3Jets' :
    W3Jets = h.Clone()

weightWJets = data.Clone()
weightWJets.Divide(data,WJets,1,1)

weightW3Jets = data.Clone()
weightW3Jets.Divide(data,W3Jets,1,1)

print '###################################'
print '###   WJets'
print '###################################'
for bin in range(weightWJets.GetNbinsX()) :
  print 'w[', bin, ']\t=',weightWJets.GetBinContent(bin),';'

print '###################################'
print '###   W3Jets'
print '###################################'
for bin in range(weightW3Jets.GetNbinsX()) :
  print 'w[', bin, ']\t=',weightW3Jets.GetBinContent(bin),';'
'''
