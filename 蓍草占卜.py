import numpy


def divination():
    total_ShiCao = 50
    results = []

    for _ in range(6):
        ShiCao = total_ShiCao - 1
        remainders = []

        for _ in range(3):
            Tian = -round(numpy.random.normal(loc=ShiCao // 2, scale=3, size=None))
            Di = ShiCao - Tian
            Tian_ShiCao_out = 1
            Tian -= Tian_ShiCao_out
            Tian_rem = Tian % 4 if Tian % 4 != 0 else 4
            Di_rem = Di % 4 if Di % 4 != 0 else 4
            total_rem = Tian_rem + Di_rem + Tian_ShiCao_out
            remainders.append(total_rem)
            ShiCao -= total_rem

        # 计算堆数并转换为爻
        Yao = ShiCao // 4
        results.append(Yao)

    return results


def generate_Gua(results):
    mapping = {6: 0, 7: 1, 8: 0, 9: 1}
    change_mapping = {6: 1, 7: 1, 8: 0, 9: 0}
    Gua = [mapping.get(result, None) for result in results]
    BianGua = [change_mapping.get(result, None) for result in results]
    Gua.reverse()
    BianGua.reverse()

    # 卦象名称
    order = ['坤','复','师','临','谦','明夷','升','泰',
             '豫','震','解','归妹','小过','丰','恒','大壮',
             '比','屯','坎','节','蹇','既济','井','需',
             '萃','随','困','兑','咸','革','大过','夬',
             '剥','颐','蒙','损','艮','贲','蛊','大畜',
             '晋','噬嗑','未济','睽','旅','离','鼎','大有',
             '观','益','涣','中孚','渐','家人','巽','小畜',
             '否','无妄','讼','履','遁','同人','姤','乾'
            ]

    # 将二进制数转换为十进制索引
    Gua_index = sum(val * (2**idx) for idx, val in enumerate(Gua))
    BianGua_index = sum(val * (2**idx) for idx, val in enumerate(BianGua))

    return order[Gua_index], order[BianGua_index]


if __name__ == "__main__":
    final_results = divination()
    print(f"六爻: {final_results}")
    Gua, BianGua = generate_Gua(final_results)
    print(f"本卦: {Gua}, 变卦: {BianGua}")
    input("...")
