#! /usr/bin/python

from fpnumber import *

class Stages40():
  NUM_STAGES_40 = 5

  STAGE1_FP_A_40 = None
  STAGE1_FP_B_40 = None
  STAGE1_SHIFTS_40 = None

  STAGE2_FP_A_40 = None
  STAGE2_FP_B_40 = None

  STAGE3_FP_A_40 = None
  STAGE3_FP_B_40 = None

  STAGE4_RESULT_40 = None
  STAGE4_RESHIFT_40 = None

  STAGE5_RESULT_40 = None


  @staticmethod
  def set_stage1_variables(fp_a_40, fp_b_40, shifts_40):
    #setting the stage 1 variables to the required values.
    Stages40.STAGE1_FP_A_40 = fp_a_40
    Stages40.STAGE1_FP_B_40 = fp_b_40
    Stages40.STAGE1_SHIFTS_40 = shifts_40

  @staticmethod
  def exec_stage1(fp_a_40, fp_b_40):
    #executing stage 1 here.
    if (fp_a_40 is None) or (fp_b_40 is None):
      return

    # Set Stage 1 Variables
    Stages40.set_stage1_variables(
        fp_a_40,
        fp_b_40,
        abs(
            convert_int_list_to_decimal_40(
                fp_a_40._exponent_40
            ) - convert_int_list_to_decimal_40(
                fp_b_40._exponent_40
            )
        )
    )


  @staticmethod
  def set_stage2_variables(fp_a_40, fp_b_40):
    Stages40.STAGE2_FP_A_40 = fp_a_40
    Stages40.STAGE2_FP_B_40 = fp_b_40
      
  @staticmethod
  def exec_stage2():
    # Get Stage 1 Variables
    fp_a_40 = Stages40.STAGE1_FP_A_40
    fp_b_40 = Stages40.STAGE1_FP_B_40
    shifts_40 = Stages40.STAGE1_SHIFTS_40
    Stages40.set_stage1_variables(None, None, None)

    if (fp_a_40 is None) or (fp_b_40 is None) or (shifts_40 is None):
      return

    if shifts_40 == 0:
      # Set Stage 2 Variables
      Stages40.set_stage2_variables(fp_a_40, fp_b_40)
      return

    if (fp_a_40._exponent_40 < fp_b_40._exponent_40):
      fp_a_40._exponent_40 = fp_b_40._exponent_40
      fp_a_40._mantissa_40 = \
          [0] * (shifts_40 - 1) + \
          fp_a_40._mantissa_int_40 + \
          fp_a_40._mantissa_40[:FPNumber40.MANTISSA_LEN_40 - shifts_40]
      fp_a_40._mantissa_int_40 = [0]
    else:
      fp_b_40._exponent_40 = fp_a_40._exponent_40
      fp_b_40._mantissa_40 = \
          [0] * (shifts_40 - 1) + \
          fp_b_40._mantissa_int_40 + \
          fp_b_40._mantissa_40[:FPNumber40.MANTISSA_LEN_40 - shifts_40]
      fp_b_40._mantissa_int_40 = [0]

    # Set Stage 2 Variables
    Stages40.set_stage2_variables(fp_a_40, fp_b_40)


  @staticmethod
  def set_stage3_variables(fp_a_40, fp_b_40):
    Stages40.STAGE3_FP_A_40 = fp_a_40
    Stages40.STAGE3_FP_B_40 = fp_b_40
      
  @staticmethod
  def exec_stage3():
    # Get Stage 2 Variables
    fp_a_40 = Stages40.STAGE2_FP_A_40
    fp_b_40 = Stages40.STAGE2_FP_B_40
    Stages40.set_stage2_variables(None, None)

    if (fp_a_40 is None) or (fp_b_40 is None):
      return

    if fp_a_40._sign_40 == fp_b_40._sign_40:
      # Set Stage 3 Variables
      Stages40.set_stage3_variables(fp_a_40, fp_b_40)
      return

    a_mantissa_40 = fp_a_40._mantissa_int_40 + fp_a_40._mantissa_40
    b_mantissa_40 = fp_b_40._mantissa_int_40 + fp_b_40._mantissa_40

    if fp_a_40._sign_40 == 1:
      a_mantissa_40 = convert_int_list_to_2s_complement_int_list_40(
          a_mantissa_40
      )
      fp_a_40._mantissa_int_40 = a_mantissa_40[:1]
      fp_a_40._mantissa_40 = a_mantissa_40[1:]

    if fp_b_40._sign_40 == 1:
      b_mantissa_40 = convert_int_list_to_2s_complement_int_list_40(
          b_mantissa_40
      )
      fp_b_40._mantissa_int_40 = b_mantissa_40[:1]
      fp_b_40._mantissa_40 = b_mantissa_40[1:]

    # Set Stage 3 Variables
    Stages40.set_stage3_variables(fp_a_40, fp_b_40)


  @staticmethod
  def set_stage4_variables(result_40, reshifts_40):
    Stages40.STAGE4_RESULT_40 = result_40
    Stages40.STAGE4_RESHIFT_40 = reshifts_40
      
  @staticmethod
  def exec_stage4():
    # Get Stage 3 Variables
    fp_a_40 = Stages40.STAGE3_FP_A_40
    fp_b_40 = Stages40.STAGE3_FP_B_40
    Stages40.set_stage3_variables(None, None)

    if (fp_a_40 is None) or (fp_b_40 is None):
      return

    result_40 = FPNumber40(0) 
    result_40._exponent_40 = fp_a_40._exponent_40
    carry = 0
    for i in reversed(range(FPNumber40.MANTISSA_LEN_40)):
      sum = carry + fp_a_40._mantissa_40[i] + fp_b_40._mantissa_40[i]
      result_40._mantissa_40[i] = sum % 2
      carry = 1 if sum >= 2 else 0
    sum = carry + fp_a_40._mantissa_int_40[0] + fp_b_40._mantissa_int_40[0] 
    result_40._mantissa_int_40 = [sum % 2]
    carry = 1 if sum >= 2 else 0
    if fp_a_40._sign_40 == fp_b_40._sign_40:
      result_40._sign_40 = fp_a_40._sign_40
      if carry == 1:
        result_40._mantissa_int_40.insert(0, carry)
    else:
      if carry == 1:
        result_40._sign_40 = 0
      else:
        result_40._sign_40 = 1
        result_mantissa_40 = result_40._mantissa_int_40 + result_40._mantissa_40
        result_mantissa_40 = convert_int_list_to_2s_complement_int_list_40(
            result_mantissa_40
        )
        result_40._mantissa_int_40 = result_mantissa_40[:1]
        result_40._mantissa_40 = result_mantissa_40[1:]
    reshifts_40 = len(result_40._mantissa_int_40) - 1

    # Set Stage 4 Variables
    Stages40.set_stage4_variables(result_40, reshifts_40)


  @staticmethod
  def set_stage5_variables(result_40):
    Stages40.STAGE5_RESULT_40 = result_40

  @staticmethod
  def exec_stage5():
    # Get Stage 4 Variables
    result_40 = Stages40.STAGE4_RESULT_40
    reshifts_40 = Stages40.STAGE4_RESHIFT_40
    Stages40.set_stage4_variables(None, None)

    if (result_40 is None) or (reshifts_40 is None):
      return

    result_40._exponent_40 = convert_decimal_to_binary_list_40(
      convert_int_list_to_decimal_40(result_40._exponent_40) + reshifts_40
    )
    result_40._mantissa_40 = result_40._mantissa_int_40[1:] + \
        result_40._mantissa_40[:FPNumber40.MANTISSA_LEN_40 - reshifts_40]
    result_40._mantissa_int_40 = [result_40._mantissa_int_40[0]]

    # Set Stage 5 Variables
    Stages40.set_stage5_variables(result_40)
