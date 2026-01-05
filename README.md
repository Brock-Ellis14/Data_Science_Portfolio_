# Quantitative Risk & Data Science Portfolio

This repository contains a suite of risk management modules and statistical research projects. The work is divided into core banking risk pillars (Market, Credit, and Model Risk) and exploratory research in high-dimensional biological and economic data.

## Banking Risk Modules (FRM)

### Market Risk – S&P 500 Regime Predictor
**Focus:** Market Regime Forecasting and Volatility Analysis.  
**Implementation:** Developed a predictive engine using **XGBoost** and **Random Forest** to forecast monthly S&P 500 regimes. Engineered a high-dimensional feature set in **R (Tidyquant)**, incorporating **multi-horizon lags** of **FRED macroeconomic data**.  
**Quant Logic:** Migrated the pipeline to **Python** for a comparative model audit. Implemented **L1/L2 regularization** to handle non-linear time-series dependencies and mitigate noise in high-volatility environments. Achieved a significant lift over the random baseline.



### Credit Risk – Macro-Financial Shock Analysis
**Focus:** Systemic Risk and Sector Correlation Dynamics.  
**Implementation:** Built a custom risk engine in **R (Tidyquant/XTS)** to analyze how macroeconomic shocks impacted 11 equity sectors across the **2008 GFC** and **2020 COVID-19** regimes.  
**Quant Logic:** Identified a **25% surge** in cross-sector synchronization during the COVID-19 shock. Quantified tail-risk using **Expected Shortfall (ES)** and **Maximum Drawdown**, aligning methodologies with **Basel III** regulatory standards.



### Model Risk – The 'FRM Auditor'
**Focus:** Quantitative Model Validation (**SR 11-7 standards**).  
**Implementation:** A diagnostic toolkit to audit model assumptions before deployment, utilizing high-dimensional biostatistical signal detection as a proxy for **Loss Forecasting**.  
**Quant Logic:** Automates the testing of residuals, normality (**QQ-plots**), and **Hosmer-Lemeshow Goodness-of-Fit**. This framework ensures that model selection—such as selecting a non-parametric test over a T-test—is mathematically justified by the underlying distribution.

## Statistical Research & Analytics

### Biotech: MS Gene Expression Analysis
**The Goal:** Differentiating MS patients from healthy controls through immune markers (CXCL10, IL7R, CD19, TNF).  
**Methodology:** Executed **Wilcoxon Rank-Sum** and **Independent T-Tests** for factor selection, followed by **Logistic Regression** for classification.  
**Result:** Identified **CXCL10** as a statistically significant predictor ($p = 0.0102$), passing the Hosmer-Lemeshow goodness-of-fit test.

### Econometrics: ROI Baseball Analytics
**The Goal:** Measuring the **Marginal Return on Investment (ROI)** of capital expenditures.  
**Methodology:** Scraped and cleaned 150+ years of financial data using **SQL** and **Python (Statsmodels)**. Applied OLS and Logit models to compare regular season win-efficiency against postseason success.  
**Result:** Implemented **HC3 Heteroscedasticity-robust standard errors** to prove diminishing marginal returns on capital. Quantified the "Championship Premium," highlighting significant **Unsystematic Risk**.

## Tech Stack

**Statistical Modeling:** Python (XGBoost, statsmodels, sklearn, scipy), R (Tidyquant, XTS, tidyverse, lubridate).  
**Data Engineering:** SQL (SQLite), Pandas, NumPy.  
**Visualization:** ggplot2, lets-plot, Matplotlib, seaborn.  
**Documentation:** LaTeX for formal mathematical reporting.

## Contact

**Brock Ellis** [LinkedIn Profile](https://www.linkedin.com/in/brock-ellis14/)  
[Email: brockalvin14@gmail.com](mailto:brockalvin14@gmail.com)
