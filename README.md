#  Pink Morsel Sales Dashboard

An interactive data visualization dashboard built with Dash and Plotly, designed to help Soul Foods analyze regional sales trends and understand the impact of a key pricing decision.

---

## 📸 App Preview

![App Preview](https://i.imgur.com/P0lwKoa.png)

---

## ✨ Features

- 📈 Interactive Line Chart
  Visualizes daily sales across regions over time.

- 🔺 Price Change Indicator
  Highlights January 15, 2021 with a red dashed vertical line to mark when prices increased.

- 🌍 Regional Comparison
  Enables insights into performance by region via radio button filters.

---

## 🧰 Built With

- Python 3.x  
- Dash by Plotly  
- Pandas  
- CSV (as data source)

---

## 🗂️ Project Structure

├── app.py               # Dash app

├── formatted_data.csv   # Cleaned sales data

├── main.py              # Optional: installs dependencies

├── requirements.txt     # Dependencies

├── run_tests.sh         # Bash script for CI testing

├── test_app.py          # Dash tests

└── README.md            # You're here!

---

### 🚀 Getting Started:

## 🟣 Option 1: Run on Replit

[![Run on Replit](https://replit.com/badge/github/azukauteh/quantium-starter-repo)](https://replit.com/@azukauteh/quantium-starter-repo)

1. Click the badge above to open the project in Replit.  
2. Press the green Run button.  
3. The dashboard will appear in the web preview pane.

---

### 💻 Option 2: Run Locally

1. Clone the repository:
   ```bash
   git clone https://github.com/azukauteh/quantium-starter-repo.git
   

2. Install dependencies:
```bash
   ./requirements.txt

📊 Data Source

 Column | Description       |
| ------ | ----------------- |
| date   | Sales date        |
| region | Sales region      |
| sales  | Daily revenue (R) |


🧠 Insights Enabled

Assess sales impact before and after the price change.
Monitor regional performance trends.
Support informed pricing decisions.


📜 License

This project is licensed under the MIT License.



Made with ❤️ using Dash & Plotly
