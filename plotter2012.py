import os
import ROOT
from ROOT import gROOT, gStyle, TFile, TCanvas, gDirectory, TH1F, THStack, TLegend, TPad, TF1, TGraphAsymmErrors, gPad
import math

gROOT.SetBatch(True)
gROOT.SetStyle("Plain")
gStyle.SetOptStat(True)
#gStyle.SetPadGridX(True)
#gStyle.SetPadGridY(True)
gStyle.SetTitleX(0.1)
gStyle.SetTitleY(0.96)
gStyle.SetTitleW(0.8)

gStyle.SetTitleStyle(0)
#gStyle.SetCanvasBorderSize(0)
#gStyle.SetFrameBorderSize(0) 
gStyle.SetLegendBorderSize(0) 
gStyle.SetStatBorderSize(0)
gStyle.SetTitleBorderSize(0) 
gStyle.SetPadTickX(1)
gStyle.SetPadTickY(1)

YAxisTitle = 'evts.'
XAxisTitle = {'svfitMass'        :'m_{#tau#tau} [Gev/c^{2}]',\
              'svfitMass*1.03'   :'m_{#tau#tau} [Gev/c^{2}]',\
              'svfitMass*0.97'   :'m_{#tau#tau} [Gev/c^{2}]',\
              'tau1Mass'         :'m_{#tau_{1}} [Gev/c^{2}]',\
              'tau2Mass'         :'m_{#tau_{2}} [Gev/c^{2}]',\
              'met'              :'ME_{T} [Gev/c^{2}]',\
              'l1Pt'             :'#tau_{1} p_{T} [Gev/c]',\
              'l2Pt'             :'#tau_{2} p_{T} [Gev/c]',\
              'jet1Pt'           :'Jet_{1} p_{T} [Gev/c]',\
              'jet2Pt'           :'Jet_{2} p_{T} [Gev/c]',\
              'visMass'          :'Visible mass [Gev/c^{2}]',\
              'visMass*1.03'     :'Visible mass [Gev/c^{2}]',\
              'visMass*0.97'     :'Visible mass [Gev/c^{2}]',\
              'nVert'            :'nVert',\
              'mt'               :'m_{T} [Gev/c^{2}]',\
              'mt1'              :'#tau_{1} m_{T} [Gev/c^{2}]',\
              'mt2'              :'#tau_{2} m_{T} [Gev/c^{2}]',\
              'pThiggs'          :'Higgs p_{T} [Gev/c]',\
              'diTauPt'          :'di-#tau p_{T} [Gev/c]',\
              'nJets'            :'n Jets',\
              'l1Eta'            :'#tau_{1} #eta',\
              'l2Eta'            :'#tau_{2} #eta',\
              'jet1Eta'          :'Jet_{1} #eta',\
              'jet2Eta'          :'Jet_{2} #eta',\
              'jet1Eta-jet2Eta'  :'#Delta#eta(j_{1},j_{2})',\
              'mjj'              :'m_{jj} [Gev/c^{2}]',\
              'dRtt'             :'#DeltaR(#tau,#tau)',\
              'dPhitt'           :'#Delta#phi(#tau,#tau)',\
              'mttj'             :'m_{#tau#tau Jet}Gev/c^{2}',\
              'diTauCharge'      :'dt-#tau charge',\
              'dEtajj'           :'|#Delta#eta(j_{1},j_{2})|',\
              'dEtatt'           :'#Delta#eta(#tau,#tau)',\
              'dEtattjj'         :'#Delta#eta(jj,#tau#tau)',\
              'dPhijj'           :'#Delta#phi(j_{1},j_{2})',\
              'dPhittjj'         :'#Delta#phi(#tau#tau,j_{1}j_{2})',\
              'l1RawMVAIso'      :'#tau_{1} MVA Iso',\
              'l2RawMVAIso'      :'#tau_{2} MVA Iso',\
              'l1LooIso'         :'',\
              'l2LooIso'         :'',\
              'l1MedIso'         :'',\
              'l2MedIso'         :'',\
              'l1TigIso'         :'',\
              'l2TigIso'         :'',\
              'l1DecayMode'      :'#tau_{1} decay mode',\
              'l2DecayMode'      :'#tau_{2} decay mode',\
              'l1MedMVAIso'      :'',\
              'l1TigMVAIso'      :'',\
              'l1LooseEle'       :'',\
              'l1MVAEle'         :'',\
              'l1LooseMu'        :'',\
              'l2MedMVAIso'      :'',\
              'l2TigMVAIso'      :'',\
              'l2LooseEle'       :'',\
              'l2MVAEle'         :'',\
              'l2LooseMu'        :''\
              }

for mass in [110,115,120,125,130,135,140,145] :

  print '*********************************************'
  print '*** Plotting script for Htautau Fully Had ***'
  print '*********************************************'
  # search in current dir
  toPlot = []
  dirList = os.listdir(os.getcwd())
  for fname in dirList:
    if os.path.isdir(fname) : continue
    if str(fname).find('mH'+str(mass)) > 0 :
      if ( ( str(fname).find("BOOSTED") > 0 or str(fname).find("VBF") > 0 ) and str(fname).find(".root") > 0 ):
        if str(fname).find("PLOT") > 0 and str(fname).find("QCD") < 0 :
          toPlot.append(fname)
          print 'I\'m going to plot histos for this file: ', str(fname)


  for i1 in toPlot :

    if str(i1).find('VBF') > 0 :
      #WSample = 'W3'
      WSample = 'W'
    else :
      WSample = 'W'

    plottare = TFile.Open(str(i1),'read')
    plottare.cd()
    dirList = gDirectory.GetListOfKeys()
  
    i2 = str(i1).strip("_PLOT.root")
    folderName = str("PLOTS_"+i2)
  
    print 'You\'ll find your plots in this folder:'
    print folderName 
  
    folderList = os.listdir(os.getcwd())
    found = False
    for f1 in folderList :
      if str(f1) == folderName :
        found = True
        print '********** WARNING **********'
        print '*** FOLDER ALREADY EXISTS ***'
        print '*****************************'

    if found == False :
      os.mkdir(folderName)
  
    for i in dirList :
      if ( str(i.GetName()).find("*0.97") > 0 or str(i.GetName()).find("*1.03") > 0) : continue
      plottare.cd(str(i.GetName()))
      histoList = gDirectory.GetListOfKeys()
      ewk = gDirectory.FindObjectAny("ZJ")
      for k1 in histoList :
	    h1 = k1.ReadObj()
        
	    if str(i.GetName()) == 'dEtajj' :
	      for bin in range(23) :
	        #print 'bin', bin
	        h1.SetBinContent(47-bin,h1.GetBinContent(bin)+h1.GetBinContent(47-bin))
             
	    if ( str(h1.GetName())==WSample  or  \
		 str(h1.GetName())=="ZL"     or  \
		 str(h1.GetName())=="WW"     or  \
		 str(h1.GetName())=="ZZ"     or  \
		 str(h1.GetName())=="VV"     or  \
		 str(h1.GetName())=="WZ"     ) :
	      ewk.Add(h1)
	    if str(h1.GetName())=="ZTT" :
	      ztt = h1
	    if str(h1.GetName())=="TT" :
	      ttb = h1
	    if str(h1.GetName())=="QCD" :
	      qcd = h1
	    if str(h1.GetName())=="data_obs" :
	      data = h1
	      #for bin in range(data.GetNbinsX()+1):
              #  if data.GetBinCenter(bin+1) > 100 and data.GetBinCenter(bin+1) < 150 :
              #    data.SetBinContent(bin+1,-100)
            if str(h1.GetName())=="VBF"+str(mass) :
	      vbf = h1
	    if str(h1.GetName())=="SM"+str(mass) :
	      ggh = h1
	    if str(h1.GetName())=="VH"+str(mass) :
	      vh  = h1
        
      hig = ggh.Clone()
      hig.Add(vbf)
      hig.Add(vh)
      
      rebin = 1

      for m in [ztt,qcd,ewk,hig,ttb] :
	    m.UseCurrentStyle()
	    m.SetLineWidth(2)
	    m.Rebin(rebin)
	    m.SetTitle('')
      
      data.SetTitle('')
      data.Rebin(rebin)  

      ztt.SetFillColor(ROOT.kOrange - 4)
      qcd.SetFillColor(ROOT.kMagenta-10)
      ewk.SetFillColor(ROOT.kRed    + 2)
      ttb.SetFillColor(ROOT.kBlue   - 8)
      
      data.SetFillColor(ROOT.kWhite)
      
      ggh.SetLineColor(ROOT.kBlue)
      vbf.SetLineColor(ROOT.kRed)
      hig.SetLineColor(ROOT.kBlue)
      hig.SetLineStyle(2)
      
      c2 = TCanvas("canvas_"+str(i.GetName())+str(mass),"canvas_"+str(i.GetName()),700,700)

      c2.cd()
      stackPad = TPad('stackPad','stackPad',0.,0.,1.,1.,0,0)
      
      stackPad.Draw()
      #stackPad.SetPadTickX(1)
      #stackPad.SetPadTickY(1)
      stackPad.cd()
      #gPad.SetLeftMargin(0.12)
      
      stack = THStack("hs",str(i.GetName()))
      
      integral = 0
      
      for s1 in [qcd,ewk,ttb,ztt,hig] : #,hig] : # order matters
        stack.Add(s1)
        integral += s1.Integral()
	
      maxY = 0
      for h2 in [ewk,qcd,ztt,hig] :
        if h2.GetMaximum() > maxY :
          maxY = maxY + h2.GetMaximum()
      if data.GetMaximum() > maxY :
          maxY = data.GetMaximum()
        
      stack.SetMaximum(maxY*1.1)
      #stack.SetMaximum(6)
      stack.SetMinimum(0)
      #stack.SetTitle('CMS Preliminary 2012D         7.3 fb^{-1},   #sqrt{s}=8 TeV         #tau_{h}#tau_{h}')
      stack.SetTitle('CMS Preliminary 2012         19.4 fb^{-1},   #sqrt{s}=8 TeV         #tau_{h}#tau_{h}')     
      #stack.SetTitle('CMS Preliminary 2012         12.1 fb^{-1},   #sqrt{s}=8 TeV         #tau_{h}#tau_{h}')     
      #stack.SetTitle('CMS Preliminary 2012         11.2 fb^{-1},   #sqrt{s}=8 TeV         #tau_{h}#tau_{h}')     
      #stack.SetTitle('CMS Preliminary 2012         5.1 fb^{-1},   #sqrt{s}=8 TeV         #tau_{h}#tau_{h}')
      stack.Draw("HIST")
      if str(i.GetName()) == 'dEtajj' :
        stack.GetXaxis().SetRangeUser(0,12)    
      stack.GetXaxis().SetTitle(XAxisTitle[str(i.GetName())])
      stack.GetYaxis().SetTitle(YAxisTitle)
      #stack.GetYaxis().SetTitle('a.u.')
      stack.GetYaxis().SetTitleOffset(1.3)
      data.Scale(integral/data.Integral())
      data.Draw("SAME")
      
      
      l1 = TLegend(0.5,0.7,0.88,0.88)
      l1.AddEntry(data,"Observed");
      l1.AddEntry(hig,"5 x H#rightarrow#tau#tau, m_{H}= "+str(mass)+" GeV","f");
      l1.AddEntry(ztt,"Z#rightarrow#tau#tau","f");
      #l1.AddEntry(ttb,"Top","f");
      l1.AddEntry(ttb,"t#bar{t}","f");
      l1.AddEntry(ewk,"Electroweak","f");
      l1.AddEntry(qcd,"Fakes","f");
      l1.SetFillColor(0)
      #l1.SetFillColor(ROOT.kWhite)
      l1.Draw('sameAEPZ');
      
      
      sumBkg = ewk.Clone()
      for s2 in [qcd,ztt,ttb] :
        sumBkg.Add(s2)

      
      c2.SaveAs(str(folderName+"/"+i.GetName()+".pdf"))
      #c2.SaveAs(str(folderName+"/"+i.GetName()+".png"))
      del ewk
      
      #### needed to solve something broken in recent ROOT releases
      #### see http://root.cern.ch/phpBB3/viewtopic.php?f=14&t=13547
      ROOT.SetOwnership(c2, False)
      ROOT.SetOwnership(stackPad, False)
      
      del stackPad
      del c2
      
