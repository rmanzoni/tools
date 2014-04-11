from ROOT import TFile, TH1F, gDirectory
import os
import math

os.system('cp htt_tt.inputs.root htt_tt.inputs.root.backup')


#ShapeBoost   = TFile.Open('QCDShapeUncertainty_plot_BOOSTED_svfitMass.root','read')
#gDirectory.cd()
shapeBoost = []
#shapeHistBoost = gDirectory.FindObjectAny('UncDown')

#ShapeVBF     = TFile.Open('QCDShapeUncertainty_plot_VBF_svfitMass.root','read')
#gDirectory.cd()
shapeVBF = []
#shapeHistVBF = gDirectory.FindObjectAny('UncDown')


LimiInput = TFile.Open('htt_tt.inputs.root','update')
gDirectory.cd('tauTau_boost')

dirList = gDirectory.GetListOfKeys()

qcdreference = gDirectory.FindObjectAny('QCD')
intBoost = qcdreference.Integral()

for bin in range(qcdreference.GetNbinsX()) :
  shapeBoost.append(1)
  #shapeBoost.append(abs(shapeHistBoost.GetBinContent(shapeHistBoost.FindFixBin(qcdreference.GetBinCenter(bin)))))
  print qcdreference.GetNbinsX(),bin, shapeBoost[bin]
  
for h1 in dirList[:] : 
  histo = h1.ReadObj()
  if h1.GetName().find('htt_tt_qcd') > 0 :
    name = h1.GetName().replace('htt_tt_qcd', 'htt_tt_boost_qcd')
    bin=int(name.split("_")[-1].strip("UpDown"))
    print name,bin,pow(qcdreference.GetBinContent(bin)-histo.GetBinContent(bin),2),pow(qcdreference.GetBinContent(bin)*shapeBoost[bin-1],2)
    squaredsum = math.sqrt(pow(qcdreference.GetBinContent(bin)-histo.GetBinContent(bin),2)+pow(qcdreference.GetBinContent(bin)*shapeBoost[bin-1],2))
    if name.find('Up')>0:
       histo.SetBinContent(bin, qcdreference.GetBinContent(bin) + squaredsum)
    else:
       histo.SetBinContent(bin, qcdreference.GetBinContent(bin) - squaredsum)
    histo.SetName(name.replace('htt_tt_boost_qcd_QCD_bin','htt_tt_bb'))
    histo.Write()
    h1.Delete()

gDirectory.cd('..')


gDirectory.cd('tauTau_vbf')

dirList = gDirectory.GetListOfKeys()

qcdreference = gDirectory.FindObjectAny('QCD')
intVbf = qcdreference.Integral()

for bin in range(qcdreference.GetNbinsX())  :
  shapeVBF.append(1)
  #shapeVBF.append(abs(shapeHistVBF.GetBinContent(shapeHistVBF.FindFixBin(qcdreference.GetBinCenter(bin)))))
  print qcdreference.GetNbinsX(),bin, shapeVBF[bin]

for h1 in dirList[:] : 
  histo = h1.ReadObj()
  if h1.GetName().find('htt_tt_qcd') > 0 :
    name = h1.GetName().replace('htt_tt_qcd', 'htt_tt_vbf_qcd')
    bin=int(name.split("_")[-1].strip("UpDown"))
    print name,bin,pow(qcdreference.GetBinContent(bin)-histo.GetBinContent(bin),2),pow(qcdreference.GetBinContent(bin)*shapeVBF[bin-1],2)
    squaredsum = math.sqrt(pow(qcdreference.GetBinContent(bin)-histo.GetBinContent(bin),2)+pow(qcdreference.GetBinContent(bin)*shapeVBF[bin-1],2))
    #squaredsum += 0.5
    if name.find('Up')>0:
       histo.SetBinContent(bin, qcdreference.GetBinContent(bin) + squaredsum)
    else:
       histo.SetBinContent(bin, qcdreference.GetBinContent(bin) - squaredsum)
    histo.SetName(name.replace('htt_tt_vbf_qcd_QCD_bin','htt_tt_vb'))
    histo.Write()
    h1.Delete()

LimiInput.Close()
