#########################
 Python Library anysolve
#########################

`anysolve` is a library for executing `AnySolve.ai <https://www.anysolve.ai>`_ tasks. It needs an `API-Key` that can be
created in the settings of an anysolve.ai account. The settings can be
found at `<https://www.anysolve.ai/settings>`_.

Please *note* that the execution of an `AnySolve.ai <https://www.anysolve.ai>`_ task may be chargeable.

**************
 Installation
**************

You can install this library by using pip. The library is designed to
use only requests as dependency.

Supported Python Versions
=========================

Python >= 3.6

Mac/Linux
=========

.. code:: console

   pip3 install anysolve

Windows
=======

.. code:: console

   pip.exe install anysolve

************************
 Create an access token
************************

You can create an access token at
`<https://www.anysolve.ai/settings/personal-access-tokens>`_

***************
 Example Usage
***************

Translation of a text (free)
============================

The following code uses the translation API for text (free):

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

`<https://www.anysolve.ai/tasks/u-ba835df8268fc301-translates-a-text>`_

Introduction from Text
======================

The following code creates an introduction from a text:

.. code:: python

   import os
   from anysolve import AnySolve

   anysolve_token = os.environ.get('ANYSOLVE_PERSONAL_ACCESS_TOKEN') # Resolve your personal access token here
   client = AnySolve(anysolve_token)
   res = client.run('create-introduction','1.0.1', {'text': 'As a swan person I like to go to lakes', 'context': 'You are a creative writer.'})

   print(res)

`<https://www.anysolve.ai/tasks/create-introduction>`_

Create Newspaper Headline from Text
===================================

The following creates a newspaper headline by a text:

.. code:: python

   import os
   from anysolve import AnySolve

   anysolve_token = os.environ.get('ANYSOLVE_PERSONAL_ACCESS_TOKEN') # Resolve your personal access token here
   client = AnySolve(anysolve_token)
   res = client.run('create-newspaper-headline','1.0.0', {'text': 'A group of police...', 'lang': 'English', 'context': 'You are a boulevard journalist.'})

   print(res)

`<https://www.anysolve.ai/tasks/create-newspaper-headline>`_

Explain Code
============

The following code explains a code:

.. code:: python

   import os
   from anysolve import AnySolve

   anysolve_token = os.environ.get('ANYSOLVE_PERSONAL_ACCESS_TOKEN') # Resolve your personal access token here
   client = AnySolve(anysolve_token)
   res = client.run('explain-code','1.0.0', {'code': 'print(\'hello world\')'})

   print(res)

`<https://www.anysolve.ai/tasks/explain-code>`_

Google Search
=============

The following code does a google search:

.. code:: python

   import os
   from anysolve import AnySolve

   anysolve_token = os.environ.get('ANYSOLVE_PERSONAL_ACCESS_TOKEN') # Resolve your personal access token here
   client = AnySolve(anysolve_token)
   res = client.run('intern-web-google-search','1.0.0', {'search_query': 'AnySolve.ai', 'location': 'us', 'language': 'lang_en', 'max_results': '5'})

   print(res)

`<https://www.anysolve.ai/tasks/intern-web-google-search>`_

Generate SEO Keywords
=====================

The following code generates SEO keywords:

.. code:: python

   import os
   from anysolve import AnySolve

   anysolve_token = os.environ.get('ANYSOLVE_PERSONAL_ACCESS_TOKEN') # Resolve your personal access token here
   client = AnySolve(anysolve_token)
   res = client.run('u-ba835df8268fc301-seo-keyword','1.0.0', {'topic': 'A plattform saas platform targeted to AI tasks'})

   print(res)

`<https://www.anysolve.ai/tasks/u-ba835df8268fc301-seo-keyword>`_

Rewrite Text Tone to Be Polite
==============================

The following code creates rewrites the text to be polite:

.. code:: python

   import os
   from anysolve import AnySolve

   anysolve_token = os.environ.get('ANYSOLVE_PERSONAL_ACCESS_TOKEN') # Resolve your personal access token here
   client = AnySolve(anysolve_token)
   res = client.run('u-ba835df8268fc301-rewrite-text-tone-to-be-polite','1.0.0', {'text': 'I want you to quit an join my business'})

   print(res)

`<https://www.anysolve.ai/tasks/u-ba835df8268fc301-rewrite-text-tone-to-be-polite>`_

Generate Alternative Titles
===========================

The following code generates alternatives to a title:

.. code:: python

   import os
   from anysolve import AnySolve

   anysolve_token = os.environ.get('ANYSOLVE_PERSONAL_ACCESS_TOKEN') # Resolve your personal access token here
   client = AnySolve(anysolve_token)
   res = client.run('u-ba835df8268fc301-generate-alternative-titles','1.0.0', {'title': 'AnySolve.ai - An AI community hub', 'field_of_use': 'Blog post'})

   print(res)

`<https://www.anysolve.ai/tasks/u-ba835df8268fc301-generate-alternative-titles>`_

Create Regex by Description
===========================

The following code creates a regex by a description:

.. code:: python

   import os
   from anysolve import AnySolve

   anysolve_token = os.environ.get('ANYSOLVE_PERSONAL_ACCESS_TOKEN') # Resolve your personal access token here
   client = AnySolve(anysolve_token)
   res = client.run('u-ba835df8268fc301-create-regex-by-description','1.0.0', {'requirement': 'allow up to 3 chars and numbers and then *', 'type': 'PCRE'})

   print(res)

`<https://www.anysolve.ai/tasks/u-ba835df8268fc301-create-regex-by-description>`_

Answer Yes/No Question about Text
=================================

The following code answers a yes / no question:

.. code:: python

   import os
   from anysolve import AnySolve

   anysolve_token = os.environ.get('ANYSOLVE_PERSONAL_ACCESS_TOKEN') # Resolve your personal access token here
   client = AnySolve(anysolve_token)
   res = client.run('u-ba835df8268fc301-answer-yesno-question-about-text','1.0.0', {'text': 'It is a hot day. Maria is on her way to the lake. She will meet her friends there.', 'question': 'Is the main character of the text female?'})

   print(res)

`<https://www.anysolve.ai/tasks/u-ba835df8268fc301-answer-yesno-question-about-text>`_

Answer Question about Text
==========================

The following code answers a question about a text:

.. code:: python

   import os
   from anysolve import AnySolve

   anysolve_token = os.environ.get('ANYSOLVE_PERSONAL_ACCESS_TOKEN') # Resolve your personal access token here
   client = AnySolve(anysolve_token)
   res = client.run('u-ba835df8268fc301-answer-question-about-text','1.0.0', {'question': 'What is the name of the main character?', 'text': 'It is a hot day. Maria is on her way to the lake. She will meet her friends there.'})

   print(res)

`<https://www.anysolve.ai/tasks/u-ba835df8268fc301-answer-question-about-text>`_

Transform Style & Tone
======================

The following code changes the style & tone of a text:

.. code:: python

   import os
   from anysolve import AnySolve

   anysolve_token = os.environ.get('ANYSOLVE_PERSONAL_ACCESS_TOKEN') # Resolve your personal access token here
   client = AnySolve(anysolve_token)
   res = client.run('u-806494eb1fbfb39f-transform-style--tone','1.0.0', {'style': 'Persuasive', 'tone': 'Formal', 'text': 'I want you to quit an join my business'})

   print(res)

`<https://www.anysolve.ai/tasks/u-806494eb1fbfb39f-transform-style--tone>`_

Text Compression
================

The following code makes a text smaller without loosing too much
information:

.. code:: python

   import os
   from anysolve import AnySolve

   anysolve_token = os.environ.get('ANYSOLVE_PERSONAL_ACCESS_TOKEN') # Resolve your personal access token here
   client = AnySolve(anysolve_token)
   res = client.run('u-806494eb1fbfb39f-text-compression','1.0.0', {'text': 'Enter text to compress'})

   print(res)

`<https://www.anysolve.ai/tasks/u-806494eb1fbfb39f-text-compression>`_

*********
 Pricing
*********

Please go to `<https://www.anysolve.ai/pricing>`_ and study the specific
tasks for prices. You may get free credits on registration and some
tasks are free.
