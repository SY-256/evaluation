# 適合率: tp / (tp + fp)
from true_false import true_positive, false_positive

def precision(y_true, y_pred) -> float:
    """適合率を計算する関数
    Args:
        y_true: 正解のリスト
        y_pred: 予測値のリスト
        return: 適合率
    """
    tp = true_positive(y_true, y_pred)
    fp = false_positive(y_true, y_pred)
    if (tp + fp) != 0:
        precision = tp / (tp + fp)
    else:
        precision = 0
    return precision