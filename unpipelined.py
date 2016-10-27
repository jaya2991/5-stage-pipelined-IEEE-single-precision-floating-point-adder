#! /usr/bin/python


from fpnumber import *
from stages import *


def fp_add_40(fp_a_40, fp_b_40):
  Stages40.exec_stage1(fp_a_40, fp_b_40)
  Stages40.exec_stage2()
  Stages40.exec_stage3()
  Stages40.exec_stage4()
  Stages40.exec_stage5()
  return Stages40.STAGE5_RESULT_40


def unpipelined_add_40(a_40, b_40):
  fp_a_40 = FPNumber40(a_40)
  fp_b_40 = FPNumber40(b_40)
  fp_result_40 = fp_add_40(fp_a_40, fp_b_40)
  print(
      '({})\t+\t({})\t=\t({})'.format(
          a_40, b_40, fp_result_40.get_decimal_40()
      )
  )


def main():
  inputs = [
    ( 100,  200),
    ( 100, - 50),
    (- 53,   35),
    (-300, - 99),
    (   0,    0),
    (   0, -171)
  ]
  for a_40, b_40 in inputs:
    unpipelined_add_40(a_40, b_40)


if __name__ == "__main__":
  main()
