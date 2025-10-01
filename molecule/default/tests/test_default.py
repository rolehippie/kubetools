import os
import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


@pytest.mark.parametrize("executable", [
    "/usr/bin/argocd",
    "/usr/bin/clusterctl",
    "/usr/bin/kind",
    "/usr/bin/stern",
    "/usr/bin/k9s",
    "/usr/bin/sonobuoy",
    "/usr/bin/flux",
])
def test_executable(host, executable):
    assert host.file(executable).is_file
