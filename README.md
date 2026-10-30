
# 📱 Smartphone Finder AI

An intelligent smartphone recommendation website that helps users explore and discover smartphones based on their specifications, ratings, and prices.

## 🚀 Project Overview

Smartphone Finder AI is a mini project developed to make smartphone discovery easier. It uses a structured smartphone dataset to display mobile phone information and help users explore suitable devices.

The project focuses on presenting smartphone specifications through a simple, interactive, and user-friendly web interface.

## 🎯 Problem Statement

Choosing a smartphone can be difficult because of the large number of available options and technical specifications.

This project aims to simplify smartphone discovery by organizing smartphone data and presenting useful information in an accessible way.

## ✨ Features

- Browse smartphone information.
- Search for smartphones.
- Explore smartphone specifications.
- Discover the top 5 smartphones.
- View ratings and prices.
- Compare specifications such as RAM, storage, camera, battery, and processor.
- Interactive and user-friendly interface.

## 🛠️ Technologies Used

- HTML – Structure of the website.
- CSS – Styling and responsive design.
- JavaScript – Functionality and dataset handling.
- CSV – Smartphone dataset.
- Python – Data cleaning and preprocessing.

## 📊 Dataset Information

The project uses a cleaned smartphone dataset containing:

- Total Records: 413
- Total Features: 11

### Dataset Columns

| Column | Description |
|---|---|
| name | Smartphone name |
| rating | Smartphone rating |
| price | Smartphone price |
| camera | Camera specifications |
| display_type | Display technology |
| display_size | Screen size |
| battery | Battery capacity |
| storage | Internal storage |
| ram | RAM capacity |
| weight | Smartphone weight |
| processor | Processor information |

## 📂 Project Structure

```text
Smartphone-Finder-AI/
│
├── index.html
│
└── DATA/
    ├── pj1 mini project.finalcleaned.csv
    ├── pj1 mini project.cleaned.csv
    ├── pj1 mini project.csv
    ├── pj1 mini project.xlsx
    ├── raw.py
    ├── datacleaning.py
    ├── exploredata.py
    └── recommend.py
```

## ⚙️ How to Run the Project

1. Download or clone this repository.
2. Open the project folder in VS Code.
3. Make sure the DATA folder is in the same directory as index.html.
4. Start a local server using:

```bash
python -m http.server 8000
```

5. Open your browser and visit:

```text
http://localhost:8000
```

6. Open the website and explore smartphone recommendations.

## 🧠 Data Processing

The dataset was cleaned and prepared before being used in the website.

The data preparation process included:

- Understanding the dataset.
- Exploring smartphone features.
- Cleaning and standardizing data.
- Preparing the cleaned CSV for frontend integration.

## ⚠️ Project Limitations

- The project currently uses a static CSV dataset.
- No backend database or API is integrated.
- Recommendations depend on the available dataset and implemented frontend logic.

## 🔮 Future Improvements

- Integrate a machine learning recommendation model.
- Add personalized recommendations.
- Develop a backend API.
- Integrate a live smartphone database.
- Improve recommendation accuracy.

## 👩‍💻 Project Author

**Iqra Parveen**

B.Tech – Computer Science and Engineering

## 📄 License

This project is developed for educational and learning purposes.