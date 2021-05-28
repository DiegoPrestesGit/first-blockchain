from uuid import uuid4
import requests
from flask import Flask, jsonify, request
from .blockchain import Blockchain

app = Flask(__name__)
blockchain = Blockchain()


@app.route('/mine_block', methods=['GET'])
def mine_block():
    previous_block = blockchain.get_previous_block()
    previous_proof = previous_block['proof']
    proof = blockchain.proof_of_work(previous_proof)
    previous_hash = blockchain.hash(previous_block)

    blockchain.add_transaction(
        sender=str(uuid4()).replace('-', ''),
        receiver='Johnny B Goode',
        amount=1
    )

    block = blockchain.create_block(proof, previous_hash)
    response = {
        'message': 'block successfully mined',
        'index': block['index'],
        'timestamp': block['timestamp'],
        'proof': block['proof'],
        'previous_hash': block['previous_hash'],
        'transaction': block['transactions']
    }

    return jsonify(response), 200


@app.route('/get_chain', methods=['GET'])
def get_chain():
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain)
    }

    return jsonify(response), 200


@app.route('/is_valid', methods=['GET'])
def is_valid():
    is_valid = blockchain.is_chain_valid(blockchain.chain)
    if is_valid:
        response = {'message': 'blockchain is valid'}
    else:
        response = {'message': 'blockchain is NOT valid'}
    return response


@app.route('/add_transaction', methods=['POST'])
def add_transaction():
    json = request.get_json()
    transaction_keys = ['sender', 'receiver', 'amount']

    if not all(key in json for key in transaction_keys):
        return 'some key element(s) missing', 400

    index = blockchain.add_transaction(json['sender'], json['receiver'], json['amount'])
    response = {'message': f'transaction added: {index}'}
    return jsonify(response), 201


@app.route('/connect_node', methods=['POST'])
def connect_node():
    json = request.get_json()
    nodes = json.get('nodes')
    if nodes is None:
        return 'cannot get nodes', 400
    for node in nodes:
        blockchain.add_node(node)
    response = {
        'message': 'nodes connected, blockchain nodes:',
        'total_nodes': list(blockchain.nodes)
    }
    return jsonify(response), 201


@app.route('/replace_chain', methods=['GET'])
def replace_chain():
    is_chain_replaced = blockchain.replace_chain()
    if is_chain_replaced:
        response = {
            'message': 'chain has been replaced',
            'new_chain': blockchain.chain
        }
    else:
        response = {
            'message': 'xqdl',
            'actual_chain': blockchain.chain
        }
    return jsonify(response), 200
