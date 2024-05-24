
---

# College Information Server

## Project Description

The College Information Server is designed to manage and analyze data related to colleges, entrance exams, and placements. It provides various functionalities to insert, update, delete, and retrieve information, as well as perform complex queries and data analysis.

## Features

### Insert
- Add details of new entrance exams.
- Add recent news/updates regarding exams, colleges, and programs.

### Delete
- Remove news/updates that are older than a year.
- Delete information about startups (business shutdown).

### Update
- Update entrance exam dates and registration details annually.

### Retrieve
#### Selection
- Find colleges with a median placement greater than 10 LPA.
- Get college rankings where IIT Madras is among the top colleges.

#### Projection
- Retrieve college names and contact details in a city offering a particular program.
- Get contact details of alumni from a given college.
- List entrance exam names and dates required for admission to branches in a given college.

#### Aggregate
- Calculate average placements (median) across all colleges in a given city.
- Determine the branch with the maximum cutoff score across all colleges for a particular exam.

#### Search
- List colleges whose names start with a specific string, e.g., "Indian".
- List branches containing the substring "Computer".

### Analysis
- List branches you are eligible for based on your exam score.
- Calculate the percentage of placements in the college with the highest NIRF ranking.
- Identify industries in which startups founded in Mumbai colleges are operating.

## Project Structure

```plaintext
College Information Server/
│
├── MiniWorld.py
├── aggregate.py
├── analysis.py
├── cadump.sql
├── colours.py
├── conandexec.py
├── delete.py
├── display.py
├── insert.py
├── modify.py
├── projection.py
├── retrieve.py
├── search.py
├── selection.py
├── update.py
├── README.md
├── hah.png
├── circle.png
├── DnA_Report (1).pdf
└── .git/
```

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/College-Information-Server.git
   cd College-Information-Server
   ```

2. **Install dependencies:**
   Make sure you have Python installed. Then, install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up the database:**
   Import the SQL dump to set up your database.
   ```bash
   mysql -u username -p database_name < cadump.sql
   ```

## Usage

1. **Running the scripts:**
   You can run any of the scripts using Python. For example:
   ```bash
   python insert.py
   ```

2. **Functionality:**
   Each script corresponds to a specific functionality as described in the features section. Modify the scripts as needed to fit your requirements.

## Contributing

1. Fork the repository.
2. Create a new branch.
3. Make your changes.
4. Submit a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

---
