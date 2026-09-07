from types import ModuleType

import cloudcoil.models.argocd as argocd


def test_has_modules():
    modules = list(filter(lambda x: isinstance(x, ModuleType), argocd.__dict__.values()))
    assert modules, "No modules found in argocd"
