#for computation of path
import os
#used to log
import logging
#used to load an INi
import configparser

##  Globals
CONFIG_FILE = 'test_j_config.ini'

## Load the configuration file
#
def load_config_file( filename_config : str() ) -> int:
    #construct path
    my_ini_filename = os.path.join(os.getcwd(), filename_config)
    #construct config parser
    my_ini = configparser.ConfigParser()

    try:
        with open(my_ini_filename) as my_opened_ini:
            my_ini.read_file(my_opened_ini)
    except OSError as problem:
        logging.error(f'problem: {problem}')
        return -1

    logging.debug(f'see the sections of the INI: {my_ini.sections()}')
    target_section = "path"
    if (target_section in my_ini.sections()):
        #fetch attributes inside the section
        target_section_attribures = list(my_ini[target_section])
        logging.debug(f"section {target_section} exist! and contain: {target_section_attribures}")
        target_attribute = "dest_file"
        if target_attribute in target_section_attribures:
            logging.debug(f"attribute >{target_attribute}< exist and is equal to: {my_ini.items(target_section, target_attribute)}")
        else:
            logging.error(f"attribute >{target_attribute}< doesn't exist...")
            return -1

    else:
        logging.error(f"section >{target_section}< doesn't exist...")
        return -1

    return 0


##
#
def main():

    ret = load_config_file( CONFIG_FILE )
    if (ret < 0):
        logging.error(f'could not load INI file {CONFIG_FILE}...')
        return -1

    return 0

#if the file is being read WITH the intent of being executed
if __name__ == '__main__':
    logging.basicConfig(
        #level of debug to show
        level=logging.DEBUG,
        #header of the debug message
        format='[%(asctime)s] %(levelname)s: %(message)s',
    )
    main()
