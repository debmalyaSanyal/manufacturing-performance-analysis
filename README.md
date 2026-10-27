# Manufacturing Performance Analysis – 2024 Equipment Efficiency

**Prepared by:** Debmalya Sanyal  
**Email:** 22f3003000@ds.study.iitm.ac.in  

## 1. Business Context

The company is experiencing rising downtime and maintenance costs.  
Current average equipment efficiency is **75.13**, while the **industry benchmark is 90**.  
The goal of this analysis is to understand the quarterly performance and support a decision to implement a **predictive maintenance program**.

## 2. Dataset

**Equipment Efficiency Rate – 2024 Quarterly Data**

| Quarter | Efficiency Rate |
|--------:|----------------:|
| Q1      | 70.54           |
| Q2      | 76.23           |
| Q3      | 78.68           |
| Q4      | 75.05           |

- **2024 Average:** **75.13**  
- **Industry Target:** **90**  
- **Average gap to target:** ≈ **14.87 points**

## 3. Analysis & Visualizations

The script `analysis.py`:

- Loads the quarterly data into a pandas DataFrame  
- Computes:
  - Average efficiency (75.13)  
  - Gap to the 90 benchmark per quarter  
  - Quarter-over-quarter changes  
- Creates two visualizations:
  - `figs/efficiency_trend.png` – quarterly trend vs industry target  
  - `figs/avg_vs_target.png` – average efficiency vs target  

After running the script, you can include the plots in this README like:
 ```markdown
![Quarterly Efficiency Trend](figs/efficiency_trend.png)

![Average vs Industry Target](figs/avg_vs_target.png)
```
### 4. Key Findings

Persistent underperformance: No quarter reaches the industry target of 90.

Partial improvement then decline: Efficiency improves from Q1 → Q3 but drops again in Q4.

Meaningful gap: The yearly average of 75.13 is ~14.87 points below the target, signifying lost capacity and higher downtime risk.

Likely reactive maintenance: The volatility suggests issues are being fixed after failures instead of being predicted and prevented.

### 5. Business Implications

Higher unplanned downtime and volatile throughput

Increased maintenance and overtime costs

Reduced asset life due to repeated breakdowns

Weaker competitiveness vs peers operating near the 90 benchmark

This pattern is not only an operational issue; it represents a strategic business risk.

### 6. Recommendation – Implement a Predictive Maintenance Program

To move toward the 90 target, the recommended solution is to implement a predictive maintenance program, which includes:

Collecting and centralizing sensor data, machine logs, and maintenance records

Using analytics / ML models to:

Predict failures and remaining useful life (RUL)

Trigger work orders before breakdowns

Scheduling maintenance in planned windows to minimize production disruption

Expected impact:

Reduced unplanned downtime

More stable and higher equipment efficiency (lifting the average from 75.13 towards 90)

Lower emergency maintenance costs and better asset utilization

### 7. How to Run the Analysis

Install dependencies:

pip install -r requirements.txt


Run the analysis:

python analysis.py


View the generated figures in the figs/ folder and refer to this README.md for the data story and recommendations.
