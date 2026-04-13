# 🥷 Kikis-Cloak

A lightweight Python tool that spoofs your MAC address on Linux, making your device unrecognizable to your router's device-based filters.

## How It Works

Your router identifies devices by their MAC address. Kikis-Cloak generates a random valid MAC address and assigns it to your network interface, making your device appear as a new, unknown device on the network.

## Requirements

- Linux
- Python 3
- `sudo` privileges (required to change network interface settings)

## Usage

```bash
sudo python main.py
```

That's it. The script will:
1. Detect your active network interface automatically
2. Generate a random valid MAC address
3. Apply it to your interface

## Verify It Worked

```bash
ip link show wlp61s0
```

Look for the `link/ether` field — it should show your new spoofed MAC. Your original MAC will appear under `permaddr`.

## ⚠️ Note

The MAC change is **temporary** and resets on reboot. Run the script again after restarting if needed.

## Tech Stack

- Python 3
- Standard library only (`subprocess`, `re`, `random`, `argparse`)
