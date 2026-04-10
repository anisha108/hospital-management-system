# hospital-management-system
A comprehensive hospital management system developed using Django to streamline essential healthcare operations, including patient management, billing, and laboratory testing. The application provides an intuitive user interface along with a dynamic dashboard for monitoring key metrics and improving operational efficiency.
Features
Patient Management
Create, update, and manage patient records
Maintain detailed patient information and status tracking
Billing System
Generate and manage invoices
Automatic calculation of totals, taxes, and final amounts
Support for multiple billing items
Laboratory Module
Manage lab tests and test categories
Record and track lab results
View detailed reports with status indicators such as Pending, Completed, and Critical
Dashboard
Display key statistics including total patients, doctors, appointments, and revenue
Visualize data using charts for better insights
Highlight critical patients for quick attention
User Interface
Clean and responsive design using Bootstrap
Interactive charts implemented with Chart.js
Technology Stack
Backend: Django (Python)
Frontend: HTML, CSS, Bootstrap
Database: SQLite (default Django database)
Data Visualization: Chart.js
Project Structure
hospital_project/
│
├── patients/       # Patient management module
├── billing/        # Billing system module
├── labs/           # Laboratory tests and results
├── templates/      # HTML templates
├── static/         # Static files (CSS, JS)
└── manage.py
Installation and Setup
Clone the repository:
git clone https://github.com/your-username/hospital-management.git
cd hospital-management
Create a virtual environment:
python -m venv venv
source venv/bin/activate      # macOS/Linux
venv\Scripts\activate         # Windows
Install dependencies:
pip install -r requirements.txt
Apply migrations:
python manage.py makemigrations
python manage.py migrate
Run the development server:
python manage.py runserver
Access the application at:
http://127.0.0.1:8000/
Sample Data
The system can be populated with sample data such as:
Patient records
Laboratory tests (e.g., blood test, MRI, X-ray)
Lab results with varying statuses
Use the Django shell to insert sample data:
python manage.py shell
Future Enhancements
Role-based authentication (Admin, Doctor, Staff)
Advanced search and filtering capabilities
Export reports in PDF format
REST API integration
Contributing
Contributions are welcome. Please fork the repository and submit a pull request for any improvements or new features.
License
This project is open-source and available under the MIT License.
