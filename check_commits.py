import requests
import os

# Replace these variables with your own repository details
REPO_OWNER = 'MrSRE'
REPO_NAME = 'Herovired_assignment_cicd'
BRANCH_NAME = 'main'  # or any branch you're interested in
COMMIT_FILE = '/mnt/p/Vscode/Devops/cicd_project/last_commit_sha.txt'  # File to store the last checked commit SHA

# GitHub API URL for commits
GITHUB_API_URL = f'https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/commits?sha={BRANCH_NAME}'

def get_latest_commit_sha():
    response = requests.get(GITHUB_API_URL)
    
    if response.status_code == 200:
        commit_data = response.json()
        latest_sha = commit_data[0]['sha']  # Access the first commit's SHA
        return latest_sha
    else:
        print(f"Failed to fetch commit data: {response.status_code}")
        return None

def read_last_commit_sha():
    if os.path.exists(COMMIT_FILE):
        with open(COMMIT_FILE, 'r') as file:
            return file.read().strip()
    return None

def write_last_commit_sha(sha):
    with open(COMMIT_FILE, 'w') as file:
        file.write(sha)

def main():
    latest_sha = get_latest_commit_sha()
    
    if latest_sha:
        last_sha = read_last_commit_sha()
        
        if latest_sha != last_sha:
            print(f"New commit detected! Latest SHA: {latest_sha}")
            write_last_commit_sha(latest_sha)
            # Trigger deployment (call deploy script here)
            os.system('/mnt/p/Vscode/Devops/cicd_project/deploy.sh')
        else:
            print("No new commits.")
    else:
        print("Could not retrieve commit information.")

if __name__ == '__main__':
    main()
