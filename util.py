#! /usr/bin/python


def convert_binary_str_to_int_40(binary_str_40):
  return int(binary_str_40, 2)


def convert_decimal_to_binary_list_40(decimal_40):
  binary_40 = bin(decimal_40)
  return [int(c) for c in binary_40[2:]]


def convert_int_list_to_char_list_40(int_list_40):
  return [str(c) for c in int_list_40]


def convert_int_list_to_decimal_40(int_list_40):
  decimal = 0
  for index, bit in enumerate(reversed(int_list_40)):
    decimal = decimal + (bit * (2 ** index))
  return decimal


def convert_int_list_to_2s_complement_int_list_40(int_list_40):
  i = len(int_list_40) - 1
  while i >= 0:
    if int_list_40[i] == 1:
      break
    i = i - 1
  i = i - 1
  while i >= 0:
    int_list_40[i] = int_list_40[i] ^ 1
    i = i - 1
  return int_list_40


def pad_list_40(
    to_be_padded_list_40,
    final_list_len_40,
    pad_with_40=0,
    pad_at_front_40=True,
):
  curr_list_len_40 = len(to_be_padded_list_40)
  assert(curr_list_len_40 <= final_list_len_40), \
      "Length of given list is {} (> {})".format(
          curr_list_len_40, final_list_len_40
      )
  if pad_at_front_40:
    return [pad_with_40] * (final_list_len_40 - curr_list_len_40) + to_be_padded_list_40
  return to_be_padded_list_40 + [pad_with_40] * (final_list_len_40 - curr_list_len_40)
