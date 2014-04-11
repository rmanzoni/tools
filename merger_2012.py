import os
import ROOT
from ROOT import gROOT, gStyle, TFile, gDirectory

gROOT.SetBatch(True)


for mass in [110,115,120,125,130,135,140,145] :
#for mass in [125] :
  print "Higgs mass =", str(mass)
  # search in current dir
  matches = []
  dirList = os.listdir(os.getcwd())
  for fname in dirList:
    if str(fname).find('mH'+str(mass)) > 0 and str(fname).find('for_smoothing_') < 0 :
      if ( str(fname).find("BOOSTED") > 0 or str(fname).find("VBF") > 0 ) :
        matches.append(fname)

  for t in ["VBF","BOOSTED"] :
  
    Files = []

    for m in matches :
      if str(m).find(t) > 0 :
        if str(m).find("svfitMass.root") > 0 :
          noShift = TFile.Open(m,'read')
          Files.append(noShift)
        elif str(m).find("svfitMass*1.03.root") > 0 :
          upShift = TFile.Open(m,'read')
          Files.append(upShift)
        elif str(m).find("svfitMass*0.97.root") > 0 :
          doShift = TFile.Open(m,'read')
          Files.append(doShift)
    
    if t == "VBF" :
      cat = "SM2"
    elif t == "BOOSTED" :
      cat = "SM1"

    print 'category: ',t, cat
    
    folderName = "LimitInputs"
    folderList = os.listdir(os.getcwd())
    found = False
    for f1 in folderList :
      if str(f1) == folderName :
        found = True

    if found == False :
      os.mkdir(folderName)
    
    if str(m).find(t) < 0 : continue
    
    Shifted = TFile.Open(str(folderName+"/tauTau_2012_"+cat+"_mH"+str(mass)+".root"),'recreate')
    Shifted.mkdir(str("tauTau_2012_"+cat))
  
    for h in Files :
      print 'File name: ',h.GetName() 
      h.cd(str("tauTau_"+cat))
      dirList = gDirectory.GetListOfKeys()
      for k1 in dirList :
        histo = k1.ReadObj()
        Shifted.cd(str("tauTau_2012_"+cat))
        histo.Write()
  
    for j in Files :
      j.Close()
      
    Shifted.Close()

print '+++++++++++'
print '+ end job +'
print '+++++++++++'


# import fnmatch
# search through dir and subdirs
# matches = []
# for root, dirnames, filenames in os.walk(os.getcwd()):
#   for filename in fnmatch.filter(filenames, '*VBF*'):
#       matches.append(os.path.join(root, filename))
