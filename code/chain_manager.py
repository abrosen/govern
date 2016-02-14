import json


class Chain(object):

    def __init__(self, root):
        self.blocks = [root]
        self.state = {"__builtins__": {}, 'validator': None, 'executor': None}
        init_func = root['init']
        exec(init_func, self.state, {})

    def consider(self, block):
        validator_func = self.state['validator']
        if validator_func(self.state, block):
            executor = self.state['executor']
            executor(self.state, block)
            return True
        else:
            return False


if __name__ == "__main__":
    b0 = {
        "init": """
global validator
validator = lambda x,y: 1
def myExecutor(state, block):
    for var in block["updates"].keys():
        state[var] = block["updates"][var]
global executor
executor = myExecutor

    """
    }
    c = Chain(b0)
    c.consider({"updates": {"test": 1}})
    print(c.state)
