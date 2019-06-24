Some useful commands for writing and maintaining BibTeX files in Sublime Text 3

# BibtexTools

This packages provides basic commands for formatting and sorting the entries in BibTeX files. It also includes a command to fetch BibTeX entries from a DOI in the clipboard.

BibTeX entries are formatted according to the settings, where all fields in each entry type and their order are defined. Apart from the default BibTeX fields some common BibLaTeX fields like `doi`, `url`, and `addendum` are supported out of the box. Additional fields and entry types can be added in the user settings.

## Commands

This package provides commands for the command palette and places the same commands in the right-click context menu. Both are however only enabled in views containing a `.bib` file.

| Command Palette            | Context Menu      | Description                                                                                                                                                                                                                     |
| --                         | --                | --                                                                                                                                                                                                                              |
| `BibtexTools:`<br>`Format` | `Format`<br>`(Bibtex)` | Format the BibTeX entries in the current view. This will replace accents by proper LaTeX code, group entries and sort fields. Unnecessary fields are removed according to the settings.                                         |
| `BibtexTools:`<br>`Sort`   | `Sort`<br>`(Bibtex)`   | Sort the BibTeX entries in the current view. Entries are grouped by their entry types and sorted alphabetically by their labels. There is no option to customize sorting at the moment.                                         |
| `BibtexTools:`<br>`Fetch`  | `Fetch`<br>`(Bibtex)`  | Fetch a BibTeX entry from a DOI in the clipboard and place it properly formatted at the current cursor position. This command is heavily inspired by the [doi2bibSublime](https://github.com/monty5811/doi2bibSublime) package. |

## Settings

| Key                | Default      | Description                                                                                                                      |
| --                 | --           | --                                                                                                                               |
| `"fields"`         | see settings | List of fields per entry type. Their order is used to format entries.                                                            |
| `"indentation"`    | `"\t"`       | Indentation of formatted BibTeX entries. If `\t` is used, Sublime Text 3 will replace it by spaces "Indent Using Spaces" is set. |
| `"case_sensitive"` | see settings | List of fields which are case sensitive and should be enclosed in additional braces.                                             |
| `"accents"`        | see settings | List of accents and their LaTeX-code replacements.                                                                               |

## Acknowledgements

* [doi2bibSublime](https://github.com/monty5811/doi2bibSublime) by Dean Montgomery