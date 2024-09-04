# Herovired_assignment_cicd
Building CI-CD Pipeline Tool

Create a complete CI-CD pipeline using bash, python, and crontabs. The list of tasks is specified below: 

Task 1: Set Up a Simple HTML Project 
Create a simple HTML project and push it to a GitHub repository. 

Task 2: Set Up an AWS EC2/Local Linux Instance with Nginx

Task 3: Write a Python Script to Check for New Commits
Create a Python script to check for new commits using the GitHub API.

Task 4: Write a Bash Script to Deploy the Code
Create a bash script to clone the latest code and restart Nginx.

Task 5: Set Up a Cron Job to Run the Python Script
Create a cron job to run the Python script at regular intervals.

Task 6: Test the Setup 
Make a new commit to the GitHub repository and check that the changes are automatically deployed. 

## Getting Started

To start contributing and practicing HTML, follow these steps:

1. **Fork the Repository**
   - Fork this repository to create a copy under your own GitHub account. This allows you to make changes without affecting the original repository.

2. **Clone the Forked Repository**
   - Clone the forked repository to your local machine using the following command:
     ```bash
     git clone https://github.com/YOUR_USERNAME/Herovired_assignment_cicd.git
     ```

3. **Navigate to the Project Directory**
   - Change into the project directory:
     ```bash
     cd Herovired_assignment_cicd
     ```

4. **Create a New Branch**
   - Create a new branch for your changes:
     ```bash
     git checkout -b my-new-branch
     ```

5. **Make Your Changes**
   - Add your HTML files or modify existing ones as needed.

6. **Commit Your Changes**
   - Stage your changes and commit them with a descriptive message:
     ```bash
     git add .
     git commit -m "Describe your changes here"
     ```

7. **Push Your Changes**
   - Push your changes to your forked repository:
     ```bash
     git push origin my-new-branch
     ```


## Local Linux Instance with Nginx ##

**install Nginx**
    - Go to Ubuntu system on local , Install Nginx 

1. **Install nginx**
   - Install nginx Ubuntu :
     ```bash
     sudo apt-get install nginx -y
     ```

     ```
2. **Enable nginx**
   - Enable nginx Ubuntu :
     ```bash
     sudo systemctl enable nginx
     ```
3. **check status of nginx**
   - checking status of nginx :
     ```bash
     sudo systemctl status nginx
     ```
4. **start nginx**
   - start nginx Ubuntu :
     ```bash
     sudo systemctl start nginx
     ```
 

## 
- Create Project Dir cicd_project , deploy file and check commit file :
     ```bash
     mkdir cicd_project
     cd cicd_project
     touch check_commits.py
     touch deploy.sh
     ```
## Python Script to Check for New Commits
- 
   ```bash
     vi  check_commits.py
   
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
     ```

## Bash Script to Deploy the Code
- 
   ```bash
     vi  deploy.sh
     #!/bin/bash

      # Variables
      REPO_URL="https://github.com/MrSRE/Herovired_assignment_cicd.git"
      CLONE_DIR="/mnt/p/Vscode/Devops/cicd_project/Herovired_assignment_cicd"

      echo "Checking if directory exists: $CLONE_DIR"

      # Clone the repository (or pull if it already exists)
      if [ ! -d "$CLONE_DIR" ]; then
         echo "Cloning repository..."
         git clone "$REPO_URL" "$CLONE_DIR"
      else
         echo "Directory exists. Pulling latest changes..."
      cd "$CLONE_DIR" || exit
      git pull
      fi

      # Check if clone or pull succeeded
      if [ $? -ne 0 ]; then
      echo "Error cloning or pulling repository."
      exit 1
      fi

      # Copy the updated index.html file to Nginx root directory
      echo "Copying index.html to /var/www/html/"
      sudo cp "$CLONE_DIR/index.html" /var/www/html/

      # Check if copy succeeded
      if [ $? -ne 0 ]; then
         echo "Error copying index.html."
         exit 1
      fi

      # Restart Nginx to apply changes
      echo "Restarting Nginx..."
      sudo systemctl restart nginx

      # Check if restart succeeded
      if [ $? -ne 0 ]; then
         echo "Error restarting Nginx."
         exit 1
      fi

      echo "Deployment completed and Nginx restarted."
     ```

## Contributing

We welcome contributions from everyone. Please follow these guidelines to contribute:

1. **Fork the repository** to your own GitHub account.
2. **Clone the forked repository** to your local machine.
3. **Create a new branch** for your changes.
4. **Make your changes** and **commit them**.
5. **Push your changes** to GitHub.
6. **Create a Pull Request** to merge your changes back into the main repository.

For more detailed guidelines, please read our [CONTRIBUTING.md](CONTRIBUTING.md).

Happy coding!
