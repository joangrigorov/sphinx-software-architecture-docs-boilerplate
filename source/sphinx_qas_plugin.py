"""
Sphinx extension to generate referenceable Quality Attribute Scenario (QAS)
diagrams that work for both HTML and LaTeX/PDF outputs.

For HTML, an SVG is generated and inserted via a raw node.
For LaTeX (and other non‑HTML) outputs, a PNG is generated and inserted via an image node.

If you supply a :name: option, the diagram is wrapped as a figure and becomes referenceable.
"""

import os
import hashlib

from docutils import nodes
from docutils.parsers.rst import Directive, directives

# Try to import the python-graphviz package.
try:
    import graphviz
except ImportError:
    graphviz = None


class QualityAttributeScenario(nodes.General, nodes.Element):
    pass


class QualityAttributeScenarioDirective(Directive):
    """
    Directive for a Quality Attribute Scenario (QAS) diagram.

    The directive takes no content but requires these options:
      - stimulus_source
      - stimulus
      - environment
      - artifact
      - response
      - response_measure

    Optionally, you may provide a caption and a name (for cross-referencing).
    """
    has_content = False
    required_arguments = 0
    optional_arguments = 0
    final_argument_whitespace = True
    option_spec = {
        'stimulus_source': directives.unchanged_required,
        'stimulus': directives.unchanged_required,
        'environment': directives.unchanged_required,
        'artifact': directives.unchanged_required,
        'response': directives.unchanged_required,
        'response_measure': directives.unchanged_required,
        'caption': directives.unchanged,
        'name': directives.unchanged,
    }

    def run(self):
        if graphviz is None:
            error = self.state_machine.reporter.error(
                "The 'graphviz' Python package is required for the qas directive.",
                line=self.lineno
            )
            return [error]

        # Retrieve options.
        ss   = self.options.get('stimulus_source', '')
        stim = self.options.get('stimulus', '')
        env  = self.options.get('environment', '')
        art  = self.options.get('artifact', '')
        resp = self.options.get('response', '')
        rm   = self.options.get('response_measure', '')
        caption = self.options.get('caption')
        name = self.options.get('name')

        # Build the Graphviz DOT source.
        dot_code = f"""
digraph QAS {{
    rankdir=LR;
    node [shape=rect, fontname="Helvetica", fontsize=10, style=filled, fillcolor=white];

    stimulus_source [label="Source of Stimulus\\n{ss}", shape=none];
    stimulus [label="Stimulus\\n{stim}", shape=box, style=filled, fillcolor=lightblue];
    environment [label="Environment\\n{env}", shape=box, style=filled, fillcolor=lightgray];
    artifact [label="Artifact\\n{art}", shape=box, style=filled, fillcolor=white];
    response [label="Response\\n{resp}", shape=box, style=filled, fillcolor=lightyellow];
    response_measure [label="Response Measure\\n{rm}", shape=none];

    stimulus_source -> stimulus;
    stimulus -> environment;
    environment -> artifact;
    artifact -> response;
    response -> response_measure;
}}
        """

        # Get the current builder.
        builder = self.state.document.settings.env.app.builder

        # For HTML output, generate an SVG.
        if builder.name in ('html', 'dirhtml'):
            try:
                src = graphviz.Source(dot_code, format="svg")
                svg_data = src.pipe().decode("utf-8")
            except Exception as e:
                error = self.state_machine.reporter.error(
                    "Error generating QAS diagram: " + str(e),
                    line=self.lineno
                )
                return [error]

            svg_node = nodes.raw('', svg_data, format='html')

            # Wrap in a figure if a caption or name is provided.
            if name or caption:
                container = nodes.figure('')
                if name:
                    self.add_name(container)
                container += svg_node
                if caption:
                    caption_node = nodes.caption(caption, caption)
                    container += caption_node
                return [container]
            else:
                return [svg_node]

        # For non-HTML output (e.g. LaTeX), generate a PNG.
        else:
            # Create a hash based on the DOT source for caching.
            hash_val = hashlib.sha1(dot_code.encode('utf-8')).hexdigest()
            image_filename = f"qas-{hash_val}.png"

            # For LaTeX (and similar builders), force use of the "_images" directory.
            images_dir = os.path.join(builder.outdir, '_images')
            relative_uri = f"/_images/{image_filename}"  # Correct path to the '_images' folder for LaTeX

            os.makedirs(images_dir, exist_ok=True)

            try:
                src = graphviz.Source(dot_code, format="png")
                base_filepath = os.path.join(images_dir, f"qas-{hash_val}")
                # render() will create "base_filepath.png" and remove extra files if cleanup=True.
                src.render(filename=base_filepath, cleanup=True)
            except Exception as e:
                error = self.state_machine.reporter.error(
                    "Error generating QAS diagram for non-HTML output: " + str(e),
                    line=self.lineno
                )
                return [error]

            img_node = nodes.image(uri=relative_uri)

            # Wrap the image in a figure if a caption or name is provided.
            if name or caption:
                figure = nodes.figure('')
                if name:
                    self.add_name(figure)
                figure += img_node
                if caption:
                    figure += nodes.caption(caption, caption)
                return [figure]
            else:
                return [img_node]


def setup(app):
    app.add_node(QualityAttributeScenario)
    app.add_directive('qas', QualityAttributeScenarioDirective)
    return {
        'version': '0.5',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
