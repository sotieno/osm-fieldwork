# ODK Convert Project

ODKConvert is a project for processing data collection using
OpenDataKit into OpenStreetMap format. It includes several utility
programs that automate part of the data flow like creating satellite
imagery basemaps and data extracts from
[OpenStreetMap](https://www.openstreetmap.org) so they can be
used with [ODK Collect](https://www.getodk.org). Many of these steps
are currently a manual process.

## odkconvert

This program converts the data collected from ODK Collect into
the proper OpenStreetMap tagging schema. The conversion is controled
by an YAML file, so easy to modify for other projects. The output is
an OSM XML formatted file for JOSM. No converted data should ever be
uploaded to OSM without validating the conversion in JOSM. To do high
quality conversion from ODK to OSM, it's best to use the XLSForm
library as templates, as everything is designed to work together.

### Install

- Directly from the main branch:
  `pip install git+https://github.com/hotosm/odkconvert.git`

- Latest on PyPi:
  `pip install ODKConvert`

### Configure

ODKConvert can be configured via environment variable:

**LOG_LEVEL**
> If present, will change the log level. Defaults to DEBUG.

**ODK_CENTRAL_URL**
> The URL for an ODKCentral server to connect to.

**ODK_CENTRAL_USER**
> The user for ODKCentral.

**ODK_CENTRAL_PASSWD**
> The password for ODKCentral.

**ODK_CENTRAL_SECURE**
> If set to False, will allow insecure connections to the ODKCentral API. Else defaults to True.

## XLSForm library

In the XForms directory is a collection of XLSForms that support the
new HOT data models for humanitarian data collection. These cover
many categories like healthcare, waterpoints, waste distribution,
etc... All of these XLSForms are designed to have an efficient mapper
data flow, edit existing OSM data, and support the data models.

The data models specify the preferred tag values for each data item,
with a goal of both tag completeness and tag correctness. Each data item
is broken down into a basic and extended survey questions when
appropriate.

## basemapper.py

This is a program that makes mbtiles basemaps for ODK convert. More
information on this program [is here](docs/programs.md).

## make_data_extract.py

This is a program that makes data extracts from OpenStreetMap for ODK
convert. More information on this program [is here](docs/programs.md).
