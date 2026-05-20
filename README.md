# Mart

Minimal custom app template ready to install on:

- Frappe v16
- ERPNext v16

## What is included

- Python package metadata (`pyproject.toml`, `setup.py`, `MANIFEST.in`)
- App module package (`mart/`)
- Frappe app config (`mart/hooks.py`)
- Module registration (`mart/modules.txt`)
- Patch scaffold (`mart/patches.txt`, `mart/patches/__init__.py`)
- Desk module card (`mart/config/desktop.py`)

## Install in an existing Bench (v16)

Run from your bench folder (where `sites/` exists):

```bash
bench get-app /path/to/mart
bench --site your-site.local install-app mart
```

If ERPNext is not installed yet:

```bash
bench get-app erpnext --branch version-16
bench --site your-site.local install-app erpnext
bench --site your-site.local install-app mart
```

## Verify

```bash
bench --site your-site.local list-apps
```

You should see both `erpnext` and `mart` in the output.

## Next steps

- Create DocTypes under module `Mart`
- Add fixtures and patches as needed
- Add tests before production rollout