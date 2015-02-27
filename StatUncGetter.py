import ROOT

class StatUncGetter(object) :

  def __init__(self, file_name_mt = 'htt_mt.inputs-mssm-8TeV-0.root',
                     file_name_et = 'htt_et.inputs-mssm-8TeV-0.root',
                     file_name_tt = 'htt_tt.inputs-mssm-8TeV-0.root'  ) :
    self.file_mt = ROOT.TFile.Open(file_name_mt,'r')
    self.file_et = ROOT.TFile.Open(file_name_et,'r')
    self.file_tt = ROOT.TFile.Open(file_name_tt,'r')
  
  def getContributionUnc(self, channel, cat, sample) :
    '''
       channel: [mt, et, tt]
       cat:     [inclusive, btag, nobtag, btag_low, btag_high, nobtag_low, nobtag_medium, nobtag_high]
       sample:  [ZTT, W, QCD, ...]
    ''' 
    if channel == 'mt' : 
      self.file_mt.cd()
      prefix = 'muTau_'
    if channel == 'et' : 
      self.file_et.cd()
      prefix = 'eleTau_'
    if channel == 'tt' : 
      self.file_tt.cd()
      prefix = 'tauTau_'
    
    ROOT.gDirectory.cd( prefix + cat )
    histo_sample = ROOT.gDirectory.FindObjectAny(sample)
    
    error = ROOT.Double()
    integral = histo_sample.IntegralAndError(-1,-1,error)
    
    return integral, error, error/integral
