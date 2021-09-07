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
    #try to load the configuration file    
    try:
        with open(my_ini_filename) as my_opened_ini:
            #use the configparser to parse the INI
            my_ini.read_file(my_opened_ini)
    #failed to open file
    except OSError as problem:
        logging.error(f'problem: {problem}')
        return -1
    #search a given section inside the INI (inside square brackets [section])
    target_section = "path"
    logging.debug(f'see the sections of the INI: {my_ini.sections()}')
    if (target_section in my_ini.sections()):
        #search a given key inside the section
        target_key = "dest_file"
        #fetch attributes inside the section and pu them inside an iterable list
        target_section_attribures = list(my_ini[target_section])
        logging.debug(f"section {target_section} exist! and contain: {target_section_attribures}")
        #search if key exist
        if target_key in target_section_attribures:
            #show the key and value
            logging.debug(f"attribute >{target_key}< exist and is equal to: {my_ini.items(target_section, target_key)}")
        #failed to find key inside section
        else:
            logging.error(f"attribute >{target_key}< doesn't exist...")
            return -1
    #failed to find section
    else:
        logging.error(f"section >{target_section}< doesn't exist...")
        return -1

    return 0


##
#
def main():
    #load the INI file
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
