# Expense Tracker 💰

A full-stack expense tracking web application built with **Django** and **PostgreSQL**, designed to help users efficiently manage and analyze their daily expenses.

---

## 🚀 Features

- **User Authentication** – Secure registration, login, and logout system.
- **CRUD Operations** – Add, edit, delete, and view expenses.
- **Categorization** – Organize expenses by category and date.
- **Responsive UI** – Clean and simple interface for seamless experience.
- **Data Validation** – Prevents invalid or incomplete data entries.
- **In-Progress:** Expense statistics and insights dashboard.

---

## 🛠️ Tech Stack

**Backend:** Django (Python)  
**Database:** PostgreSQL  
**Frontend:** HTML, CSS, Bootstrap  
**Version Control:** Git & GitHub

---

## ⚙️ Installation and Setup

### Prerequisites

Make sure you have the following installed:

- Python (≥ 3.8)
- pip
- PostgreSQL
- Git

### Steps

1. **Clone the Repository**

   ```bash
   git clone https://github.com/<your-username>/ExpenseTracker.git
   cd ExpenseTracker
   ```

2. **Create a Virtual Environment**

   ```bash
   python -m venv venv
   source venv/bin/activate     # For Mac/Linux
   venv\Scripts\activate        # For Windows
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Database Setup**

   - Create a PostgreSQL database
   - Update your database credentials in `settings.py`

5. **Run Migrations**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Start the Development Server**
   ```bash
   python manage.py runserver
   ```
   Visit [http://localhost:8000](http://localhost:8000) in your browser.

---

## 📂 Project Structure

```
ExpenseTracker/
│
├── manage.py
├── requirements.txt
├── expense_app/
│   ├── migrations/
│   ├── templates/
│   ├── static/
│   ├── views.py
│   ├── models.py
│   ├── urls.py
│   └── forms.py
└── ...
```

---

## 🔮 Future Enhancements

- Add expense statistics dashboard (charts, monthly insights)
- Export data to CSV/PDF
- Add budgeting and goal-tracking module

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

---

## 🧾 License

This project is open-source and available under the [MIT License](LICENSE).
