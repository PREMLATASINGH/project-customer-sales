# README — project.py

This repository contains a small exploratory script, `project.py`, that loads a CSV sales dataset and prints basic summaries and visualizations.

## What `project.py` does
- Reads `customer_sales_5000.csv` into a pandas DataFrame.
- Prints head, info, descriptive statistics, column list, and simple aggregations.
- Computes and prints mean/median/min/max/std and value counts for `total_amount`.
- Shows top transactions, grouped summaries by `payment_method`, and null-count checks.
- Drops rows with missing values in-place and computes a `revenue` series as `price * quantity`.
- Displays three plots: histogram of `total_amount`, scatter plot of `quantity` vs `total_amount`, and a boxplot of `total_amount`.

## Dependencies
- Python 3.9+
- `numpy`
- `pandas`
- `matplotlib`

Install with:

```bash
pip install -r requirements.txt
```

## Run
Place `customer_sales_5000.csv` in the project root and run:

```bash
python project.py
```

The script prints outputs to the console and opens matplotlib windows for the plots.

## Notes & suggestions
- The script uses `dropna(inplace=True)` which mutates the DataFrame; consider assigning the result instead.
- Add argument parsing to specify input file and output options.
- Save plots to files for non-interactive runs using `plt.savefig()` before `plt.show()`.
- Add basic logging and error handling around reading the CSV.

For more help or a README expanded with examples and schema, tell me what you'd like included.
