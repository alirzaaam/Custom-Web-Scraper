# NBA Stats Scraper

🧠 **Overview**  
This Python project scrapes NBA player statistics from [NBA.com](https://www.nba.com/stats/leaders) using **Selenium** and **BeautifulSoup**, then saves the data into a CSV file. It collects key player stats such as points, games played, minutes, and points per game.  

💡 **Key Features**  
- Scrapes live NBA stats from the official NBA website.  
- Collects key statistics: Player name, Points, Games Played (GP), Minutes (MIN), and Points per Game (PTS).  
- Saves the data into a structured CSV file for further analysis.  
- Handles dynamic page content with Selenium.  

⚙️ **How to Run**  

1. **Clone the repository**  

```bash
git clone https://github.com/yourusername/nba-stats-scraper.git
cd nba-stats-scraper
Install dependencies

bash
Copy code
pip install selenium beautifulsoup4 pandas
Download ChromeDriver

Make sure ChromeDriver is installed and compatible with your Chrome browser version.

Add it to your system PATH or provide its path in the code:

python
Copy code
driver = webdriver.Chrome(executable_path="path/to/chromedriver")
Run the scraper

bash
Copy code
python nba_scraper.py
Check the output

The scraped stats will be saved in nba_leader_stats.csv.

📁 File Structure

bash
Copy code
.
├── nba_scraper.py           # Main Python script for scraping
├── nba_leader_stats.csv     # Output CSV (generated after running)
└── README.md                # Project documentation
🌐 Features Summary

✅ Scrapes NBA player stats from the official site
✅ Handles dynamic page loading with Selenium
✅ Saves structured data to CSV
✅ Works with live data, ready for analysis

🧰 Technologies Used

Python

Selenium

BeautifulSoup

Pandas

⚠️ Notes

Ensure your internet connection is stable as the scraper fetches live data.

The NBA website structure may change, which could require updates to the code.
