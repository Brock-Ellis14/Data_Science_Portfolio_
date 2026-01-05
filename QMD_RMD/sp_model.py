

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from lets_plot import *

# DATA REFINEMENT & REGIME BINNING

data = pd.read_csv('my_data_final.csv')
data['target_percent_change'] /= 100  # Scale to decimal for financial math

# Drop initial metadata to keep the dataframe clean
cols_initial_drop = ['Unnamed: 0', 'percent_change', 'month', 'year', 'high_max', 
                     'low_min', 'avg_open', 'avg_close', 'sd_high', 'sd_low', 'sd_close']
data = data.drop(columns=[c for c in cols_initial_drop if c in data.columns])

# Define Market Regimes based on 1.5% Volatility Thresholds
bins, labels = [-np.inf, -0.015, 0.0, 0.015, np.inf], [0, 1, 2, 3]
data['y_value_classified'] = pd.cut(data['target_percent_change'], bins=bins, labels=labels, right=False).astype(int)

# Create string columns for visualization purposes only
regime_order = ['0: Downside Risk (Worst)', '1: Weak/Neutral', '2: Moderate Growth', '3: Strong Upside (Best)']
regime_map = {i: regime_order[i] for i in range(4)}
data['market_regime_label'] = data['y_value_classified'].map(regime_map)
data['y_class_str'] = data['y_value_classified'].astype(str)

# MACRO-RISK VISUALIZATIONS

sns.set_style("whitegrid")
custom_palette = {regime_order[0]: 'red', regime_order[1]: 'deeppink', regime_order[2]: 'skyblue', regime_order[3]: 'green'}

# Yield Curve Spread vs. Momentum
fig, ax = plt.subplots(figsize=(14, 8))
sns.scatterplot(data=data, x='yield_curve_slope', y='open_1mo_ret', hue='market_regime_label', 
                hue_order=regime_order, s=150, palette=custom_palette, alpha=0.8, ax=ax)
ax.axvline(0, color='red', linestyle='-', linewidth=3, label='Inverted Yield Curve')
ax.set_title('Macro Risk vs. Momentum: Market Regime Classification', fontsize=18, fontweight='bold')

# policy Stance Heatmap
color_limit = data['open_1mo_ret'].abs().max() * 1.05
fig2, ax2 = plt.subplots(figsize=(12, 10))
h = ax2.hist2d(data['yield_curve_slope'], data['real_fed_funds'], weights=data['open_1mo_ret'], 
               bins=25, cmap='RdYlGn', vmin=-color_limit, vmax=color_limit)
plt.colorbar(h[3], ax=ax2, label='Avg Monthly Return')
ax2.axvline(0, color='darkred', linestyle='--')
ax2.axhline(1.0, color='navy', linestyle=':')
ax2.set_title('Market Regime Heatmap: Spread vs. Real Rates', fontsize=18, fontweight='bold')

# SEQUENTIAL STRATIFICATION (The Fix: Dropping String Columns)
cols_to_exclude = [
    'y_value_classified',
    'date', 
    'market_regime_label',
    'y_class_str',
    'target_percent_change'
]

X = data.drop(columns=cols_to_exclude)
y = data['y_value_classified'].astype(int)

# Sequential Split
holdout_split = int(len(data) * 0.9)
X_train_val, X_holdout = X.iloc[:holdout_split], X.iloc[holdout_split:]
y_train_val, y_holdout = y.iloc[:holdout_split], y.iloc[holdout_split:]

X_train, X_val, y_train, y_val = train_test_split(X_train_val, y_train_val, test_size=0.2, shuffle=False)

print("\n--- Model Training Context ---")
print(f"Features utilized: {X_train.columns.tolist()}")
print(f"Training samples: {len(X_train)}")

#  MODEL SUIT
models = {
    "Decision Tree": DecisionTreeClassifier(min_samples_split=50, class_weight='balanced', criterion='entropy', 
                                            max_depth=10, min_samples_leaf=230, random_state=42),
    "Random Forest": RandomForestClassifier(n_estimators=5000, max_depth=30, min_samples_split=12, 
                                            min_samples_leaf=19, n_jobs=-1, random_state=42),
    "XGBoost": XGBClassifier(n_estimators=1000, learning_rate=0.1, max_depth=12, min_child_weight=10, 
                             gamma=2, eval_metric='merror', random_state=42)
}

for name, model in models.items():
    model.fit(X_train, y_train)
    val_acc = accuracy_score(y_val, model.predict(X_val))
    print(f"{name} Validation Accuracy: {val_acc:.4f}")

# FINAL HOLDOUT AUDIT &VISUALS
y_pred = models["XGBoost"].predict(X_holdout)
target_names = ['Below -1.5%', '-1.5% to 0%', '0% to 1.5%', 'Above 1.5%']

# Generate Classification Report
report = classification_report(y_holdout, y_pred, target_names=target_names, output_dict=True)
report_df = pd.DataFrame(report).transpose().loc[target_names, :].reset_index().melt(id_vars='index', value_vars=['precision', 'recall', 'f1-score'])

# Interactive Plot Setup
LetsPlot.setup_html()
plot_metrics = ggplot(report_df, aes(x='index', y='value', fill='variable')) + \
               geom_bar(stat='identity', position='dodge') + \
               scale_fill_manual(values=['#1b9e77', '#d95f02', '#7570b3']) + \
               labs(title='XGBoost Audit: Precision, Recall, & F1-Score', x='Regime', y='Score')
print(plot_metrics)

# Confusion Matrix Heatmap
cm = confusion_matrix(y_holdout, y_pred)
cm_data = pd.DataFrame(cm, index=target_names, columns=target_names).stack().reset_index(name='Count')

plot_cm = ggplot(cm_data, aes(x='level_1', y='level_0', fill='Count')) + \
          geom_tile(width=0.95, height=0.95) + geom_text(aes(label='Count')) + \
          scale_fill_gradient(low="#edf8fb", high="#2c7fb8") + \
          labs(title='Confusion Matrix: Holdout Set Audit', x='Predicted', y='Actual')
print(plot_cm)

plt.show()