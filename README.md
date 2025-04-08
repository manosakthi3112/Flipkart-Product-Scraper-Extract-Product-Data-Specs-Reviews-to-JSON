
# 🛒 Flipkart Product Scraper

This Python script scrapes product data (names, prices, images, reviews, and specifications) from [Flipkart](https://www.flipkart.com), one of India’s largest e-commerce websites. It outputs the collected data in a well-formatted JSON file with a timestamp.

## 📌 Features

- Scrapes product names, prices, and image links
- Follows product links to gather detailed specifications and user reviews
- Saves data into a timestamped `.json` file
- Uses `requests` and `BeautifulSoup` for clean and fast scraping

## 🖼 Sample Output

```json
[
  {
    "NAME": "Product Name",
    "PRICE": "₹XX,XXX",
    "IMAGE_LINK": "https://image-url.jpg",
    "VISIT_LINK": "https://www.flipkart.com/...",
    "REVIEW": {
      "Review Title": "Review content"
    },
    "SPECS": {
      "Display": "6.5 inch AMOLED",
      "Battery": "5000 mAh",
      ...
    }
  },
  ...
]
```

## 🚀 Getting Started

### 🔧 Prerequisites

Ensure you have the following Python packages installed:

```bash
pip install requests beautifulsoup4 html5lib
```

### ▶️ Running the Script

```bash
python flipkart_scraper.py
```

The output will be saved in the same directory with a timestamped filename like:

```
2025-04-08_14-22-33.json
```

## ⚠️ Disclaimer

- This script is for **educational purposes only**.
- Flipkart may update their website structure at any time, which can break this scraper.
- Always check and respect a website’s [`robots.txt`](https://www.flipkart.com/robots.txt) and Terms of Service before scraping.

## 📚 Technologies Used

- Python 3.x
- `requests`
- `BeautifulSoup` (`bs4`)
- `html5lib`
- `json`
- `datetime`

## 📌 Future Enhancements

- Add support for multiple categories
- Export to CSV/Excel
- Add CLI arguments for page range and keyword filtering
- Integrate logging and better error handling

## 🧑‍💻 Author

**Samruddhi Patil**  
📫 [LinkedIn](https://linkedin.com/) | 💻 [GitHub](https://github.com/)

---

📝 _If you like this project, feel free to star ⭐ the repo and contribute!_
