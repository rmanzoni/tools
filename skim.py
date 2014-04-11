def skimming(tree):
  if ( tree.againstElectronLooseMVA3_2>0.5) : return True

  else : return False
  
def skimming2(tree):
  if ( tree.l1Pt>45 and tree.l2Pt>45 and abs(tree.l1Eta)<2.1 and abs(tree.l2Eta)<2.1 ) and\
  ( tree.l1LooseEle>0.5          and tree.l2LooseEle>0.5 )                             and\
  ( tree.l1LooseMu>0.5           and tree.l2LooseMu>0.5 )                              and\
  ( tree.l1RawDB3HIso<10.        and tree.l2RawDB3HIso<10.)                            and\
  ( tree.muon1Pt==-1             and tree.electron1Pt==-1 )                            : return True
#   ( tree.muon1Pt==-1             and tree.electron1Pt==-1 )                            and\
#   ( tree.l1TrigMatched!=0        and tree.l2TrigMatched!=0 )                           : return True

  else : return False

def skimming3(tree):
  if ( tree.l1TrigMatched_diTau>0.5) and ( tree.l2TrigMatched_diTau>0.5) : return True

  else : return False


def skimming4(tree):
  if ( tree.l1TrigMatched_diTauJet>0.5) and ( tree.l2TrigMatched_diTauJet>0.5) and ( tree.jetTrigMatched_diTauJet>0.5): return True

  else : return False

def skimming5(tree):
  if ( ( tree.l1TrigMatched_diTauJet>0.5) and ( tree.l2TrigMatched_diTauJet>0.5) and ( tree.jetTrigMatched_diTauJet>0.5) ) or\
     ( ( tree.l1TrigMatched_diTau>0.5) and ( tree.l2TrigMatched_diTau>0.5) )                                               : return True

  else : return False

def skimming6(tree):
  if ( tree.l1TrigMatched_diTauJet>0.5) and ( tree.l2TrigMatched_diTauJet>0.5) : return True

  else : return False

def skimming7(tree):
  if ( tree.againstElectronLoose_1>0.5) and ( tree.againstElectronLoose_2>0.5) and ( tree.againstMuonLoose2_1>0.5) and ( tree.againstMuonLoose2_2>0.5) : return True

  else : return False


def skimming8(tree):
  if ( tree.byCombinedIsolationDeltaBetaCorrRaw3Hits_1<1.) and ( tree.byCombinedIsolationDeltaBetaCorrRaw3Hits_2<1.) : return True

  else : return False

def skimming9(tree):
  if ( tree.jpt_1>50.) and ( tree.jeta_1<3.0 or tree.jeta_1>-3.0) : return True

  else : return False


def skimming10(tree):
  if ( (tree.l1TrigMatched_diTauJet>0.5) and (tree.l2TrigMatched_diTauJet>0.5) and (tree.jetTrigMatched_diTauJet>0.5) and (tree.jpt_1>50.) and (tree.jeta_1>-3.0 or tree.jeta_1<3.0) ) or  \
     ( (tree.l1TrigMatched_diTau   >0.5) and (tree.l2TrigMatched_diTau   >0.5)                                        and (tree.jpt_1>30.) and (tree.jeta_1>-4.7 or tree.jeta_1<4.7) ) and \
     ( (tree.againstElectronLoose_1>0.5) and (tree.againstElectronLoose_2>0.5) and (tree.againstMuonLoose_1>0.5) and ( tree.againstMuonLoose_2>0.5) )	                               : return True

  else : return False

def skimming13(tree):
  if ( (tree.l1TrigMatched_diTauJet>0.5) and (tree.l2TrigMatched_diTauJet>0.5) and (tree.jetTrigMatched_diTauJet>0.5) and (tree.jet1Pt>50.) and (tree.jet1Eta>-3.0 or tree.jet1Eta<3.0) ) or  \
     ( (tree.l1TrigMatched_diTau   >0.5) and (tree.l2TrigMatched_diTau   >0.5)                                        and (tree.jet1Pt>30.) and (tree.jet1Eta>-4.7 or tree.jet1Eta<4.7) ) and \
     ( (tree.l1LooseEle>0.5) and (tree.l2LooseEle>0.5) and (tree.l1LooseMu>0.5) and ( tree.l2LooseMu>0.5) )	                               : return True

  else : return False



def skimming11(tree):
  if (tree.againstElectronLoose_1>0.5) and (tree.againstElectronLoose_2>0.5) and (tree.againstMuonLoose_1>0.5) and ( tree.againstMuonLoose_2>0.5) : return True

  else : return False

def skimming12(tree):
  if tree.evt != 250249722 and tree.evt != 269311494 and tree.electron1Pt==-1 : return True

  else : return False

def skimming14(tree):
  if (tree.electron1Pt==-1) and ( tree.muon1Pt==-1) and (tree.nbtag==0): return True

  else : return False

def skimming15(tree):
  if (tree.electron1Pt==-1) and ( tree.muon1Pt==-1) and (tree.q_1*tree.q_2<0) and (tree.againstElectronNewLooseMVA3_2>0.5): return True

  else : return False

def skimming16(tree):
  if (tree.electron1Pt==-1) and ( tree.muon1Pt==-1) : return True

  else : return False


def skimmingVBF(tree):
  if ( tree.electron1Pt == -1                    ) and \
     ( tree.muon1Pt == -1                        ) and \
     ( tree.jet1Pt > 30.                         ) and \
     ( tree.jet1Eta > -4.7 or tree.jet1Eta < 4.7 ) and \
     ( tree.jet2Pt > 30.                         ) and \
     ( tree.jet2Eta > -4.7 or tree.jet2Eta < 4.7 ) and \
     ( tree.mjj > 500                            ) and \
     ( tree.dEtajj < -3.5 or tree.dEtajj > 3.5   ) and \
     ( tree.pThiggs > 100.                       ) and \
     ( tree.nbJets == 0                          ) and \
     ( tree.nCentralJets == 0                    ) and \
     ( tree.l1MediumDB3HIso > 0.5                ) and \
     ( tree.l2MediumDB3HIso > 0.5                ) and \
     ( tree.l2againstElectronNewLooseMVA3 > 0.5  ) and \
     ( tree.diTauCharge == 0                     ) and \
     ( tree.l1LooseEle > 0.5                     ) and \
     ( tree.l2LooseEle > 0.5                     ) and \
     ( tree.l1LooseMu > 0.5                      ) and \
     ( tree.l2LooseMu > 0.5                      ) and \
     ( ( ( tree.l1TrigMatched_diTauJet > 0.5 ) and \
         ( tree.l2TrigMatched_diTauJet > 0.5 ) and \
         ( tree.jetTrigMatched_diTauJet> 0.5 ) and \
         ( tree.jet1Pt > 50.)                  and \
         ( tree.jet1Eta > -3.0 or tree.jet1Eta < 3.0 ) ) or \
       ( ( tree.l1TrigMatched_diTau > 0.5 ) and \
         ( tree.l2TrigMatched_diTau > 0.5 ) ) ) : return True

  else : return False



def skimmingCJV(tree):
  if (tree.nCentralJets==0) : return True

  else : return False


def skimmingAOD(tree):
  if (tree.EventAuxiliary.id_.event_==912141783 or tree.EventAuxiliary.id_.event_==104090628) : return False

  else : return True



#   ( tree.l1againstElectronLooseMVA3>0.5 and tree.l2againstElectronLooseMVA3>0.5 )      and
#   ( tree.l2againstElectronLooseMVA3>0.5 )                                              and\

