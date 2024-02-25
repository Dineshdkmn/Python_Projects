# Markov Chain Text Composer

The Markov Chain Text Composer is a technique used in natural language processing and text generation. It's based on Markov chains, which are mathematical systems that transition from one state to another according to certain probabilistic rules. In the context of text generation, each state represents a word, and the transitions represent the likelihood of moving from one word to another.

This Python program generates text compositions based on a provided text file using a Markov Chain algorithm implemented with a graph data structure.

## Features

1. **Text Parsing**: The program extracts words from a provided text file, removing punctuation and converting all words to lowercase.
2. **Graph Generation**: It constructs a directed graph where each word in the text file is represented as a vertex, and the frequency of transition between words is represented as weighted edges.
3. **Text Composition**: Using the constructed graph, the program generates a text composition of a specified length by randomly traversing the graph and selecting the next word based on the probabilities of transitions from the current word.
4. **Randomness**: The composition process introduces randomness by selecting the initial word randomly and choosing subsequent words probabilistically.
5. **Limitations**: Due to the randomness introduced, each composition may vary, and the coherence of the generated text may vary depending on the input text and length of the composition.
6. **Customization**: The program allows customization of the length of the composition and can be easily extended to work with different text sources.

## Usage

1. Clone the repository
2. Navigate to the project directory: 
3. Ensure you have Python installed on your system.
4. Run the program by executing `python compose.py`.

## Dependencies

- `graph.py`: Contains the implementation of the graph data structure and associated methods.
- `texts/hp_sorcerer_stone.txt`: Example text file for generating compositions. You can replace it with your own text file.

## Contributing

Contributions are welcome! If you have suggestions for improvements or encounter any issues, feel free to open an issue or submit a pull request.
