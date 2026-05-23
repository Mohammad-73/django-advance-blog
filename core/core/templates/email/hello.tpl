{% extends "mail-templated/base.tpl" %}

{% block subject %}
Account Activation
{% endblock %}

{% block html %}
{{token}}
{% endblock %}