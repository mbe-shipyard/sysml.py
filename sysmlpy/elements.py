"""
Model Elements

---------

Model Elements are the building blocks that make up the 9 SysML diagrams
"""

import traceback

class Block(object):
    """This class defines a \xabblock\xbb stereotype for use in a BDD 
    (block definition diagram) or ibd (internal block diagram)
    
    Parameters
    ----------
    label : string, default None
        
    values : dict, default None
        
    parts : list, default None
        
    references : list, default None
        
    flowProperties : dict, default None
        

    Examples
    --------
    >>> warpcore = Block(label='warp core',
    ...                 parts=[antimatterinjector, Dilithiumcrystalchamber],
    ...                 flowProperties={'in':{'inflow':'antimatter'},
                                        'out':{'outflow':'power'}})
    ...         references=[antimatter])
    >>> warpdrive = Block(label='warp drive',
    ...             values={'class':7},
    ...             parts=[antimattercontainment, warpcore, plasmainducer],

    """

    stereotype = "\xabblock\xbb"
    _id_no = 0
    
    def __init__(self, label=None, values=None, parts=None, references=None, flowProperties=None):
        # Label
        if label is None:
            Block._id_no += 1
            self.label = 'Block' + str(Block._id_no)
        elif type(label) is str:
            self.label = label
        else:
            raise TypeError("argument is not a string!")
        ## Value Property
        if values is None:
            self._values = {}
        elif type(values) is dict:
            self._values = values
        else:
            raise TypeError("argument is not a dictionary!")
        ## Part Property
        if parts is None:
            self._parts = []
        elif type(parts) is list:
            self._parts = parts
        else:
            raise TypeError("argument is not a list!")
        ## Reference Property
        if references is None:
            self._references = []
        elif type(references) is list:
            self._references = references
        else:
            raise TypeError("argument is not a list!")
        ## Flow Property
        if flowProperties is None:
            self._flowProperties = {}
        elif type(flowProperties) is dict:
            self._flowProperties = flowProperties
        else:
            raise TypeError("argument is not a dictionary!")
        ## Operations
        self.operations = []
        ## Constraints
        self.constaints = []
    def __repr__(self):
        return "\xabblock\xbb '{}'".format(self.label)
    ## Setters
    def add_parts(self, *partv):
        """add one or more Blocks to parts
        
        """
        for part in partv:
            if type(part) is Block:
                self._parts.append(part)
            else:
                raise TypeError("argument is not a 'Block'!")
    def add_references(self, *referencev):
        """add one or more Blocks to references
        
        """
        for reference in referencev:
            if type(reference) is Block:
                self._references.append(reference)
            else:
                raise TypeError("argument is not a 'Block'!")
    def add_values(self, values):
        """add values dictionary to values
        
        """
        if type(values) is dict:
            for key in values:
                if type(key) is str:
                    self.values[key] = values[key]
                else:
                    raise TypeError("key is not a string!")
        else:
            raise TypeError("argument is not a dictionary!")
    def add_flowProperties(self, flowProperties):
        """add flowProperties dictionary to flowProperties
        
        """
        if type(flowProperties) is dict:
            for flowPort in flowProperties:
                if type(flowPort) is str:
                    self._flowProperties[flowPort] = flowProperties[flowPort]
                else:
                    raise TypeError("key is not a string!")
        else:
            raise TypeError("argument is not a dictionary!")
    ## Getters
    @property
    def parts(self):
        return self._parts
    @property
    def values(self):
        return self._values
    @property
    def references(self):
        return self._references
    @property
    def flowProperties(self):
        return self._flowProperties

class Requirement:
    """This class defines a requirement for use in a requirements diagram"""

    _id_no = 0   # requirement id no.

    def __init__(self, name='', txt='', id_no=None, trace=[], refine=[], verify=[]):
        if id_no is None:
            Requirement._id_no += 1
            id_no = Requirement._id_no
        self.name = name
        self.id = 'ID'+str(_id_no).zfill(3)
        self.txt = txt
        self.trace = trace     # list of model elements which satisfies requirement
        self.refine = refine    # list of model elements which refines requirement
        self.verify = verify    # list of model elements which verifies requirement
    def __repr__(self):
        return "\xabrequirement\xbb {self.name}"
    ## requirement relations
    def addrelation(self, source, relationtype='dependency'):
        if relationtype is 'satisfy':
            self.trace.append(source)
            print(source, "satisfies", self)
        elif relationtype is 'refine':
            self.refine.append(source)
            print(source, "refines", self)
        elif relationtype is 'verify':
            self.verify.append(source)
            print(source, "verifies", self)
        else:
            print("Source and target nodes must be of valid types")

class InternalBlock:
    """This class defines an internal block diagram"""

    def __init__(self):
        pass
