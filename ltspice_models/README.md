# LTSpice Models

This folder contains some LTSpice models used in the HiFi amplifier.

# Stand-alone components

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
`

# Transistor models

## Installation

Append the following lines to your `Documents\LTspiceXVII\lib\cmp\standard.bjt`

```
.model bc547a NPN BF=400 NE=1.3 ISE=10.3F IKF=50M IS=10F VAF=80 ikr=12m
+ BR=9.5 NC=2 VAR=10 RB=280 RE=1 RC=40 VJE=.48 tr=.3u tf=.5n
+cje=12p vje=.48 mje=.5 cjc=6p vjc=.7 mjc:.33 isc=47p kf=2f
.model bc547b NPN BF=500 NE=1.3 ISE=9.72F IKF=80M IS=20F VAF=50 ikr=12m
+ BR=10 NC=2 VAR=10 RB=280 RE=1 RC=40 VJE=.48 tr=.3u tf=.5n
+cje=12p vje=.48 mje=.5 cjc=6p vjc=.7 mjc:.33 isc=47p kf=2f
.model bc547c NPN BF=730 NE=1.4 ISE=29.5F IKF=80M IS=60F VAF=25 ikr=12m
+ BR=10 NC=2 VAR=10 RB=280 RE=1 RC=40 VJE=.48 tr=.3u tf=.5n
+cje=12p vje=.48 mje=.5 cjc=6p vjc=.7 mjc:.33 isc=47.6p kf=2f
.model BC557a PNP BF=190 NE=1.5 ISE=12F IKF=90M IS=10F VAF=50 ikr=12m
+ nc=2 br=4 var=10 rb=280 re=1 rc=40 vje=.48 tf=.5n tr=.3u
+cje=12p vje=.48 mje=.5 cjc=6p vjc=.7 mjc:.33 isc=47.6p kf=2f
.model BC557b PNP BF=335 NE=1.5 ISE=7.35F IKF=82M IS=10F VAF=40 ikr=12m
+ nc=2 br=4 var=10 rb=280 re=1 rc=40 vje=.48 tf=.5n tr=.3u
+cje=12p vje=.48 mje=.5 cjc=6p vjc=.7 mjc:.33 isc=47.6p kf=2f
.model BC557c PNP BF=490 NE=1.5 ISE=12.4F IKF=78M IS=60F VAF=36 ikr=12m
+ nc=2 br=4 var=10 rb=280 re=1 rc=40 vje=.48 tf=.5n tr=.3u
+cje=12p vje=.48 mje=.5 cjc=6p vjc=.7 mjc:.33 isc=47.6p kf=2f
```
