import pandas as pd
import matplotlib.pyplot as plt

def plot_results(results):
    plt.figure(figsize=(8,4))
    plt.plot(results["Iteration"], results["N-XAI"], label="N-XAI")
    plt.plot(results["Iteration"], results["LSTM"], label="LSTM")
    plt.xlabel("Iteration")
    plt.ylabel("Accuracy")
    plt.legend()
    plt.show()

def save_results(results):
    df = pd.DataFrame(results)
    df.to_csv("results/accuracy_results.csv", index=False)
