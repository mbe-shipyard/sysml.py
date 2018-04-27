"""
The `Model` class consists of stereotypes which classify as either elements or relationships

---------

Model elements and relationships are the building blocks that make up the 9 SysML diagrams
"""

import traceback

# developer notes: to use hidden vs unhidden attributes

class Model(object):
    """This class defines a SysML model for subsuming stereotypes which classify as either model elements or relationships.
    """

    def __init__(self, label=None, elements={}, relationships={}):
        self.label = label
        #elements
        self.block = block

    #@block.setter
    #def block

class _Block(object):
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
    #tk: need to fix id_no state; store all existing id_no's in a list?

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
        elif type(parts) is list: #tk: change to accept block or list of blocks
            self._parts = parts
        else:
            raise TypeError("argument is not a list!")
        ## Reference Property
        if references is None:
            self._references = []
        elif type(references) is list: #tk: change to accept block or list of blocks
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

class _Requirement:
    """This class defines a requirement for use in a requirements diagram"""

    stereotype = "\xabrequirement\xbb"
    _id_no = 0
    #tk: need to fix id_no state; store all existing id_no's in a list?

    def __init__(self, label=None, txt=None, id_no=None, satisfy=None, verify=None, refine=None):
        # ID no.
        if id_no is None:
            Requirement._id_no += 1
            self._id_no = 'ID' + str(Requirement._id_no).zfill(3)
        elif type(id_no) in [int,float]:
            self._id_no = 'ID' + str(id_no).zfill(3)
        else:
            raise TypeError("argument is not int or float!")
        # Label
        if label is None:
            self._label = 'Requirement' + str(self._id_no)
        elif type(label) is str:
            self.label = label
        else:
            raise TypeError("argument is not a string!")
        # Text
        if txt is None:
            self.txt = ''
        elif type(label) is str:
            self.txt = txt
        else:
            raise TypeError("argument is not a string!")
        # Satisfy
        if satisfy is None:
            self._satisfy = []
        elif type(satisfy) is []: #tk: change to accept block or list of blocks
            self._satisfy = satisfy
        # Verify
        if verify is None:
            self._verify = []
        elif type(verify) is []: #tk: change to accept block or list of blocks
            self._verify = verify
        # Refine
        if refine is None:
            self.refine = []
        elif type(refine) is []: #tk: change to accept block or list of blocks
            self._refine = refine
        # Trace
        if trace is None:
            self.trace = []
        elif type(trace) is []: #tk: change to accept block or list of blocks
            self._trace = trace
    def __repr__(self):
        return "\xabrequirement\xbb {self.name}"
    ## Set requirement relations
    def satisfiedBy(self, *sourcev):
        for source in sourcev:
            self._satisfy.append(source)
    def refinedBy(self, *sourcev):
        for source in sourcev:
            self._refine.append(source)
    def verifiedBy(self, *sourcev):
        for source in sourcev:
            self._verify.append(source)

class InternalBlock:
    """This class defines an internal block diagram"""

    def __init__(self):
        pass
