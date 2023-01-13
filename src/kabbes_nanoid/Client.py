import kabbes_nanoid
import kabbes_user_client
import py_starter as ps

class Client( kabbes_nanoid.Nanoid ):

    BASE_CONFIG_DICT = {
        "_Dir": kabbes_nanoid._Dir,
    }

    def __init__( self, dict={}, **kwargs ):

        dict = ps.merge_dicts( Client.BASE_CONFIG_DICT, dict )
        self.cfg_nano = kabbes_user_client.Client( dict=dict, **kwargs ).cfg
        kabbes_nanoid.Nanoid.__init__( self )

    def make_Nanoid( self, **kwargs ):

        default_kwargs = {
            "alphabet": self.cfg_nano['alphabet'], 
            "size": self.cfg_nano['size']
        }

        return kabbes_nanoid.Nanoid( **ps.merge_dicts(default_kwargs, kwargs) )
