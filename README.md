# Flickr Parser

Small app to parse images from [Flickr](https://www.flickr.com/) image hosting service.
You need an API key which can be obtained [here](https://www.flickr.com/services/apps/create/apply)

## Installation

[Python 3.8](https://www.python.org/downloads/release/python-3813/) is required.

```bash
git clone https://github.com/DenkingOfficial/flickr-parser.git
cd flickr-parser
pip install -r requirements.txt
```
    
## Usage/Examples

### Now to use

```
python flickr-parser.py -k [Your API key in format Key:Secret]
                        -w [Word to search]
                        -n [Number of images]
                        -o [Output folder]
```

### Example usage:
```
python flickr-parser.py -k ab6d695092ca8854f58bb2df612a4693:9bd763f85b316ed2
                        -w "beautiful cat"
                        -n 100
                        -o "C:\Images\Cats\Beautiful cat"
```
## Acknowledgements

 - [Flickr API Library](https://github.com/sybrenstuvel/flickrapi)
 - [TQDM Library](https://github.com/tqdm/tqdm)