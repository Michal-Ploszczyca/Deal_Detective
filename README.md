# 🕵️‍♂️ Deal Detective: iPhone Price Scraper & Analyzer 📱

**Deal Detective** is an intelligent Python-based scraper tool designed to sift through selected online retailers and capture the real-time pricing data for the iPhone 14 series. It then carefully archives this data in an SQLite database, laying the groundwork for insightful analytics, especially price trends and potential deals.

---

## 🛠️ Features:

- **Multi-site Scanning:** Actively fetches data from platforms like Morele, Xcom, and MediaMarkt.
- **Dynamic Data Storage:** All the scraped smartphone names and prices are securely stored in an SQLite database for further use.
- **Flexibility:** The tool has been structured to be adaptable, making it easier to include other smartphone models or online retailers in the future.
- **User-Friendly Output:** The data is presented in a clean, clear manner, making it easy to understand at a glance.

---

## 🗃️ SQLite Database:

Every scrape session populates the `smartphone.db` SQLite database. This allows for historic data storage and further SQL operations, from simple lookups to more intricate analytics. You can view and query this database using tools like DB Browser for SQLite or by using SQL capabilities within the PyCharm environment.

---

## ⚙️ Installation & Setup:

1. **Prerequisites:**
    - Make sure you have Python 3.x installed. You can download it from [here](https://www.python.org/downloads/).
    - Ensure you have Chrome installed as the WebDriver uses Chrome for scraping.

2. **Dependencies:** 
    - You need to install required Python packages. Navigate to your script's directory in the terminal or command prompt and run: 
      ```
      pip install selenium
      pip install selenium webdriver_manager
      ```

3. **Database:** 
    - The SQLite database (`smartphones.db`) will be created automatically when you run the script. No additional setup is needed.

---

## 🚀 Running the Script:

1. Open your terminal or command prompt.
2. Navigate to the directory containing the script.
3. Run the script using: python main.py
