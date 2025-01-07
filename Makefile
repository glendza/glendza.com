.ONESHELL:
.SHELL := /bin/bash
.PHONY: setup deploy vault-create vault-edit decrypt view rekey

# Load environment variables from .env.make:
include .env.make
export

ANSIBLE_DIR=./ansible

# Setup SSH agent and add key:
setup:
	@echo "Setting Visual Studio Code as the editor..."
	export EDITOR="$${EDITOR}"
	@echo "Setup complete."

# Deploy using Ansible playbook:
deploy: setup
	@echo "Setting up SSH agent..."
	eval "$$(ssh-agent -s)" && \
	ssh-add $${SSH_KEY_LOCATION}
	@echo "Running Ansible playbook..."
	cd $${ANSIBLE_DIR} && \
	ansible-playbook playbooks/main.yml --vault-password-file $${ANSIBLE_PASSWORD_FILE}

# Create a new encrypted vault file:
vault-create: setup
	@echo "Creating a new encrypted file..."
	cd $${ANSIBLE_DIR} && ansible-vault create $$(read -p "Enter file location: " loc && echo $$loc) --vault-password-file $${ANSIBLE_PASSWORD_FILE}

# Edit an existing encrypted vault file:
vault-edit: setup
	@echo "Editing an encrypted file..."
	cd $${ANSIBLE_DIR} && ansible-vault edit $$(read -p "Enter file location: " loc && echo $$loc) --vault-password-file $${ANSIBLE_PASSWORD_FILE}

# Decrypt a file (temporarily view decrypted content):
decrypt: setup
	@echo "Decrypting a file..."
	cd $${ANSIBLE_DIR} && ansible-vault decrypt $$(read -p "Enter file location: " loc && echo $$loc) --vault-password-file $${ANSIBLE_PASSWORD_FILE}

# View a file (decrypt without saving changes):
view: setup
	@echo "Viewing an encrypted file..."
	cd $${ANSIBLE_DIR} && ansible-vault view $$(read -p "Enter file location: " loc && echo $$loc) --vault-password-file $${ANSIBLE_PASSWORD_FILE}

# Rekey a file (change password):
rekey: setup
	@echo "Rekeying an encrypted file..."
	cd $${ANSIBLE_DIR} && ansible-vault rekey $$(read -p "Enter file location: " loc && echo $$loc) --vault-password-file $${ANSIBLE_PASSWORD_FILE}

# Edit the inventory.ini encrypted vault file:
edit-inventory: setup
	@echo "Editing the inventory.ini file..."
	cd $${ANSIBLE_DIR} && ansible-vault edit inventory.ini --vault-password-file $${ANSIBLE_PASSWORD_FILE}

# Edit the ansible/vars/encrypted_vars/app_env_vars.yml encrypted vault file:
edit-host-vars: setup
	@echo "Editing app_env_vars.yml file..."
	cd $${ANSIBLE_DIR} && ansible-vault edit ./vars/encrypted_vars/host_vars.yml --vault-password-file $${ANSIBLE_PASSWORD_FILE}

# Edit the ansible/vars/encrypted_vars/app_env_vars.yml encrypted vault file (another path):
edit-app-env-vars: setup
	@echo "Editing another app_env_vars.yml file..."
	cd $${ANSIBLE_DIR} && ansible-vault edit ./vars/encrypted_vars/app_env_vars.yml --vault-password-file $${ANSIBLE_PASSWORD_FILE}
