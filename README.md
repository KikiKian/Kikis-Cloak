# Kikis Cloak

## Requirements

- Python 3
- sudo privileges

---

## Installation & Setup

### Step 1 — Clone or download the project

```bash
git clone https://github.com/your-username/kikis-cloak.git
```

### Step 2 — Navigate to the project directory

```bash
cd src/kikis-cloak
```

### Step 3 — Install dependencies (if any)

```bash
pip install -r requirements.txt
```

### Step 4 — Run the script

```bash
sudo python main.py
```

---

## Automate with a Shell Script

### Step 1 — Create the script

Create a file called `cloak` with the following content:

```bash
#!/bin/bash
cd /full/path/to/src/kikis-cloak && sudo python main.py
```

> Replace `/full/path/to/` with the actual path on your system.

### Step 2 — Make it executable

```bash
chmod +x cloak
```

### Step 3 — Move it to your PATH

```bash
sudo mv cloak /usr/local/bin/
```

### Step 4 — Run from anywhere

```bash
cloak
```

---

## Verify Your PATH (optional)

```bash
echo $PATH
```

If you'd prefer to install for your user only (no sudo), place the script in `~/.local/bin/` instead and make sure it's in your PATH by adding this to `~/.bashrc`:

```bash
export PATH="$HOME/.local/bin:$PATH"
```

Then reload:

```bash
source ~/.bashrc
```
