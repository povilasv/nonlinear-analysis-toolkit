import sys
import subprocess
import cStringIO
import numpy as np
import pandas
from StringIO import StringIO

__all__ = ["lorenz", "ikeda", "makenoise", "low121", "stp", "corr", "autocor", "mutual", "delay", "recurr",
           "false_nearest", "d2", "c2naive"]


def replace_param(dict, p1, p2):
    if dict.has_key(p1):
        element = dict.get(p1)
        del dict[p1]
        dict[p2] = element
    return dict


def param_dict_to_list(dict):
    res = []
    for key, value in dict.iteritems():
        res.append('-' + str(key))
        res.append(str(value))

    return res


def program(method):
    def call(**kwargs):
        input = None
        additional_params = []
        V = 0

        # TISEAN uses #,% as parameter names.
        kwargs = replace_param(kwargs, 'hashtag', '#')
        kwargs = replace_param(kwargs, 'percentage', '%')
        # Pass data to stdin
        if kwargs.has_key('data'):
            data = kwargs.get('data')
            if isinstance(data, pandas.Series):
                data = data.values

            buffer = StringIO()
            np.savetxt(buffer, data)
            input = buffer.getvalue()
            buffer.close()
            del kwargs['data']

        if kwargs.has_key('additional_params'):
            additional_params = kwargs.get('additional_params')
            del kwargs['additional_params']

        # Verbosity levels
        if kwargs.has_key('V'):
            V = kwargs.get('V')
            del kwargs['V']

        keys = kwargs.keys()
        for key in keys:
            if kwargs[key] is None:
                del kwargs[key]

        args = [method] + ['-V', str(V)] + param_dict_to_list(kwargs) + additional_params
        proc = subprocess.Popen(args=args, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                universal_newlines=True,
                                bufsize=-1)

        stdout, stderr = proc.communicate(input=input)
        stdout = cStringIO.StringIO(stdout)
        stderr = cStringIO.StringIO(stderr)

        return stdout, stderr

    return call


module_obj = sys.modules[__name__]

for method in __all__:
    setattr(module_obj, method, program(method))
