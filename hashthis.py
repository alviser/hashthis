#!/usr/bin/env python3

# hashthis.py
# this script takes a string and hashes it with a bunch of algorithms
# possibily encoding it with different encodings too
# with the -c switch it checks if a given hash matches a given string

import argparse
import sys
import hashlib
import base64
import urllib.parse

def get_options(cmd_args=None):
    """
    Parse command line arguments
    """
    cmd_parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    cmd_parser.add_argument(
        '-a',
        '--hash_algo',
        help="""List of hash algorithms to use""",
        type=str,
        default='plain,sha3_256,sha,sha1,sha256,sha384,sha512,md4,md5')
    cmd_parser.add_argument(
        '-e',
        '--encoders',
        help="""List of encoders to use""",
        type=str,
        default='plain,base64,base32,base16,urlenc,urlplus')
    cmd_parser.add_argument(
        '-s',
        '--source_string',
        help="""String to hash""",
        type=str,
        default='')
    cmd_parser.add_argument(
        '-c',
        '--compare_with',
        help="""string to compare the results with (if not present all the transformations will be printed to stdout)""",
        type=str,
        default='')

    args = cmd_parser.parse_args(cmd_args)

    options = {}
    options['source_string'] = args.source_string
    options['hash_algo'] = args.hash_algo
    options['encoders'] = args.encoders
    options['compare_with'] = args.compare_with

    return options

def makeHash(algo,value):
	if (algo == "plain"):
		return value
	elif (algo in hashlib.algorithms_available):
		hsh = hashlib.new(algo)
		hsh.update(value.encode("utf-8"))

		if (algo == "shake_128"):
			return hsh.hexdigest(128)
		elif (algo == "shake_256"):
			return hsh.hexdigest(256)
		else:
			return hsh.hexdigest()
	else:
		return ""

def doEncode(enc,value):
	if (enc == "plain"):
		return value
	elif (enc == "base64"):
		return base64.b64encode(value.encode("utf-8")).decode()
	elif (enc == "base32"):
		return base64.b32encode(value.encode("utf-8")).decode()
	elif (enc == "base16"):
		return base64.b16encode(value.encode("utf-8")).decode()
	elif (enc == "urlenc"):
		return urllib.parse.quote(value)
	elif (enc == "urlplus"):
		return urllib.parse.quote_plus(value)		# same as urlenc, but spaces are encoded with plus signs

def main(options):
	# print(options["source_string"])

	# hashes = hashlib.algorithms_available
	if (not options['hash_algo'] == ''):
		hashes = options['hash_algo'].split(",")
	else:
		hashes = [
			'plain',
			# 'MDC2',
			# 'blake2s',
			# 'blake2b',
			# 'ripemd160',
			# 'whirlpool',
			# 'DSA',
			# 'DSA-SHA',
			# 'dsaWithSHA',
			# 'ecdsa-with-SHA1',
			# 'dsaEncryption',
			# 'sha3_224',
			'sha3_256',
			# 'sha3_384',
			# 'sha3_512',
			'sha',
			'sha1',
			# 'sha224',
			'sha256',
			'sha384',
			'sha512',
			# 'shake_128',
			# 'shake_256',
			# 'mdc2',
			'md4',
			'md5',
		]

	if (not options['encoders'] == ''):
		encoders = options['encoders'].split(",")
	else:
		encoders = [
			"plain",
			"base64",
			"base32",
			"base16",
			"urlenc",
			"urlplus"
		]

	for a in hashes:
		hsh = makeHash(a,options["source_string"])

		if hsh == '':						# if you pass some unknown hash algorithm name along with
			print("unknown algorithm " + a)	# others that are valid this does not break everything
			continue

		for enc in encoders:
			s = doEncode(enc,hsh)
			if (not options['compare_with'] == ''):
				if (s == options['compare_with']):
					print("MATCH FOUND WITH: " + a + " " + enc)	
			else:
				print("["+a+"]["+enc+"] "+ s)



if __name__ == "__main__":
    sys.exit(main(get_options()))