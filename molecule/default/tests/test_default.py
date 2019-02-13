import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_installed_packages(host):
    packages = [
        'nginx', 'php7.3', 'php7.3-curl', 'php7.3-common', 'php7.3-fpm',
        'php7.3-cli',
    ]
    for package in packages:
        assert host.package(package).is_installed


def test_files(host):
    directories = ['etc', 'log', 'tmp', 'run', 'bin']
    for directory in directories:
        assert host.file('/home/php/%s' % directory).is_directory

    absent_files = [
        '/etc/init.d/php7.3-fpm',
        '/etc/init/php7.3-fpm.conf',
        '/etc/php/7.3/fpm/pool.d/www.conf',
    ]
    for absent_file in absent_files:
        assert not host.file(absent_file).exists

    files = [
        '/etc/nginx/includes/php_fpm_status',
        '/etc/init.d/php', '/home/php/bin/php7.3-fpm-checkconf',
        '/home/php/etc/php-fpm.conf', '/home/php/etc/php.ini',
    ]
    for file in files:
        assert host.file(file).exists
