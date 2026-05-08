from jinja2 import Environment
from jinja2 import FileSystemLoader

# Template folder
env = Environment(
    loader=FileSystemLoader("templates")
)

def render_template(template_name, context):

    template = env.get_template(template_name)

    rendered_html = template.render(context)

    return rendered_html