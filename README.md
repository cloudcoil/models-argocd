# cloudcoil-models-argocd

Versioned argocd models for cloudcoil.

[![PyPI](https://img.shields.io/pypi/v/cloudcoil.models.argocd.svg)](https://pypi.python.org/pypi/cloudcoil.models.argocd)
[![Downloads](https://static.pepy.tech/badge/cloudcoil.models.argocd)](https://pepy.tech/project/cloudcoil.models.argocd)
[![License: Apache-2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/license/apache-2-0/)
[![CI](https://github.com/cloudcoil/models-argocd/actions/workflows/ci.yml/badge.svg)](https://github.com/cloudcoil/models-argocd/actions/workflows/ci.yml)

Models generated from the upstream tagged CRD schemas pinned in `pyproject.toml`.

```python
from cloudcoil.models.argocd import get_model

Application = get_model("Application", api_version="argoproj.io/v1alpha1")
```
