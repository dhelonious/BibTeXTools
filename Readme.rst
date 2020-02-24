Some useful commands for writing and maintaining BibTeX files in Sublime Text 3

BibTeXTools
###########

This packages provides basic commands for formatting and sorting the entries in BibTeX files. It also includes a command to fetch BibTeX entries from a DOI in the clipboard. BibTeX entries are formatted according to the settings, where all fields in each entry type and their order are defined. Apart from the default BibTeX fields some common BibLaTeX fields like ``doi``, ``url``, and ``addendum`` are supported out of the box. Additional fields and entry types can be added in the user settings.

BibTeXTools should be considered as a complement for `LaTeXTools`_ package, which already provides syntax highlighting for BibTeX files.

Commands
========

This package provides commands for the command palette and places the same commands in the right-click context menu. Both are however only enabled in views containing a ``.bib`` file.

+-------------------------+---------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Command Palette         | Context Menu        | Description                                                                                                                                                                             |
+=========================+=====================+=========================================================================================================================================================================================+
| ``BibTeXTools: Format`` | ``Format (Bibtex)`` | Format the BibTeX entries in the current view. This will replace accents by proper LaTeX code, group entries and sort fields. Unnecessary fields are removed according to the settings. |
+-------------------------+---------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``BibTeXTools: Sort``   | ``Sort (Bibtex)``   | Sort the BibTeX entries in the current view. Entries are grouped by their entry types and sorted alphabetically by their labels. There is no option to customize sorting at the moment. |
+-------------------------+---------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``BibTeXTools: Fetch``  | ``Fetch (Bibtex)``  | Fetch a BibTeX entry from a DOI in the clipboard and place it properly formatted at the current cursor position. This command is heavily inspired by the `doi2bibSublime`_ package.     |
+-------------------------+---------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Settings
========

+--------------------------+--------------+------------------------------------------------------------------------------------------------------------------------------------+
| Key                      | Default      | Description                                                                                                                        |
+==========================+==============+====================================================================================================================================+
| ``"fields"``             | see settings | List of fields per entry type. Their order is used to format entries.                                                              |
+--------------------------+--------------+------------------------------------------------------------------------------------------------------------------------------------+
| ``"indentation"``        | ``"\t"``     | Indentation of formatted BibTeX entries. If ``\t`` is used, Sublime Text 3 will replace it by spaces "Indent Using Spaces" is set. |
+--------------------------+--------------+------------------------------------------------------------------------------------------------------------------------------------+
| ``"case_sensitive"``     | see settings | List of fields which are case sensitive and should be enclosed in additional braces.                                               |
+--------------------------+--------------+------------------------------------------------------------------------------------------------------------------------------------+
| ``"accents"``            | see settings | List of accents and their LaTeX-code replacements.                                                                                 |
+--------------------------+--------------+------------------------------------------------------------------------------------------------------------------------------------+
| ``"replace_url"``        | ``true``     | Replace or add URLs of the form "https://doi.org/...".                                                                             |
+--------------------------+--------------+------------------------------------------------------------------------------------------------------------------------------------+
| ``"abbreviate_journal"`` | ``true``     | Replace journal names by an approximation of its ISO4 abbreviation.                                                                |
+--------------------------+--------------+------------------------------------------------------------------------------------------------------------------------------------+

Advanced settings
-----------------

Although this should not be necessary, title word abbreviations can be configured using the ``BibTeXTools (Abbreviations).sublime-settings`` file. See the comments in the settings file for more details.

Acknowledgements
================

- `doi2bibSublime`_ by Dean Montgomery
- `abbrevIso`_ by Marcin Wrochna

.. _LaTeXTools: https://github.com/SublimeText/LaTeXTools
.. _doi2bibSublime: https://github.com/monty5811/doi2bibSublime
.. _abbrevIso: https://github.com/marcinwrochna/abbrevIso
