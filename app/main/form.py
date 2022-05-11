from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import InputRequired

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Write a brief bio about you.',validators = [InputRequired()])
    submit = SubmitField('Save')

class PitchForm(FlaskForm):
    title = StringField('Title', validators=[InputRequired()])
    post = TextAreaField('Your Pitch', validators=[InputRequired()])
    category = SelectField('Category', choices=[('Events','Events'),('Job','Job'),('Advertisement','Advertisement')],validators=[InputRequired()])
    submit = SubmitField('Post')

class CommentForm(FlaskForm):
    comment = StringField('Leave a comment',validators=[InputRequired()])
    submit = SubmitField('Comment')