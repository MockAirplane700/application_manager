class GenerateCoverLetter:

    def __init__(self, first_name, last_name, current_date):
        self.first_name = first_name
        self.last_name = last_name
        self.current_date = current_date

    def generate_cover(self, addressed_to, position, body_content, relevant_position, email, website):
        try:
            result = {}
            #   INTRODUCTION
            first_name = self.first_name
            last_name = self.last_name
            current_date = self.current_date

            base_string = (f'{current_date}\n\n'
                           f'Dear {addressed_to}\n\n'
                           f'As a {relevant_position} and co-founder of a software solutions service, '
                           f'I am excited and grateful to apply for this project {position}.')
            result['introduction'] = base_string
            #   BODY
            body_base_string = (f'My experience as a {relevant_position} has taught me the importance simple but '
                                f'elegant solutions. This lets me strive to create intuitive solutions, while keeping '
                                f'in mind potential problems the set solution might encounter. Achievements I am most '
                                f'proud of include and are not limited to the following.'
                                f'\n\t{body_content}')
            result['body'] = body_base_string
            #   CONCLUSION
            base_conclusion_string = (f'In summary, my experience as {relevant_position} coupled with continuous growth'
                                      f'designing and implementing software solutions makes me and ideal candidate for '
                                      f'the project at hand, {position}. I look forward to hearing from you. \n '
                                      f'Sincerely {first_name} {last_name}')
            result['conclusion'] = base_conclusion_string
            #   HEADER
            header_object = {
                'right_col': f'{first_name} {last_name}',
                'left_col': f'{email} {website}'
            }
            result['header'] = header_object
            return result
        except Exception as error:
            print(error)
            return {}
