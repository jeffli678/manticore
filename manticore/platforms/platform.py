from manticore.utils.event import Eventful


class OSException(Exception):
    pass


class SyscallNotImplemented(OSException):
    ''' Exception raised when you try to call an unimplemented
        system call. Go to linux.py and add it!
    '''

    def __init__(self, idx, name):
        msg = 'Syscall index "{}" ({}) not implemented.'.format(idx, name)
        super().__init__(msg)


class ConcretizeSyscallArgument(OSException):
    def __init__(self, reg_num, message='Concretizing syscall argument', policy='SAMPLED'):
        self.reg_num = reg_num
        self.message = message
        self.policy = policy
        super().__init__(message)


class Platform(Eventful):
    '''
    Base class for all operating system platforms.
    '''

    def __init__(self, path, **kwargs):
        super().__init__(**kwargs)

    def invoke_model(self, model, prefix_args=None):
        self._function_abi.invoke(model, prefix_args)

    def __setstate__(self, state):
        super().__setstate__(state)

    def __getstate__(self):
        state = super().__getstate__()
        return state

    def generate_workspace_files(self):
        return {}
