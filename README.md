# 🧁 Pink Morsel Sales Dashboard

An interactive data visualization dashboard built with [Dash](https://dash.plotly.com/) and [Plotly](https://plotly.com/python/), designed to help Soul Foods analyze regional sales trends and understand the impact of a key pricing decision.

---

## 📸 Preview

![App Preview](https://i.imgur.com/9Nlu8iH.png)
---

## �� Features

- 📈 Interactive Line Chart
  Visualizes daily `Sales` across regions over time.

- 🔺 Price Change Indicator
  Highlights January 15, 2021 with a red dashed vertical line to mark when prices increased.

- 🌍 Regional Comparison  
  Allows clear insights into sales performance by `region`.

- 🧰 Built With
  - Python 3.x
  - Dash by Plotly
  - Pandas (for data handling)
  - CSV file as data source

---

## 🗂️ Project Structure

```bash
.
├── App.py                   # Main dashboard application
├── formatted_data.csv       # Cleaned sales data
├── assets/                  # Optional Dash styles and scripts
└── README.md

📦 Installation

# Clone the repository

# Install dependencies
pip install -r requirements.txt

# Run the app
python App.py


📊 Data Source

The dataset used (formatted_data.csv) contains:
date: Sales date
region: Sales region
Sales: Daily revenue 

🧠 Insights Enabled
Assess sales impact pre- and post-price increase
Monitor regional performance trends
Support data-driven pricing decisions

📜 License
This project is licensed under the MIT License.

---

