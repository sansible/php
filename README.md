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




## ansible.cfg

This role is designed to work with merge "hash_behaviour". Make sure your
ansible.cfg contains these settings

```INI
[defaults]
hash_behaviour = merge
```




## Dependencies

No dependencies




## Tags

This role uses two tags: **build** and **configure**

* `build` - Installs PHP.
* `configure` - (re-)Configures PHP and FPM.




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

If you want to install some extra PHP packages, simply add it to `php.extras` list.

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
      php:
        extras:
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
      php:
        fpm:
          description: my awesome application
          chroot: /home/my_awesome_application/code/public
          group: awesome_application
          user: awesome_application
~~~
