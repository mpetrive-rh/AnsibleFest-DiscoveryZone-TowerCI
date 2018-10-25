import os
import pytest
# import requests

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

pkgs_svcs = ['nginx', 'firewalld']


@pytest.mark.parametrize('pkg', pkgs_svcs)
def test_pkg(host, pkg):
    package = host.package(pkg)

    assert package.is_installed


@pytest.mark.parametrize('svc', pkgs_svcs)
def test_svc(host, svc):
    service = host.service(svc)

    assert service.is_running
    assert service.is_enabled

    # r = requests.get('http://localhost/')
    # assert r.status_code == 200
    # assert 'Managed by Ansible' in r.text
    assert host.socket('tcp://80').is_listening
