class findandWriteFCIDs:
    """Reads output csv files from export entities, matches TDA aliases with found FCIDs, writes to a new csv"""
    def __init__(self, hba_port_file_name, storage_port_file_name):
        """The init method instantiates the known list of ips to track"""
        self.hba_port_file_name = hba_port_file_name
        self.storage_port_file_name = storage_port_file_name
        self.identification(self.hba_port_file_name, self.storage_port_file_name)

    def read_files(self, file_name, seperator = ", "):
        """A generic read file generator to check bad file inputs and read line by line"""
        try:
            fp = open(file_name, 'r')
        except FileNotFoundError:
            raise FileNotFoundError ("Could not open {}".format(file_name))
        else:
            with fp:
                for line in fp:
                    l = line.strip().split(seperator)
                        yield l.strip()

    def identification(self, hba_port_file_name, storage_port_file_name):
        """This function takes the information from the generator and then matches the alias with the FCID"""
        read_hba_port_file = self.read_files(hba_port_file_name, seperator = ", ")
        read_storage_port_file = self.read_files(storage_port_file_name)
        for line in read_hba_port_file:
        return None

def main():
    hba_port_file_name = ""
    storage_port_file_name = "" 
    matching_FCID_Aliases = findandWriteFCIDs(hba_port_file_name, storage_port_file_name)


if __name__ == '__main__':
    main()