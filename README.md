# Quantium starter repo


```
# 🍽️ Soul Foods - Pink Morsel Sales Data Processing

This project processes and formats transaction data from Soul Foods' Morsel product line. The goal is to extract and analyze **Pink Morsel** sales across different regions and dates, and output a clean dataset for visualization or further analysis.

## 📁 Project Structure

```

/workspace/
│
├── data/
│   ├── daily\_sales\_data\_0.csv
│   ├── daily\_sales\_data\_1.csv
│   └── daily\_sales\_data\_2.csv
│
├── formatted\_sales\_data.csv   # Final output file
├── main.py                    # Main script to process data
└── README.md                  # This file

````

## 📌 Task Overview

1. Load three raw CSV files containing morsel sales data.
2. Filter for rows where `product == "Pink Morsel"`.
3. Calculate `Sales = quantity * price`.
4. Keep only relevant columns: `Sales`, `date`, and `region`.
5. Output the cleaned dataset to a new CSV file.

## 🛠️ How to Run

1. **Install dependencies** (if using Replit Shell):
   ```bash
   pip install pandas
````

2. Run the script:

   ```bash
   python main.py
   ```

3. **Output**: The processed data will be saved in `formatted_sales_data.csv`.

## 📊 Output Format

| Sales | date       | region |
| ----- | ---------- | ------ |
| 120   | 2024-02-01 | West   |
| 300   | 2024-02-02 | South  |

## 💡 Notes

* Only "Pink Morsel" product sales are retained.
* Make sure the raw CSV files are placed in the `/data` folder.
* File paths in `main.py` are hardcoded to match this structure.

```

---


