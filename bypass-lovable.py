import subprocess
import os

# GitHub credentialsy
token = "insert GitHub personal access token"
username = "insert GitHub username"

# Make sure your Lovable project is in this GitHub account

# To run: Install python3
# go to this file path in your terminal using {cd "file-path"} and enter "python3 bypass-lovable"

# === STEP 1: Ask for repo to clone ===
first_repo = input("Enter repository name to clone (without .git): ")

print(f"Clone: {first_repo}")
input("Press Enter to continue...")

# === STEP 2: Clone the first repo ===
clone_url = f"https://{token}@github.com/{username}/{first_repo}.git"
try:
    subprocess.run(["git", "clone", clone_url], check=True)
except subprocess.CalledProcessError as e:
    print(f"❌ Failed to clone {first_repo}: {e}")
    exit(1)

# === STEP 3: Ask for second repo name ===
second_repo = input("Enter second repository name to push to (without .git): ")

print(f"Push: {second_repo}")
input("Press Enter to continue...")

# === STEP 4: Change into cloned repo directory ===
os.chdir(first_repo)

# === STEP 5: Push to second repo URL ===
push_url = f"https://{token}@github.com/{username}/{second_repo}.git"
try:
    subprocess.run(["git", "push", push_url, "--force"], check=True)
except subprocess.CalledProcessError as e:
    print(f"❌ Failed to push to {second_repo}: {e}")
    exit(1)

print("✅ Done.")

