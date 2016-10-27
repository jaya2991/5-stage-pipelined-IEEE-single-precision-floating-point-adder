#! /usr/bin/python


from fpnumber import *
from stages import *


def pipelined_add_40(inputs):
  fp_inputs = [
    (
        FPNumber40(a_40),
        FPNumber40(b_40)
    ) for a_40, b_40 in inputs
  ]

  clock = 0
  #Executing 5 stages here.
  while True:
    Stages40.exec_stage5()
    Stages40.exec_stage4()
    Stages40.exec_stage3()
    Stages40.exec_stage2()
    if clock < len(fp_inputs):
      fp_a_40, fp_b_40 = fp_inputs[clock]
      Stages40.exec_stage1(fp_a_40, fp_b_40)

    clock = clock + 1
    inputs_index = clock - Stages40.NUM_STAGES_40

    if inputs_index >= len(inputs):
      break

    if inputs_index < 0:
      print('Clock {}:'.format(clock))
    else:
      a_40, b_40 = inputs[inputs_index]
      print(
          'Clock {}:\t({})\t+\t({})\t=\t({})'.format(
              clock, a_40, b_40,
              Stages40.STAGE5_RESULT_40.get_decimal_40()
          )
      )


def main():
  inputs = [
    ( 100,  200),
    ( 100, - 50),
    (- 53,   35),
    (-300, - 99),
    (   0,    0),
    (   0, -171),
  ]
  pipelined_add_40(inputs)


if __name__ == "__main__":
  main()
