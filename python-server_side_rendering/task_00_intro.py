#!/usr/bin/python3
import re
import os


def generate_invitations(template, attendees):
    try:
        if type(template) is not str:
            raise ValueError('Template is not of type string')
        if not all(isinstance(row, dict) for row in attendees):
            raise ValueError('Attendees is not a list of dicts')
        if len(template) == 0:
            raise ValueError('Template is empty, no output files generated.')
        if len(attendees) == 0:
            raise ValueError('No data provided, no output files generated.')

        template_fields = re.findall(r"\{(.*?)\}", template)
        for key in template_fields:
            for row in attendees:
                if key not in row:
                    row[value] = 'N/A'

        edited_list = []
        for row in attendees:
            working_template = template
            for key, value in row.items():
                working_template = (working_template
                                    .replace(f'{{{key}}}', f'{value}'))
            edited_list.append(working_template)

        for i, email in enumerate(edited_list):
            if os.path.exists(f'output-{i}.txt'):
                raise ValueError('email already created')
            with open(f'output-{i}.txt', 'w') as f:
                f.write(email)
    except Exception as e:
        print(e)