from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import InputRequired

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Update bio below..',validators = [InputRequired()])
    submit = SubmitField('Save')

class PitchForm(FlaskForm):
    title = StringField('Title', validators=[InputRequired()])
    category = SelectField('Category', choices=[('Interview','Interview'),('Introductory','Introductory'),('Punchline','Punchline')],validators=[InputRequired()])
    post = TextAreaField('Your Speech', validators=[InputRequired()])
    submit = SubmitField('Pitch')

class CommentForm(FlaskForm):
    comment = TextAreaField('Leave a comment',validators=[InputRequired()])
    submit = SubmitField('Comment')

class UpvoteForm(FlaskForm):
    submit = SelectField('Like')