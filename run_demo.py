from src.icoer_calc import compute_icoer

if __name__ == "__main__":
    print("Running ICOER v7.1 demo...")
    result = compute_icoer("data/sample_texts.json", "data/simulated_eeg.csv")
    print(f"ICOER Score: {result}")
