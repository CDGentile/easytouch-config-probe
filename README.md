# EasyTouch Config Probe

A lightweight Node.js utility to connect to a Pentair EasyTouch pool controller over RS485 using a Seeed `reComputer R1025-10`.  

The purpose of this tool is to:
- Poll and log configuration messages from the EasyTouch system
- Help observe and record the pool equipment setup (pumps, valves, heater)
- Serve as a backend foundation before building a custom web UI.

---

## 🚀 Project status

✅ In development.

---

## ⚡ Requirements

- **Hardware**: 
  - Seeed `reComputer R1025-10`
  - RS485 connection to Pentair EasyTouch RS485 bus
  - GPIO pin 6 for TX enable on `/dev/ttyAMA2`

- **Software**:
  - Raspberry Pi OS
  - Node.js LTS (installed via `nvm` recommended)
  - Docker (optional, for containerization later)

---

## 🔧 Setup

```bash
# Clone this repository:
git clone git@github.com:<your-github-username>/easytouch-config-probe.git

# Change directory:
cd easytouch-config-probe

# Install dependencies (once implemented):
npm install

## 📋 Usage

Coming soon: Node.js script to open `/dev/ttyAMA2`, enable RS485 TX/RX, and log configuration frames.

## 📝 Notes

- Use GPIO6 to control RS485_1 DE/RE line
- Baud rate: 9600 (typical for Pentair)
- Observe bus polarity (`A` and `B` wires may need swapping if no comms)

---

## 🖋️ Author

Chris Gentile  
MIT-style license.