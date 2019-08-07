Prerequisites
-------------

Before you install and configure the {{cookiecutter.service}} service,
you must create a database, service credentials, and API endpoints.

#. To create the database, complete these steps:

   * Use the database access client to connect to the database
     server as the ``root`` user:

     .. code-block:: console

        $ mysql -u root -p

   * Create the ``{{cookiecutter.module_name}}`` database:

     .. code-block:: none

        CREATE DATABASE {{cookiecutter.module_name}};

   * Grant proper access to the ``{{cookiecutter.module_name}}`` database:

     .. code-block:: none

        GRANT ALL PRIVILEGES ON {{cookiecutter.module_name}}.* TO '{{cookiecutter.module_name}}'@'localhost' \
          IDENTIFIED BY '{{cookiecutter.module_name|upper}}_DBPASS';
        GRANT ALL PRIVILEGES ON {{cookiecutter.module_name}}.* TO '{{cookiecutter.module_name}}'@'%' \
          IDENTIFIED BY '{{cookiecutter.module_name|upper}}_DBPASS';

     Replace ``{{cookiecutter.module_name|upper}}_DBPASS`` with a suitable password.

   * Exit the database access client.

     .. code-block:: none

        exit;
