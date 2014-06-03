import ROOT
from DataFormats.FWLite import Events, Handle

ROOT.gROOT.SetBatch()        # don't pop up canvases

events = Events (['root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/VBF_HToTauTau_M-125_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_1.root',
    'root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/VBF_HToTauTau_M-125_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_10.root',
    'root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/VBF_HToTauTau_M-125_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_100.root',
    'root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/VBF_HToTauTau_M-125_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_101.root',
    'root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/VBF_HToTauTau_M-125_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_102.root',
    'root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/VBF_HToTauTau_M-125_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_103.root',
    'root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/VBF_HToTauTau_M-125_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_11.root',
    'root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/VBF_HToTauTau_M-125_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_12.root',
    'root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/VBF_HToTauTau_M-125_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_13.root',
    'root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/VBF_HToTauTau_M-125_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_14.root',
    'root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/VBF_HToTauTau_M-125_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_15.root',
    'root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/VBF_HToTauTau_M-125_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_16.root',
    'root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/VBF_HToTauTau_M-125_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_17.root',
    'root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/VBF_HToTauTau_M-125_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_18.root',
    'root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/VBF_HToTauTau_M-125_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_19.root',
    'root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/VBF_HToTauTau_M-125_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_2.root',
    'root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/VBF_HToTauTau_M-125_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_20.root',
    'root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/VBF_HToTauTau_M-125_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_21.root',
    'root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/VBF_HToTauTau_M-125_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_22.root',
    'root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/VBF_HToTauTau_M-125_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_23.root',
    'root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/VBF_HToTauTau_M-125_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_24.root',
    'root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/VBF_HToTauTau_M-125_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_25.root',
    'root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/VBF_HToTauTau_M-125_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_26.root',
    'root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/VBF_HToTauTau_M-125_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_27.root',
    'root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/VBF_HToTauTau_M-125_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_28.root',
    'root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/VBF_HToTauTau_M-125_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_29.root',
    'root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/VBF_HToTauTau_M-125_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_3.root',
    'root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/VBF_HToTauTau_M-125_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_30.root',
    'root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/VBF_HToTauTau_M-125_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_31.root',
    'root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/VBF_HToTauTau_M-125_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_32.root',
    'root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/VBF_HToTauTau_M-125_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_33.root',
    'root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/VBF_HToTauTau_M-125_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_34.root',
    'root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/VBF_HToTauTau_M-125_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_35.root',
    'root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/VBF_HToTauTau_M-125_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_36.root',
    'root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/VBF_HToTauTau_M-125_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_37.root',
    'root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/VBF_HToTauTau_M-125_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_38.root',
    'root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/VBF_HToTauTau_M-125_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_39.root',
    'root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/VBF_HToTauTau_M-125_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_4.root',
    'root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/VBF_HToTauTau_M-125_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_40.root',
    'root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/VBF_HToTauTau_M-125_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_41.root',
    'root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/VBF_HToTauTau_M-125_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_42.root',
    'root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/VBF_HToTauTau_M-125_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_43.root',
    'root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/VBF_HToTauTau_M-125_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_44.root',
    'root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/VBF_HToTauTau_M-125_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_45.root',
    'root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/VBF_HToTauTau_M-125_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_46.root',
    'root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/VBF_HToTauTau_M-125_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_47.root',
    'root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/VBF_HToTauTau_M-125_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_48.root',
    'root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/VBF_HToTauTau_M-125_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_49.root',
    'root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/VBF_HToTauTau_M-125_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_5.root',
    'root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/VBF_HToTauTau_M-125_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_50.root',
    'root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/VBF_HToTauTau_M-125_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_51.root',
    'root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/VBF_HToTauTau_M-125_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_52.root',
    'root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/VBF_HToTauTau_M-125_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_53.root',
    'root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/VBF_HToTauTau_M-125_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_54.root',
    'root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/VBF_HToTauTau_M-125_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_55.root',
    'root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/VBF_HToTauTau_M-125_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_56.root',
    'root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/VBF_HToTauTau_M-125_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_57.root',
    'root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/VBF_HToTauTau_M-125_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_58.root',
    'root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/VBF_HToTauTau_M-125_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_59.root',
    'root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/VBF_HToTauTau_M-125_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_6.root',
    'root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/VBF_HToTauTau_M-125_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_60.root',
    'root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/VBF_HToTauTau_M-125_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_61.root',
    'root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/VBF_HToTauTau_M-125_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_62.root',
    'root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/VBF_HToTauTau_M-125_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_63.root',
    'root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/VBF_HToTauTau_M-125_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_64.root',
    'root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/VBF_HToTauTau_M-125_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_65.root',
    'root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/VBF_HToTauTau_M-125_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_66.root',
    'root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/VBF_HToTauTau_M-125_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_67.root',
    'root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/VBF_HToTauTau_M-125_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_68.root',
    'root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/VBF_HToTauTau_M-125_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_69.root',
    'root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/VBF_HToTauTau_M-125_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_7.root',
    'root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/VBF_HToTauTau_M-125_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_70.root',
    'root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/VBF_HToTauTau_M-125_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_71.root',
    'root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/VBF_HToTauTau_M-125_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_72.root',
    'root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/VBF_HToTauTau_M-125_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_73.root',
    'root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/VBF_HToTauTau_M-125_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_74.root',
    'root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/VBF_HToTauTau_M-125_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_75.root',
    'root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/VBF_HToTauTau_M-125_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_76.root',
    'root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/VBF_HToTauTau_M-125_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_77.root',
    'root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/VBF_HToTauTau_M-125_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_78.root',
    'root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/VBF_HToTauTau_M-125_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_79.root',
    'root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/VBF_HToTauTau_M-125_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_8.root',
    'root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/VBF_HToTauTau_M-125_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_80.root',
    'root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/VBF_HToTauTau_M-125_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_81.root',
    'root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/VBF_HToTauTau_M-125_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_82.root',
    'root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/VBF_HToTauTau_M-125_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_83.root',
    'root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/VBF_HToTauTau_M-125_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_84.root',
    'root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/VBF_HToTauTau_M-125_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_85.root',
    'root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/VBF_HToTauTau_M-125_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_86.root',
    'root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/VBF_HToTauTau_M-125_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_87.root',
    'root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/VBF_HToTauTau_M-125_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_88.root',
    'root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/VBF_HToTauTau_M-125_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_89.root',
    'root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/VBF_HToTauTau_M-125_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_9.root',
    'root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/VBF_HToTauTau_M-125_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_90.root',
    'root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/VBF_HToTauTau_M-125_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_91.root',
    'root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/VBF_HToTauTau_M-125_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_92.root',
    'root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/VBF_HToTauTau_M-125_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_93.root',
    'root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/VBF_HToTauTau_M-125_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_94.root',
    'root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/VBF_HToTauTau_M-125_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_95.root',
    'root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/VBF_HToTauTau_M-125_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_96.root',
    'root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/VBF_HToTauTau_M-125_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_97.root',
    'root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/VBF_HToTauTau_M-125_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_98.root',
    'root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/VBF_HToTauTau_M-125_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_99.root'])

tau_handle  = Handle ('vector<cmg::Tau>')
tau_label = ("cmgTauSel")

pfjet_handle  = Handle ('vector<cmg::PFJet>')
pfjet_label = ("cmgPFJetSel")

pfbasejet_handle  = Handle ('vector<cmg::BaseJet>')
pfbasejet_label = ("cmgPFBaseJetLead")

vtx_handle  = Handle ('vector<reco::Vertex>')
vtx_label = ("offlinePrimaryVertices")

# int                                   "nJetsPtGt1"                ""              "PAT"

blacklist = [
#652,
3370,
# 9318,
# 12347,
# 18030,
# 18082,
# 22873,
# 34253,
# 34282,
# 34291,
# 47745,
# 57693,
# 86773,
# 109227,
# 109242,
# 112554,
# 144312,
# 144391,
# 169588,
# 180989,
# 191499,
263199,
# 276040,
# 282653,
# 402074,
# 443404,
# 482713,
# 498313,
# 540265,
# 555512,
# 555574,
# 558578,
# 665355,
# 714544,
# 805457,
# 814120,
# 861815,
]

for i, event in enumerate(events) :
  if event.eventAuxiliary().event() not in blacklist : continue

  print '=========> event =',event.eventAuxiliary().event()

  event.getByLabel (tau_label, tau_handle)
  tau = tau_handle.product()

  event.getByLabel (pfjet_label, pfjet_handle)
  pfjet = pfjet_handle.product()

  event.getByLabel (pfbasejet_label, pfbasejet_handle)
  pfbasejet = pfbasejet_handle.product()

  event.getByLabel (vtx_label, vtx_handle)
  vtx = vtx_handle.product()

  import pdb ; pdb.set_trace()






#
# 652, mva met diff= 6.48792
# 3370, mva met diff= -18.8962
# 9318, mva met diff= -31.1003
# 12347, mva met diff= -6.23656
# 18030, mva met diff= 11.9298
# 18082, mva met diff= -5.22733
# 22873, mva met diff= 9.80279
# 34253, mva met diff= -17.0816
# 34282, mva met diff= -7.68933
# 34291, mva met diff= -9.26188
# 47745, mva met diff= -7.32683
# 57693, mva met diff= -7.38869
# 86773, mva met diff= -28.8057
# 109227, mva met diff= -25.9015
# 109242, mva met diff= -10.0514
# 112554, mva met diff= -12.1091
# 144312, mva met diff= -10.2082
# 144391, mva met diff= -23.0886
# 169588, mva met diff= -12.2829
# 180989, mva met diff= -12.5999
# 191499, mva met diff= -15.1102
# 263199, mva met diff= 7.4857
# 276040, mva met diff= -9.40798
# 282653, mva met diff= -8.84776
# 402074, mva met diff= -10.2168
# 443404, mva met diff= -14.4827
# 482713, mva met diff= 7.06372
# 498313, mva met diff= -11.5474
# 540265, mva met diff= -16.422
# 555512, mva met diff= -5.64504
# 555574, mva met diff= 11.6264
# 558578, mva met diff= -20.2695
# 665355, mva met diff= -14.2156
# 714544, mva met diff= -9.52112
# 805457, mva met diff= 6.61647
# 814120, mva met diff= -6.0299
# 861815, mva met diff= -16.2857