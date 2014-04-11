from ROOT import TFile, TH1F, gDirectory
import os

dirList = os.listdir(os.getcwd())
for fname in dirList:
  if os.path.isdir(fname) : continue
  if ( ( str(fname).find("BOOSTED") > 0 or str(fname).find("VBF") > 0 ) and str(fname).find(".root") > 0 ):
    if str(fname).find("PLOT") > 0 and str(fname).find("_QCD_") > 0 and str(fname).find("125") > 0  and str(fname).find("CORRELATIONS") < 0 :
      name = str(fname)
      print 'FILE TROVATO: ', name

dirList = os.listdir(os.getcwd())
for fname in dirList:
  if os.path.isdir(fname) : continue
  if ( ( str(fname).find("BOOSTED") > 0 or str(fname).find("VBF") > 0 ) and str(fname).find(".root") > 0 ):
    if str(fname).find("PLOT") > 0 and str(fname).find("_QCD_") < 0 and str(fname).find("125") > 0 :
      nameMC = str(fname)


#directories = ['nVert','l1Pt','l2Pt','dRtt']
#directories = ['dRtt','nVert','l1jetWidth','l2jetWidth','l1jetPt','l2jetPt']
#directories = ['dRtt','pThiggs','nVert']
#directories = ['l1jetPt']
directories = ['nVert','l1jetPt']

for dir in directories : 
  print '################################'
  print '##       ',dir,'                '
  print '################################'

  qcdFile = TFile.Open(name,'read')
  gDirectory.cd(dir)

  histoList = gDirectory.GetListOfKeys()

  for k1 in histoList :
    h1 = k1.ReadObj()
    if h1.GetName() == 'QCDtightSS' :
      tight = h1.Clone()
      #tight.Scale(1/h1.Integral())
    if h1.GetName() == 'QCDlooseSS' :
      loose = h1.Clone()  
      #loose.Scale(1/h1.Integral())
  
  
  MCFile = TFile.Open(nameMC,'read')
  gDirectory.cd(dir)

  histoListMC = gDirectory.GetListOfKeys()
  
  

  for k2 in histoListMC :    
    h2 = k2.ReadObj()
    if ( h2.GetName() == 'QCD' or h2.GetName() == 'SM125' or h2.GetName() == 'VBF125' or h2.GetName() == 'VH125' or h2.GetName() == 'data_obs' ) : continue

    if h2.GetName() == 'ZTT' :
      print h2.GetName(), '\t integrale:', h2.Integral()
      tightMC = h2.Clone()
      found = True
    else :
      print h2.GetName(), '\t integrale:', h2.Integral()
      tightMC.Add(h2,1)
      
  print 'tight\t',tight.Integral(),'\t tightMC\t', tightMC.Integral()
  #tight.Add(tightMC,-1)
  
  tight.Scale(1/tight.Integral())
  loose.Scale(1/loose.Integral())

  ratio = tight.Clone()
  ratio.Divide(tight,loose,1,1)

  for bin in range(ratio.GetNbinsX()) :
    if ratio.GetBinContent(bin) > 0 : binContent = ratio.GetBinContent(bin)
    else                            : binContent = 0.
    
    print 'w[', bin, ']\t=',binContent,';'
  
  del ratio
  del tight
  del loose
  qcdFile.Close()
  MCFile.Close()
  #gDirectory.cd('..')

