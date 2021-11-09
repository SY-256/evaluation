# 再現率: tp / (tp + fn)

from true_false import true_positive, false_negative

def recall(y_true, y_pred):
    """再現率を計算する関数
    Args:
        y_true: 正解のリスト
        y_pred: 予測値のリスト
        return: 再現率
    """
    tp = true_positive(y_true, y_pred)
    fn = false_negative(y_true, y_pred)
    if (tp + fn) != 0:
        recall = tp / (tp + fn)
    else:
        recall = 0
    return recall