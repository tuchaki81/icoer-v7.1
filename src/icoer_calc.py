
from src.slecma import analyze_text
from src.eeg_module import analyze_eeg
from src.synchronizer import sync_temporal
from src.entropy import compute_entropy

def compute_icoer(text_path, eeg_path):
    S = analyze_text(text_path)['S']
    B = analyze_eeg(eeg_path)['B']
    T = sync_temporal()['T']
    H = compute_entropy()['H']
    ws, wb, wt, lam = 0.3, 0.3, 0.3, 0.1
    return ws * S + wb * B + wt * T - lam * H
