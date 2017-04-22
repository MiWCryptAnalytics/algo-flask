#!/usr/bin/python3
import re

def main():
    output = """
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, IntegerField, RadioField
from wtforms.validators import DataRequired

"""
    file = open("algo", "r")
    algo = file.read()
    nf = re.findall(r'(?P<name>.*?) \(\) {\s*(?P<function>[\w\W]*?)\n}', algo)
    for name, function in nf:
        formname = name.replace("_", '').title()
        if name == "algo_provisioning":
            platforms = re.findall(r'\d\. (?P<platform>.*)', function)
            output += "\nclass AlgoForm(FlaskForm):\n"
            output += "    platform = StringField('What provider would you like to use? Choices: %s', validators=[DataRequired()])\n" % ' '.join(platforms)
        elif name == "deploy":
            continue
        else:
            formname = "Algo%s" % formname
            output += "\nclass %sForm(FlaskForm):\n" % formname

        vars = re.findall(r'read -p "\n(?P<string>[\w\W]*?): " -r[s ]* (?P<var>.*)', function)
        for string, var in vars:
            option = re.search(r'(?P<question>[\w\W]*?)\[(?P<choice>.*)\]', string)
            question = string.replace('$ADDITIONAL_PROMPT', '').strip()
            fieldtype = "StringField"
            if option:
                choice = option.group('choice')
                question = option.group('question').replace('$ADDITIONAL_PROMPT', '').strip()
                if choice == "y/N":
                    fieldtype = "BooleanField"
                elif choice.isdigit():
                    fieldtype = "IntegerField"
            else:
                choice = ""
            clean_question = question.replace('\n', '\\n').replace('\'', '\\\'')
            field = "    %s = %s(\'%s\', default=\'%s\', validators=[DataRequired()])\n" % (var, fieldtype, clean_question, choice)
            output+=field

    out = open("app/forms.py", "w")
    print(output)
    out.write(output)
    out.close()



if __name__ == "__main__":
    main()