# 🛡️ Mini DoS (Denial-of-Service) Attack Simulation

A beginner-friendly Python project built to understand the **working principles of Denial-of-Service (DoS) attacks** in a safe and controlled local environment.

The primary objective of this project is **learning**, not attacking real systems. It demonstrates how repeated requests can consume server resources and affect service availability by simulating a basic DoS scenario on a locally hosted HTTP server.

---

## 📌 Project Objective

This project was built as part of my cybersecurity learning journey to gain a practical understanding of:

- How a Denial-of-Service (DoS) attack works
- How repeated HTTP requests impact a server
- The difference between theoretical concepts and practical implementation
- Safe and ethical cybersecurity experimentation using localhost

Instead of targeting external systems, the entire simulation runs on **localhost**, ensuring a controlled learning environment.

---

## 🚀 Features

- Local HTTP Server built using Python
- Python-based DoS traffic generator
- Request counter to monitor incoming traffic
- Simulates repeated HTTP GET requests
- Displays server-side request count in real time
- Measures successful requests
- Demonstrates basic resource exhaustion concepts
- Safe and ethical implementation (localhost only)

---

## 📂 Project Structure

```
DoS-Lab/
│
├── server.py          # Local HTTP server (victim server)
├── dos_attack.py      # Request flooding simulation
├── README.md
└── .gitignore
```

---

## ⚙️ How It Works

1. A local HTTP server is started using Python.
2. The server listens on **localhost:8000**.
3. A second Python script sends multiple HTTP GET requests to the server.
4. The server counts every incoming request.
5. The simulation demonstrates how excessive requests can occupy server resources and affect service responsiveness.

---

## ▶️ Running the Project

### Clone the repository

```bash
git clone https://github.com/IshitaPadhi/Mini-DoS-Demo-Cybersecurity.git
```

### Navigate to the project folder

```bash
cd Mini-DoS-Demo-Cybersecurity
```

### Install dependencies

```bash
pip install requests
```

### Start the local server

```bash
python server.py
```

### In another terminal, run the simulation

```bash
python dos_attack.py
```

---

## 📸 Sample Output

### Server

```
Victim Server Running
URL : http://localhost:8000

Requests Received : 1
Requests Received : 2
Requests Received : 3
...
Requests Received : 500
```

### Client

```
Mini DoS Attack Started

Request 1 Sent | Status : 200
Request 2 Sent | Status : 200
Request 3 Sent | Status : 200

...

Attack Completed

Total Requests Sent : 500
Successful Requests : 500
Failed Requests     : 0
```

---

## 🧠 Concepts Learned

Through this project I gained a practical understanding of:

- Denial-of-Service (DoS) attacks
- HTTP Request Flooding
- Client-Server Communication
- Request Handling
- Python HTTP Server
- Resource Consumption
- Safe Cybersecurity Experimentation
- Ethical Security Testing

---

## 🛠 Technologies Used

- Python
- HTTPServer
- Requests Library
- Basic Networking Concepts

---

## 🔮 Future Improvements

- Multi-threaded request generation
- Adjustable attack intensity
- Request rate control
- Real-time monitoring dashboard
- Logging and statistics
- Wireshark traffic analysis
- Docker-based lab environment
- Comparison between DoS and DDoS simulations

---

## 📚 Learning Resources

This project was developed after studying:

- CrowdStrike Cybersecurity 101 – Denial-of-Service (DoS) Attacks
- IBM Technology – SYN Flood Attack Concepts
- Python HTTP Server Documentation

---

## ⚠️ Disclaimer

This project is developed **strictly for educational purposes** to understand the concepts behind Denial-of-Service (DoS) attacks.

The simulation is performed **only against a locally hosted server (localhost)** owned by the developer. It must **never** be used against systems, networks, or services without explicit authorization.

---

## 👩‍💻 Author

**Ishita Padhi**

Computer and Communication Engineering Undergraduate

Cybersecurity • AI/ML • Software Development
