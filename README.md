pytlas-light [![Build Status](https://travis-ci.org/atlassistant/pytlas-light.svg?branch=master)](https://travis-ci.org/atlassistant/pytlas-light) ![License]( https://img.shields.io/badge/License-GPL%20v3-blue.svg)
===

Skill light for the [pytlas assistant](https://github.com/atlassistant/pytlas). Use it as a starting point to make your own skills.

*For detailed informations about skill creation please take a look at [this article (in french)](https://julien.leicher.me/coding/writing-your-first-pytlas-skill/).*

## How to use this light?

This light provides a good starting point if you want to create your own skills. The `skill.py` contains the code needed to trigger and handle your first intent along with comments on how to extend your skill capabilities.

You will have to replace all references to `pytlas-light` or placeholder definitions to match your specific needs.

## Supported languages

*Write down all languages supported by your skill below:*

- English
- French

## Typical sentences

*Write some examples of how a user may trigger and interact with your skill:*

- allume la lumière du salon
- light the living room light

## Configuration

*If your skill needs some [configuration](https://pytlas.readthedocs.io/en/latest/writing_skills/settings.html), write them here.*

## Launching tests

In order to launch tests, you will need to install required dependencies and then launch the test suite with:

```bash
$ pip install -r requirements_tests.txt
$ python -m nose --with-coverage --cover-package=pytlas-light
```
