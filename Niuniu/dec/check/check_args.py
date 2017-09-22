import wrapt
from typing import List
from Niuniu.exc import ExceptionHTTP
from .paramrule import ParamRule


def check_args(param_rules: List[ParamRule] = list(), param_rules_optional: List[ParamRule] = list()):
    """ HTTP search params (query string) checkout

    :param param_rules: List of ParamsRule, with param name and type. this decorator will check if all params exist and
                        type correct.
    :param param_rules_optional: like params_rules, but only check if type correct.
    """
    @wrapt.decorator
    def decorated_function(wrapped, instance, args, kwargs):
        _args = instance.args

        # Check if all params exist & data type correct
        for param_rule in param_rules:
            try:
                param = _args[param_rule.name]
                v = param_rule.type(param)
                _args[param_rule.name] = v
            except KeyError:
                raise ExceptionHTTP(400, f"Missing Search Param: \"{param_rule.name}\"")
            except ValueError:
                raise ExceptionHTTP(400, f"Wrong Param Type: Type(\"{param_rule.name}\") Is {param_rule.type.__name__}")

        # Check if all optional params data type correct
        for param_rule in param_rules_optional:
            try:
                param = _args[param_rule.name]
                v = param_rule.type(param)
                _args[param_rule.name] = v
            except KeyError:
                pass
            except ValueError:
                raise ExceptionHTTP(400, f"Wrong Param Type: Type(\"{param_rule.name}\") Is {param_rule.type.__name__}")

        instance.args = _args
        return wrapped(*args, **kwargs)

    return decorated_function
