**Simulation-Based Analysis of Supply Chain Resilience: Postponement vs. No Postponement**

---

**Objective:**
This document outlines the step-by-step process, methodology, and calculations used in a simulation to compare two inventory strategies under demand uncertainty: one with product postponement and one without. The goal is to assess which strategy better supports supply chain resilience.

---

**Step 1: Define Product Forecasts and Uncertainty**
Three distinct products (A, B, C) are considered. Each product has a unique forecasted mean demand and a different standard deviation representing demand variability. This setup reflects real-world unpredictability in customer demand across product categories.

---

**Step 2: Simulate Actual Demand**
For each iteration in the simulation, actual demand is randomly generated for each product using a normal distribution based on its respective forecast and standard deviation. This simulates real-life uncertainty where demand fluctuates around expected values.

---

**Step 3: Determine Inventory Levels**

*Case 1: No Postponement*
Each product is produced and stocked individually. Safety stock is calculated using the formula:

Inventory = Forecast + Z \* Standard Deviation

Where Z represents the service level factor (e.g., 1.65 for 95% confidence).

*Case 2: With Postponement*
A single pooled inventory of base products is held. Safety stock is calculated using risk pooling:

Total Forecast = Sum of product forecasts
Pooled Standard Deviation = Square root of the sum of variances
Pooled Inventory = Total Forecast + Z \* Pooled Standard Deviation

This method reduces overall inventory by consolidating variability.

---

**Step 4: Fulfillment and Shortage Calculations**

*No Postponement*
Each product's actual demand is compared to its inventory. Fulfilled demand is the lesser of the two. Excess inventory and stockouts are calculated accordingly.

*With Postponement*
Total actual demand across all products is compared to the pooled inventory. Fulfilled demand is the minimum of total demand and pooled inventory. Excess and stockouts are derived from the difference.

---

**Step 5: Cost Calculation**
Two types of costs are calculated:

* Holding Cost = Cost per unit of excess inventory
* Shortage Cost = Cost per unit of unmet demand

Total Cost = (Holding Cost \* Excess Inventory) + (Shortage Cost \* Stockout)

This captures both inefficiency (excess) and customer service impact (stockouts).

---

**Step 6: Service Level Calculation**
Service level is calculated as:

Service Level = Fulfilled Demand / Total Actual Demand

This reflects the proportion of demand that is successfully met.

---

**Step 7: Repeat Simulation**
The simulation is run for 1,000 iterations. In each iteration, actual demand, fulfillment, costs, and service levels are recalculated. Results are stored for comparison.

---

**Step 8: Analyze Results**
The average performance across all simulations is computed for each strategy. Key performance indicators compared include:

* Stockouts
* Excess inventory
* Service level
* Total cost

---

**Summary of Findings:**
The simulation demonstrates that the postponement strategy:

* Requires less total inventory (thanks to risk pooling)
* Achieves higher service levels under variability
* Reduces both excess and stockouts
* Lowers overall supply chain cost

This confirms that postponement is an effective strategy to enhance supply chain resilience by improving responsiveness, minimizing performance dips during disruptions, and placing inventory buffers more intelligently.

---

**What This Simulation Helped Us Understand About Resilience:**

* **How fast can you respond?** Postponement allows delayed differentiation, enabling faster and more accurate response to actual demand rather than relying solely on forecast.

* **How big is the performance dip?** Without postponement, stockouts and excess inventory were higher, indicating a sharper performance decline under demand uncertainty. Postponement softened this dip and maintained service levels more consistently.

* **How much buffer do you need — and is it smartly placed?** Postponement reduced the total inventory required due to risk pooling. It smartly places the buffer at the base-product level where it offers the most flexibility and efficiency.

This illustrates how simulation-based analysis can inform smarter, more resilient supply chain design choices.
