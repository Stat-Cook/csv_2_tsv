# CSV 2 TSV

Implementation of a *.csv to .tsv* conversion tool that has been generalized to a broader range of file types.

In addition to the python module, a CLI has been included for ease of use.

To install the package run:

``` 
pip install git+https://github.com/Stat-Cook/csv_2_tsv
```

Then from the command line, the command:

```
csv_2_tsv [root] 
```

will convert all *.csv* files found at *root*, and in nested sub-directories, to *.tsv* files.  

### Optional flags

To improve usability three optional flags are included for quality of life:

*  `-r` - file format to **read** in (e.g. *xlsx*, *csv*, *xlsb*)
*  `-w` - file format to **write** out (e.g. *xlsx*, *csv*, *xlsb*)
*  `-n` - **new** data directory to write to, preserving folder structure

