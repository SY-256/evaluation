# 正答率：　(TP + TN) / (TP + TN + FP + FN)

from true_false import true_negative, true_positive, false_positive, false_negative

def accuracy_v2(y_true, y_pred) -> float:
    """
    真陽性、真陰性、偽陽性、偽陰性を用いて正答率を計算する関数
    Args:
        y_true: 正解のリスト
        y_pred: 予測値のリスト
        return: 正答率
    """
    tp = true_positive(y_true, y_pred)
    tn = true_negative(y_true, y_pred)
    fp = false_positive(y_true, y_pred)
    fn = false_negative(y_true, y_pred)
    accuracy_score = (tp + tn) / (tp + tn + fp + fn)
    return accuracy_score