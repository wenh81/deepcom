"""Tests for Convolutional Code Encoder"""
import numpy as np
from ..utils import generate_random_binary_sequence
from .ConvolutionalCodeEncoder import ConvolutionalCodeEncoder

def test_convolutional_code_encoder():

    NUM_SEQS = 5
    BLOCK_LEN = 10
    DATA_RATE = 1/2
    CONSTRAINT_LEN = 3

    # For reproducability
    np.random.seed(2018)

    # Create a random message bits
    msg_bit_sequences = [None for _ in range(NUM_SEQS)]
    for i in range(NUM_SEQS):
        message_bits = generate_random_binary_sequence(BLOCK_LEN)
        msg_bit_sequences[i] = message_bits
    
    # Define a Conv Code Encoding Scheme
    encoder = ConvolutionalCodeEncoder(
        constraint_length=CONSTRAINT_LEN,
        data_rate=DATA_RATE)

    # Encode data
    encoded_sequences = [None for _ in range(NUM_SEQS)]
    for idx, message_bits in enumerate(msg_bit_sequences):
        coded_bits = encoder.encode(message_bits)
        encoded_sequences[idx] = coded_bits

    expected_msg_bit_sequences = np.array(
    [[0, 1, 0, 1, 1, 0, 0, 0, 0, 1], 
    [0, 0, 0, 1, 1, 0, 0, 1, 0, 0], 
    [1, 1, 0, 1, 0, 1, 1, 0, 0, 0], 
    [1, 1, 1, 0, 0, 1, 0, 1, 1, 0], 
    [0, 1, 1, 1, 0, 0, 0, 0, 0, 0]])
    assert np.all(np.asarray(msg_bit_sequences) == expected_msg_bit_sequences)

    exptected_encoded_bits =  np.array(
    [[0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0],
    [1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0],
    [0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])

    assert np.all(np.asarray(encoded_sequences) == exptected_encoded_bits)

    assert np.shape(msg_bit_sequences) == (NUM_SEQS, BLOCK_LEN)
    assert np.shape(encoded_sequences) == (NUM_SEQS, (BLOCK_LEN + 2) * (CONSTRAINT_LEN - 1))