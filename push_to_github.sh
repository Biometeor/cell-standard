#!/bin/bash
# Push to GitHub using Personal Access Token
# Usage: bash push_to_github.sh <your_github_token>

if [ -z "$1" ]; then
    echo "Usage: bash push_to_github.sh <github_personal_access_token>"
    echo "Token needs 'repo' scope permission"
    exit 1
fi

TOKEN="$1"
REPO_URL="https://${TOKEN}@github.com/Biometeor/cell-standard.git"

cd "D:/OneDrive - BGI Tech Solutions (Hongkong) Co., Ltd/个人文件/项目/2026/数据整理/cell-standard-docs"

echo "Pushing to GitHub..."
git push "$REPO_URL" main

if [ $? -eq 0 ]; then
    echo "✓ Successfully pushed to GitHub!"
    echo "✓ Repository: https://github.com/Biometeor/cell-standard"
    echo ""
    echo "Next: Configure ReadTheDocs at https://readthedocs.org/dashboard/"
else
    echo "✗ Push failed. Check token permissions (need 'repo' scope)"
fi
