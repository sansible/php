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

This role uses two tags: **build** and **configure**

* `build` - Installs PHP.
* `configure` - (re-)Configures PHP and FPM.


## Arguments

Argument | Default | Description
----------|---------|------------
sansible_php_version | php7.0 | The PHP version to be installed
sansible_php_extras | | Extra modules to be installed
sansible_php_pecl | | Extensions to be installed
sansible_php_modules | [php7.0-curl] | Default modules to be installed
sansible_php_path_etc | /etc/php7.0/ | PHP /etc/ path
sansible_php_path_fpm_pool | /etc/php7.0/fpm/pool.d/ | FPM pool path
sansible_php_fpm_bin | php7.0-fpm | FPM binary name
sansible_php_fpm_port | 9000 | FPM port
sansible_php_fpm_max_children | 100 | Max FPM children
sansible_php_fpm_start_servers | 2 | FPM servers to start with
sansible_php_fpm_min_spare_servers | 2 | FPM min spare servers
sansible_php_fpm_max_spare_servers | 10 | FPM max spare servers
sansible_php_fpm_max_requests | 4000 | FPM max requests
sansible_php_fpm_status_path | /status/ | PHP status path
sansible_php_fpm_nginx_status | yes | Create fpm status nginx include
sansible_php_fpm_rlimit | | Linux memory limit
sansible_php_fpm_description | | Description of the server
sansible_php_fpm_user | | PHP user
sansible_php_fpm_group | | PHP group
sansible_php_fpm_chroot | | PHP chroot



## Examples

To simply add PHP to your box.

~~~YML
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
    - sansible.php
~~~

If you want to install some extra PHP packages, simply add it to `sansible_php_extras` list.

~~~YML
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
    - name: sansible.php
      sansible_php_extras:
        - php5-xdebug
~~~

If you want to install PHP with a custom FPM worker.

~~~YAML
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
    - name: sansible.php
      sansible_php_fpm_description: my awesome application
      sansible_php_fpm_chroot: /home/my_awesome_application/code/public
      sansible_php_fpm_group: awesome_application
      sansible_php_fpm_user: awesome_application
~~~

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
    - name: sansible.php
      sansible_php_install_base_packages: no
      sansible_php_modules:
        - php7.0=7.0.32*
        - php7.0-common=7.0.32*
        - php7.0-fpm=7.0.32*
        - php7.0-cli=7.0.32*
```