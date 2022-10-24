---
layout: default
title:  "regex"
---


# Regex - Regular Expressions 

* [RegexOne Tutorials](https://regexone.com/)
* [Browser Regex 1](https://regex101.com/)
* [Browser Regex 2](https://regexr.com/)
* [Regex Crossword](https://regexcrossword.com/)


| Expression | Matches |
|:----------:|:-------|
| `[A-Za-z]` | any alphabet |
| `[A-z]` | will contain `[/]^_` | 
| `[^0-9]` | exclude numbers | 
| `[^A-Z]` | exclude capital letters | 
| `.` | any character, except newline | 
| `\w` |  any character, except whitespace and underline |
| `^pattern` | starts with pattern |
| `pattern$` | ends with pattern | 
| `\b` | end of word |
| `{n}` | exactly `n` occurrences |
| `{n,}` | at least `n` occurrences |
| `{0,m}` | at most `m` occurrencs | 
| `{n,m}` | between `n` and `m` occurrences, inclusive | 
| `?` | `{0,1}` |
| `*` | `{0,}` |
| `+` | `{1,}` | 
