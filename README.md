# PHP

Master: ![Build Status](https://travis-ci.org/sansible/php.svg?branch=master)
Develop: ![Build Status](https://travis-ci.org/sansible/php.svg?branch=develop)

* [ansible.cfg](#ansible-cfg)
* [Dependencies](#dependencies)
* [Tags](#tags)
* [Examples](#examples)

This is a role to install PHP with CLI and FPM support.

This playbook allows you to create isolated per application user FPM services.
This comes with some limitations:
* One FPM service for one application (OS) user
* One application root directory
* One php.ini per application (OS) user
* You have to provide control handlers for the user specific FPM service.


## Dependencies

No dependencies


## Tags

This role uses one tag: **build**

* `build` - Installs PHP.


## Arguments

See [defaults/main.yml](defaults/main.yml)


## Examples

To simply add PHP7.3 to your box.

```YAML
- name: My Awesome Playbook
  hosts: sandbox

  pre_tasks:
    - name: Update apt
      become: yes
      apt:
        cache_valid_time: 1800
        update_cache: yes
      tags:
        - build

  roles:
    - role: sansible.php
```

Install a different version of PHP to your box.

```YAML
- name: My Awesome Playbook
  hosts: sandbox

  pre_tasks:
    - name: Update apt
      become: yes
      apt:
        cache_valid_time: 1800
        update_cache: yes
      tags:
        - build

  roles:
    - role: sansible.php
      sansible_php_version: php7.2
```


If you want to install some extra PHP packages, simply add it to `sansible_php_extras` list.

```YAML
- name: My Awesome Playbook
  hosts: sandbox

  pre_tasks:
    - name: Update apt
      become: yes
      apt:
        cache_valid_time: 1800
        update_cache: yes
      tags:
        - build

  roles:
    - role: sansible.php
      sansible_php_extras:
        - php5-xdebug
```

If you want to install PHP with a custom FPM worker.

```YAML
- name: My Awesome Playbook
  hosts: sandbox

  pre_tasks:
    - name: Update apt
      become: yes
      apt:
        cache_valid_time: 1800
        update_cache: yes
      tags:
        - build

  roles:
    - role: sansible.php
      sansible_php_fpm_description: my awesome application
      sansible_php_fpm_chroot: /home/my_awesome_application/code/public
      sansible_php_fpm_group: awesome_application
      sansible_php_fpm_user: awesome_application
```

If you want complete control over installed packages (ie. to preserve exact versions):

```YAML
- name: My Awesome Playbook
  hosts: sandbox

  pre_tasks:
    - name: Update apt
      become: yes
      apt:
        cache_valid_time: 1800
        update_cache: yes
      tags:
        - build

  roles:
    - role: sansible.php
      sansible_php_install_base_packages: no
      sansible_php_modules:
        - php7.3=7.0.32*
        - php7.3-common=7.0.32*
        - php7.3-fpm=7.0.32*
        - php7.3-cli=7.0.32*
```