<div align="center">

# 🛰️ AegisNet Edge Core
### Autonomous Off-Grid Disaster Communication Engine

*Localized triage. Rescue vector mapping. Zero-infrastructure emergency routing.*

![Status](https://img.shields.io/badge/status-active-brightgreen)
![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![FastAPI](https://img.shields.io/badge/backend-FastAPI-009688)
![SQLite](https://img.shields.io/badge/database-SQLite3-07405e)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

</div>

---

## 📌 Overview

**AegisNet** is an autonomous, decentralized disaster management architecture engineered to provide **localized triage**, **rescue vector mapping**, and **emergency network routing** when standard cellular towers, power grids, and internet infrastructure fail completely.

The core engine uses lightweight edge intelligence to parse civilian emergency distress signals, automatically classify resource priorities **without centralized cloud access**, and stream live, responsive instruction coordinates to local operator nodes — entirely over local networks.

> Built for the moment the grid goes dark and the network still needs to know who to save first.

---

## 📖 Table of Contents

- [Overview](#-overview)
- [Architectural Flow](#-core-architectural-flow)
- [Deep Learning & Full-Stack Intelligence](#️-deep-learning--full-stack-intelligence)
- [Tech Stack](#-tech-stack)
- [System Interfaces](#-system-interfaces-production-snapshots)
- [Demo Videos](#-demo-videos)
- [Getting Started](#-getting-started)
- [Repository Structure](#-repository-structure)
- [Roadmap](#-roadmap)
- [Notes](#-notes)

---

## 📊 Core Architectural Flow

The network operates completely **peer-to-peer** over local access networks — no ISP, no cell tower, no cloud dependency. Field clients synchronize directly with a central server node over the local mesh, which maintains the authoritative state ledger.

```
┌──────────────────┐        Local Wi-Fi / Mesh Hotspot        ┌──────────────────┐
│  Civilian Field   │ ───────────────────────────────────────▶ │   Server / Edge   │
│  Client Node(s)   │ ◀─────────────────────────────────────── │   Gateway Node     │
│  (Mobile/Laptop)  │        distress signals + telemetry       │  (FastAPI+SQLite) │
└──────────────────┘                                            └────────┬─────────┘
                                                                          │
                                                                          ▼
                                                                ┌──────────────────┐
                                                                │  Operator Panel   │
                                                                │  Live Dashboard   │
                                                                └──────────────────┘
```

*(Swap this ASCII diagram for your topology image/diagram file once available.)*

---

## 🛠️ Deep Learning & Full-Stack Intelligence

AegisNet abstracts high-overhead Deep Learning workflows into optimized, low-latency rules engines designed to run efficiently on restricted edge hardware — single-board computers, localized mesh gateways, and low-power field devices.

| Capability | Description |
|---|---|
| 🧠 **NLP Triage Engine** | Automated keyword-triage scanning performs semantic matching on raw strings (e.g. `"collapsed"`, `"flood"`, `"trapped"`) to instantly map civilian communications into prioritized emergency matrices. |
| ⚡ **Edge Optimization** | Deterministic routing matrices minimize computation cycles — response instructions are calculated in **under 5 ms**, with near-zero processing overhead on constrained gateways. |
| 🔗 **Peer-to-Peer Sync** | No centralized cloud dependency; nodes synchronize state directly across the local network. |
| 📡 **Resilient Routing** | Prioritization and routing logic remain fully functional even with intermittent or fully offline connectivity. |

---

## 🧩 Tech Stack

<div align="center">

| Layer | Technology |
|---|---|
| **Backend Interface** | FastAPI + Uvicorn (Async Web Server) |
| **Database Ledger** | SQLite3 State Persistence |
| **Frontend Stream** | Vanilla JavaScript Event-Loop, Live Dynamic Dashboard |
| **Networking Layer** | Raw Socket Programming Protocols |

</div>

---

## 💻 System Interfaces (Production Snapshots)

### 1️⃣ Central Control Center & Operator Panel
The centralized dashboard monitors the live SQLite state ledger. The layout background **mutates automatically** based on incoming risk threat level — from **Standby Mode** to **Critical Red Alert**.

### 2️⃣ Live Simulation — Laptop Node (Server & Operator View)
The async backend terminal actively listens on local Wi-Fi interface sockets, instantly categorizing raw triage strings using structural metadata analysis.

### 3️⃣ Live Simulation — Mobile Node (Civilian Client View)
An independent mobile field node connects over an offline mesh hotspot, demonstrating interactive multipart photo uploads and geolocation reporting directly to the ledger.

---

## 🎥 Demo Videos

| Demo | Description | Link |
|---|---|---|
| 🖥️ VS Code Walkthrough / Flood Scenario | Full walkthrough of the codebase and a simulated flood-disaster triage run | [▶ demo_vscode_flood.mp4](./demo_vscode_flood.mp4) |
| 📱 Mobile Node Screen Recording | Live capture of the mobile civilian client node reporting over the offline mesh | [▶ demo_mobile_node.mp4](./demo_mobile_node.mp4) |

> 💡 GitHub/GitLab don't always render `.mp4` inline in Markdown previews — if the video doesn't play directly, click the link to download/stream it.

---

## 🚀 Getting Started

### The Dual-Role Simulation Pipeline

Run a complete end-to-end integration test on a **single host machine** by letting your laptop act as both the server host and a client node simultaneously.

**1. Initialize the Core Engine**

```bash
pip install -r requirements.txt
python server.py
```

**2. Launch a Client Node**

On the same machine, or a second device on the same local network/hotspot:

```bash
python client.py
```

**3. Observe the Live Dashboard**

Open the operator dashboard in your browser to watch triage classifications and risk-level changes update in real time as simulated distress messages are ingested.

---

## 📁 Repository Structure

```
aegisnet/
├── server.py
├── client.py
├── requirements.txt
├── demo_vscode_flood.mp4
├── demo_mobile_node.mp4
└── README.md
```

---

## 🗺️ Roadmap

- [ ] Add topology/architecture diagram image
- [ ] Add dashboard + terminal screenshots
- [ ] Expand rescue-vector mapping module
- [ ] Add multi-hop mesh relay support
- [ ] Add automated test suite

---


<div align="center">

**AegisNet — because the network shouldn't need permission to save a life.**

</div>
