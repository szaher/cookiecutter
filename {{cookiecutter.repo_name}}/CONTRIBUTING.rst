If you would like to contribute to the development of {{cookiecutter.service}}, you must
follow the steps in this page:

   {{cookiecutter.docs_website}}

If you already have a good understanding of how the system works and your
accounts are set up, you can skip to the development workflow
section of this documentation to learn how changes to {{cookiecutter.service}} should be
submitted for review via the {{cookiecutter.review_site}}:

   {{cookiecutter.docs_website}}


Bugs should be filed on {{ cookiecutter.bug_tracker }}

{%- if cookiecutter.bug_tracker == 'Launchpad' -%}
   https://bugs.launchpad.net/{{ cookiecutter.bug_project }}
{%- elif cookiecutter.bug_tracker == 'Github' -%}
   https://github.com/{{ cookiecutter.repo_group }}/{{ cookiecutter.bug_project }}/issues
{%- elif cookiecutter.bug_tracker == 'Gitlab' -%}
   https://gitlab.com/{{ cookiecutter.repo_group }}/{{ cookiecutter.bug_project }}/issues
{%- endif -%}
