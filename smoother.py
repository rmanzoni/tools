import os, sys
import array
from ROOT import * 
from os import path

gROOT.Reset()
gROOT.SetStyle("Plain")
gStyle.SetOptStat(0)
gStyle.SetOptFit(0)
gStyle.SetTitleOffset(1.2,"Y")
gStyle.SetPadLeftMargin(0.18)
gStyle.SetPadBottomMargin(0.15)
gStyle.SetPadTopMargin(0.08)
gStyle.SetPadRightMargin(0.05)
gStyle.SetMarkerSize(0.5)
gStyle.SetHistLineWidth(1)
gStyle.SetStatFontSize(0.020)
gStyle.SetTitleSize(0.06, "XYZ")
gStyle.SetLabelSize(0.05, "XYZ")
gStyle.SetNdivisions(510, "XYZ")
gStyle.SetLegendBorderSize(0)

if __name__ == '__main__': 
 
 dirList = os.listdir(os.getcwd())
 for d in dirList:
   if d == 'bkp_smoother' :
      sys.exit("bkp_smoother already exists, BE CAREFUL")
      
 os.system('mkdir bkp_smoother')
 
 for d in dirList:
   if 'svfitMass' in d and '.root' in d :
     os.system('cp '+d+' bkp_smoother') 
 
 for var,sample in [("svfitMass","ZL"),("svfitMass","T") ]:   ## BOOSTED                
 #for var,sample in [("svfitMass","W"),("svfitMass","ZL"),("svfitMass","ZJ") ]:   ## BOOSTED                
 #for var,sample in [("svfitMass","W"),("svfitMass","ZL"),("svfitMass","ZJ"),("svfitMass","TT")]:   ## VBF              

   for mH in [125]:
  
    canvas = TCanvas("","",0,0,200,200)    
    
    for fname in dirList:
      if   str(fname).find("for_smoothing_mH"+str(mH)+"_"+var+".root") > 0 and str(fname).find("BOOSTED") > 0 :
        fileName = fname
        f = TFile.Open(fileName)
        print 'BOOST', fileName
        cat = 'SM1'
      elif str(fname).find("for_smoothing_mH"+str(mH)+"_"+var+".root") > 0 and str(fname).find("VBF") > 0 :
        fileName = fname
        f = TFile.Open(fileName)
        print 'VBF', fileName
        cat = 'SM2'
        
    print '\n\n'    
    print len('*** File Name: '+fileName+' *** '+var+' *** '+sample+' *** '+str(mH)+' ***')*'*'
    print '*** File Name:',fileName,'***',var,'***',sample,'***',str(mH),'***'
    print len('*** File Name: '+fileName+' *** '+var+' *** '+sample+' *** '+str(mH)+' ***')*'*'
    
    hist=f.Get("tauTau_"+cat+"_for_smoothing/"+sample)
    print 'hist',hist.GetName()
    hist.SetLineColor(1)
    hist.SetLineStyle(1)
    hist.SetFillStyle(0)
    hist.SetMarkerStyle(0)
    hist.GetYaxis().SetTitle("N")
    hist.Draw("hist")

    t=TTree('smoother','smoother')
    
    gROOT.ProcessLine(\
      "struct MyStruct{\
        Double_t svfitMass;\
        Double_t weight;\
       };")
       
    s=MyStruct()
    t.Branch('svfitMass',AddressOf(s,'svfitMass'),'svfitMass/D')
    t.Branch('weight',AddressOf(s,'weight'),'weight/D')
    
    if hist.Integral() < 0.1 : continue
    
    for b in range(hist.GetNbinsX()):
        if hist.GetBinContent(b+1)>0:
            s.svfitMass = hist.GetBinCenter(b+1)
	    s.weight = hist.GetBinContent(b+1)
            t.Fill()
    
    rho=2
    
    svfitMass = RooRealVar("svfitMass","svfitMass",0,350 ,"GeV")
    weight    = RooRealVar("weight"   ,"weight"   ,0,1000,""   )
    
    dataset   = RooDataSet("data","data",t,RooArgSet(svfitMass,weight),'','weight')
    pdf       = RooKeysPdf("pdf" ,"pdf" ,svfitMass, dataset,RooKeysPdf.NoMirror,rho)
    
    if cat == 'SM1' :
      hist2     = pdf.createHistogram("svfitMass",70,0,350)
    elif cat == 'SM2' :
      hist2     = pdf.createHistogram("svfitMass",70,0,350)
    hist2.Scale(hist.Integral()/hist2.Integral())
    hist2.Draw("lsame")

    fname2 = fileName.replace('for_smoothing_','')
    #print 'picked', fname2
    f3 = TFile.Open(fname2,'update')
    f3.cd('')
    FileList = gDirectory.GetListOfKeys()
    found = False
    for k1 in FileList:
      obj = k1.ReadObj()
      if obj.GetName() == "tauTau_"+cat :
        found = True
    if found :
      f3.cd("tauTau_"+cat)
    else :
      f3.mkdir("tauTau_"+cat)
      f3.cd("tauTau_"+cat)
    
    gDirectory.Delete(sample+';*')
    #f3.Delete('*;*')
    
#    gDirectory.FindObjectAny(sample).Delete(sample)
#    gDirectory.Delete(sample)
#     FileList2 = gDirectory.GetListOfKeys()
#     for k2 in FileList2 :
#       obj2 = k2.ReadObj()
#       print obj2.GetName(), sample 
#       if obj2.GetName() == sample :
#         obj2.Delete()

    FileList3 = gDirectory.GetListOfKeys()
    for k3 in FileList3 :
      obj3 = k3.ReadObj()
      print obj3.GetName(), sample 
         
    hist2.SetName(sample)
    hist2.Write()
    f3.cd('..')
    f3.Close()
    
    canvas.SaveAs("smoother_"+sample+".pdf")
    del canvas
 
 #os.system('mv bkp/* '+ str(os.getcwd()))
 #os.system('rm -r bkp')
    
