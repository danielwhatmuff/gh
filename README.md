# gh - a tool to open Github projects in a browser from the command line
![](https://raw.githubusercontent.com/danielwhatmuff/gh/master/img/GitHub-Mark-32px.png)

## Overview
* Install and execute to open a Github project in your browser from the command line
* Run from within a repo directory

### Install the CLI and view the available options
```bash
$ pip install gh
$ gh --help
```

### Open a projects pull requests page
```bash
$ cd your-repo-dir
$ gh --pulls
```

### Open a projects releases page
```bash
$ cd your-repo-dir
$ gh -r
```

### Available options as of 0.0.3
```
  --home               Open at the home page (Default action)
  -p, --pulls          Open at pull requests page
  -b, --branches       Open at Branches page
  -s, --settings       Open at Settings page
  -r, --releases       Open at Releases page
  -t, --tags           Open at Tags page
  -c, --collaboration  Open at collaboration page
  -w, --wiki           Open at Wiki
  -i, --issues         Open at Issues page
```

## Feel free to fork/PR any contributions
