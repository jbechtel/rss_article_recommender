import pd

class ZoteroLibrary(object):
    """ Object that reads Zotero libraries and can output cleaned data to train against """

    def __init__(self):
        self.library_df = None

    def read_library(self, library_csv):
        self.library_df = pd.read_csv(library_csv)

    def consolidate_zotero_library(self, library_df):
        ''' Takes a full zotero dataframe and reduces it to columns of interest '''
        return library_df.loc['Title','Abstract Note','Automatic Tags']

    def get_library(self)
        return consolidate_zotero_library(self.library_df)