#! /usr/bin/python


from util import *


class FPNumber40(object):
  BIAS_40 = 127
  SIGN_LEN_40 = 1
  EXPONENT_LEN_40 = 8
  MANTISSA_LEN_40 = 23

  
  def __init__(self, dec_number_40):
    #determining sign integer
    self._sign_40 = 0 if dec_number_40 >= 0 else 1
    bin_number_40 = convert_decimal_to_binary_list_40(
        abs(dec_number_40)
    )
    assert(len(bin_number_40) >= 1), \
        "Invalid decimal number {}".format(dec_number_40)
    biased_exponent_40 = len(bin_number_40) - 1
    self._exponent_40 = pad_list_40(
        convert_decimal_to_binary_list_40(
            FPNumber40.BIAS_40 + biased_exponent_40
        ),
        FPNumber40.EXPONENT_LEN_40
    )
    self._mantissa_int_40 = [bin_number_40[0]]
    self._mantissa_40 = pad_list_40(
        bin_number_40[1:],
        FPNumber40.MANTISSA_LEN_40,
        pad_at_front_40 = False
    )


  def __repr__(self):
    return ("sign: {}, exponent: {}, mantissa: {}.{} "
        "decimal: {}".format(
            self._sign_40,
            self._exponent_40,
            self._mantissa_int_40,
            self._mantissa_40,
            self.get_decimal_40()
        )
    )


  def get_decimal_40(self):
    sign_part_40 = (-1) ** (self._sign_40)
    exponent_part_40 = convert_binary_str_to_int_40(
        ''.join(
            convert_int_list_to_char_list_40(self._exponent_40)
        )
    ) - FPNumber40.BIAS_40
    mantissa_40 = ''.join(
        convert_int_list_to_char_list_40(self._mantissa_40)
    )
    mantissa_part_40 = float(
        '{}.{}'.format(
            convert_binary_str_to_int_40(
                ''.join(
                    convert_int_list_to_char_list_40(self._mantissa_int_40) + [
                        str(c) for c in self._mantissa_40[:exponent_part_40]
                    ]
                )
            ),
            convert_binary_str_to_int_40(
                ''.join(
                    [str(c) for c in self._mantissa_40[exponent_part_40:]]
                )
            )
        )
    )
    return int(sign_part_40 * mantissa_part_40)
