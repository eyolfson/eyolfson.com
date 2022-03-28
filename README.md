# eyolfson.com

A simple Django site.

## Quickstart Commands

To get a development environment started with default settings, run the
following commands:

    python -m venv venv
    source venv/bin/activate
    pip install -U pip; pip install -r requirements.txt
    python manage.py migrate
    python manage.py syncstatic
    python manage.py runserver

## Static Files

The only static files in this repository are the JavaScript source files. All
other files either need to be created locally or synchronized with the server. 
To get any missing files from the canonical server run the following command:

    python manage.py syncstatic

If you'd like, you can generate the CSS files yourself. On macOS, you can
install the command line tool with `brew install sass/sass/sass`. Afterwards,
run the following command in the base directory:

    sass --no-source-map sass/main.scss static/css/main.css

## Docker

The `build.sh` creates a properly versioned Docker image with two tags: latest,
and one matching the version. This script runs `version.sh` and ensures the
`VERSION` file in the Docker image and the tag is consistent.

## License

Copyright 2021-2022 Jonathan Eyolfson

Licensed under the Apache License, Version 2.0 (the "License"); you may not use
this file except in compliance with the License. You may obtain a copy of the
License at

<http://www.apache.org/licenses/LICENSE-2.0>

Unless required by applicable law or agreed to in writing, software distributed
under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
CONDITIONS OF ANY KIND, either express or implied. See the License for the
specific language governing permissions and limitations under the License.
