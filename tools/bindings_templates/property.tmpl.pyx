{#
TODO: some properties has / in there name
TODO: some properties pass a parameter to the setter/getter
TODO: see PinJoint.params/bias for a good example
#}

{% macro render_property(prop) %}

@property
def {{ prop["name"].replace('/', '_') }}(self):
    return self.{{ prop["getter"] }}()

{% if prop["setter"] %}
@{{ prop["name"].replace('/', '_') }}.setter
def {{ prop["name"].replace('/', '_') }}(self, val):
    self.{{ prop["setter"] }}(val)
{% endif %}

{% endmacro %}