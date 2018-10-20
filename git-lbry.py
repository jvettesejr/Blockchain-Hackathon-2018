import sys
import os
import datetime


ARG_LIST = {
    'commit': 'file',
    'add': 'file',
    'status': 'singular',
    'pull': 'url',
    'push': 'url',
    'branch': 'singular',
    'init': 'file',
    '-h': 'singular',
}


HELP_LIST = {
    'init': '\tdirectory\tInitializes the git-LBRY repo',
    'commit': '\tfile_name\tCommits all staged files',
    'add': '\tfile_name\tAdds file to staging',
    'status': '\tNone\t\tChecks file status',
    'pull': '\turl\t\tPulls new commits from LBRY URL',
    'push': '\turl\t\tPushes commits to LBRY URL',
    'branch': '\tNone\t\tShows current branch',
    '-h': '\tNone\t\tHelp section',
}


APP_NAME = 'GIT-LBRY' 


## Displays all staged files
def get_status(current_dir_path):
    directory = '.lbry'
    if os.path.exists(directory):
        if not os.path.isfile(f'{current_dir_path}/{directory}/.add'):
            print('No Files Added')
            return
        with open('{}/.add'.format(directory), 'r') as record_file:
            print('Staged files:\n-------------------')
            for line in record_file.readlines():
                print(line)
    else:
        print(f'Not a valid {APP_NAME} repository')


## Adds file to the current working add
def add_to_add(filename):
    directory = '.lbry'
    if os.path.exists(directory):
        current_dir_path = os.path.dirname(os.path.realpath(__file__))
        if os.path.isfile(f'{current_dir_path}/{directory}/{filename}'):
            ## Reads the add file to see if the file has already been added
            with open('{}/.add'.format(directory), 'r') as record_file:
                for line in record_file.readlines():
                    if line == filename:
                        print(f'{filename} is already added')
                        return
        
        ## Appends file to add 
        with open('{}/.add'.format(directory), 'a') as record_file:
            record_file.write(f'{filename}\n')
    else:
        print(f'Not a valid {APP_NAME} directory')
        return 


## Initalizes the lbry repository
def init_git_lbry():
    directory = '.lbry'
    if not os.path.exists(directory):
        os.makedirs(directory)
        record_file = open('{}/.record'.format(directory), 'w+')


## https://stackoverflow.com/questions/9727673/list-directory-tree-structure-in-python
def view_file_structure(startpath):
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        print('{}{}/'.format(indent, os.path.basename(root)))
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            print(f'{subindent}{f}')

def show_help():
    print(f'------------------\n| {APP_NAME} Help |\n------------------')
    for key, value in HELP_LIST.items():
        print('{}\t{}'.format(key, value))


def push_content():
    pass


def pull_content(content_url):
    pass


def main():
    if len(sys.argv) <= 1:
        show_help()
        return 

    arguments = sys.argv[1:]
    command = arguments[0]

    if command not in ARG_LIST:
        print('{} is not a valid command. Use -h to view all commands'.format(command))
        return

    if ARG_LIST[command] != 'singular' and len(arguments) < 1:
        print('{} command requires another argument'.format(command))
        return

    if command == '-h':
        show_help()

    elif command == 'status':
        current_dir_path = os.path.dirname(os.path.realpath(__file__))
        get_status(current_dir_path)

    elif command == 'init':
        init_git_lbry()

    elif command == 'add':
        current_dir_path = os.path.dirname(os.path.realpath(__file__))
        files = arguments[1:]
        for filename in files:
            if os.path.isfile(f'{current_dir_path}/{filename}'):
                add_to_add(filename)
            else:
                print(f'{filename} is not is not a valid file name/path. Other files added.')

    elif command == 'push':
        push_content()

    elif command == 'pull:
        content_url = arguments[1:]
        pull_content(content_url)


if __name__ == '__main__':
    main()
    