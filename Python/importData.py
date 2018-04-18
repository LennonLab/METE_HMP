import numpy as np

def import_obs_pred_data(input_filename):   # TAKEN FROM THE mete_sads.py script used for White et al. (2012)
    if '75' in input_filename:
        data = np.genfromtxt(input_filename, dtype = "f8,f8,f8,f8", names = ['site','obs', 'predPln', 'pred7525'], delimiter = " ")
    else:
        data = np.genfromtxt(input_filename, dtype = "f8,f8,f8", names = ['site','obs','pred'], delimiter = " ")
    return data

def import_subsampled_data(input_filename):
    if ('zipf' in input_filename):
        # 33 for zipf
        # this needs to be fixesd, I put the file name twice in old code
        data = np.genfromtxt(input_filename, \
        dtype = "f8,f8,f8,f8,f8,f8,f8,f8,f8,f8,f8,f8,f8,f8,f8,f8,f8,f8,f8,f8,f8,f8,f8,f8,f8,f8,f8,f8,f8,f8,f8,f8,f8,f8", \
        names = ['site','site2','N0','S0','Nmax', \
        'N0_05','S0_05','Nmax_05', 'r2_05', 'gamma_05', \
        'N0_025','S0_025','Nmax_025', 'r2_025', 'gamma_025', \
        'N0_0125','S0_0125','Nmax_0125', 'r2_0125', 'gamma_0125', \
        'N0_00625','S0_00625','Nmax_00625', 'r2_00625', 'gamma_00625', \
        'N0_003125','S0_003125','Nmax_003125', 'r2_003125', 'gamma_003125',
        'N0_0015625','S0_0015625','Nmax_0015625','r2_0015625', 'gamma_0015625'], \
        delimiter = " ")
    else:
        # 27 columns for mete and geom
        data = np.genfromtxt(input_filename, \
        dtype = "f8,f8,f8,f8,f8,f8,f8,f8,f8,f8,f8,f8,f8,f8,f8,f8,f8,f8,f8,f8,f8,f8,f8,f8,f8,f8,f8", \
        names = ['site','N0','S0','Nmax', \
        'N0_05','S0_05','Nmax_05','r2_05', \
        'N0_025','S0_025','Nmax_025','r2_025', \
        'N0_0125','S0_0125','Nmax_0125','r2_0125', \
        'N0_00625','S0_00625','Nmax_00625','r2_00625', \
        'N0_003125','S0_003125','Nmax_003125','r2_003125', \
        'N0_0015625','S0_0015625','Nmax_0015625','r2_0015625'], \
        delimiter = " ")
    return data

def import_subsampled_data_pandas(input_filename):
    if ('zipf' in input_filename):
        names = ['site','site2','N0','S0','Nmax', \
        'N0_05','S0_05','Nmax_05', 'r2_05', 'gamma_05', \
        'N0_025','S0_025','Nmax_025', 'r2_025', 'gamma_025', \
        'N0_0125','S0_0125','Nmax_0125', 'r2_0125', 'gamma_0125', \
        'N0_00625','S0_00625','Nmax_00625', 'r2_00625', 'gamma_00625', \
        'N0_003125','S0_003125','Nmax_003125', 'r2_003125', 'gamma_003125',
        'N0_0015625','S0_0015625','Nmax_0015625','r2_0015625', 'gamma_0015625']
        #data_table = pd.read_table(input_filename, names = names, header = None, sep=' ')

    else:
        names = ['site','N0','S0','Nmax', \
        'N0_05','S0_05','Nmax_05','r2_05', \
        'N0_025','S0_025','Nmax_025','r2_025', \
        'N0_0125','S0_0125','Nmax_0125','r2_0125', \
        'N0_00625','S0_00625','Nmax_00625','r2_00625', \
        'N0_003125','S0_003125','Nmax_003125','r2_003125', \
        'N0_0015625','S0_0015625','Nmax_0015625','r2_0015625']
    data_table = pd.read_table(input_filename, names = names, header = None, sep=' ')
    return data_table


def import_NSR2_data(input_filename):   # TAKEN FROM THE mete_sads.py script used for White et al. (2012)
    input_filename_str = str(input_filename)
    #NSR2_method = input_filename_split[-4]
    #method = str(NSR2_method.split('/')[1])
    if '/Stratified/' in input_filename_str:
        if 'geom' in input_filename_str:
            data = np.genfromtxt(input_filename, dtype = "f8,f8,f8,f8,f8,f8,f8,f8,f8,f8,f8", \
                names = ['site','N','S', 'NmaxObs', 'NmaxPred', 'evennessObs', \
                    'evennessPred', 'skewnessObs', 'skewnessPred','ll','R2'], delimiter = " ")
        elif 'mete' in input_filename_str:
            data = np.genfromtxt(input_filename, dtype = "f8,f8,f8,f8,f8,f8,f8,f8,f8,f8,f8,f8", \
                names = ['site','N','S', 'NmaxObs', 'NmaxPred', 'evennessObs', \
                    'evennessPred', 'skewnessObs', 'skewnessPred', 'p', 'll', 'R2'], delimiter = " ")
        elif 'zipf' in input_filename_str:
            data = np.genfromtxt(input_filename, dtype = "f8,f8,f8,f8,f8,f8,f8,f8,f8,f8,f8,f8", \
                names = ['site','N','S', 'NmaxObs', 'NmaxPred', 'evennessObs', \
                    'evennessPred', 'skewnessObs', 'skewnessPred','gamma','ll','R2'], delimiter = " ")
        elif 'lognorm' in input_filename_str:
            data = np.genfromtxt(input_filename, dtype = "f8,f8,f8,f8,f8,f8,f8,f8,f8,f8,f8,f8,f8", \
                names = ['site','N','S', 'NmaxObs', 'NmaxPred', 'evennessObs', \
                    'evennessPred', 'skewnessObs', 'skewnessPred','mu','sigma','ll','R2'], delimiter = " ")
    elif '/Stratified_Test/' in input_filename_str and '95' not in input_filename_str \
        and  '97' not in input_filename_str and  '99' not in input_filename_str:
        if 'geom' in input_filename_str:
            data = np.genfromtxt(input_filename, dtype = "f8,f8,f8,f8,f8,f8,f8,f8,f8,f8,f8, \
            f8,f8,f8,f8,f8,f8,f8,f8,f8,f8,f8,f8,f8,f8,f8,f8,f8", \
                names = ['site','N','S', 'NmaxObs', 'NmaxPred', 'evennessObs', \
                    'evennessPred', 'skewnessObs', 'skewnessPred', 'll','R2', 'R2std', 'R2Nmax',\
                    'NmaxPredSlope', 'NmaxPredIntercept', 'NmaxPredR', 'NmaxPredP', 'NmaxPredStd', \
                    'evennessPredSlope', 'evennessPredIntercept', 'evennessPredR', 'evennessPredP', 'evennessPredStd', \
                    'skewnessPredSlope', 'skewnessPredIntercept', 'skewnessPredR', 'skewnessPredP', 'skewnessPredStd'] \
                    , delimiter = " ")
        elif 'zipf' in input_filename_str:
            data = np.genfromtxt(input_filename, dtype = "f8,f8,f8,f8,f8,f8,f8,f8,f8,f8, \
            f8,f8,f8,f8,f8,f8,f8,f8,f8,f8,f8,f8,f8,f8,f8,f8,f8,f8", \
                names = ['site','N','S', 'NmaxObs', 'NmaxPred', 'evennessObs', \
                    'evennessPred', 'skewnessObs', 'skewnessPred','gamma', 'll', 'R2', 'R2std', 'R2Nmax',\
                    'NmaxPredSlope', 'NmaxPredIntercept', 'NmaxPredR', 'NmaxPredP', 'NmaxPredStd', \
                    'evennessPredSlope', 'evennessPredIntercept', 'evennessPredR', 'evennessPredP', 'evennessPredStd', \
                    'skewnessPredSlope', 'skewnessPredIntercept', 'skewnessPredR', 'skewnessPredP', 'skewnessPredStd'] \
                    , delimiter = " ")
        if 'mete' in input_filename_str:
            data = np.genfromtxt(input_filename, dtype = "f8,f8,f8,f8,f8,f8,f8,f8,f8,f8, \
            f8,f8,f8,f8,f8,f8,f8,f8,f8,f8,f8,f8,f8,f8,f8,f8,f8,f8,f8", \
                names = ['site','N','S', 'NmaxObs', 'NmaxPred', 'evennessObs', \
                    'evennessPred', 'skewnessObs', 'skewnessPred','p','ll', 'R2', 'R2std', 'R2Nmax', \
                    'NmaxPredSlope', 'NmaxPredIntercept', 'NmaxPredR', 'NmaxPredP', 'NmaxPredStd', \
                    'evennessPredSlope', 'evennessPredIntercept', 'evennessPredR', 'evennessPredP', 'evennessPredStd', \
                    'skewnessPredSlope', 'skewnessPredIntercept', 'skewnessPredR', 'skewnessPredP', 'skewnessPredStd'] \
                    , delimiter = " ")
        if 'lognorm' in input_filename_str:
            data = np.genfromtxt(input_filename, dtype = "f8,f8,f8,f8,f8,f8,f8,f8,f8,f8, \
            f8,f8,f8,f8,f8,f8,f8,f8,f8,f8,f8,f8,f8,f8,f8,f8,f8,f8,f8", \
                names = ['site','N','S', 'NmaxObs', 'NmaxPred', 'evennessObs', \
                    'evennessPred', 'skewnessObs', 'skewnessPred','mu','sigma','ll', 'R2', 'R2std', 'R2Nmax', \
                    'NmaxPredSlope', 'NmaxPredIntercept', 'NmaxPredR', 'NmaxPredP', 'NmaxPredStd', \
                    'evennessPredSlope', 'evennessPredIntercept', 'evennessPredR', 'evennessPredP', 'evennessPredStd', \
                    'skewnessPredSlope', 'skewnessPredIntercept', 'skewnessPredR', 'skewnessPredP', 'skewnessPredStd'] \
                    , delimiter = " ")

    elif '/geom_MGRAST95_NSR2.txt' in  input_filename_str or \
        '/geom_MGRAST97_NSR2.txt' in  input_filename_str  or \
        '/geom_MGRAST99_NSR2.txt' in  input_filename_str:
        data = np.genfromtxt(input_filename, dtype = "f8,f8,f8,f8,f8,f8,f8,f8,f8,f8,f8", \
        names = ['site','N','S','NmaxObs', 'NmaxPred', 'evennessObs', \
            'evennessPred', 'skewnessObs', 'skewnessPred','ll', 'R2'], delimiter = " ")
    elif '/mete_MGRAST95_NSR2.txt' in  input_filename_str or \
        '/mete_MGRAST97_NSR2.txt' in  input_filename_str  or \
        '/mete_MGRAST99_NSR2.txt' in  input_filename_str:
            data = np.genfromtxt(input_filename, dtype = "f8,f8,f8,f8,f8,f8,f8,f8,f8,f8,f8,f8", \
            names = ['site','N','S','NmaxObs', 'NmaxPred', 'evennessObs', \
                'evennessPred', 'skewnessObs', 'skewnessPred', 'p', 'll','R2'], delimiter = " ")
    elif '/lognorm_pln_MGRAST95_NSR2.txt' in  input_filename_str or \
        '/lognorm_pln_MGRAST97_NSR2.txt' in  input_filename_str  or \
        '/lognorm_pln_MGRAST99_NSR2.txt' in  input_filename_str:
        data = np.genfromtxt(input_filename, dtype = "f8,f8,f8,f8,f8,f8,f8,f8,f8,f8,f8,f8,f8", \
        names = ['site','N','S','NmaxObs', 'NmaxPred', 'evennessObs', \
            'evennessPred', 'skewnessObs', 'skewnessPred','mu', 'sigma', 'll', 'R2'],\
            delimiter = " ")
    elif '/zipf_mle_MGRAST97_NSR2.txt' in  input_filename_str or \
        '/zipf_mle_MGRAST95_NSR2.txt' in  input_filename_str or \
        '/zipf_mle_MGRAST99_NSR2.txt' in  input_filename_str:
        data = np.genfromtxt(input_filename, dtype = "f8,f8,f8,f8,f8,f8,f8,f8,f8,f8,f8,f8", \
            names = ['site','N','S', 'NmaxObs', 'NmaxPred', 'evennessObs', \
            'evennessPred', 'skewnessObs', 'skewnessPred','gamma','ll', 'R2'], delimiter = " ")
    elif ('95'in input_filename_str or '97'in input_filename_str or '99'in input_filename_str) and \
        '/Stratified_Test/' in  input_filename_str:
        data = np.genfromtxt(input_filename, dtype = "f8,f8,f8,f8,f8", \
            names = ['site','N','S', 'R2', 'R2std'], delimiter = " ")

    else:
        if ('zipf' in input_filename_str):
            if 'HMP' in input_filename_str:
                data = np.genfromtxt(input_filename, dtype = "f8,f8,f8,f8,f8,f8,f8,f8,f8,f8,f8,f8,f8", \
                names = ['site','N','S', 'NmaxObs', 'NmaxPred', 'evennessObs', \
                    'evennessPred', 'skewnessObs', 'skewnessPred','gamma', 'll','R2', 'NAP'], delimiter = " ")
            else:
                data = np.genfromtxt(input_filename, dtype = "f8,f8,f8,f8,f8,f8,f8,f8,f8,f8,f8,f8", \
                names = ['site','N','S', 'NmaxObs', 'NmaxPred', 'evennessObs', \
                    'evennessPred', 'skewnessObs', 'skewnessPred','gamma', 'll','R2'], delimiter = " ")

        elif  'mete' in input_filename_str:
            if 'HMP' in input_filename_str:
                data = np.genfromtxt(input_filename, dtype = "f8,f8,f8,f8,f8,f8,f8,f8,f8,f8,f8,f8,f8", \
                names = ['site','N','S','NmaxObs', 'NmaxPred', 'evennessObs', \
                    'evennessPred', 'skewnessObs', 'skewnessPred', 'p', 'll','R2', 'NAP'], delimiter = " ")
            else:
                data = np.genfromtxt(input_filename, dtype = "f8,f8,f8,f8,f8,f8,f8,f8,f8,f8,f8,f8", \
                names = ['site','N','S','NmaxObs', 'NmaxPred', 'evennessObs', \
                    'evennessPred', 'skewnessObs', 'skewnessPred', 'p', 'll','R2'], delimiter = " ")

        elif 'lognorm' in input_filename_str:
            if 'HMP' in input_filename_str:
                data = np.genfromtxt(input_filename, dtype = "f8,f8,f8,f8,f8,f8,f8,f8,f8,f8,f8,f8,f8,f8", \
                names = ['site','N','S','NmaxObs', 'NmaxPred', 'evennessObs', \
                    'evennessPred', 'skewnessObs', 'skewnessPred','mu', 'sigma', 'll', 'R2', 'NAP'], delimiter = " ")
            else:
                data = np.genfromtxt(input_filename, dtype = "f8,f8,f8,f8,f8,f8,f8,f8,f8,f8,f8,f8,f8", \
                names = ['site','N','S','NmaxObs', 'NmaxPred', 'evennessObs', \
                    'evennessPred', 'skewnessObs', 'skewnessPred','mu', 'sigma', 'll', 'R2'], delimiter = " ")

        elif 'geom' in input_filename_str:
            if 'HMP' in input_filename_str:
                data = np.genfromtxt(input_filename, dtype = "f8,f8,f8,f8,f8,f8,f8,f8,f8,f8,f8,f8", \
                names = ['site','N','S', 'NmaxObs', 'NmaxPred', 'evennessObs', \
                    'evennessPred', 'skewnessObs', 'skewnessPred', 'll','R2','NAP'], delimiter = " ")
            else:
                data = np.genfromtxt(input_filename, dtype = "f8,f8,f8,f8,f8,f8,f8,f8,f8,f8,f8", \
                names = ['site','N','S','NmaxObs', 'NmaxPred', 'evennessObs', \
                    'evennessPred', 'skewnessObs', 'skewnessPred', 'll','R2'], delimiter = " ")
    return data
