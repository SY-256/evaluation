# F1-score: 適合率と再現率の調和平均
# F1 score = 2PR / (P + R) = 2TP / (2TP + FP + FN)

from precision_score import precision
from recall_score import recall

def f1(y_true, y_pred) -> float:
    """F1スコアを計算する関数
    Args:
        y_true: 正解のリスト
        y_pred: 予測値のリスト
        return: F1スコア
    """
    p = precision(y_true, y_pred)
    r = recall(y_true, y_pred)
    
    f1_score = 2 * p * r / (p + r)
    
    return f1_score