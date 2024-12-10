# **University Timetable Web Application**

## **Description**

This project is a **University Timetable Web Application** developed using **Flask** and connected to a **PostgreSQL database** hosted on **Amazon RDS**. The application allows users to dynamically view a timetable based on selected student levels (Undergraduate or Graduate). It is hosted on an **EC2 instance** and styled with a minimalistic, professional design.

---

## **Technologies Used**

- **Flask**: Backend framework.
- **PostgreSQL**: Database system hosted on Amazon RDS.
- **pg8000**: Database driver for connecting Flask to PostgreSQL.
- **HTML & CSS**: For frontend development.
- **Amazon EC2**: Hosting the Flask application.
- **Amazon RDS**: Hosting the PostgreSQL database.

---

## **Steps Followed During Development**

### **1. Project Setup**

- Created a project directory structure:
    
    ```
    university_timetable_gulnoza/
    ├── app.py
    ├── templates/
    │   ├── index.html
    │   └── timetable_gulnoza.html
    ├── venv/
    └── requirements.txt
    ```
    
- Set up a virtual environment:
    
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
    
- Installed required libraries:
    
    ```bash
    pip install flask pg8000
    ```
    

---

### **2. Database Setup**

- Configured a PostgreSQL database hosted on Amazon RDS.
- Created the `timetable` table with sample data:
    
    ```sql
    CREATE TABLE timetable (
        id SERIAL PRIMARY KEY,
        course_name VARCHAR(100),
        level VARCHAR(20),
        day VARCHAR(20),
        time VARCHAR(20)
    );
    
    INSERT INTO timetable (course_name, level, day, time)
    VALUES
    	('Data Structures I', 'Undergraduate', 'Monday', '11:30 AM'),
        ('Database Applications', 'Undergraduate', 'Tuesday', '04:30 PM'),
        ('Principles of Programming', 'Undergraduate', 'Monday', '04:30 PM'),
        ('Operating Systems', 'Undergraduate', 'Tuesday', '02:30 PM'),
        ('Computer Languages', 'Undergraduate', 'Monday', '02:30 PM');
        ('Math 101', 'Undergraduate', 'Monday', '10:00 AM'),
        ('Physics 202', 'Undergraduate', 'Tuesday', '12:00 PM'),
        ('Business 303', 'Graduate', 'Wednesday', '2:00 PM'),
        ('History 404', 'Undergraduate', 'Thursday', '4:00 PM'),
        ('CS 505', 'Graduate', 'Friday', '6:00 PM');
    ```
    

---

### **3. Backend Development**

- Developed the `app.py` file for handling routes:
    - **`/`**: Displays the main form for selecting levels.
    - **`/timetable`**: Fetches and displays timetable data from the database.

---

### **4. Frontend Development**

- Designed two HTML templates with responsive and professional styling:
    - **`index.html`**: Form for selecting student levels.
    - **`timetable_gulnoza.html`**: Displays timetable data dynamically.

---

### **5. Hosting and Deployment**

- Deployed the Flask application on an Amazon EC2 instance.
- Connected the EC2 instance to the RDS database using security group configurations.


## **How to Run**

1. Clone the repository:
    
    ```bash
    git clone https://github.com/khayrullaevna/university_timetable_gulnoza.git
    cd university_timetable_gulnoza
    
    ```
    
2. Set up the virtual environment:
    
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```
    
    - if `python3` is not available, use `python -m venv venv`
    
    if windows:
    
    ```bash
    python3 -m venv venv
    venv\Scripts\activate
    pip install -r requirements.txt
    ```
    
3. Run the application:
    
    ```bash
    python app.py
    ```
    
4. Open your browser and navigate to:
    
    ```
    http://127.0.0.1:8000
    ```
    

---