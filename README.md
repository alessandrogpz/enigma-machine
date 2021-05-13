# Enigma Machine 'Shark' M4

![GitHub top language](https://img.shields.io/github/languages/top/alessandrogpz/enigma-machine)
![GitHub repo size](https://img.shields.io/github/repo-size/alessandrogpz/enigma-machine)
![GitHub](https://img.shields.io/github/license/alessandrogpz/enigma-machine)

This is an Enigma Machine simulator based on the M4 'Shark' (U-Boats) machines.

## Getting Started

### Prerequisites

```Python 3.x```

### Installing & Running

1) Clone the repository.

2) Open the enigma-machine folder in your terminal. 

This code runs on terminal using the rotors name, positions and offsets as arguments.
The arguments needed to initialze the machine are in order for each rotor (1st Rotor, 2nd Rotor, 3rd Rotor & Zusatzwalze)  ```[Rotor]``` ```[Rotor Position]``` ```[Rotor Offset]``` and least
of all the Reflector ```[Reflector]```  

* The options for the Rotors are ```[I, II, III, IV, V, VI, VII, VIII]```

* The the initial position for the Rotors and Zusatzwalze are the alphabet letters ```[A - Z]```

* The initial offset for the Rotors and Zusatzwalze are the numbers ```[1 - 26]```

* The available Zusatzwalze are ```[ZW-B, ZW-B]```

* The available Reflectors are ```[UKW-B-THIN, UKW-C-THIN]```

An example of a valid argument would be:

Windows
```
python main.py I A 1 II B 2 III C 3 ZW-B D 4 UKW-B-THIN
```

Mac
```
python3 main.py I A 1 II B 2 III C 3 ZW-B D 4 UKW-B-THIN
```

3) After that you will be prompted to select the number of letter-pairs for the Plugboard. The number must be in between ```0 - 13```, 
followed by assigning 2 unique letters to each of the number of letter-pairs chosen. 

An example of a letter-pair choice would be:

```
AB
```

4) The last input needed is the plaintext code of your choice that will be used during the encryption process.

## Authors

* Alessandro Perez

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/alessandrogpz/enigma-machine/blob/master/LICENSE) file for details

## Project Status

This project is completed.

## Sources, Tools & References

This project was realizes using Python 3 only.

All the sources used for this project are listed below.

### Enigma Simulator
[Cryptii](https://cryptii.com/pipes/enigma-machine)

[Universal Enigma](http://people.physik.hu-berlin.de/~palloks/js/enigma/enigma-u_v26_en.html)

### Enigma Mechanisms
[Overview of the Enigma Machine](https://en.wikipedia.org/wiki/Enigma_machine)

[Technical Details for the Enigma Machine M4](http://users.telenet.be/d.rijmenants/en/enigmatech.htm)

[Ring Settings](https://crypto.stackexchange.com/questions/29315/how-does-the-ring-settings-of-enigma-change-wiring-tables)

[Rotor Details](https://en.wikipedia.org/wiki/Enigma_rotor_details)
