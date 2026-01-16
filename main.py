from src.data_preprocessing import load_and_preprocess
from src.evaluate import plot_results, save_results

accuracy_results = load_and_preprocess(
    data_path="data/carclaims_small.csv",
    iterations=21
)

plot_results(accuracy_results)
save_results(accuracy_results)

print("Project execution completed successfully.")
