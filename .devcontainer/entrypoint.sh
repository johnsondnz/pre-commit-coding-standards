#!/bin/bash

set -e

echo "==> Configure pre-commit"
pre-commit install --install-hooks

[ -s ./.devcontainer/pip-requirements.txt ] && echo "==> Install pip packages" && pip3 install --no-cache-dir -r ./.devcontainer/pip-requirements.txt || echo "==> No additional packages to install"

echo "==> Clone ansible-prod" 
sudo chown cclops:cclops /workspaces
git clone git@github.com:ComputerConceptsLimited/ansible-prod.git /workspaces/ansible-prod

echo "==> Prevent push to ansible-prod"
echo "==> Can still commit and test"
mv /workspaces/ansible-prod/.git/config /workspaces/ansible-prod/.git/config.bak
