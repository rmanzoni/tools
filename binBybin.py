from ROOT import TFile, TH1F, gDirectory
import os
import math

LimitInput = TFile.Open('htt_tt.inputs-sm-8TeV.root','update')

gDirectory.cd('tauTau_boost')
dirList = gDirectory.GetListOfKeys()
for h1 in dirList : 
  histo = h1.ReadObj()
  if 'CMS_htt_tt_bb' in h1.GetName() :
    name = h1.GetName()
    histo.SetName(name.replace('CMS_htt_tt_bb','CMS_htt_tt0'))
    for bin in range(histo.GetNbinsX()+1) :
      if histo.GetBinContent(bin) < 0. :
        histo.SetBinContent(bin,0.)
    histo.Write()
    h1.Delete()
  #if 'CMS_scale_t' in h1.GetName() :
  #  name = h1.GetName()
  #  histo.SetName(name.replace('CMS_scale_t','CMS_scale_t_tautau_8TeV'))
  #  histo.Write()
  #  h1.Delete()
  
  
#     for n in ['ZTT','ggH','qqH','VH'] :
#       if n not in h1.GetName() : 
#         h1.Delete()
#     else : 
#       name = h1.GetName()
#       histo.SetName(name.replace('CMS_scale_t','CMS_scale_t_tautau_8TeV'))
#       histo.Write()
#       h1.Delete()


gDirectory.cd('..')
gDirectory.cd('tauTau_vbf')
dirList = gDirectory.GetListOfKeys()
for h1 in dirList : 
  histo = h1.ReadObj()
  if 'CMS_htt_tt_bb' in h1.GetName() :
    name = h1.GetName()
    histo.SetName(name.replace('CMS_htt_tt_bb','CMS_htt_tt1'))
    for bin in range(histo.GetNbinsX()+1) :
      if histo.GetBinContent(bin) < 0. :
        histo.SetBinContent(bin,0.)
    histo.Write()
    h1.Delete()
  #if 'CMS_scale_t' in h1.GetName() :
  #  name = h1.GetName()
  #  histo.SetName(name.replace('CMS_scale_t','CMS_scale_t_tautau_8TeV'))
  #  histo.Write()
  #  h1.Delete()

LimitInput.Close()
