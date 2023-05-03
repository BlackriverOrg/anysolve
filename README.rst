# AnySolve.ai Client Library

Python Library anysolve
========================================

`anysolve` is a library for executing AnySolve.ai tasks. It needs an `API-Key` that can be created in the settings of an anysolve.ai account. The settings can be found at https://www.anysolve.ai/settings.

Please *note* that the execution of an AnySolve.ai task may be chargeable.

Installation
~~~~~~~~~~~~

You can install this library by using pip. The library is designed to use only requests as dependency. 

Supported Python Versions
^^^^^^^^^^^^^^^^^^^^^^^^^
Python >= 3.6

Mac/Linux
^^^^^^^^^

.. code-block:: console

    <your-env>/bin/pip install anysolve


Windows
^^^^^^^

.. code-block:: console

    <your-env>\Scripts\pip.exe install anysolve


Example Usage
~~~~~~~~~~~~~

Translation of a text (free):

.. code:: python

    from anysolve import AnySolve

    client = AnySolve(
        "your_api_key"
    )

    result = client.run(
        "intern-translation-free",
        "1.0.0",
        {
            "source_language": "de",
            "text": "Das ist ein rotes Haus.",
            "target_language": "en",
        },
    )

    print(result)

