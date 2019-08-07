{%- macro set_header_markup(header_text_length) -%}
{%- set servicelength = cookiecutter.service|length -%}
{%- for _ in range(0, servicelength + header_text_length) -%}={%- endfor -%}
{%- endmacro -%}
{%- macro set_header(header_text) -%}
{{ set_header_markup(header_text|length) }}
{{cookiecutter.service}}{{header_text}}
{{ set_header_markup(header_text|length) }}
{%- endmacro -%}
{{ set_header(" service installation guide") }}

.. toctree::
   :maxdepth: 2

   get_started.rst
   install.rst
   verify.rst
   next-steps.rst

The {{cookiecutter.service}} service ({{cookiecutter.module_name}}) provides...

This chapter assumes a working setup of  following the
`Installation Tutorial
<{{cookiecutter.docs_website}}>`_.
