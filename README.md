# hashthis
Python script to produce hashes of a given string with a bunch of different algorithms and possibily to check if a given hash matches the string

## usage
`python hashthis.py -h` shows available options

`-s <source string>` use `<source string>` as the source for hashing

`-c <hash>` compare the various hashes of `<source string>` with `<hash>`, any output is suppressed but for matching notices

`-a <list of hashing algorithms>` comma separated list of hashing algoritms, as of now `hashlib.algorithms_available` are available. Default is: `plain,sha3_256,sha,sha1,sha256,sha384,sha512,md4,md5`

`-e <list of encodings>` comma separated list of encodings. Default is: `plain,base64,base32,base16,urlenc,urlplus`

## notes
`base64` encoding is the standard one

`urlenc` encoding is URL encoding using %20 for spaces

`urlplus` encoding is URL encoding using + for spaces