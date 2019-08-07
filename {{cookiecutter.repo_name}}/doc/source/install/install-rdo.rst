.. _install-rdo:

Install and configure for Red Hat Enterprise Linux and CentOS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


This section describes how to install and configure the {{cookiecutter.service}} service
for Red Hat Enterprise Linux 8 and CentOS 8.

.. include:: common_prerequisites.rst

Install and configure components
--------------------------------

#. Install the packages:

   .. code-block:: console

      # yum install

.. include:: common_configure.rst

Finalize installation
---------------------

Start the {{cookiecutter.service}} services and configure them to start when
the system boots:

.. code-block:: console

   # systemctl enable {{cookiecutter.module_name}}-api.service

   # systemctl start {{cookiecutter.module_name}}-api.service
