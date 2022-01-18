# eyolfson.com

A simple Django site.

# Static Files

You need to ensure you have the CSS files setup. If you're on macOS, you can
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
