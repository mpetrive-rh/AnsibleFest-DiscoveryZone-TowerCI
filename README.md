# Demo: Tower Onboarding and GitLab CI
This project provides an environment to demonstrate a basic GitLab CI/CD pipeline for Ansible playbook/role verification.

[Recording of demo](https://drive.google.com/file/d/1tSDOCBxqHqBUWDe-0t2ZUX-YuC_k6hHI/view?usp=sharingRecording) utilizing this environment and associated [slide deck](https://drive.google.com/file/d/1CWBJJn1fyK8Vxa2N5UVztMVbZT6MdOvy/view?usp=sharing)

### Software Requirements
* Vagrant (tested on v2.1.1)
* VirtualBox (tested on v5.2.18)
* Ansible (tested on v2.7)

### License requirements
* Ansible Tower license placed at `REPO_DIR/license.txt`.  A demo license can be obtained here https://www.ansible.com/license


### Software Installed & Provided

* Gitlab CE latest version installed via https://galaxy.ansible.com/geerlingguy/gitlab
* Gitlab Runner latest version installed via https://galaxy.ansible.com/riemers/gitlab-runner
* Ansible Tower latest version (currently 3.3) provided via `ansible/tower` vagrant box

### Machines provisioned
* GitLab URL: [https://172.16.2.50/](https://172.16.2.50/)
* Gitlab Runner : 172.16.2.51
* Ansible Tower: [https://172.16.2.52](https:/172.16.2.52)

### Gitlab Runner

This CI runner will be provisioned with molecule and docker installed to allow for
validation roles

### Provisioning Steps

* Clone this repo and change to project dir

```
# REPO = this github repo
# REPO_DIR = target dir for the clone
git clone REPO REPO_DIR
cd REPO DIR
```

* Copy vars file template to vars file utilized

```
cp vars/main_template.yml vars/main.yml
```

* Add Ansible Tower license file at correct location, `license.txt`

```
cp LICENSE_FILE_LOCATION license.txt
```

* Install required roles:

```
ansible-galaxy install -r roles/requirements.yml -p roles/
```

* Create gitlab CE server:

```
vagrant up gitlab
```

* Follow instructions in ansible playbook error to create an access token and add to `vars/main.yml`

```
gitlab_private_token is not defined.  Please login in to the web interface
as root and obtain a personal access token at https://gitlab/profile/personal_access_tokens.
The token values should be added to the vars/main.yml file
```

* Finish provisioning on gitlab CE server

```
vagrant provision gitlab
```

* Create and provision gitlab runner and ansible tower

```
vagrant up gitlab-runner ansible-tower
```

if this step fails make sure you have valid Tower file at the location specified above


* Follow the steps in the recorded demo to exercise Tower onboarding and Gitlab CI functionality
