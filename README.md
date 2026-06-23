# CI/CD Pipeline with GitHub Actions + AWS ECR

Automated CI/CD pipeline that builds Docker images and pushes to AWS ECR on every git push.

## Pipeline Flow
1. Developer pushes code to GitHub
2. GitHub Actions triggers automatically
3. Docker image is built and tested
4. Image pushed to AWS ECR with commit SHA tag

## Tech Stack
- GitHub Actions
- AWS ECR
- Docker
- Python Flask

## Author
Prasad Sonar - github.com/prasad-sonar-code
