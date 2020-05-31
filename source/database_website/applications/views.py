import flask


class FormViewMixin:
    form_class = None
    template_name = None
    title = None
    current_page = None

    def get_form_class(self):
        return self.form_class

    def get_form(self):
        form_class = self.get_form_class()

        form = form_class()

        return form

    def get_template_name(self):
        return self.template_name

    def get_title(self):
        return self.title

    def get(self):
        form = self.get_form()
        template_name = self.get_template_name()
        title = self.get_title()

        return flask.render_template(
            template_name_or_list=template_name,
            form=form,
            title=title,

        )
