# ICOER v7.1

This repository contains the full implementation of the Informational Coherence Index (ICOER) v7.1, integrating symbolic analysis, simulated or real EEG data, and temporal synchronization based on the Unified Spin Informational Theory (TGU).

## Quickstart

```bash
git clone https://github.com/your-username/icoer-v7.1.git
cd icoer-v7.1
pip install -r requirements.txt
python run_demo.py
```

## Modules
- `slecma.py`: SLECMA symbolic coherence engine.
- `eeg_module.py`: EEG data interface and band analysis.
- `synchronizer.py`: temporal alignment between symbolic and biological signals.
- `entropy.py`: informational entropy calculator.
- `icoer_calc.py`: final aggregation of modules into the ICOER score.

## License
MIT
