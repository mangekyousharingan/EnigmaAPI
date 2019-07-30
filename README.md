# _Enigma API_
## Simple API to encode and decode text.

It is not “encryption” because humans can usually read it quite easily. But machines may
find it difficult to read without the list of original words. Except of having fun, there are
real-world applications for this, e.g. if encryption is forbidden by law in your country, but
you still don’t want your email content to get automatically processed somehow.

For each original word in the original text, leave the first and last character of it in that
position, but shuffle (permutate) all the characters in the middle of the word.
To make decoding by a machine possible, your encoder shall also output a sorted list of original words 
(only include words that got shuffled, not text that did not).
The composite output of the encoder (see example below) contains encoded text
(WeirdText) and also the sorted list of original words.

## Example:

_Original Text:_

**‘This is a long looong test sentence, with some big (biiiiig) words!’**

_Encoded Text:_

**‘\n—weird—\nTihs is a lnog loonog tset sntceene, wtih smoe big (biiiiig) wdros!\n—weird—\nlong looong sentence some test This with words’**

_Decoded Text:_

**‘This is a long looong test sentence, with some big (biiiiig) words!’**

## Technology stack:

- [Python](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/en/1.1.x/)
- [Docker](https://www.docker.com/)
- [Travis CI](https://travis-ci.org/)
- [Heroku](https://www.heroku.com/)


## Base URL:

https://invulnerable-baguette-19588.herokuapp.com

## API Specification:
[Swagger](https://app.swaggerhub.com/apis/swdowiarz/EnigmaAPI/1.0.0)
