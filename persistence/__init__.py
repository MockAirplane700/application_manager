from persistence.generate_cover_letter import GenerateCoverLetter
import datetime


class PersistenceLayer:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.strings_months = [
            '', 'January', 'February', 'March', 'April', 'May',
            'June', 'July', 'August', 'September', 'October',
            'November', 'December'
        ]
        self.strings_days = [
            '', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'
        ]

    def generate_proposal_cover(self, addressed_to, position, body_content, relevant_position, email, website):
        current_timestamp = datetime.datetime.utcnow()
        current_date = (f'{current_timestamp.weekday()} {current_timestamp.day} '
                        f'{self.strings_months[current_timestamp.month]} {current_timestamp.year}')

        cover_manager = GenerateCoverLetter(self.first_name, self.last_name, current_date)
        return cover_manager.generate_cover(addressed_to, position, body_content, relevant_position, email, website)


