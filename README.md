# PHP

Master: ![Build Status](https://travis-ci.org/ansible-city/php.svg?branch=master)  
Develop: ![Build Status](https://travis-ci.org/ansible-city/php.svg?branch=develop)

This is a role to install PHP with CLI and FPM support.

This playbook allows you to create isolated per application user FPM services.
This comes with some limitations:
* One FPM service for one application (OS) user
* One application root directory
* One php.ini per application (OS) user
* You have to provide control handlers for the user specific FPM service.




## Example Playbook

To simply add PHP to your box.

~~~YML
- name: My Awesome Playbook
  hosts: sandbox

  roles:
    - php
~~~

If you want to install some extra PHP packages, simply add it to `php.extras` list.

~~~YML
- name: My Awesome Playbook
  hosts: sandbox

  vars:
    php:
      extras:
        - php5-xdebug

  roles:
    - php
~~~

If you want to install PHP with a custom FPM worker.

~~~YAML
- name: My Awesome Playbook
  hosts: sandbox

  vars:
    php:
      fpm:
        description: my awesome application
        chroot: /home/my_awesome_application/code/public
        group: awesome_application
        user: awesome_application

  roles:
    - php
~~~
