##  load configurations inside an INI file inside a module
#   require configuration file named: test_j_config.ini with section [path] and key dest_file="test_j_output.txt"

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
def load_config_file( filename_config : str(), ini_sections, ini_keys : list() ):
    """load configuration file
    checks that a list of sections and a list of keys are contained inside the INI
    return the INI file
    """
    #construct path
    my_ini_filename = os.path.join(os.getcwd(), filename_config)
    #construct config parser
    my_ini = configparser.ConfigParser()
    #try to load the configuration file    
    try:
        with open(my_ini_filename) as my_opened_ini:
            #use the configparser to parse the INI
            my_ini.read_file(my_opened_ini)
            #method .read get a path

    #failed to open file
    except OSError as problem:
        logging.error(f'problem: {problem}')
        return -1

    #search a given section inside the INI (inside square brackets [section])
    logging.debug(f'see the sections of the INI: {my_ini.sections()}')
    if ini_sections in my_ini.sections():
        #search a given key inside the section
        #fetch attributes inside the section and pu them inside an iterable list
        target_section_attributes = list(my_ini[ini_sections])
        logging.debug(f"section {ini_sections} exist! and contain: {target_section_attributes}")
        #search if keys exist
        if all(key in target_section_attributes for key in ini_keys):
            #show the key and value
            logging.debug(f"attribute >{ini_keys}< exist and is equal to: {my_ini.items(ini_sections, ini_keys)}")
        #failed to find key inside section
        else:
            logging.error(f"attribute >{ini_keys}< doesn't exist...")
            return -1

    #failed to find section
    else:
        logging.error(f"section >{ini_sections}< doesn't exist...")
        return -1

    return 0


##
def awesome_ini_loader( filename_config : str(), ini_sections : list(), ini_keys : list() ):
    """
    """


    return


##
#
def main():
    #load the INI file
    ret = load_config_file( CONFIG_FILE,"path" ,["dest_file" , "csv_file"] )
    #if (ret < 0):
        #logging.error(f'could not load INI file {CONFIG_FILE}...')
        #return -1

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
