import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from StrategyLearner import StrategyLearner
from marketsimcode import compute_portvals
import util as ut


def author():
    return "nanyanwu3"  # Replace with your GT username


def experiment_impact_analysis(symbol="JPM", sd=pd.Timestamp(2008, 1, 1), ed=pd.Timestamp(2009, 12, 31), sv=100000):

    impact_values = [0.0, 0.005, 0.01, 0.02]

    # Prepare data structures to hold results
    cumulative_returns = []
    avg_daily_returns = []
    std_daily_returns = []

    # Iterate over different impact values
    for impact in impact_values:
        print(f"Testing Strategy Learner with impact = {impact}...")

        # Initialize the Strategy Learner
        learner = StrategyLearner(verbose=False, impact=impact, commission=9.95)

        # Train
        learner.add_evidence(symbol=symbol, sd=sd, ed=ed, sv=sv)

        # Test the learner
        trades = learner.testPolicy(symbol=symbol, sd=sd, ed=ed, sv=sv)

        # Simulate portfolio values using marketsimcode
        portvals = compute_portvals(trades=trades, start_val=sv, commission=9.95, impact=impact)

        # Normalize
        norm_portvals = portvals / portvals.iloc[0]

        # Compute
        daily_returns = norm_portvals.pct_change().dropna()
        cr = norm_portvals.iloc[-1, 0] - 1  # Cumulative return
        adr = daily_returns.mean()[0]  # Average daily return
        sddr = daily_returns.std()[0]  # Standard deviation of daily returns

        # Store
        cumulative_returns.append(cr)
        avg_daily_returns.append(adr)
        std_daily_returns.append(sddr)

        # Plot
        plt.plot(norm_portvals, label=f"Impact: {impact:.3f}")

    # Generate
    plt.title(f"Portfolio Performance with Varying Impact ({symbol})")
    plt.xlabel("Date")
    plt.ylabel("Normalized Portfolio Value")
    plt.legend(loc="best")
    plt.grid()
    plt.savefig("impact_analysis_performance.png")
    plt.show()

    # Output
    results = pd.DataFrame({
        "Impact": impact_values,
        "Cumulative Return": cumulative_returns,
        "Avg Daily Return": avg_daily_returns,
        "Std Daily Return": std_daily_returns,
    })

    # Save results to CSV
    results.to_csv("impact_analysis_results.csv", index=False)

    # Print summary table
    print("Impact Analysis Results:")
    print(results)

    # Plot
    plt.figure(figsize=(8, 6))
    plt.plot(impact_values, cumulative_returns, marker='o', label="Cumulative Return", color="blue")
    plt.xlabel("Impact")
    plt.ylabel("Cumulative Return")
    plt.title("Cumulative Return vs. Impact")
    plt.grid()
    plt.savefig("impact_vs_cumulative_return.png")
    plt.show()

    # Plot average d
    plt.figure(figsize=(8, 6))
    plt.plot(impact_values, avg_daily_returns, marker='o', label="Avg Daily Return", color="green")
    plt.xlabel("Impact")
    plt.ylabel("Average Daily Return")
    plt.title("Avg Daily Return vs. Impact")
    plt.grid()
    plt.savefig("impact_vs_avg_daily_return.png")
    plt.show()

    # Plot standard
    plt.figure(figsize=(8, 6))
    plt.plot(impact_values, std_daily_returns, marker='o', label="Std Dev Daily Return", color="red")
    plt.xlabel("Impact")
    plt.ylabel("Std Dev of Daily Return")
    plt.title("Std Dev of Daily Returns vs. Impact")
    plt.grid()
    plt.savefig("impact_vs_std_dev_daily_return.png")
    plt.show()


if __name__ == "__main__":
    # Run the experiment
    experiment_impact_analysis()
