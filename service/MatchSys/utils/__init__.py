from .doc_vec_tool import Doc2VecTool
from .filters import get_recent_repeated_responses
from .snowkey import IdWorker
from .response_selection import get_first_response, get_most_frequent_response

def print_progress_bar(description, iteration_counter, total_items, progress_bar_length=20):
    """
    Print progress bar
    :param description: Training description
    :type description: str

    :param iteration_counter: Incremental counter
    :type iteration_counter: int

    :param total_items: total number items
    :type total_items: int

    :param progress_bar_length: Progress bar length
    :type progress_bar_length: int

    :returns: void
    :rtype: void
    """
    import sys

    percent = float(iteration_counter) / total_items
    hashes = '#' * int(round(percent * progress_bar_length))
    spaces = ' ' * (progress_bar_length - len(hashes))
    sys.stdout.write('\r{0}: [{1}] {2}%'.format(description, hashes + spaces, int(round(percent * 100))))
    sys.stdout.flush()
    if total_items == iteration_counter:
        print('\r')


def import_module(dotted_path):
    """
    Imports the specified module based on the
    dot notated import path for the module.
    """
    import importlib

    module_parts = dotted_path.split('.')
    module_path = '.'.join(module_parts[:-1])
    module = importlib.import_module(module_path)
    return getattr(module, module_parts[-1])


def initialize_class(data, *args, **kwargs):
    """
    :param data: A string or dictionary containing a import_path attribute.
    """
    if isinstance(data, dict):
        import_path = data.get('import_path')
        data.update(kwargs)
        Class = import_module(import_path)

        return Class(*args, **data)
    else:
        Class = import_module(data)

        return Class(*args, **kwargs)


def validate_adapter_class(validate_class, adapter_class):
    """
    Raises an exception if validate_class is not a
    subclass of adapter_class.

    :param validate_class: The class to be validated.
    :type validate_class: class

    :param adapter_class: The class type to check against.
    :type adapter_class: class

    :raises: Adapter.InvalidAdapterTypeException
    """
    from service.MatchSys.adapters import Adapter

    # If a dictionary was passed in, check if it has an import_path attribute
    if isinstance(validate_class, dict):

        if 'import_path' not in validate_class:
            raise Adapter.InvalidAdapterTypeException(
                'The dictionary {} must contain a value for "import_path"'.format(
                    str(validate_class)
                )
            )

        # Set the class to the import path for the next check
        validate_class = validate_class.get('import_path')

    if not issubclass(import_module(validate_class), adapter_class):
        raise Adapter.InvalidAdapterTypeException(
            '{} must be a subclass of {}'.format(
                validate_class,
                adapter_class.__name__
            )
        )


def get_response_time(chatbot, statement='Hello'):
    """
    Returns the amount of time taken for a given
    chat bot to return a response.

    :param chatbot: A chat bot instance.
    :type chatbot: ChatBot

    :returns: The response time in seconds.
    :rtype: float
    """
    import time

    start_time = time.time()

    chatbot.get_response(statement)

    return time.time() - start_time



__all__ = (
    'print_progress_bar',
    'import_module',
    'initialize_class',
    'validate_adapter_class',
    'get_response_time',

    'IdWorker',

    'Doc2VecTool',

  
    'get_recent_repeated_responses',
    'get_first_response',
    'get_most_frequent_response'
)