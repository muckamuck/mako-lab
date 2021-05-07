from mako.template import Template

things = [1, 2, 3]
template = Template(filename='foo.template')
print(template.render(things=things).strip())
