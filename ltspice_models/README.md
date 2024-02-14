# LTSpice Models

This folder contains some LTSpice models used in the HiFi amplifier.

## Installation

1. Copy `bdx3*.asy` to `Documents\LTspiceXVII\lib\sym`.
2. Copy `bdx*.lib` to `Documents\LTspiceXVII\lib\sub`.

### Linux + Wine
Make sure to run it in the same directory as the models.
```sh
ln -s $(pwd)/bdx33c.asy ~/.wine/drive_c/users/$USER/Documents/LTspiceXVII/lib/sym/bdx33c.asy
ln -s $(pwd)/bdx34c.asy ~/.wine/drive_c/users/$USER/Documents/LTspiceXVII/lib/sym/bdx34c.asy
ln -s $(pwd)/bdx33c.lib ~/.wine/drive_c/users/$USER/Documents/LTspiceXVII/lib/sub/bdx33c.lib
ln -s $(pwd)/bdx34c.lib ~/.wine/drive_c/users/$USER/Documents/LTspiceXVII/lib/sub/bdx34c.lib
```

```sh
mklink %cd%\bdx33c.asy %userprofile%\Documents\LTspiceXVII\lib\sym\bdx33c.asy
mklink %cd%\bdx34c.asy %userprofile%\Documents\LTspiceXVII\lib\sym\bdx34c.asy
mklink %cd%\bdx33c.lib %userprofile%\Documents\LTspiceXVII\lib\sub\bdx33c.lib
mklink %cd%\bdx34c.lib %userprofile%\Documents\LTspiceXVII\lib\sub\bdx34c.lib
```
