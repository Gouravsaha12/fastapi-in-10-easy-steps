# 1_Project_Setup_&_Developer_Ergonomics

## Quickstart

```bash
# 1. Clone
git clone https://github.com/you/1_Project_Setup_&_Developer_Ergonomics.git
cd 1_Project_Setup_&_Developer_Ergonomics

# 2. (venv) Create & activate env
python3 -m venv .venv
source .venv/bin/activate   # or `.venv\Scripts\activate` on Windows

# 3. Install deps
pip install -r requirements.txt

# 4. Launch
uvicorn main:app --reload
