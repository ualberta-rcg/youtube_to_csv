# youtube_to_csv
Convert a Youtube channel feed into a CSV file for ingesting in TeSS.

Metadata is configured and enhanced via a YAML file.

This runs on the command line and takes a yaml file as an argument
(default is `config.yml`). An example file is provided.

```
python -m youtube_to_csv config.yml.example
```

The YAML file has the configuration for generating the CSV file. Specifically:
  * it has a URL to a Youtube RSS feed for our channel.
  * it has the column names the CSV file should have.
  * it has some default metadata values to apply to each video.
  * it also has some specific metadata values for each specific video (identified by title).

The example YAML file will illustrate how this is formatted.

For an example of an input and an output (and a Github action to generate the ouput)
check out this repository: https://github.com/ualberta-rcg/explora_export
