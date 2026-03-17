import pandas as pd
import matplotlib.pyplot as plt
from ManualStrategy import ManualStrategy
from StrategyLearner import StrategyLearner
from marketsimcode import compute_portvals


def author():
    return "nanyanwu3"  # Replace with your GT username


def run_experiment():
    """
    Compare the performance of the ManualStrategy and StrategyLearner.
    """
    # Set up
    symbol = "JPM"
    sd = pd.Timestamp(2008, 1, 1)
    ed = pd.Timestamp(2009, 12, 31)
    sv = 100000  # Starting value of the portfolio

    # Manual Strategy
    ms = ManualStrategy()
    print("Testing Manual Strategy...")
    manual_trades = ms.testPolicy(symbol=symbol, sd=sd, ed=ed, sv=sv)
    manual_portvals = compute_portvals(trades=manual_trades, start_val=sv)

    # Strategy Learner
    sl = StrategyLearner(verbose=False, impact=0.005)

    print("Training Strategy Learner...")

    sl.add_evidence(symbol=symbol, sd=sd, ed=ed, sv=sv)

    print("Testing Strategy Learner...")

    lea_trades = sl.testPolicy(symbol=symbol, sd=sd, ed=ed, sv=sv)

    learner_portvals = compute_portvals(trades=lea_trades, start_val=sv)

    # Normalize portfolio
    normal_manual_portvals = manual_portvals / manual_portvals.iloc[0]
    normal_learner_portvals = learner_portvals / learner_portvals.iloc[0]

    # Plot the results
    plt.figure(figsize=(10, 6))
    plt.plot(normal_manual_portvals, label="Manual Strategy", color="red")
    plt.plot(normal_learner_portvals, label="Strategy Learner", color="blue")
    plt.title("Performance Comparison: Manual Strategy vs. Strategy Learner")
    plt.xlabel("Date")
    plt.ylabel("Normalized Portfolio Value")
    plt.legend()
    plt.grid()
    plt.savefig("experiment1_comparison.png")
    plt.show()

    # Print cumulative returns for comparison
    cr_manual = normal_manual_portvals.iloc[-1, 0] - 1
    cr_learner = normal_learner_portvals.iloc[-1, 0] - 1
    print(f"Cumulative Return of Manual Strategy: {cr_manual:.6f}")
    print(f"Cumulative Return of Strategy Learner: {cr_learner:.6f}")


if __name__ == "__main__":
    run_experiment()
