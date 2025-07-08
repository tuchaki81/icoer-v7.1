from src.slecma import analyze_text
from src.eeg_module import analyze_eeg
from src.synchronizer import sync_temporal
from src.entropy import compute_entropy

def compute_icoer(text_path, eeg_path):
    # Análise simbólica
    S = analyze_text(text_path)['S']
    
    # Análise EEG
    B = analyze_eeg(eeg_path)['B']
    
    # Sincronização temporal
    T = sync_temporal()['T']
    
    # Entropia
    H = compute_entropy()['H']
    
    # Pesos dos módulos
    ws, wb, wt, lam = 0.3, 0.3, 0.3, 0.1

    # Cálculo do ICOER
    ICOER = ws * S + wb * B + wt * T - lam * H

    # Retorno completo
    return {
        'S': S,
        'B': B,
        'T': T,
        'H': H,
        'ICOER': ICOER
    }
