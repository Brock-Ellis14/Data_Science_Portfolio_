This repository contains a suite of risk management modules and statistical research projects. The work is divided into core banking risk pillars (Market, Credit, and Model Risk) and exploratory research in high-dimensional biological and economic data.
🏦 Banking Risk Modules (FRM)
Market Risk – The NIM Stress TesterFocus: Interest Rate Risk in the Banking Book (IRRBB).
Implementation: Developed a framework to stress-test Net Interest Margin (NIM) against parallel and non-parallel yield curve shifts.
Quant Logic: Utilized repricing gap analysis and duration-matching to quantify the impact of interest rate volatility on Net Interest Income (NII).

Credit Risk – The CRE Concentration AnalyzerFocus: Commercial Real Estate portfolio risk.
Implementation: Built a tool to identify concentration risk across property types and geographies.
Quant Logic: Structured the data to calculate Expected Loss (EL) and loss-given-default (LGD) scenarios, focusing on the sensitivity of high-LTV loans to market downturns.

Model Risk – The 'FRM Auditor'Focus: Quantitative Model Validation (SR 11-7 standards).
Implementation: A diagnostic toolkit to audit model assumptions before deployment.
Quant Logic: Automates the testing of residuals, normality (QQ-plots), and heteroscedasticity. It ensures that the model choice (e.g., Parametric vs. Non-Parametric) is mathematically justified by the data distribution.

🔬 Statistical Research & AnalyticsBiotech: 
MS Gene Expression AnalysisThe Goal: Differentiating MS patients from healthy controls through immune markers (CXCL10, IL7R, CD19, TNF).
Methodology: Used Welch’s T-tests and Wilcoxon Rank-Sum tests for feature selection, followed by Logistic Regression for classification.
Result: Identified CXCL10 as a statistically significant predictor ($p = 0.0102$), passing the Hosmer-Lemeshow goodness-of-fit test.Econometrics: 

ROI Baseball AnalyticsThe Goal: Measuring the marginal cost of a win in Major League Baseball.
Methodology: Scraped and cleaned 150+ years of salary and performance data using SQL (SQLite). Applied OLS and Logit models to find the ROI of payroll on regular season vs. postseason success.
Result: Quantified the "Postseason Crapshoot" theory, where salary explains 6.5% of regular-season wins but only 1.8% of championship outcomes.

💻 Tech StackStatistical Modeling: Python (statsmodels, scipy), R (tidyverse).Data Engineering: SQL (SQLite), Pandas, NumPy.Visualization: ggplot2, lets-plot, Matplotlib.Documentation: LaTeX for formal mathematical reporting.

📩 Contact[Brock Ellis] [(https://www.linkedin.com/in/brock-ellis14/)][brockalvin14@gmail.com]
