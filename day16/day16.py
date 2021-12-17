from dataclasses import dataclass
from typing import Tuple

# Docstrings written by OpenAI Codex using my tool

@dataclass
class Literal:
    """
    A dataclass to represent a single literal.

    Attributes:
        version (int):
            The version number of the literal
        type_id (int):
            The type id of the literal
        value (int):
            The value of the literal

    Methods:
        get_version_numbers(self)
            Returns the version number of the literal

        get_value(self)
            Returns the value of the literal
    """
    version: int
    type_id: int
    value: int

    def get_version_numbers(self) -> int:
        return self.version

    def get_value(self) -> int:
        return self.value


@dataclass
class Packet:
    """
    A class to hold a single packet of data.

    Attributes:
        version (int):
            Version number of the packet
        type_id (int):
            Type ID of the packet
        contents (list):
            List of contents of the packet

    Methods:
        get_version_numbers(self)
            Returns the sum of the version numbers of all contents in the packet

        get_value(self)
            Returns the value of the packet, depending on the type ID
    """
    version: int
    type_id: int
    contents: list

    def get_version_numbers(self) -> int:
        return self.version + sum(x.get_version_numbers() for x in self.contents)

    def get_value(self) -> int:
        if self.type_id == 0:
            # Sum packet
            return sum(x.get_value() for x in self.contents)

        elif self.type_id == 1:
            # Product packet
            product = 1
            for x in self.contents:
                product *= x.get_value()

            return product

        elif self.type_id == 2:
            # Min packet
            return min(x.get_value() for x in self.contents)

        elif self.type_id == 3:
            # Max packet
            return max(x.get_value() for x in self.contents)

        elif self.type_id == 4:
            # This should never get called
            print("ERROR: Literal should have been parsed!")

        elif self.type_id == 5:
            # Greater than packet
            if len(self.contents) != 2:
                print("ERROR! Greater than packet should have 2 subpackets!")
                raise Exception("ERROR IN 5")

            return self.contents[0].get_value() > self.contents[1].get_value()

        elif self.type_id == 6:
            # Less than packet
            if len(self.contents) != 2:
                print("ERROR! Less than packet should have 2 subpackets!")
                raise Exception("ERROR IN 6")

            return self.contents[0].get_value() < self.contents[1].get_value()

        elif self.type_id == 7:
            # Equal to packet
            if len(self.contents) != 2:
                print("ERROR! Equal to packet should have 2 subpackets!")
                raise Exception("ERROR IN 7")

            return self.contents[0].get_value() == self.contents[1].get_value()


def parse_literal(section) -> Tuple[int, str]:
    """
    Parses a string of binary digits and returns the associated literal's value
    along with the remaining values in the section.

    Literal value packets encode a single binary number.
    To do this, the binary number is padded with leading zeroes until its length
    is a multiple of four bits, and then it is broken into groups of four bits.
    Each group is prefixed by a 1 bit except the last group, which is prefixed
    by a 0 bit.

    Parameters:
        section (str): A string of binary digits

    Returns:
        (int, str): A tuple of an integer and a string
                    (string is the remaining section of section)
    """
    number = ""

    done = False

    while not done:
        next_five = section[:5]
        section = section[5:]

        number += next_five[1:5]

        if next_five[0] == "0":
            done = True
            continue

    return int(number, 2), section


def parse_packet(section) -> Tuple[Packet, list]:
    """
    Parses a packet and returns a tuple of the parsed packet and the remaining
    section of the packet.

    Parameters:
        section (str): The section of the packet to be parsed

    Returns:
        (Packet, str): The parsed packet and the remaining section of the section
    """
    packet_version = int(section[0:3], 2)
    section = section[3:]

    packet_type_id = int(section[0:3], 2)
    section = section[3:]

    if packet_type_id == 4:
        packet_value, section = parse_literal(section)

        return Literal(packet_version, packet_type_id, packet_value), section

    # It's an operator
    length_type_id = int(section[0], 2)
    section = section[1:]

    if length_type_id == 0:
        next_section_length = int(section[:15], 2)
        section = section[15:]

        next_section = section[:next_section_length]
        section = section[next_section_length:]

        subpackets = []
        while next_section:
            subpacket, next_section = parse_packet(next_section)
            subpackets.append(subpacket)

        return Packet(packet_version, packet_type_id, subpackets), section

    elif length_type_id == 1:
        number_subpackets = int(section[:11], 2)
        section = section[11:]

        subpackets = []
        while len(subpackets) < number_subpackets:
            subpacket, section = parse_packet(section)
            subpackets.append(subpacket)

        return Packet(packet_version, packet_type_id, subpackets), section

    print("Error! Unknown length type id!")

def hex_to_bin(char: str) -> str:
    """
    Returns the binary value of a hexadecimal character, padded to 4 bits
    """

    return str(bin(int(char, 16))[2:]).rjust(4, "0")

if __name__ == "__main__":
    with open("day16input.txt") as f:
        input_data = f.read().strip()

    binaries = [hex_to_bin(x) for x in input_data]

    binary_string = "".join(binaries)

    packet, rem = parse_packet(binary_string)
    print("Part 1:", packet.get_version_numbers())

    print("Part 2:", packet.get_value())
