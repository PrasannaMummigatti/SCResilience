import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import norm

# -------------------------------
# Simulation Parameters
# -------------------------------
np.random.seed(42)
n_simulations = 1000
products = ['A', 'B', 'C']

# Forecast demand and std deviation per product
forecast_demand = {'A': 120, 'B': 100, 'C': 80}
demand_std = {'A': 25, 'B': 30, 'C': 35}  # product-specific variability

Z = 1.65  # for ~95% service level
h_cost = 2
s_cost = 10

# Inventory Levels (No Postponement)
indiv_inventory = {p: forecast_demand[p] + Z * demand_std[p] for p in products}

# Pooled inventory calculation (Postponement)
total_forecast = sum(forecast_demand[p] for p in products)
total_variance = sum(demand_std[p]**2 for p in products)
pooled_inventory = total_forecast + Z * np.sqrt(total_variance)

# Results Storage
results = []

# -------------------------------
# Simulation Loop
# -------------------------------
for _ in range(n_simulations):
    actual_demand = {
        p: max(0, int(np.random.normal(forecast_demand[p], demand_std[p])))
        for p in products
    }
    total_actual = sum(actual_demand.values())

    # --- Without Postponement ---
    fulfilled_A = sum(min(actual_demand[p], indiv_inventory[p]) for p in products)
    excess_A = sum(max(0, indiv_inventory[p] - actual_demand[p]) for p in products)
    stockout_A = total_actual - fulfilled_A
    cost_A = h_cost * excess_A + s_cost * stockout_A
    service_A = fulfilled_A / total_actual if total_actual > 0 else 1.0

    # --- With Postponement ---
    fulfilled_B = min(total_actual, pooled_inventory)
    stockout_B = total_actual - fulfilled_B
    excess_B = max(0, pooled_inventory - total_actual)
    cost_B = h_cost * excess_B + s_cost * stockout_B
    service_B = fulfilled_B / total_actual if total_actual > 0 else 1.0

    results.append({
        'stockout_A': stockout_A,
        'excess_A': excess_A,
        'service_A': service_A,
        'cost_A': cost_A,
        'stockout_B': stockout_B,
        'excess_B': excess_B,
        'service_B': service_B,
        'cost_B': cost_B,
    })

# -------------------------------
# Results Analysis
# -------------------------------
df = pd.DataFrame(results)
print("\n📊 Average Results Over", n_simulations, "Simulations:\n")
print(df.mean().round(2))
#df.to_csv('postponement_simulation_results.csv', index=False)

# -------------------------------
# Visualization
# -------------------------------
metrics = [
    ('excess_A', 'excess_B', 'Excess Inventory', (0,350), 30),
    ('stockout_A', 'stockout_B', 'Stockouts', (0, 30), 30),
    ('service_A', 'service_B', 'Service Level', (0.97, 1.0), 100),
    ('cost_A', 'cost_B', 'Total Cost', None, 50),
]

fig, axs = plt.subplots(2, 2, figsize=(14, 10))
axs = axs.flatten()
fig.set_facecolor('lightyellow')
colors = ['tab:blue', 'tab:orange']

for ax, (col_a, col_b, title, xlim, bins) in zip(axs, metrics):
    for col, label, color in zip([col_a, col_b], ['No Postponement', 'With Postponement'], colors):
        data = df[col]
        mean = data.mean()
        std = data.std()

        # Histogram
        ax.hist(data, bins=bins, alpha=0.4, label=f'{label}', color=color, density=True)

        # PDF curve
        x_vals = np.linspace(data.min(), data.max(), 300)
        pdf = norm.pdf(x_vals, mean, std)
        ax.plot(x_vals, pdf, color=color, linestyle='--', linewidth=2)

        # Mean line with label in legend
        ax.axvline(mean, color=color, linestyle=':', linewidth=2)
        ax.plot([], [], color=color, linestyle=':', label=f'Mean ({label}): {mean:.2f}')

    ax.set_title(title, fontsize=14, fontweight='bold')
    #ax.set_xlabel('Value')
    #ax.set_ylabel('Density')
    ax.legend(facecolor='lightyellow', frameon=False)
    ax.set_facecolor('lightyellow')
    # Remove the borders (spines)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.yaxis.set_ticks([])  # Hide y-axis ticks
    if xlim:
        ax.set_xlim(xlim)

plt.tight_layout()
plt.show()
