# Hospital Management System

A comprehensive hospital management system developed using **Django** to streamline essential healthcare operations. This application integrates patient management, billing, and laboratory modules into a single platform with an intuitive dashboard for real-time monitoring.

---

## 🚀 Features

### **Patient Management**
* **Record Keeping:** Create, update, and manage comprehensive patient profiles.
* **Status Tracking:** Maintain detailed history and current status of each patient.

### **Billing System**
* **Invoice Generation:** Create professional invoices for services rendered.
* **Automated Calculations:** Real-time calculation of totals, taxes, and final amounts.
* **Multi-item Support:** Add multiple billing items (consultations, medicine, room charges) to a single invoice.

### **Laboratory Module**
* **Test Management:** Define and manage lab test categories.
* **Result Tracking:** Record and monitor lab results.
* **Status Indicators:** View reports with visual cues for **Pending**, **Completed**, and **Critical** results.

### **Dynamic Dashboard**
* **Key Metrics:** View total counts for patients, doctors, appointments, and revenue.
* **Data Visualization:** Interactive charts for trend analysis.
* **Critical Alerts:** Highlight patients requiring immediate attention.

---

## 🛠️ Technology Stack

* **Backend:** [Django](https://www.djangoproject.com/) (Python)
* **Frontend:** HTML5, CSS3, [Bootstrap 5](https://getbootstrap.com/)
* **Database:** SQLite (Default)
* **Charts:** [Chart.js](https://www.chartjs.org/)

---

## 📂 Project Structure

```text
hospital_project/
│
├── patients/       # Patient management & records module
├── billing/        # Invoicing and payment system
├── labs/           # Lab tests, categories, and results
├── templates/      # Shared HTML templates
├── static/         # Assets (CSS, JavaScript, Images)
└── manage.py       # Django project manager
```

---

## ⚙️ Installation and Setup

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/hospital-management.git
    cd hospital-management
    ```

2.  **Create a virtual environment:**
    ```bash
    # macOS/Linux
    python3 -m venv venv
    source venv/bin/activate

    # Windows
    python -m venv venv
    venv\Scripts\activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Apply database migrations:**
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5.  **Run the development server:**
    ```bash
    python manage.py runserver
    ```

6.  **Access the application:**
    Open your browser and navigate to `http://127.0.0.1:8000/`

---

## 🧪 Sample Data
You can populate the system with initial data (Patients, MRI/Blood Tests, etc.) using the Django shell:
```bash
python manage.py shell
```

---

## 🔮 Future Enhancements
- [ ] **Role-Based Access Control (RBAC):** Distinct permissions for Admin, Doctor, and Staff.
- [ ] **Advanced Filtering:** Search patients and records using complex queries.
- [ ] **PDF Export:** Generate downloadable reports for billing and lab results.
- [ ] **REST API:** Integration for mobile applications via Django Rest Framework.

---

## 🤝 Contributing
Contributions are what make the open-source community such an amazing place to learn, inspire, and create.
1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License
Distributed under the **MIT License**. See `LICENSE` for more information.
