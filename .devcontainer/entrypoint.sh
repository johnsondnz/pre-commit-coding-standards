set -e
PATH=$PATH:~/.local/bin

[ -s .pre-commit-config.yaml ] && echo "Configure pre-commit..." && pre-commit install --install-hooks || echo "==> No pre-commit to install"
[ -s ./.devcontainer/pip-requirements.txt ] && echo "==> Install pip packages..." && pip3 install --no-cache-dir -r ./.devcontainer/pip-requirements.txt || echo "==> No additional pip packages to install"
[ -s ./.devcontainer/apt-requirements.txt ] && echo "==> Install apt packages..." && sudo apt update && sudo xargs apt-get install -y <./.devcontainer/apt-requirements.txt || echo "==> No additional apt packages to install"
sudo chown generic:generic /home/generic/.gnupg && echo "==> Set permissions on gnupg..." || echo "==> No permissions to set on gnupg"
sudo chmod 666 /var/run/docker.sock && echo "==> Set permissions on docker socket..." || echo "==> Docker socket not mounted, use -v option to mount"
[ -s ./.devcontainer/.password ] && echo "==> Logging into ghcr.io..." && cat ./.devcontainer/.password | docker login ghcr.io --username johnsondnz --password-stdin || echo "==> ghcr.io password not found"
zsh
