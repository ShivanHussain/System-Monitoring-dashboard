# System Monitoring Dashboard (Flask + psutil)

A modern **System Monitoring Dashboard** built using **Python Flask** and **psutil** that displays real-time CPU and Memory usage of the server.  
The dashboard features an interactive UI with **Plotly gauges**, uptime tracking, and alert notifications for high resource utilization.

---

##  Features

- Real-time CPU utilization monitoring  
- Memory usage visualization  
- Total CPU cores detection  
- Server uptime display  
- Automatic alerts for high CPU or memory usage  
- Modern, responsive UI with animations  
- Interactive gauges using Plotly  

---

## Tech Stack

- **Backend:** Python, Flask  
- **System Metrics:** psutil  
- **Frontend:** HTML, CSS, JavaScript  
- **Charts:** Plotly.js  

---

## Project Structure

```
.
├── app.py
├── requirements.txt
├── templates
│   └── index.html
└── README.md
```

---

## Installation & Setup

### 1 Clone the Repository
```bash
git clone https://github.com/ShivanHussain/System-Monitoring-dashboard.git
cd system-monitoring-dashboard
```

### 2 Create Virtual Environment (Optional)
```bash
python3 -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate    # Windows
```

### 3 Install Dependencies
```bash
pip3 install -r requirements.txt
```

---

## Run the Application

```bash
python3 app.py
```

The Flask server will start on:

```
http://localhost:5001/
```

---

## Dashboard Details

The homepage displays:

- CPU usage percentage  
- Memory utilization percentage  
- Number of CPU cores  
- Server uptime  
- Visual gauges with color-coded status  
- Alert messages when usage exceeds safe limits  

---

## Alert Levels

| Usage % | Status   |
|-------|----------|
| < 50% | Normal   |
| 50–85% | Warning |
| ≥ 85% | Critical|

---

## Dependencies

See `requirements.txt` for the complete list of dependencies.

---



##  Docker Support

###  Build Docker Image

```bash
docker build -t system-monitoring-dash .
```

### Run Docker Container

```bash
docker run -d -p 5001:5001 
    --name system-dash
    system-monitoring-dash
```


---

##  Docker Compose 

###  Start Application

```bash
docker-compose up -d
```

### Stop Application

```bash
docker-compose down
```


---

##  Future Improvements

- Auto-refresh using AJAX  
- Disk & Network monitoring  
- Authentication  
- Docker support  

---

## License

This project is licensed under the **MIT License**.

---

