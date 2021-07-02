from typing import List, Dict, Callable, Tuple
SlotValidationResult = Tuple[bool, bool, str, Dict]


class Validate:
    """
    Parent class for finite and numerical enitity value validation sub classes.
    """
    def __init__(self):
        ##  Initialize the output fields
        self.filled           = True
        self.part_filled      = False
        self.trigger          = ''
        self.parameters       = {}
    
    """ SETTERS """
    def set_filled(self, val: bool) -> None:
        self.filled = val

    def set_part_filled(self, val: bool) -> None:
        self.part_filled = val

    def set_trigger(self, val: str) -> None:
        self.trigger = val

    def set_parameters(self, values: List[str], key: str, support_multiple: bool = True, pick_first: bool = False) -> None:
        # In case both support_multiple and pick_first are set to true or false, support_multiple will be prioritized.
        if values != []:
            if support_multiple or (not support_multiple and not pick_first):
                self.parameters = {key : values} # If support_multiple is true, list of all valid values are sent in response
            else:
                self.parameters = {key : values[0]} # If pick_first is true, the first valid value is sent as a response
    
    """ GETTERS """
    def get_filled(self) -> bool:
        return self.filled

    def get_part_filled(self) -> bool:
        return self.part_filled

    def get_trigger(self) -> str:
        return self.trigger

    def get_parameters(self) -> Dict:
        ## get values
        return self.parameters


    def get_response(self) -> SlotValidationResult:
        ## Output response
        return (
	        self.get_filled(),
                self.get_part_filled(),
                self.get_trigger(),
                self.get_parameters()
        )