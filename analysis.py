import pandas as pd
import matplotlib.pyplot as plt
import os

# -----------------------------
# 1. Data setup
# -----------------------------
data = {
    "Quarter": ["Q1", "Q2", "Q3", "Q4"],
    "Efficiency": [70.54, 76.23, 78.68, 75.05]
}

df = pd.DataFrame(data)
industry_target = 90

# Compute metrics
df["Gap_to_Target"] = industry_target - df["Efficiency"]
df["QoQ_Change"] = df["Efficiency"].diff()

avg_efficiency = df["Efficiency"].mean()
print(f"Average equipment efficiency: {avg_efficiency:.2f}")  # should be 75.13

# -----------------------------
# 2. Ensure figs directory exists
# -----------------------------
os.makedirs("figs", exist_ok=True)

# -----------------------------
# 3. Line chart: quarterly trend vs benchmark
# -----------------------------
plt.figure(figsize=(8, 5))
plt.plot(df["Quarter"], df["Efficiency"], marker="o", linewidth=2, label="Equipment Efficiency")
plt.axhline(industry_target, linestyle="--", linewidth=1.5, label="Industry Target (90)")
plt.title("Quarterly Equipment Efficiency Rate - 2024")
plt.xlabel("Quarter")
plt.ylabel("Efficiency Rate")
plt.ylim(60, 95)
plt.grid(True, linestyle="--", alpha=0.4)
plt.legend()
plt.tight_layout()
plt.savefig("figs/efficiency_trend.png", dpi=300)
plt.close()

# -----------------------------
# 4. Bar chart: average vs target
# -----------------------------
plt.figure(figsize=(6, 5))
x_labels = ["2024 Avg", "Industry Target"]
values = [avg_efficiency, industry_target]

bars = plt.bar(x_labels, values)
plt.title("Average Equipment Efficiency vs Industry Target")
plt.ylabel("Efficiency Rate")
plt.ylim(60, 95)

# Highlight bars
for i, v in enumerate(values):
    plt.text(i, v + 1, f"{v:.2f}", ha="center", fontweight="bold")

plt.tight_layout()
plt.savefig("figs/avg_vs_target.png", dpi=300)
plt.close()

# -----------------------------
# 5. Simple console summary
# -----------------------------
print("\n=== Summary ===")
print(df)
print(f"\nAverage efficiency (should be 75.13): {avg_efficiency:.2f}")
print(f"Gap to target: {industry_target - avg_efficiency:.2f} points")
