import sys, os
import subprocess
import urllib, optparse
from flask import Flask, jsonify, request, abort, make_response
#from werkzeug.utils import secure_filename

import seq2seq


###GLOBAL VARIABLES###############################

app = Flask(__name__)

##################################################
@app.route('/', methods=['GET'])
def hello_world():
	return jsonify('Hello World!- This Flask App is working!!')

#assumes parameter is encoded using quote_plus
@app.route('/broken2complete', methods=['GET'])
def broken2complete():
	if request.method == 'GET':
		#os.environ['PYTHON_PATH']=os.environ['PYTHON_PATH'] + ":" + os.path.join(os.getcwd(), "SimpleText", "nmt")
		text_encoded = request.args.get('text')
		if(text_encoded is None or text_encoded==''):
			abort(400)

		text = urllib.parse.unquote_plus(text_encoded)
		subprocess.run(['python', '-m', 'nmt.nmt', '--out_dir='+ os.path.join('model','nmt_attention_bpe_2_layers_native'), '--inference_input_file=\''+ text+'\'', '--inference_output_file='+ os.path.join('test', 'inference.txt')])


		#enter model stuff here
		#output = seq2seq.translate(text)
		output = open(os.path.join('SimpleText', 'test', 'inference.txt')).readline()

		return jsonify(output)

#assumes parameter is encoded using quote_plus
@app.route('/complex2simple', methods=['GET'])
def complex2simple():
	if request.method == 'GET':
		text_encoded = request.args.get('text')
		if(text_encoded is None or text_encoded==''):
			abort(400)

		text = urllib.unquote_plus(text_encoded)

		#enter model stuff here
		output = seq2seq.translate(text)
		return jsonify(output)


@app.errorhandler(404) # resource not found
def error404(error):
	return make_response(jsonify({'error':'The requested endpoint does not exist'}),404)

@app.errorhandler(400) # payload too large
def error413(error):
	return make_response(jsonify({'error':'Invalid input string'}),400)


if __name__ == '__main__':
	default_host="127.0.0.1"
	default_port="5000"
	parser = optparse.OptionParser()
	parser.add_option("-H", "--host",
					  help="Hostname of the Flask app " + \
						   "[default %s]" % default_host,
					  default=default_host)
	parser.add_option("-P", "--port",
					  help="Port for the Flask app " + \
						   "[default %s]" % default_port,
					  default=default_port)

	# Two options useful for debugging purposes, but 
	# a bit dangerous so not exposed in the help message.
	parser.add_option("-d", "--debug",
					  action="store_true", dest="debug",
					  help=optparse.SUPPRESS_HELP)
	parser.add_option("-p", "--profile",
					  action="store_true", dest="profile",
					  help=optparse.SUPPRESS_HELP)

	options, _ = parser.parse_args()

	app.run(
		debug=options.debug,
		host=options.host,
		port=int(options.port)
	)
