# Herovired_assignment_cicd
Building CI-CD Pipeline Tool

* Create a complete CI-CD pipeline using bash, python, and crontabs. The list of tasks is specified below: 

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
 
## Contributing

We welcome contributions from everyone. Please follow these guidelines to contribute:

1. **Fork the repository** to your own GitHub account.
2. **Clone the forked repository** to your local machine.
3. **Create a new branch** for your changes.
4. **Make your changes** and **commit them**.
5. **Push your changes** to GitHub.
6. **Create a Pull Request** to merge your changes back into the main repository.

For more detailed guidelines, please read our [CONTRIBUTING.md](CONTRIBUTING.md).

## Code of Conduct

Please read our [Code of Conduct](CODE_OF_CONDUCT.md) before contributing. We are committed to providing a friendly, safe, and welcoming environment for all.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Happy coding!
