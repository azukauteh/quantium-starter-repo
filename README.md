# quantium-starter-repo


```markdown
# 🧁 Pink Morsel Sales Visualiser

This project analyzes and visualizes sales data for Soul Foods' Pink Morsels product line using Python and Dash.

---

## 📊 Purpose

Soul Foods wants to answer a key business question:

> Were sales higher before or after the Pink Morsel price increase on January 15, 2021?

This project filters and formats raw sales data, and provides a visual dashboard to clearly answer that question.

---

## 📁 Project Structure

```

workspace/
├── data/
│   ├── daily\_sales\_data\_0.csv
│   ├── daily\_sales\_data\_1.csv
│   ├── daily\_sales\_data\_2.csv
│   └── formatted\_sales\_data.csv    # Cleaned sales data for Pink Morsels
├── main.py                         # Dash app to visualize sales trends
├── README.md

````

---

## ⚙️ How It Works

1. Data Processing
   - Filters raw sales records to only include **Pink Morsels**
   - Computes daily total sales using `sales = quantity * price`
   - Exports the cleaned dataset to `formatted_sales_data.csv`

2. Dash Visualization
   - Line chart showing **daily sales trends**
   - Highlights price change date (**January 15, 2021**)

---

## 📦 Requirements

Install project dependencies:

```bash
pip install pandas dash plotly
````

---

## 🚀 Run the App

In your terminal, from the root folder:

```bash
python3 main.py
```

Then open your browser and go to: [http://localhost:8050](http://localhost:8050)

---

## 📝 Outcome

With this dashboard, stakeholders at Soul Foods can easily **compare sales before and after the price increase and make informed business decisions.

---

## 👤 Author

* GitHub: [azukauteh](https://github.com/azukauteh)

```

---


```
