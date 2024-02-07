# kubetools

[![Source Code](https://img.shields.io/badge/github-source%20code-blue?logo=github&logoColor=white)](https://github.com/rolehippie/kubetools)
[![General Workflow](https://github.com/rolehippie/kubetools/actions/workflows/general.yml/badge.svg)](https://github.com/rolehippie/kubetools/actions/workflows/general.yml)
[![Readme Workflow](https://github.com/rolehippie/kubetools/actions/workflows/docs.yml/badge.svg)](https://github.com/rolehippie/kubetools/actions/workflows/docs.yml)
[![Galaxy Workflow](https://github.com/rolehippie/kubetools/actions/workflows/galaxy.yml/badge.svg)](https://github.com/rolehippie/kubetools/actions/workflows/galaxy.yml)
[![License: Apache-2.0](https://img.shields.io/github/license/rolehippie/kubetools)](https://github.com/rolehippie/kubetools/blob/master/LICENSE)
[![Ansible Role](https://img.shields.io/badge/role-rolehippie.kubetools-blue)](https://galaxy.ansible.com/rolehippie/kubetools)

Ansible role to install cli tools around kubernetes.

## Sponsor

Building and improving this Ansible role have been sponsored by my current and previous employers like **[Cloudpunks GmbH](https://cloudpunks.de)** and **[Proact Deutschland GmbH](https://www.proact.eu)**.

## Table of content

- [Requirements](#requirements)
- [Default Variables](#default-variables)
  - [kubetools_argocd_arch](#kubetools_argocd_arch)
  - [kubetools_argocd_download](#kubetools_argocd_download)
  - [kubetools_argocd_enabled](#kubetools_argocd_enabled)
  - [kubetools_argocd_version](#kubetools_argocd_version)
  - [kubetools_clusterctl_arch](#kubetools_clusterctl_arch)
  - [kubetools_clusterctl_download](#kubetools_clusterctl_download)
  - [kubetools_clusterctl_enabled](#kubetools_clusterctl_enabled)
  - [kubetools_clusterctl_version](#kubetools_clusterctl_version)
  - [kubetools_flux_arch](#kubetools_flux_arch)
  - [kubetools_flux_download](#kubetools_flux_download)
  - [kubetools_flux_enabled](#kubetools_flux_enabled)
  - [kubetools_flux_version](#kubetools_flux_version)
  - [kubetools_install_path](#kubetools_install_path)
  - [kubetools_k9s_arch](#kubetools_k9s_arch)
  - [kubetools_k9s_download](#kubetools_k9s_download)
  - [kubetools_k9s_enabled](#kubetools_k9s_enabled)
  - [kubetools_k9s_version](#kubetools_k9s_version)
  - [kubetools_kind_arch](#kubetools_kind_arch)
  - [kubetools_kind_download](#kubetools_kind_download)
  - [kubetools_kind_enabled](#kubetools_kind_enabled)
  - [kubetools_kind_version](#kubetools_kind_version)
  - [kubetools_sonobuoy_arch](#kubetools_sonobuoy_arch)
  - [kubetools_sonobuoy_download](#kubetools_sonobuoy_download)
  - [kubetools_sonobuoy_enabled](#kubetools_sonobuoy_enabled)
  - [kubetools_sonobuoy_version](#kubetools_sonobuoy_version)
  - [kubetools_stern_arch](#kubetools_stern_arch)
  - [kubetools_stern_download](#kubetools_stern_download)
  - [kubetools_stern_enabled](#kubetools_stern_enabled)
  - [kubetools_stern_version](#kubetools_stern_version)
- [Discovered Tags](#discovered-tags)
- [Dependencies](#dependencies)
- [License](#license)
- [Author](#author)

---

## Requirements

- Minimum Ansible version: `2.10`

## Default Variables

### kubetools_argocd_arch

Architecture for argocd

#### Default value

```YAML
kubetools_argocd_arch: "{{ 'arm64' if ansible_architecture == 'aarch64' else 'amd64'
  }}"
```

### kubetools_argocd_download

URL to download argocd from

#### Default value

```YAML
kubetools_argocd_download: https://github.com/argoproj/argo-cd/releases/download/v{{
  kubetools_argocd_version }}/argocd-linux-{{ kubetools_argocd_arch }}
```

### kubetools_argocd_enabled

Enable installation of argocd cli

#### Default value

```YAML
kubetools_argocd_enabled: true
```

### kubetools_argocd_version

Version of argocd to install

#### Default value

```YAML
kubetools_argocd_version: 2.10.0
```

### kubetools_clusterctl_arch

Architecture for clusterctl

#### Default value

```YAML
kubetools_clusterctl_arch: "{{ 'arm64' if ansible_architecture == 'aarch64' else 'amd64'
  }}"
```

### kubetools_clusterctl_download

URL to download clusterctl from

#### Default value

```YAML
kubetools_clusterctl_download: https://github.com/kubernetes-sigs/cluster-api/releases/download/v{{
  kubetools_clusterctl_version }}/clusterctl-linux-{{ kubetools_clusterctl_arch }}
```

### kubetools_clusterctl_enabled

Enable installation of clusterctl cli

#### Default value

```YAML
kubetools_clusterctl_enabled: true
```

### kubetools_clusterctl_version

Version of clusterctl to install

#### Default value

```YAML
kubetools_clusterctl_version: 1.6.1
```

### kubetools_flux_arch

Architecture for flux

#### Default value

```YAML
kubetools_flux_arch: "{{ 'arm64' if ansible_architecture == 'aarch64' else 'amd64'
  }}"
```

### kubetools_flux_download

URL to download flux from

#### Default value

```YAML
kubetools_flux_download: https://github.com/fluxcd/flux2/releases/download/v{{ kubetools_flux_version
  }}/flux_{{ kubetools_flux_version }}_linux_{{ kubetools_flux_arch }}.tar.gz
```

### kubetools_flux_enabled

Enable installation of flux cli

#### Default value

```YAML
kubetools_flux_enabled: true
```

### kubetools_flux_version

Version of flux to install

#### Default value

```YAML
kubetools_flux_version: 2.2.3
```

### kubetools_install_path

Path to install the binaries

#### Default value

```YAML
kubetools_install_path: /usr/bin
```

### kubetools_k9s_arch

Architecture for k9s

#### Default value

```YAML
kubetools_k9s_arch: "{{ 'arm64' if ansible_architecture == 'aarch64' else 'amd64'
  }}"
```

### kubetools_k9s_download

URL to download k9s from

#### Default value

```YAML
kubetools_k9s_download: https://github.com/derailed/k9s/releases/download/v{{ kubetools_k9s_version
  }}/k9s_Linux_{{ kubetools_k9s_arch }}.tar.gz
```

### kubetools_k9s_enabled

Enable installation of k9s cli

#### Default value

```YAML
kubetools_k9s_enabled: true
```

### kubetools_k9s_version

Version of k9s to install

#### Default value

```YAML
kubetools_k9s_version: 0.31.8
```

### kubetools_kind_arch

Architecture for kind

#### Default value

```YAML
kubetools_kind_arch: "{{ 'arm64' if ansible_architecture == 'aarch64' else 'amd64'
  }}"
```

### kubetools_kind_download

URL to download kind from

#### Default value

```YAML
kubetools_kind_download: https://github.com/kubernetes-sigs/kind/releases/download/v{{
  kubetools_kind_version }}/kind-linux-{{ kubetools_kind_arch }}
```

### kubetools_kind_enabled

Enable installation of kind cli

#### Default value

```YAML
kubetools_kind_enabled: true
```

### kubetools_kind_version

Version of kind to install

#### Default value

```YAML
kubetools_kind_version: 0.21.0
```

### kubetools_sonobuoy_arch

Architecture for sonobuoy

#### Default value

```YAML
kubetools_sonobuoy_arch: "{{ 'arm64' if ansible_architecture == 'aarch64' else 'amd64'
  }}"
```

### kubetools_sonobuoy_download

URL to download sonobuoy from

#### Default value

```YAML
kubetools_sonobuoy_download: https://github.com/vmware-tanzu/sonobuoy/releases/download/v{{
  kubetools_sonobuoy_version }}/sonobuoy_{{ kubetools_sonobuoy_version }}_linux_{{
  kubetools_sonobuoy_arch }}.tar.gz
```

### kubetools_sonobuoy_enabled

Enable installation of sonobuoy cli

#### Default value

```YAML
kubetools_sonobuoy_enabled: true
```

### kubetools_sonobuoy_version

Version of sonobuoy to install

#### Default value

```YAML
kubetools_sonobuoy_version: 0.57.1
```

### kubetools_stern_arch

Architecture for stern

#### Default value

```YAML
kubetools_stern_arch: "{{ 'arm64' if ansible_architecture == 'aarch64' else 'amd64'
  }}"
```

### kubetools_stern_download

URL to download stern from

#### Default value

```YAML
kubetools_stern_download: https://github.com/stern/stern/releases/download/v{{ kubetools_stern_version
  }}/stern_{{ kubetools_stern_version }}_linux_{{ kubetools_stern_arch }}.tar.gz
```

### kubetools_stern_enabled

Enable installation of stern cli

#### Default value

```YAML
kubetools_stern_enabled: true
```

### kubetools_stern_version

Version of stern to install

#### Default value

```YAML
kubetools_stern_version: 1.28.0
```

## Discovered Tags

**_kubetools_**


## Dependencies

- None

## License

Apache-2.0

## Author

[Thomas Boerger](https://github.com/tboerger)
