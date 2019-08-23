===============================
{{ cookiecutter.repo_name }}
===============================

{{ cookiecutter.project_short_description}}

Please fill here a long description which must be at least 3 lines wrapped on
80 cols, so that distribution package maintainers can use it in their packages.
Note that this is a hard requirement.

* Free software: Apache license
* Documentation: {{ cookiecutter.docs_website }}/{{ cookiecutter.repo_name }}/ 
{%- if cookiecutter.bug_tracker == 'Launchpad' -%} 
* Bugs: https://bugs.launchpad.net/{{ cookiecutter.bug_project }} 

{%- elif cookiecutter.bug_tracker == 'Github' -%} 
* Source: https://{{ cookiecutter.bug_tracker }}.com/{{cookiecutter.repo_group}}/{{ cookiecutter.repo_name }} 
* Bugs: https://github.com/{{ cookiecutter.repo_group }}/{{ cookiecutter.bug_project }}/issues 

{%- elif cookiecutter.bug_tracker == 'Gitlab' -%}

* Source: https://{{ cookiecutter.bug_tracker }}.com/{{cookiecutter.repo_group}}/{{ cookiecutter.repo_name }} 
* Bugs: https://gitlab.com/{{ cookiecutter.repo_group }}/{{ cookiecutter.bug_project }}/issues 


{%- endif -%}


Features
--------

* TODO

