# Machine Learning for Algorithmic Trading

**Subject Area:** Machine Learning · Quantitative Finance · Reinforcement Learning · Algorithm Design

---

## What It Does

This project applies machine learning techniques to algorithmic trading strategy development. It includes implementations of custom **decision tree and ensemble learners** benchmarked for regression accuracy, a **Q-learning agent** that learns optimal trading policies from market data, and a full **StrategyLearner** that combines technical indicators with the Q-learner to generate buy/sell signals — compared against a manually tuned benchmark strategy.

### Project Components

**`Assess_ML_Learners/`** — Custom ML implementations benchmarked for regression:
- `DTLearner.py` — Decision tree learner built from scratch (no scikit-learn)
- `RTLearner.py` — Random tree learner (randomized feature selection at each split)
- `BagLearner.py` — Bagging ensemble wrapper (works with any base learner)
- `InsaneLearner.py` — Ensemble-of-bags for extreme variance reduction

**`Q_Learning_Trader/`** — Tabular Q-learner:
- `QLearner.py` — Reinforcement learning agent using Dyna-Q with experience replay

**`Strategy_Learner/`** — Full trading system:
- `StrategyLearner.py` — Q-learning-based trading strategy with discretized technical indicators
- `ManualStrategy.py` — Hand-crafted technical indicator trading rules (benchmark)
- `experiment1.py` — In-sample vs. out-of-sample performance comparison
- `experiment2.py` — Impact of market impact parameter on strategy profitability

## Problem Addressed

Profitable algorithmic trading strategies must generalize beyond their training window. This project confronts the core challenge of applying ML in non-stationary, adversarial financial environments: building learners that avoid overfitting, discretizing continuous market signals into actionable states, and designing a reward signal that aligns the agent's behavior with portfolio performance rather than raw accuracy.

## Practical Relevance

The techniques demonstrated here — ensemble learning, reinforcement learning for sequential decision-making, and time-series feature engineering — transfer directly to domains beyond finance, including anomaly detection, adaptive security policies, and AI agent design. The Q-learner architecture is a direct precursor to deep RL approaches used in production AI systems.

## Tools, Languages, and Libraries

Python · NumPy · pandas · custom scikit-learn-compatible API · tabular Q-learning · Dyna-Q

## Skills Demonstrated

- ML algorithm implementation from scratch: decision trees, random trees, bagging
- Reinforcement learning: Q-learning with state discretization, reward design, and Dyna-Q planning
- Feature engineering: technical indicator construction (momentum, Bollinger Bands, RSI)
- Experimental design: controlled in-sample vs. out-of-sample evaluation
- Quantitative analysis: portfolio performance metrics (cumulative return, Sharpe ratio, drawdown)

## Extension Ideas

- Upgrade the Q-learner to a deep Q-network (DQN) with continuous state space
- Add transaction cost modeling and slippage to make the simulation more realistic
- Apply the StrategyLearner to a different asset class (crypto, fixed income ETFs) and compare generalization
- Use SHAP values to interpret which indicators the StrategyLearner weights most heavily

---

*Georgia Institute of Technology — MS Computer Science · CS 7646: Machine Learning for Trading*
