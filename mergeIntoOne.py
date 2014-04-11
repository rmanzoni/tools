import os
import ROOT
import math
import copy
import array
from ROOT import gROOT, gStyle, TFile, gDirectory, Math

gROOT.SetBatch(True)

grandeFile = TFile.Open('htt_tt.inputs-sm-8TeV.root','recreate')
grandeFile.mkdir("tauTau_boost")
grandeFile.mkdir("tauTau_vbf")
#grandeFile.mkdir("tauTau_incl")
#grandeFile.mkdir("tauTau_vh")

scaleSignalggH = {          \
     "ggH110":25.04*8.02e-2,\
     "ggH115":22.96*7.65e-2,\
     "ggH120":21.13*7.10e-2,\
     "ggH125":19.52*6.37e-2,\
     "ggH130":18.07*5.48e-2,\
     "ggH135":16.79*4.52e-2,\
     "ggH140":15.63*3.54e-2,\
     "ggH145":14.59*2.61e-2,\
              }

scaleSignalvbfH = {          \
     "qqH110":1.791*8.02e-2,\
     "qqH115":1.709*7.65e-2,\
     "qqH120":1.632*7.10e-2,\
     "qqH125":1.559*6.37e-2,\
     "qqH130":1.490*5.48e-2,\
     "qqH135":1.425*4.52e-2,\
     "qqH140":1.365*3.54e-2,\
     "qqH145":1.306*2.61e-2,\
              }
              
scaleSignalVH = {          \
    "VH110":(1.060 +0.5869+0.1887) *8.02e-2,\
    "VH115":(0.9165+0.5117+0.1663) *7.65e-2,\
    "VH120":(0.7859+0.4483+0.1470) *7.10e-2,\
    "VH125":(0.6966+0.3943+0.1302) *6.37e-2,\
    "VH130":(0.6095+0.3473+0.1157) *5.48e-2,\
    "VH135":(0.5351+0.3074+0.1031) *4.52e-2,\
    "VH140":(0.4713+0.2728+0.09207)*3.54e-2,\
    "VH145":(0.4164+0.2424+0.08246)*2.61e-2,\
              }
   
   
doIscale = True
#doIscale = False
           
for mass in [110,115,120,125,130,135,140,145] :
#for mass in [125] :

  print "Higgs mass =", str(mass)
  # search in current dir
  matches = []
  dirList = os.listdir(os.getcwd())
  for fname in dirList:
    if str(fname).find('mH'+str(mass)) > 0 :
      if ( ( str(fname).find("_SM1_") > 0 or str(fname).find("_SM2_") > 0 or str(fname).find("_SM0_") > 0 or str(fname).find("_SM3_") > 0 ) and ( str(fname).find(".root") > 0 ) ) :
        matches.append(fname)


  #for t in ["_SM1_","_SM2_","_SM0_","_SM3_"] :
  for t in ["_SM1_","_SM2_"] : 
  
    Files = []
    
    print matches
    
    for m in matches :
      if str(m).find(t) > 0 :
        print 'file: ', str(m)
        if str(m).find("_SM1_") > 0: 
          folder = "tauTau_2012_SM1"
          folderNew = "tauTau_boost"
        if str(m).find("_SM2_") > 0: 
          folder = "tauTau_2012_SM2"
          folderNew = "tauTau_vbf"
        if str(m).find("_SM0_") > 0: 
          folder = "tauTau_2012_SM1"
          folderNew = "tauTau_incl"
        if str(m).find("_SM3_") > 0: 
          folder = "tauTau_2012_SM1"
          folderNew = "tauTau_vh"
        
        myFile = TFile.Open(m,'read')
        gDirectory.cd(folder)
        
        dirList = gDirectory.GetListOfKeys()
        
        print 'mass', mass 
        if mass == 125 :
          for k1 in dirList :
            #histo = k1.ReadObj()
            histo = copy.deepcopy(k1.ReadObj())
            print 'name ', str(histo.GetName())	
            if str(histo.GetName()) == 'QCD' :
              for bin in range(histo.GetNbinsX()) :
                if histo.GetBinContent(bin) < 0.001 :
                  histo.SetBinContent(bin,0.001) 
                  alpha = 1 - 0.6827  ### 68% quantile of Poisson distributoin
                  #binError = 0.20*Math.gamma_quantile_c(alpha/2,1,1)
                  binError = 1. ### as the other guys do, scale factor < 1. ==> good
                  histo.SetBinError(bin,binError) 
                #print histo.GetName(),histo.GetBinContent(bin)               
                #print histo.GetName(),histo.GetBinError(bin)               
            
            if str(histo.GetName()) == 'ZTT' :
              alpha = 1 - 0.6827  ### 68% quantile of Poisson distributoin
              for bin in range(histo.GetNbinsX()) :
                if histo.GetBinContent(bin) < 0.01 :
                  histo.SetBinContent(bin,0.01) 
                  #binError = 1.2*Math.gamma_quantile_c(alpha/2,1,1)
                  #binError = 0.5*Math.gamma_quantile_c(alpha/2,1,1)
                  binError = 1.  ### as the other guys do, scale factor < 1. ==> good
                  histo.SetBinError(bin,binError) 
                print bin,'\t con',histo.GetName(),histo.GetBinContent(bin) 
                print bin,'\t err',histo.GetName(),histo.GetBinError(bin)               
            
            if str(histo.GetName()).find('SM') >= 0: 
              if doIscale : scala = 1/scaleSignalggH["ggH"+str(mass)]
              if doIscale : histo.Scale(scala)
              newName = str(histo.GetName()).replace('SM','ggH')
              print 'NEW name ', str(histo.GetName()), newName
              histo.SetName(newName)
            if str(histo.GetName()).find('VBF') >= 0:
              if doIscale : scala = 1/scaleSignalvbfH["qqH"+str(mass)]
              if doIscale : histo.Scale(scala)
              newName = str(histo.GetName()).replace('VBF','qqH')
              histo.SetName(newName)
            if str(histo.GetName()).find('VH') >= 0:
              if doIscale : scala = 1/scaleSignalVH["VH"+str(mass)]
              if doIscale : histo.Scale(scala)
            grandeFile.cd(folderNew)
            histo.Write()
            del histo
          gDirectory.cd('..')
        else :
          for k1 in dirList :
            if ( str(k1).find(str(mass)) < 0 or str(k1).find(str(mass)) < 0 ) : continue
            histo = copy.deepcopy(k1.ReadObj())
            if str(histo.GetName()).find('SM') >= 0: 
              if doIscale : scala = 1/scaleSignalggH["ggH"+str(mass)]
              if doIscale : histo.Scale(scala)
              newName = str(histo.GetName()).replace('SM','ggH')
              print 'name ', str(histo.GetName()), newName
              histo.SetName(newName)
            if str(histo.GetName()).find('VBF') >= 0:
              if doIscale : scala = 1/scaleSignalvbfH["qqH"+str(mass)]
              if doIscale : histo.Scale(scala)
              newName = str(histo.GetName()).replace('VBF','qqH')
              histo.SetName(newName)
            if str(histo.GetName()).find('VH') >= 0:
              if doIscale : scala = 1/scaleSignalVH["VH"+str(mass)]
              if doIscale : histo.Scale(scala)
            grandeFile.cd(folderNew)
            histo.Write()
            del histo
          gDirectory.cd('..')

grandeFile.Close()

