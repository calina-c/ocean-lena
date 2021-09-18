# OCEAN Lena
Algorithms for image processing, designed for OCEAN Protocol compute to data (samples).

### Requirements

- Python 3.7+

### Installation for testing and development
```
#get repo
git clone git clone https://github.com/calina-c/ocean-lena.git
cd ocean-lena

#set up virtualenv
python -m venv venv
source venv/bin/activate

#install virtualenv dependencies
pip install -r requirements.txt
```

### Local usage
Run any of the algorithms locally e.g. for grayscale:

```console
python grayscale.py local
```

The result will be saved in output/grayscale.png. The output folder is gitignored.


### Running for OCEAN compute-to-data

Assumes "DIDS" is set as an environment variable, input relies in `/data/ddos`, and output is sent to `data/outputs/result`):

```console
python grayscale.py
```

### Lena
Lena is a standard test image widely used in the field of image processing since 1973.
It is a picture of the Swedish model Lena Forsén, shot by photographer Dwight Hooker, cropped from the centerfold of the November 1972 issue of Playboy magazine.

![The famous Lena image](lena.png)
