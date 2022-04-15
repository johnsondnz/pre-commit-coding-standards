[![pipeline status](https://gitlab.com/ComputerConceptsLimited/pre-commit-hooks/badges/master/pipeline.svg)](https://gitlab.com/ComputerConceptsLimited/pre-commit-hooks/-/commits/master)

# pre-commit-hooks
Some out-of-the-box hooks for pre-commit.

See also: https://github.com/pre-commit/pre-commit

# Available hooks
- `vlan-dup` : Checks for duplicate VLANs in yml files.
- `vlan-keys` : Checks all keys are present for a VLAN.
- `vlan-tag-exists` : Checks VLAN tags exists on a handover.
- `fmg-client-variables` : Checks esp_clients.yml data is valid.
- `ansible-lint` : [ansible-lint](https://github.com/ansible/ansible-lint)
- `jinja2-lint` : Check jinja2 templates for correct syntax
- `orphan-handover-tags` : Check handovers for orphan tags
- `duplicate-interfaces` : Prevents duplicate interface assignment
- `duplicate-mlags` : Prevents duplicate MLAG id assignment for a switch pair
- `inventory` : Check ansible-inventory can be parsed

# Installation
[Install instructions](https://gitlab.com/ComputerConceptsLimited/pre-commit-hooks/blob/master/docs/INSTALL.md)

# Usage
[Install instructions](https://gitlab.com/ComputerConceptsLimited/pre-commit-hooks/blob/master/docs/USAGE.md)

## Run a single hook manually without commit
`pre-commit run orphan-handover-tags --verbose --all-files`
Where `orphan-handover-tags` is the hook to run.

# Adding Hooks
Clone `ccl-pre-commit-hooks`.  Follow examples.  Ensure hook names use underscores and not dashes.
- python3 hooks go into the `hooks/` dir.
- Add the hook into the `console_scripts` section of setup.cfg
- update `.pre-commit-hooks.yaml` in target repositories.

# Versioning
`setup.cfg` line two stores the current version number.  Version is incremented for every change and a new tag added to the repo.

## Updating tags
- Check current tags here; [releases](https://gitlab.com/ComputerConceptsLimited/pre-commit-hooks/-/tags).
- Uses CLI commandlet `git tag <new tag>; git send --tags` to push a new release to gitlab

## Updating ansible-prod
- Update `.pre-commit-config.yaml` rev key to match the new tag above.
  This will force users to pickup the new pre-commit-hooks as they are released.
- Push the change to ansible-prod on github.

## Development
Other tags can be used as required when testing releases locally with ansible-prod.

# Tests
All hooks ideally will testbe tested using `.gitlab-ci.yml` configuration.  GitLab runners can check against dummy data stored in `tests/test-data` to ensure there are no issues with scripts.

# Deprecated / replaced hooks

# Message Levels
Intention is for errors to result in failures.  In some cases a warning might suffice.  In which case developers can look into cleanups where required without pre-commit checks preventing merges.

## Current Warning
- Orphan tags detected on handover, tag not in vlans.yml

## Levels
- 'ERR': Error (default)
- 'WARN': Warning
- 'INFO': Informational

## Overriding
```
def message_logging(**kwargs) -> None:
    """
    Takes the inputs and print logging message to stdout
    params:
        kwargs:
            level: Indicated level (default = ERR)
            filename: Name of the file tested.
            message_title: Title of the message
            message: Message
    Returns: None
    """

    level = kwargs.get("level") if "level" in kwargs else "ERR"
    filename = kwargs.get("filename")
    message_title = kwargs.get("message_title")
    message = kwargs.get("message")

    print(f"[{level}] {filename} - {message_title}: {message}")

    return None
```

Submitting the `level='WARN'` would override the printed message.

```
~/Coding/ComputerConceptsLimited/ansible-prod on  n00-arista-production ⌚ 14:23:04
$ python3 ../pre-commit-hooks/hooks/orphan_handover_tags.py ~/Coding/ComputerConceptsLimited/ansible-prod/host_vars/vcan-c00-e0935-ltr01b.yml
[WARN] host_vars/vcan-c00-g1222-ltr01b.yml - Orphan Tag Detected: Tag 'pure_sct`' found on handover not in vlans.yml
```


# Developing new hooks locally
from: https://pre-commit.com/#developing-hooks-interactively

You can call pre-commit with `try repo` and the relative path from `ansible-prod` to the hooks repo.  Passing in the test then allows you to target a single test without the need to change any files.

## Example
```
~/Coding/ComputerConceptsLimited/ansible-prod on  master ⌚ 15:05:36
$ pre-commit try-repo ../pre-commit-hooks orphan-handover-tags --verbose --all-files
===============================================================================
Using config:
===============================================================================
repos:
-   repo: ../pre-commit-hooks
    rev: 2b8ae6811e94fa69faa30ae7baa4abcf34186346
    hooks:
    -   id: orphan-handover-tags
===============================================================================
[INFO] Initializing environment for ../pre-commit-hooks.
[INFO] Installing environment for ../pre-commit-hooks.
[INFO] Once installed this environment will be reused.
[INFO] This may take a few minutes...
[orphan-handover-tags] Check handovers for orphan tags.......................Passed
hookid: orphan-handover-tags

[WARN] host_vars/vcan-c00-g1222-ltr01b.yml - Orphan Tag Detected: Tag 'pure_sct`' found on handover not in vlans.yml
[WARN] host_vars/vcan-c00-g1222-ltr01b.yml - Orphan Tag Detected: Tag 'pure_sct`' found on handover not in vlans.yml
[WARN] host_vars/vcan-c00-g1222-ltr01b.yml - Orphan Tag Detected: Tag 'pure_sct`' found on handover not in vlans.yml
[WARN] host_vars/vcan-c00-g1222-ltr01b.yml - Orphan Tag Detected: Tag 'pure_sct`' found on handover not in vlans.yml
[WARN] host_vars/vcan-c00-g1222-ltr01b.yml - Orphan Tag Detected: Tag 'pure_sct`' found on handover not in vlans.yml
[WARN] host_vars/vcan-c00-g1222-ltr01b.yml - Orphan Tag Detected: Tag 'pure_sct`' found on handover not in vlans.yml
[WARN] host_vars/vcan-c00-g1222-ltr01b.yml - Orphan Tag Detected: Tag 'pure_sct`' found on handover not in vlans.yml
[WARN] host_vars/vcan-c00-g1222-ltr01b.yml - Orphan Tag Detected: Tag 'pure_sct`' found on handover not in vlans.yml
[WARN] host_vars/vcan-c00-g1222-ltr01b.yml - Orphan Tag Detected: Tag 'pure_sct`' found on handover not in vlans.yml
[WARN] host_vars/vcan-c00-g1222-ltr01b.yml - Orphan Tag Detected: Tag 'pure_sct`' found on handover not in vlans.yml
[WARN] host_vars/vcan-c00-g1222-ltr01b.yml - Orphan Tag Detected: Tag 'pure_sct`' found on handover not in vlans.yml
[WARN] host_vars/vcan-c00-g1222-ltr01b.yml - Orphan Tag Detected: Tag 'pure_sct`' found on handover not in vlans.yml
[WARN] host_vars/vcan-c00-g1222-ltr01b.yml - Orphan Tag Detected: Tag 'pure_sct`' found on handover not in vlans.yml
[WARN] host_vars/vcan-c00-g1222-ltr01b.yml - Orphan Tag Detected: Tag 'pure_sct`' found on handover not in vlans.yml
[WARN] host_vars/vcan-c00-g1222-ltr01b.yml - Orphan Tag Detected: Tag 'pure_sct`' found on handover not in vlans.yml
[WARN] host_vars/vcan-c00-g1222-ltr01b.yml - Orphan Tag Detected: Tag 'pure_sct`' found on handover not in vlans.yml
[WARN] host_vars/vcan-c00-g1222-ltr01b.yml - Orphan Tag Detected: Tag 'pure_sct`' found on handover not in vlans.yml
[WARN] host_vars/vcan-c00-g1222-ltr01b.yml - Orphan Tag Detected: Tag 'pure_sct`' found on handover not in vlans.yml
[WARN] host_vars/vcan-c00-g1222-ltr01b.yml - Orphan Tag Detected: Tag 'pure_sct`' found on handover not in vlans.yml
[WARN] host_vars/vcan-c00-g1222-ltr01b.yml - Orphan Tag Detected: Tag 'pure_sct`' found on handover not in vlans.yml
[WARN] host_vars/vcan-c00-g1222-ltr01b.yml - Orphan Tag Detected: Tag 'pure_sct`' found on handover not in vlans.yml
[WARN] host_vars/vcan-c00-g1222-ltr01b.yml - Orphan Tag Detected: Tag 'pure_sct`' found on handover not in vlans.yml
[WARN] host_vars/vcan-c00-g1222-ltr01b.yml - Orphan Tag Detected: Tag 'pure_sct`' found on handover not in vlans.yml
[WARN] host_vars/vcan-c00-g1222-ltr01b.yml - Orphan Tag Detected: Tag 'pure_sct`' found on handover not in vlans.yml
[WARN] host_vars/vcan-c00-g1222-ltr01b.yml - Orphan Tag Detected: Tag 'pure_sct`' found on handover not in vlans.yml
[WARN] host_vars/vcan-c00-g1222-ltr01b.yml - Orphan Tag Detected: Tag 'pure_sct`' found on handover not in vlans.yml
[WARN] host_vars/vcan-c00-g1222-ltr01b.yml - Orphan Tag Detected: Tag 'pure_sct`' found on handover not in vlans.yml
[WARN] host_vars/vcan-c00-g1222-ltr01b.yml - Orphan Tag Detected: Tag 'pure_sct`' found on handover not in vlans.yml
[WARN] host_vars/vcan-c00-g1222-ltr01b.yml - Orphan Tag Detected: Tag 'pure_sct`' found on handover not in vlans.yml
[WARN] host_vars/vcan-c00-g1222-ltr01b.yml - Orphan Tag Detected: Tag 'pure_sct`' found on handover not in vlans.yml

```
