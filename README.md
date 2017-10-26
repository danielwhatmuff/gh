# gh - a tool to open Github projects in a browser from the command line
![](https://raw.githubusercontent.com/danielwhatmuff/gh/master/img/GitHub-Mark-32px.png)

## Overview
* Install and execute to open a Github project in your browser from the command line
* Useful for command line git users e.g. to push changes and open up a PR `git push origin feature/mything && gh --pulls`
* Must from within the root directory of a checked out repo

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
  --home               Open the Home page (Default action)
  -p, --pulls          Open the Pull requests page
  -b, --branches       Open the Branches page
  -s, --settings       Open the Settings page
  -r, --releases       Open the Releases page
  -t, --tags           Open the Tags page
  -c, --collaboration  Open the Collaboration page
  -w, --wiki           Open the Wiki
  -i, --issues         Open the Issues page
```

## Feel free to fork/PR any contributions
