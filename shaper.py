from ROOT import TFile, TH1F, gDirectory
import os

os.system('cp htt_tt.inputs.root htt_tt.inputs.root.backup')


ShapeBoost   = TFile.Open('QCDShapeUncertainty_plot_BOOSTED_svfitMass.root','read')
gDirectory.cd()
shapeBoost = []
shapeHistBoost = gDirectory.FindObjectAny('UncDown')

ShapeVBF     = TFile.Open('QCDShapeUncertainty_plot_VBF_svfitMass.root','read')
gDirectory.cd()
shapeVBF = []
shapeHistVBF = gDirectory.FindObjectAny('UncDown')


LimiInput = TFile.Open('htt_tt.inputs.root','update')
gDirectory.cd('tauTau_boost')

dirList = gDirectory.GetListOfKeys()

for h1 in dirList : 
  histo = h1.ReadObj()
  if h1.GetName().find('htt_tt_qcd') > 0 :
    name = h1.GetName().replace('htt_tt_qcd', 'htt_tt_boost_qcd')
    h1.SetName(name)


dummy = gDirectory.FindObjectAny('QCD')
intBoost = dummy.Integral()

qcdDownBoost = dummy.Clone()
qcdDownBoost.SetName('QCD_CMS_htt_tt_boost_QCDshapeDown')

qcdUpBoost = dummy.Clone()
qcdUpBoost.SetName('QCD_CMS_htt_tt_boost_QCDshapeUp')


for bin in range(dummy.GetNbinsX()) :
  shapeBoost.append(abs(shapeHistBoost.GetBinContent(shapeHistBoost.FindBin(dummy.GetBinCenter(bin+1)))))


for bin in range(dummy.GetNbinsX())  :
  shapeVBF.append(abs(shapeHistVBF.GetBinContent(shapeHistVBF.FindBin(dummy.GetBinCenter(bin+1)))))


for bin in range(dummy.GetNbinsX())  :
  bc = qcdDownBoost.GetBinContent(bin+1)
  sh = 1 - shapeBoost[bin]
  qcdDownBoost.SetBinContent(bin+1, bc*sh)

scaleDB = 1/qcdDownBoost.Integral()*intBoost
qcdDownBoost.Scale(scaleDB)
qcdDownBoost.Write()

for bin in range(dummy.GetNbinsX())  :
  bc = qcdUpBoost.GetBinContent(bin+1)
  sh = 1 + shapeBoost[bin]
  qcdUpBoost.SetBinContent(bin+1, bc*sh)

scaleUB = 1/qcdUpBoost.Integral()*intBoost
qcdUpBoost.Scale(scaleDB)
qcdUpBoost.Write()

del dummy

gDirectory.cd('..')



gDirectory.cd('tauTau_vbf')

dirList = gDirectory.GetListOfKeys()

for h1 in dirList : 
  histo = h1.ReadObj()
  if h1.GetName().find('htt_tt_qcd') > 0 :
    name = h1.GetName().replace('htt_tt_qcd', 'htt_tt_vbf_qcd')
    h1.SetName(name)

dummy = gDirectory.FindObjectAny('QCD')
intVBF = dummy.Integral()

qcdDownVBF = dummy.Clone()
qcdDownVBF.SetName('QCD_CMS_htt_tt_vbf_QCDshapeDown')

qcdUpVBF = dummy.Clone()
qcdUpVBF.SetName('QCD_CMS_htt_tt_vbf_QCDshapeUp')

for bin in range(dummy.GetNbinsX()) :
  bc = qcdDownVBF.GetBinContent(bin+1)
  sh = 1 - shapeVBF[bin]
  qcdDownVBF.SetBinContent(bin+1, bc*sh)

scaleDV = 1/qcdDownVBF.Integral()*intVBF
qcdDownVBF.Scale(scaleDV)
qcdDownVBF.Write()

for bin in range(dummy.GetNbinsX())  :
  bc = qcdUpVBF.GetBinContent(bin+1)
  sh = 1 + shapeVBF[bin]
  qcdUpVBF.SetBinContent(bin+1, bc*sh)

scaleUV = 1/qcdUpVBF.Integral()*intVBF
qcdUpVBF.Scale(scaleUV)
qcdUpVBF.Write()

del dummy



LimiInput.Close()



