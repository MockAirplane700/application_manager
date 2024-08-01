from persistence import PersistenceLayer
from file_manager import FileManager

if __name__ == '__main__':
    #   FILE MANAGER
    manager_file = FileManager('C:\\Users\\sizib\\PycharmProjects\\upwork_manager\\assets\\json_files\\personal_data'
                               '.json')
    #   USER INPUTS AND OTHER VARS
    #   ASK FOR FIRST AND LAST NAME
    first_name = input("Please enter your first name. If you have a middle name, include it as part of your first name"
                       "for example Edwin Edward\n\t")
    last_name = input("Please enter your last name.\n\t")
    job_title = input("Please enter the job title/ proposal you are applying for\n\t")
    #   ASK FOR USER EMAIL AND WEBSITE
    user_email = input("Please enter the email address you wish to use.\n\t")
    user_website = input("Please enter the website url you wish to use. \n\t")
    #   ASK FOR WHO IT IS ADDRESSED TO
    addressed_to = input("To whom do you want to address the letter to?\n\t")
    print("Please select the relevant relevant job title from the list below, if it does not appear enter 0 otherwise "
          "select the title you wish to use by entering the number associated with it\n")
    resultant = {}
    count = 1
    for key in manager_file.read_file_get_keys():
        print(f'{count}. {key}')
        resultant[f'{count}'] = key
        count += 1
    print('\n\n\t')
    use_existing = input('')
    if use_existing == '0' or use_existing == 0:
        #   ENTER NEW JSON SUBMISSION AND MAKE IT THE SELECTED JOB
        title = input("Enter the job title\n\t")
        #   TODO: TAKE LIST INPUT
        #   CHANGE VALUE OF USE_EXISTING TO CURRENT INDEX COUNT
        use_existing = len(manager_file.read_file_get_keys()) + 1
    relevant_position = resultant[use_existing]
    #   GIVE LIST OF AVAILABLE JOB TITLES CREATE NEW ONES AS FIT
    json_file_object = manager_file.read_file_get_json()
    body_content = json_file_object[resultant[use_existing]]

    persistence_layer = PersistenceLayer(first_name, last_name)
    result = persistence_layer.generate_proposal_cover(addressed_to, job_title, body_content, relevant_position,
                                                       user_email, user_website)
    print(result)
