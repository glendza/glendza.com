# Glendza

![Web app deploy](https://github.com/glendza/glendza/actions/workflows/run-ansible.yml/badge.svg)

# Deployment notes

## Github secrets

| Key | Description |
| ------------- | ------------- |
| **ANSIBLE_PASSWORD** | The password used for encrypting and decrypting Ansible vault files. |
| **HOST_SSH_PRIVATE_KEY** | The private SSH key used for authenticating the server during deployment. |
