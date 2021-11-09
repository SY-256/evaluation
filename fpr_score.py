# FPR: TPRの対の関係
# FPR = FP / (TN + FP)

from true_false import true_negative, false_positive

def fpr_value(y_true, y_pred):
    """FPRを計算する関数
    Args:
        y_true: 正解のリスト
        y_pred: 予測値のリスト
        return: FPR
    """
    fp = false_positive(y_true, y_pred)
    tn = true_negative(y_true, y_pred)
    fpr = fp / (tn + fp)
    
    return fpr