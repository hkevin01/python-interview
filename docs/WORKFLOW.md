# Development Workflow

## Branching Strategy
- Use `main` for stable releases
- Create feature branches for new features
- Use `dev` for integration and testing
- Merge via pull requests with code review

## CI/CD Pipeline
- GitHub Actions for build, test, and deploy
- Linting and code style checks on every push
- Automated testing for all PRs
- Deployment to release branch or package registry

## Code Review Process
- All changes require PRs
- At least one reviewer approval
- Automated checks must pass before merge
- Use CODEOWNERS for critical files

## Issue and PR Templates
- Use provided templates for bug reports and feature requests
- PR template requires description, checklist, and linked issues

## Security
- Report vulnerabilities via SECURITY.md
- Critical fixes prioritized
